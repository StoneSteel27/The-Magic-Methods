"""
Decode an image built by encoder.encode
"""

import numpy as np
import PIL.Image

from .constants import HEADER_SIZE, MAGIC_NUMBER, USED_BITS_MASK, USED_BITS_PER_BYTE


def decode(image: PIL.Image.Image):
    """
    Extract the text from an image built by encoder.encode
    """
    im_arr = np.array(image)
    flat = im_arr.flatten()
    chunks = np.bitwise_and(flat, USED_BITS_MASK)
    magic_test = 0
    for i, off in zip(range(4), range(12, -1, -4)):
        magic_test |= chunks[i] << off
    if magic_test != MAGIC_NUMBER:
        raise ValueError("magic number does not match")
    code_len = 0
    for i, off in zip(range(4, 12), range(28, -1, -4)):
        code_len |= chunks[i] << off
    chunks_per_char = 8 // USED_BITS_PER_BYTE
    num_code_chunks = code_len * chunks_per_char
    code_chunks = chunks[HEADER_SIZE:HEADER_SIZE + num_code_chunks]
    code_chars = []
    for i in range(0, len(code_chunks), chunks_per_char):
        char = 0
        for char_chunk in code_chunks[i:i + chunks_per_char]:
            # print(char_chunk)
            char = (char << USED_BITS_PER_BYTE) | char_chunk
        code_chars.append(char)
    return bytes(code_chars).decode("ascii")
