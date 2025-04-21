import requests
import binascii

# Method to get all values. Only run once and then saved the text values
"""
ciphertexts = set()

for i in range(100):
    ciphertext = requests.get("http://aes.cryptohack.org/stream_consciousness/encrypt").json()['ciphertext']
    ciphertexts.add(ciphertext)

for c in ciphertexts:
    print(c)
"""
ciphertexts = [
"46d3c0df392f2a4cb15df9cae2ffc59cf8fd5ee7f88b733f4d9900d3e56b13c4f5af",
"5dd4d7ce356e7a50bf4cecd1aef597d9c0f91beab0866f711a8c49d6ff240c85f9ee96106d6388dd86be50d533c4b7098d7f09f308d2a1e3994e3f42c972bcf0de9f5446d2cb5ff56b34e87ee5f58aafe875e09f50fbee1ff356f2c394",
#"50c881c27f6e4302b84fe993a3e2d1d9e3f80dfbb0966f3f5f9d49d4ff6b0fcdf4a193596e79999dd48e50df268af90e80",
#"46d3d88b7d212a56b84bf493a5e38896fab10ef2f98c7476539f49dcff2f5bc7e4e88d54607f8a9c95ab1c9c338cbb5ad5360cf940",
#"55c9c4d86a636743bb47e3d4e2edc69db4dc17fffc8b6e7a4f81",
"5fd48d8b5069664ef049e293abe2888dfbb13afcfc8e793f5c960d9de52e17c9b1e98442296299ce95ae17d433c4b10fd5",
"46d3c0df392f2a4ebf5aaddca4acdc91fdff19e0b096687e49d81dd5f4255bd6f4e48c556d3199d3d4aa159c348bfe17c02d17f9139ea6e387073245cc26a0f0d8c50e099bd156f22710b23be3e199eaa979e1dc5cfee253fe4ae4c4ddf45a751a9289bb1b5dddbd0a172e34709a2e27445de1e2045989b52d24ffafad74ff8b558cb9d6f8483a536b330c80698ab926c28c60014ad2df94af985011a85fd5",
"45d3c48b6d2b7850b94ce1d6e2f8c090faf65efae3c274775c8c49c9f92e5bd5f0f295106a70839b80e712d96790b108cf7f0ee90bd2abefd44e27588874baf1cdc254",
"589bd2c378226602bc41fed6e2e9de9ce6e80afbf98c673f5c960d9dff240f85f6e495106178809c96a613d769",
"72c9d8db6d217149e357b884b0bf9c94cbe34de6a5d15f2e08a70f89a67f17d8",
"589bd2c37822660ef067aadfaeacc496e7f45ef6e6877266499000d3f66b12c3b1e984106d7e88cf9ae0049c248bb31f813d00ff14dc",
"55d4cdc7606e7d4bbc42adc7aae5c692b4e516f2e4c2493850d805d8f03d12cbf6a180107a748ed39aa350d43297bc1bcf3b41fd1196e9e29c46270bdc6eb0ecdcd7151a979f7eb02600ed6fabf39afdec77fd9f51f6a71af904e3c5dfba44611c9f8ffb",
"45d3c4d87c6e624da25de8c0eeacdc91fde25ef0f19072765c9f0c9dbc6b13cae6a1a810657e8cc89ca250d13e97bb16c77f08f25f86a1ff8707304ada74bcffded45a45d2cb5ff53252ec7eabe183e3a973edcc08b3e506e304de8dc9f2527f1fd186b019148ffc17166b606c976b3e0c55e8e41e17ee",
"5eced3943919625bf041f8c1fd",
"41ded3c3783e7902b84baddba3ff8894fde20df6f4c2747758d81dcff0221585f0ef85106062cdde95a41b9c259dfe14ce284fbc2893a7e2d44a3c59cd26bdebd4d8160193cb5eff2554",
"589ccc8b6c206243a05ef49fe2c5889df1e21be1e687207649d449c9f92e5bc3f0f48d442e62cdd19da915906786ab0e811646f15f87a7fe955723528867b9f299c5120dd2cc56fd2e59be73eeec9fafe47eaa",
"58cf81c878202d56f04ce893b6e3da97b4fe0be7bcc2626a49d800c9b1281acbb1e38410607683d386a21492",
"53ced58b506e7d4bbc42adc0aae3dfd9fcf813bd",
"59d4d68b693c6557b40eecdda6acc098e4e107b3f887277351d80bd8b13c13c0ffa18955297688c887e71dc5678ab10ec47e",
"50d5c58b506e794ab142e193abebc696e6f45efae4cc",
"46d4d4c77d6e4302b84ffbd6e2eecd95fdf408f6f4c27477589649c9f92a0f85d8a1825f7c7d899c86a211df2fc4ad0fc23741f81a82bdfe87073c4d886ea0f3d0dd130986d658fe74"]


# Method to looop through each ciphertext and test it with the keysteam
def xor_all(ciphertexts, test_keystream):
    # If a letter is no ASCII, reject this keysteam
    for text_hex in ciphertexts:
        cipher = bytes.fromhex(text_hex)
        # Decrypt only up to the length of the test keystream
        for i in range(len(test_keystream)):
            if i >= len(cipher):
                break
            decrypted_byte = test_keystream[i] ^ cipher[i]

            # Check if decrypted byte is printable ASCII
            if not (32 <= decrypted_byte < 127):  
                # Incorrect keystream
                return False  # reject this keystream

            # Print for debugging
            print(chr(decrypted_byte), end='')
        print()
    # Keystream is correct
    return True


# Known beginning of the flag, upated with guessing next letters of values
#known_prefix = b'crypto{'
#known_prefix = b"Dolly will think that I'm leaving"
#known_prefix = b'The terrible'
#known_prefix = b'Love, probably'
#known_prefix = b'I shall lose everything an'
#known_prefix = b'What a lot of things that'
#known_prefix = b"I shall, I'll lose everyth"
#known_prefix = b'These horses, this carriage,'
#known_prefix = b"No, I'll go in to Dolly any"
#known_prefix = b'crypto{k3y57r34m_r3u53_15_f4'
#known_prefix = b'Perhaps he has missed the train'
known_prefix = b"Dolly will think that I'm leavin"



# The keystream
discovered_keystream = []

# Try each ciphertext as the one that could contain the flag
for text_hex in ciphertexts:
    cipher = bytes.fromhex(text_hex)

    # Attempt to guess the keystream using known prefix
    candidate_keystream = []
    for i in range(len(known_prefix)):
        candidate_keystream.append(known_prefix[i] ^ cipher[i])

    # Test the candidate keystream on all ciphertexts
    if xor_all(ciphertexts, candidate_keystream):
        # Update the keystream and exit loop
        discovered_keystream[:] = candidate_keystream
        break
