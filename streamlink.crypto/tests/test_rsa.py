#!/usr/bin/env python
import base64
import logging
import unittest
import os.path
from mock import patch

log = logging.getLogger(__name__)

pkey = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDxXRQEYXnMrwbmhiJFK1hTNmMNSIatf25VDTepknGBiHzc"\
       "Br8VDw2wOWDhaLTOQ1uDm18zrzGprM+NYnIxXvgcNeQ0eEWx3YmPdRI01gNsl0nz5PEzHRkKiiTJ"\
       "xUuO1UgVt9YYAlrvVc77JnawN7nm3Yc9lQkC4B3JOBxXIYFai+Cq94WuNsiLLjM3FwpZuiMD55oY"\
       "UZ4abPP854+aH6fqS3Zzym8aTiO6v1AHpVQBl7Xj5/ZBhmYtOMh4q69ioI7aE669ZX3lEvIXGA54"\
       "i5yyXpo3YUom0+x34+gi/n+9dS9iOY80E6fQvmnPVEjefMBnyayJqfocwEaUvMuMeFhP"



class TestAES(unittest.TestCase):
    @patch("os.urandom")
    def test_encrypt(self, random):
        from Crypto.Cipher import PKCS1_v1_5
        from Crypto.PublicKey import RSA

        random.side_effect = lambda x: b'\x01' * x

        message = b'To be encrypted'

        key = RSA.importKey(pkey)
        cipher = PKCS1_v1_5.new(key)
        ciphertext = cipher.encrypt(message)
        self.assertEqual(
            b"b]\xea\xb9\xe9\x1d6\rJ\xca\xf2\xcf\x8aaE\nZ\rV\xc3\xc3\x9b\x06'0\x02\xaf\xa5\xcdllE\xcc}A,"
            b"-\xa5\xdc\xda\xaf\xc3\x9b\xff\xe6\x99\x07\xbe2\xba\x88\xa4\x92\xa9\xa8\xa2\xd8\xd9Z\xe6\xc0c\xc0\x0c"
            b"\xea\xbf\xc2\xc9\xec\x0enj\x0b7\xb0\xeb\x8e\x00\x89B\x1b\xff\xb1m\xa3\x01\xdd\xe4\xbb\xa3e\xfb\xcev\xb6"
            b"\xb6 \xc1s\xb9\x9b\x12\n.\xbbR\xa4o\xa0\xe9\x8d\xb0Px>\x9c;$\x02\x82\xfe\xd8\x05\x84\x08;\xfd\x93$\xc5"
            b"\xed\xaa\xf2\xd9\xe6n\xe5\xb7\x02\x12X\x8b\x97\xdaBJ\x94\x89Q\x9e#I\xd2\x12\xb8mF$\xeczF\xfd\x07\x8c"
            b"\x7f\x01\xdf\xa3\xa67Ndp\xf0VT\xa9]\xe7\xbf\xa2\xcaq\xc5Y\xba\x9e&\xa2\xc0D\xd7@\xc9\x98\x8f\x9eE\xc3$"
            b"\x84\xb7\xd9\xe4\xaf\x1c\xe8\xb4\xdd!\x92\xf4=\x83\xb3s\x9a3\x0e\nZZ'\xb5\xe6\xe4\xb7\xd2_\xb0O["
            b"\xd3\xee\xfe\x1a\xb9\x9d\xfb~:N\x83\x8d\x81\xf9\x00O\xa8v\x16}\xa34C?",
            ciphertext
        )

