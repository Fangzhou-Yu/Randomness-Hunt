// adopted from ChatGpt, modified by Fangzhou Yu
// used to generate randombytes

#include <openssl/rand.h>
#include <stdio.h>

int main()
{
    FILE *fp;
    unsigned char random_bytes[350];

    // Step 1: Open the file
    fp = fopen("random_bytes.bin", "wb");
    if (fp == NULL) {
        return 1;
    }

    for (int i = 0; i < 1000; i++){
        

        // Step 2: Call RAND_bytes()
        if (RAND_bytes(random_bytes, sizeof(random_bytes)) != 1) {
            return 2;
        }

        size_t bytes_written = fwrite(random_bytes, sizeof(unsigned char), sizeof(random_bytes), fp);
        if (bytes_written != sizeof(random_bytes)) {
            // Handle error here
            return 3;
        }
    }

    // Step 4: Close the file
    fclose(fp);

    return 0;
}
