"""Global constants"""

MAGIC_NUMBER = 57764
USED_BITS_PER_BYTE = 4
USED_BITS_MASK = 0b1111

# header: magic number, length of code
# use second half of each byte of im[0, 0, :] (4 bytes / 2 = 16 bits) to store a magic number
# use second half of each byte of im[0, [1, 2], :] (8 bytes / 2 = 32 bits) to store length of code
HEADER_SIZE = 12
