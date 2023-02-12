# Makefile for generating random bytes
#
# Fangzhou Yu
# CS 62, Winter 2023
 
CC=gcc
OBJS = randBytes.o
MAKE = make
CC = gcc

randBytes: randBytes.o
	gcc randBytes.o -o randBytes -lcrypto

randBytes.o: randBytes.c
	gcc -c randBytes.c -o randBytes.o -lcrypto

test: randBytes
	./randBytes

# clean up after our compilation
clean:
	rm -f core
	rm -f *~ *.o
	rm -f randBytes random_bytes.txt
