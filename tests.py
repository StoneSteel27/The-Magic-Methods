# -*- coding: utf-8 -*-
import unittest
from src.encoder import encode
from src.decoder import decode
from src.utils import compress_image, scale_image


class EncoderDecoderTest(unittest.TestCase):
    def setUp(self):
        self.code = """
        for i in range(9):
            print(i)
        """

    def tearDown(self):
        del self.code

    def test_code_doesnt_change_after_encoding_decoding(self):
        """Encode the code in Image and decode it. The code decoded
        should not change"""
        image = encode(self.code)
        self.assertEqual(self.code, decode(image))

    def test_code_doesnt_change_after_img_compression(self):
        """Compress the encoded image and decode it. The code decoded
        should not change."""
        original_image = encode(self.code)
        compressed_image = compress_image(original_image)
        self.assertEqual(decode(original_image), decode(compressed_image))

    def test_code_doesnt_change_after_img_scaling(self):
        """Scale the encoded image and decode it. The code decoded
        should not change."""
        original_image = encode(self.code)
        scaled_image = scale_image(original_image)
        self.assertEqual(decode(original_image), decode(scaled_image))


if __name__ == "__main__":
    unittest.main()
