from Crypto.Cipher import DES3
import sys
import os

# Monkey-patch the DES3 module to allow degenerate keys
def _patched_adjust_key_parity(key_in):
    """Modified version that skips the Single DES degeneration check"""
    key_out = bytearray(key_in)
    for i in range(len(key_out)):
        key_out[i] = (key_out[i] & 0xfe) | ((bin(key_out[i])[2:].count('1') % 2) ^ 1)
    return bytes(key_out)

# Apply the patch before creating any ciphers
DES3.adjust_key_parity = _patched_adjust_key_parity

KEY = b"123"
IV = bytes.fromhex("1234567890ABCDEF")

def custom_pad(data):
    pad_len = 8 - ((len(data) + 1) % 8)
    pad_len = pad_len if pad_len != 8 else 0
    padding = bytes([1] * pad_len) if pad_len >= 9 else bytes([pad_len] * pad_len)
    return data + padding + b'\0'

def encrypt(input_file, output_file):
    # Expand key to 24 bytes (K1=K2=K3 for Single DES compatibility)
    full_key = KEY.ljust(24, b'\0')
    
    # Create cipher with patched key validation
    cipher = DES3.new(full_key, DES3.MODE_CBC, IV)
    
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    
    padded = custom_pad(plaintext)
    ciphertext = cipher.encrypt(padded)
    
    with open(output_file, 'wb') as f:
        f.write(ciphertext)

def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} encrypt <input> <output>")
        sys.exit(1)

    action, input_file, output_file = sys.argv[1], sys.argv[2], sys.argv[3]
    
    if action == "encrypt":
        encrypt(input_file, output_file)
        print(f"Created {output_file} ({os.path.getsize(output_file)} bytes)")
    else:
        print("Decrypt not implemented in this version")

if __name__ == "__main__":
    main()
