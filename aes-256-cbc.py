from Crypto.Util.Padding import pad
import base64
import random
from base64 import b64decode, b64encode
from Crypto.Cipher import AES
# pip3 install pycryptodome
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def aes_encrypt(key, iv, payload):
    aes = AES.new(key.encode('utf-8'), AES.MODE_CBC,iv.encode('utf8'))
    pad_pkcs7 = pad(payload.encode('utf-8'), AES.block_size, style='pkcs7')
    encrypt_aes = aes.encrypt(pad_pkcs7)
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')
    encrypted_text_str = encrypted_text.replace("\n", "")
    return encrypted_text_str

def aes_decrypt(key, iv, garble):
    encrypted_text = b64decode(garble)
    cipher = AES.new(key=key.encode(), mode=AES.MODE_CBC, IV=iv.encode())
    decrypted_text = cipher.decrypt(encrypted_text)
    return unpad(decrypted_text).decode('utf-8')

if __name__ == '__main__':
    key = "fwA7SuUnwIC5cnz4ykoPjC3CwnNaQe06"
    iv = "SoU1ZJ67w6d4fQXa"
    payload = 'TESTDATA123456'

    encryption_result = aes_encrypt(key, iv, payload)
    print(encryption_result)
    
    garble = "pCfJ+Mi30ZBnGAN1Tz7fig=="
    decrypt_result = aes_decrypt(key, iv, garble)
    print(decrypt_result)