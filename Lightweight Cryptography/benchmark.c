// This code uses the ascon-c repository here: https://github.com/ascon/ascon-c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <sys/resource.h>
#include <openssl/evp.h>
#include <openssl/rand.h>
#include "api.h"  // Contains ASCON constants like CRYPTO_KEYBYTES, CRYPTO_NPUBBYTES, etc.

// --- ASCON function declarations from the ASCON library ---
int crypto_aead_encrypt(unsigned char*, unsigned long long*, const unsigned char*, unsigned long long,
                        const unsigned char*, unsigned long long, const unsigned char*,
                        const unsigned char*, const unsigned char*);

int crypto_aead_decrypt(unsigned char*, unsigned long long*, unsigned char*,
                        const unsigned char*, unsigned long long,
                        const unsigned char*, unsigned long long,
                        const unsigned char*, const unsigned char*);

// --- Helper function: calculates time difference in seconds between two time points ---
double time_diff(struct timespec start, struct timespec end) {
    return (end.tv_sec - start.tv_sec) + 1e-9 * (end.tv_nsec - start.tv_nsec);
}

// --- Helper function: returns peak memory usage (in kilobytes) ---
long get_memory_kb() {
    struct rusage usage;
    getrusage(RUSAGE_SELF, &usage);  // Get memory usage statistics of the current process
    return usage.ru_maxrss;  // Return maximum resident set size (memory used)
}

// --- Helper function: generate a realistic blood glucose reading as plaintext data ---
void generate_glucose_reading(char *buffer) {
    int value = rand() % 150 + 70;  // Random value between 70 and 220
    sprintf(buffer, "Blood Glucose: %d mg/dL", value);  // Format as readable string
}

int main() {
    srand(time(NULL));  // Initialize random number generator

    const unsigned char ad[] = "metadata";  // Associated data for AEAD (used in both ASCON and AES-GCM)
    int iterations = 10000;  // Number of messages to encrypt/decrypt

    // ========================== ASCON SECTION ==========================

    // --- Generate key and nonce for ASCON ---
    unsigned char ascon_key[CRYPTO_KEYBYTES];
    unsigned char ascon_nonce[CRYPTO_NPUBBYTES];
    RAND_bytes(ascon_key, sizeof(ascon_key));       // Generate random 128-bit key
    RAND_bytes(ascon_nonce, sizeof(ascon_nonce));   // Generate random nonce (128-bit for ASCON)

    // --- Buffers for ciphertext and plaintext ---
    unsigned char ct_ascon[1024], pt_ascon[1024];
    unsigned long long ctlen_ascon, ptlen_ascon;
    int ascon_correct = 0;  // Counter for correct decryptions

    struct timespec start, end;
    long mem_before = get_memory_kb();  // Memory before ASCON operations

    // --- Start timing for ASCON encryption/decryption ---
    clock_gettime(CLOCK_MONOTONIC, &start);

    for (int i = 0; i < iterations; i++) {
        char message[64];
        generate_glucose_reading(message);  // Create a new glucose reading

        // Encrypt using ASCON
        crypto_aead_encrypt(ct_ascon, &ctlen_ascon,
                            (unsigned char*)message, strlen(message),
                            ad, strlen((char*)ad),
                            NULL, ascon_nonce, ascon_key);

        // Decrypt using ASCON
        crypto_aead_decrypt(pt_ascon, &ptlen_ascon,
                            NULL, ct_ascon, ctlen_ascon,
                            ad, strlen((char*)ad),
                            ascon_nonce, ascon_key);

        pt_ascon[ptlen_ascon] = '\0';  // Null-terminate decrypted message

        // Compare decrypted text to original message
        if (strcmp(message, (char*)pt_ascon) == 0) {
            ascon_correct++;
        }
    }

    clock_gettime(CLOCK_MONOTONIC, &end);
    long mem_after = get_memory_kb();  // Memory after ASCON operations

    // --- Report ASCON performance and correctness ---
    printf("ASCON (10,000 ops)\n");
    printf("  Time:   %.6f sec\n", time_diff(start, end));
    printf("  Memory: %ld KB\n", mem_after - mem_before);
    printf("  Correct decryptions: %d / %d\n\n", ascon_correct, iterations);

    // ========================== AES-GCM SECTION ==========================

    // --- Generate AES key and IV (96-bit IV for GCM mode) ---
    unsigned char aes_key[16];      // 128-bit AES key
    unsigned char aes_iv[12];       // 96-bit IV
    unsigned char aes_tag[16];      // Authentication tag
    unsigned char ct_aes[1024], pt_aes[1024];
    int len, ctlen_aes, ptlen_aes;
    int aes_correct = 0;  // Counter for correct AES decryptions

    RAND_bytes(aes_key, sizeof(aes_key));
    RAND_bytes(aes_iv, sizeof(aes_iv));

    EVP_CIPHER_CTX *ctx;
    mem_before = get_memory_kb();  // Memory before AES-GCM operations
    clock_gettime(CLOCK_MONOTONIC, &start);  // Start timing AES-GCM

    for (int i = 0; i < iterations; i++) {
        char message[64];
        generate_glucose_reading(message);  // Create new glucose reading

        // --- AES-GCM ENCRYPTION ---
        ctx = EVP_CIPHER_CTX_new();  // Create a new AES encryption context
        EVP_EncryptInit_ex(ctx, EVP_aes_128_gcm(), NULL, NULL, NULL);
        EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_GCM_SET_IVLEN, sizeof(aes_iv), NULL);  // Set IV length
        EVP_EncryptInit_ex(ctx, NULL, NULL, aes_key, aes_iv);  // Set key and IV
        EVP_EncryptUpdate(ctx, NULL, &len, ad, strlen((char*)ad));  // Encrypt AAD (Associated Data)
        EVP_EncryptUpdate(ctx, ct_aes, &len, (unsigned char*)message, strlen(message));  // Encrypt message
        ctlen_aes = len;
        EVP_EncryptFinal_ex(ctx, ct_aes + len, &len);  // Finalize encryption
        ctlen_aes += len;
        EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_GCM_GET_TAG, sizeof(aes_tag), aes_tag);  // Get auth tag
        EVP_CIPHER_CTX_free(ctx);  // Clean up context

        // --- AES-GCM DECRYPTION ---
        ctx = EVP_CIPHER_CTX_new();
        EVP_DecryptInit_ex(ctx, EVP_aes_128_gcm(), NULL, NULL, NULL);
        EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_GCM_SET_IVLEN, sizeof(aes_iv), NULL);
        EVP_DecryptInit_ex(ctx, NULL, NULL, aes_key, aes_iv);
        EVP_DecryptUpdate(ctx, NULL, &len, ad, strlen((char*)ad));  // Provide AAD
        EVP_DecryptUpdate(ctx, pt_aes, &len, ct_aes, ctlen_aes);  // Decrypt message
        ptlen_aes = len;
        EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_GCM_SET_TAG, sizeof(aes_tag), aes_tag);  // Set expected tag
        EVP_DecryptFinal_ex(ctx, pt_aes + len, &len);  // Finalize decryption
        ptlen_aes += len;
        EVP_CIPHER_CTX_free(ctx);

        pt_aes[ptlen_aes] = '\0';  // Null-terminate decrypted message

        // Compare with original
        if (strcmp(message, (char*)pt_aes) == 0) {
            aes_correct++;
        }
    }

    clock_gettime(CLOCK_MONOTONIC, &end);
    mem_after = get_memory_kb();  // Memory after AES-GCM operations

    // --- Report AES-GCM performance and correctness ---
    printf("AES-GCM (10,000 ops)\n");
    printf("  Time:   %.6f sec\n", time_diff(start, end));
    printf("  Memory: %ld KB\n", mem_after - mem_before);
    printf("  Correct decryptions: %d / %d\n", aes_correct, iterations);

    return 0;
}
