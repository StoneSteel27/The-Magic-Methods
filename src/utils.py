# -*- coding: utf-8 -*-

import PIL.Image


def compress_image(image: PIL.Image, compress_ratio: float = 0.5) -> PIL.Image:
    """Compress the image"""
    assert compress_ratio <= 1 and compress_ratio > 0
    new_width = int(image.width * compress_ratio)
    new_height = int(image.height * compress_ratio)
    compressed_image = image.resize((new_width, new_height))
    return compressed_image


def scale_image(image: PIL.Image, scale_ratio: float = 1.5) -> PIL.Image:
    """Scale the Image"""
    assert scale_ratio >= 1
    new_width = int(image.width * scale_ratio)
    new_height = int(image.height * scale_ratio)
    scaled_image = image.resize((new_width, new_height))
    return scaled_image
