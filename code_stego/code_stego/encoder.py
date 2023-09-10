"""Implements the main encoder function, and its helper functions"""

from io import BytesIO
from typing import Sequence

import numpy as np
import PIL.Image
from pygments import highlight
from pygments.formatters import get_formatter_by_name
from pygments.lexers import get_lexer_by_name

from .constants import (
    HEADER_SIZE, MAGIC_NUMBER, USED_BITS_MASK, USED_BITS_PER_BYTE
)


def make_image(code: str, *, language: str = "python", **formatter_options) -> PIL.Image.Image:
    """
    Generates image of the provided source code

    :param code: source code, to be converted into image
    :param language: programming language of source code
    :param formatter_options: custom formatter options
    :return: Image of source code
    """
    if not formatter_options:
        # default formatter option
        formatter_options = dict(
            style="lightbulb",
            line_number_bg=None,
            line_number_separator=True,
            line_number_pad=10,
            image_pad=20,
        )
    lexer = get_lexer_by_name(language)
    formatter = get_formatter_by_name("png", **formatter_options)
    result = highlight(code, lexer, formatter)
    return PIL.Image.open(BytesIO(result)).convert("RGBA")


def chunk(data: Sequence[int]):
    """
    Splits given byte array into array of bit chunks

    Size of each chunk is determined by USED_BITS_PER_BYTE
    """
    assert 8 % USED_BITS_PER_BYTE == 0
    chunks = []
    for byte in data:
        group = []
        for _ in range(8 // USED_BITS_PER_BYTE):
            group.append(byte & USED_BITS_MASK)
            byte >>= USED_BITS_PER_BYTE
        chunks.extend(reversed(group))
    return chunks


def encode(code: str, **formatter_options) -> PIL.Image.Image:
    """
    Stores source code data into generated image of source code

    This function uses LSB(Least Significant Bit) Steganography algorithm to
    store the source code into the generated Image of the source code
    """
    # create the image of source code
    image = make_image(code, **formatter_options)
    image_array = np.array(image)

    # encode and chunk the source code to bytes via ascii encoding
    code_bytes = code.encode(encoding="ascii")
    data_chunks = chunk(code_bytes)
    length_of_code = len(code_bytes)

    # initialise mask array from data, and create space for header
    mask_array = np.array(data_chunks, dtype=np.uint8)
    mask_array = np.pad(
        mask_array, (HEADER_SIZE, image_array.size - mask_array.size - HEADER_SIZE)
    )

    # store header data in mask array
    for i, off in zip(range(4), range(12, -1, -4)):
        mask_array[i] = (MAGIC_NUMBER >> off) & USED_BITS_MASK
    for i, off in zip(range(4, 12), range(28, -1, -4)):
        mask_array[i] = (length_of_code >> off) & USED_BITS_MASK
    mask_array = mask_array.reshape(image_array.shape)

    # make space in image for header and data
    accommodate_image_array = np.bitwise_and(image_array, ~np.uint8(USED_BITS_MASK))

    # store the mask array into image
    encoded_image_array = np.bitwise_or(accommodate_image_array, mask_array)

    encoded_image = PIL.Image.fromarray(encoded_image_array)
    return encoded_image
