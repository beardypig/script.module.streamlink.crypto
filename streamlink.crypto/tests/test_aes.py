#!/usr/bin/env python
import logging
import unittest

log = logging.getLogger(__name__)


class TestAES(unittest.TestCase):
    def test_encrypt(self):
        from Crypto.Cipher import AES
        cipher = AES.new(b"0" * 16, AES.MODE_CBC, b"0" * 16)
        self.assertEqual(
            b'\x9d\xad~\xb0 P\xd6\x9c\xfe\x16\xee\x8e\xacB\x99(',
            cipher.encrypt(b"t" * 16))

    def test_decrypt(self):
        from Crypto.Cipher import AES
        cipher = AES.new(b"0" * 16, AES.MODE_CBC, b"0" * 16)
        self.assertEqual(
            b"t" * 16,
            cipher.decrypt(b'\x9d\xad~\xb0 P\xd6\x9c\xfe\x16\xee\x8e\xacB\x99('))


