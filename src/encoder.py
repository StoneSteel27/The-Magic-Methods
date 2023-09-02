"""
Make a screenshot of the code with the text steganography'd in
"""

from io import BytesIO
from typing import Sequence

import numpy as np
import PIL.Image
from pygments import highlight
from pygments.formatters import get_formatter_by_name
from pygments.lexers import get_lexer_by_name

from .constants import HEADER_SIZE, MAGIC_NUMBER, USED_BITS_MASK, USED_BITS_PER_BYTE


def make_image(code: str, *, language: str = "python", **formatter_options) -> PIL.Image.Image:
    """
    Make a screenshot of the code
    """
    if not formatter_options:
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
    Split up each byte in given list,
    such that each element in the new list fits within USED_BITS_PER_BYTE bits
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
    Make a screenshot of the code with the text steganography'd in
    """
    image = make_image(code, **formatter_options)
    im_arr = np.array(image)
    code_bytes = code.encode(encoding="ascii")
    code_chunks = chunk(code_bytes)
    code_len = len(code_bytes)
    mask_arr = np.array(code_chunks, dtype=np.uint8)
    mask_arr = np.pad(
        mask_arr, (HEADER_SIZE, im_arr.size - mask_arr.size - HEADER_SIZE)
    )

    for i, off in zip(range(4), range(12, -1, -4)):
        mask_arr[i] = (MAGIC_NUMBER >> off) & USED_BITS_MASK
    for i, off in zip(range(4, 12), range(28, -1, -4)):
        mask_arr[i] = (code_len >> off) & USED_BITS_MASK
    mask_arr = mask_arr.reshape(im_arr.shape)

    steg_im_arr = np.bitwise_or(
        np.bitwise_and(im_arr, ~np.uint8(USED_BITS_MASK)), mask_arr
    )
    steg_im = PIL.Image.fromarray(steg_im_arr)
    return steg_im
