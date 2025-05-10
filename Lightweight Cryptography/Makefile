# Compiler and flags
CC = gcc
CFLAGS = -O3 -std=c99 -march=native
LDFLAGS = -lssl -lcrypto

# Directories
ASCON_DIR = ascon/crypto_aead/asconaead128/ref
INCLUDES = -I$(ASCON_DIR)

# Source files
SRCS = benchmark.c $(ASCON_DIR)/aead.c $(ASCON_DIR)/printstate.c
OBJS = $(SRCS:.c=.o)

# Output binary
OUTPUT = benchmark

# Default target
all: $(OUTPUT)

# Compilation rule for the final binary
$(OUTPUT): $(OBJS)
	$(CC) $(CFLAGS) $(INCLUDES) -o $(OUTPUT) $(OBJS) $(LDFLAGS)

# Rule for compiling .c to .o (object files)
%.o: %.c
	$(CC) $(CFLAGS) $(INCLUDES) -c $< -o $@

# Clean up compiled object files and binary
clean:
	rm -f $(OBJS) $(OUTPUT)

# Run the program
run: $(OUTPUT)
	./$(OUTPUT)

# To run everything, use `make run`
