# Fangzhou YU
# read binary file and write to text file
# adopted from ChatGpt, modified by Fangzhou Yu
def write_to_text_file(binary_data, filename):
    with open(filename, "w") as f:
        # Convert each byte to a sequence of 8 bits (0 or 1)
        bit_sequences = [format(b, "08b") for b in binary_data]
        # Join the sequences and write to the file
        f.write("".join(bit_sequences))


with open("random_bytes.bin", "rb") as binary_fp:
    binary_data = binary_fp.read()

write_to_text_file(binary_data, "binary_data.txt")

file = open("binary_data.txt", "r")
for line in file:
    print(len(line))
file.close()

