#!/usr/bin/env python
import base64
import logging
import unittest

log = logging.getLogger(__name__)


class TestAES(unittest.TestCase):
    def test_encrypt(self):
        from Crypto.Cipher import Blowfish
        key = base64.b64decode("eWVMJmRhRDM=")
        cipher = Blowfish.new(key, Blowfish.MODE_ECB)

        self.assertEqual(
            b'\xdbI\xca\x904\xee\xff\x8b',
            cipher.encrypt(b"test1234"))

    def test_decrypt(self):
        from Crypto.Cipher import Blowfish
        key = base64.b64decode("eWVMJmRhRDM=")
        cipher = Blowfish.new(key, Blowfish.MODE_ECB)

        self.assertEqual(
            b"test1234",
            cipher.decrypt(b'\xdbI\xca\x904\xee\xff\x8b'))
