"""Implements decoder function"""

import numpy as np
import PIL.Image

from .constants import (
    HEADER_SIZE, MAGIC_NUMBER, USED_BITS_MASK, USED_BITS_PER_BYTE
)


def decode(image: PIL.Image.Image):
    """Extracts the text from encoded image"""
    # loads the image and retrieves encoded chunks from the image
    image_array = np.array(image)
    flattened_array = image_array.flatten()
    chunks = np.bitwise_and(flattened_array, USED_BITS_MASK)

    # tests for checking if the stored data is damaged
    magic_number_test = 0
    for i, off in zip(range(4), range(12, -1, -4)):
        magic_number_test |= chunks[i] << off
    if magic_number_test != MAGIC_NUMBER:
        raise ValueError("magic number does not match")

    # reads stored header data
    code_length = 0
    for i, off in zip(range(4, 12), range(28, -1, -4)):
        code_length |= chunks[i] << off

    # removing header data
    chunks_per_character = 8 // USED_BITS_PER_BYTE
    num_code_chunks = code_length * chunks_per_character
    code_chunks = chunks[HEADER_SIZE:HEADER_SIZE + num_code_chunks]

    # convert chunk array to bytes of data
    code_chars = []
    for i in range(0, len(code_chunks), chunks_per_character):
        character = 0
        for character_chunk in code_chunks[i:i + chunks_per_character]:
            character = (character << USED_BITS_PER_BYTE) | character_chunk
        code_chars.append(character)

    # convert bytes to string
    decoded_text = bytes(code_chars).decode("ascii")

    return decoded_text
