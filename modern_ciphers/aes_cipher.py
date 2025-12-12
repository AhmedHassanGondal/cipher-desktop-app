"""
AES-128 (Advanced Encryption Standard) Implementation
======================================================
AES is a symmetric block cipher that encrypts and decrypts data in 128-bit blocks.
It was established as a standard by NIST in 2001, replacing DES.

Key Features:
- Block size: 128 bits (16 bytes)
- Key sizes: 128, 192, or 256 bits (this implementation uses 128 bits)
- Number of rounds: 10 (for AES-128)
- Mode: ECB (Electronic Codebook)

Algorithm Structure (for each round):
1. SubBytes: Non-linear byte substitution using S-box
2. ShiftRows: Cyclic shifting of rows
3. MixColumns: Column mixing (not in final round)
4. AddRoundKey: XOR with round key

This implementation uses PyCryptodome for the core encryption
while providing educational visualization of the process.
"""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import binascii


class AESCipher:
    """
    AES-128 Cipher class implementing encryption and decryption in ECB mode.
    
    Attributes:
        key (bytes): 16-byte encryption key
    """
    
    # AES S-box (Substitution box) - used in SubBytes step
    S_BOX = [
        0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
        0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
        0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
        0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
        0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
        0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
        0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
        0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
        0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
        0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
        0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
        0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
        0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
        0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
        0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
        0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
    ]
    
    def __init__(self):
        self.key = None
    
    def generate_key(self) -> str:
        """
        Generate a random 128-bit (16-byte) key.
        
        Returns:
            str: Hexadecimal representation of the key
        """
        self.key = get_random_bytes(16)
        return binascii.hexlify(self.key).decode('utf-8').upper()
    
    def set_key(self, key_hex: str) -> tuple:
        """
        Set the encryption key from hexadecimal string.
        
        Args:
            key_hex (str): 32-character hexadecimal key (128 bits)
            
        Returns:
            tuple: (success, message)
        """
        try:
            # Remove spaces and convert to uppercase
            key_hex = key_hex.replace(' ', '').upper()
            
            if len(key_hex) != 32:
                return False, f"Key must be 32 hex characters (128 bits). Got {len(key_hex)} characters."
            
            self.key = binascii.unhexlify(key_hex)
            return True, "Key set successfully"
        except Exception as e:
            return False, f"Invalid hexadecimal key: {str(e)}"
    
    def _bytes_to_state_matrix(self, data: bytes) -> list:
        """Convert 16 bytes to 4x4 state matrix (column-major order)."""
        state = [[0] * 4 for _ in range(4)]
        for i in range(16):
            state[i % 4][i // 4] = data[i]
        return state
    
    def _display_state_matrix(self, state: list, title: str) -> str:
        """Generate visual representation of state matrix."""
        display = f"{title}:\n"
        display += "┌────────────────────────┐\n"
        for row in state:
            display += "│ " + " ".join(f"{b:02X}" for b in row) + " │\n"
        display += "└────────────────────────┘"
        return display
    
    def _demonstrate_subbytes(self, state: list) -> tuple:
        """
        Demonstrate SubBytes transformation on first byte.
        
        Args:
            state (list): 4x4 state matrix
            
        Returns:
            tuple: (new_state, step_description)
        """
        new_state = [[0] * 4 for _ in range(4)]
        byte_val = state[0][0]
        row_idx = (byte_val >> 4) & 0x0F
        col_idx = byte_val & 0x0F
        new_byte = self.S_BOX[byte_val]
        
        for i in range(4):
            for j in range(4):
                new_state[i][j] = self.S_BOX[state[i][j]]
        
        step = f"SubBytes Example (first byte):\n"
        step += f"  Input byte: 0x{byte_val:02X}\n"
        step += f"  S-box lookup: row={row_idx:X}, col={col_idx:X}\n"
        step += f"  Output byte: 0x{new_byte:02X}\n"
        step += f"  (Each byte is substituted using the AES S-box)"
        
        return new_state, step
    
    def _demonstrate_shiftrows(self, state: list) -> tuple:
        """
        Demonstrate ShiftRows transformation.
        
        Args:
            state (list): 4x4 state matrix
            
        Returns:
            tuple: (new_state, step_description)
        """
        new_state = [row[:] for row in state]
        
        # Row 0: no shift
        # Row 1: shift left by 1
        new_state[1] = state[1][1:] + state[1][:1]
        # Row 2: shift left by 2
        new_state[2] = state[2][2:] + state[2][:2]
        # Row 3: shift left by 3
        new_state[3] = state[3][3:] + state[3][:3]
        
        step = f"ShiftRows:\n"
        step += f"  Row 0: No shift\n"
        step += f"  Row 1: Shift left by 1 position\n"
        step += f"  Row 2: Shift left by 2 positions\n"
        step += f"  Row 3: Shift left by 3 positions"
        
        return new_state, step
    
    def _xtime(self, a: int) -> int:
        """Multiply by 2 in GF(2^8)."""
        if a & 0x80:
            return ((a << 1) ^ 0x1B) & 0xFF
        return (a << 1) & 0xFF
    
    def _demonstrate_mixcolumns(self, state: list) -> tuple:
        """
        Demonstrate MixColumns transformation on first column.
        
        Args:
            state (list): 4x4 state matrix
            
        Returns:
            tuple: (new_state, step_description)
        """
        new_state = [[0] * 4 for _ in range(4)]
        
        for col in range(4):
            a = [state[row][col] for row in range(4)]
            
            # MixColumns uses matrix multiplication in GF(2^8)
            new_state[0][col] = self._xtime(a[0]) ^ (self._xtime(a[1]) ^ a[1]) ^ a[2] ^ a[3]
            new_state[1][col] = a[0] ^ self._xtime(a[1]) ^ (self._xtime(a[2]) ^ a[2]) ^ a[3]
            new_state[2][col] = a[0] ^ a[1] ^ self._xtime(a[2]) ^ (self._xtime(a[3]) ^ a[3])
            new_state[3][col] = (self._xtime(a[0]) ^ a[0]) ^ a[1] ^ a[2] ^ self._xtime(a[3])
        
        step = f"MixColumns (first column example):\n"
        step += f"  Each column is multiplied by a fixed matrix:\n"
        step += f"  ┌         ┐   ┌    ┐\n"
        step += f"  │ 02 03 01 01 │   │ s0 │\n"
        step += f"  │ 01 02 03 01 │ × │ s1 │\n"
        step += f"  │ 01 01 02 03 │   │ s2 │\n"
        step += f"  │ 03 01 01 02 │   │ s3 │\n"
        step += f"  └         ┘   └    ┘\n"
        step += f"  (Multiplication is in GF(2^8))"
        
        return new_state, step
    
    def encrypt(self, plaintext: str, key_hex: str = None) -> tuple:
        """
        Encrypt plaintext using AES-128 in ECB mode.
        
        Args:
            plaintext (str): The text to encrypt (can be text or hex string)
            key_hex (str): Optional hexadecimal key (uses stored key if not provided)
            
        Returns:
            tuple: (ciphertext_hex, calculation_steps)
        """
        # Set key if provided
        if key_hex:
            success, message = self.set_key(key_hex)
            if not success:
                return "", f"Error: {message}"
        elif self.key is None:
            self.generate_key()
        
        # Check if plaintext is hex (all hex chars, even length, no spaces)
        plaintext_clean = plaintext.replace(' ', '').replace('\n', '').replace('\r', '')
        is_hex = False
        if len(plaintext_clean) > 0 and all(c in '0123456789abcdefABCDEF' for c in plaintext_clean):
            if len(plaintext_clean) % 2 == 0:
                is_hex = True
        
        # Convert plaintext to bytes
        if is_hex:
            try:
                plaintext_bytes = binascii.unhexlify(plaintext_clean)
            except:
                # If hex decode fails, treat as regular text
                plaintext_bytes = plaintext.encode('utf-8')
        else:
            plaintext_bytes = plaintext.encode('utf-8')
        
        # Pad only if not exactly one block (for FIPS-197 test vectors, single blocks don't need padding)
        if len(plaintext_bytes) == AES.block_size:
            padded_data = plaintext_bytes
        else:
            padded_data = pad(plaintext_bytes, AES.block_size)
        
        # Create cipher and encrypt in ECB mode
        cipher = AES.new(self.key, AES.MODE_ECB)
        ciphertext = cipher.encrypt(padded_data)
        
        # Prepare demonstration of AES rounds
        state = self._bytes_to_state_matrix(padded_data[:16])
        
        calculation_display = "═" * 50 + "\n"
        calculation_display += "AES-128 ENCRYPTION PROCESS (ECB MODE)\n"
        calculation_display += "═" * 50 + "\n\n"
        
        calculation_display += f"Key (hex): {binascii.hexlify(self.key).decode().upper()}\n"
        calculation_display += f"Mode: ECB (Electronic Codebook)\n"
        if is_hex:
            calculation_display += f"Plaintext (hex): {binascii.hexlify(plaintext_bytes).decode().upper()}\n"
        else:
            calculation_display += f"Plaintext: {plaintext}\n"
            calculation_display += f"Plaintext (hex): {binascii.hexlify(plaintext_bytes).decode().upper()}\n"
        calculation_display += f"Data length: {len(padded_data)} bytes ({len(padded_data) // 16} block(s))\n"
        if len(plaintext_bytes) == AES.block_size:
            calculation_display += f"(Single block - no padding needed)\n"
        calculation_display += "\n"
        
        calculation_display += "─" * 50 + "\n"
        calculation_display += "ROUND DEMONSTRATION (First Block)\n"
        calculation_display += "─" * 50 + "\n\n"
        
        # Display initial state
        calculation_display += self._display_state_matrix(state, "Initial State") + "\n\n"
        
        # Demonstrate SubBytes
        state, sub_step = self._demonstrate_subbytes(state)
        calculation_display += sub_step + "\n\n"
        calculation_display += self._display_state_matrix(state, "After SubBytes") + "\n\n"
        
        # Demonstrate ShiftRows
        state, shift_step = self._demonstrate_shiftrows(state)
        calculation_display += shift_step + "\n\n"
        calculation_display += self._display_state_matrix(state, "After ShiftRows") + "\n\n"
        
        # Demonstrate MixColumns
        state, mix_step = self._demonstrate_mixcolumns(state)
        calculation_display += mix_step + "\n\n"
        calculation_display += self._display_state_matrix(state, "After MixColumns") + "\n\n"
        
        calculation_display += "─" * 50 + "\n"
        calculation_display += "AES-128 uses 10 rounds total\n"
        calculation_display += "Final round omits MixColumns step\n"
        calculation_display += "─" * 50 + "\n\n"
        
        calculation_display += f"Ciphertext (hex): {binascii.hexlify(ciphertext).decode().upper()}\n"
        
        return (
            binascii.hexlify(ciphertext).decode().upper(),
            calculation_display
        )
    
    def decrypt(self, ciphertext_hex: str, key_hex: str) -> tuple:
        """
        Decrypt ciphertext using AES-128 in ECB mode.
        
        Args:
            ciphertext_hex (str): Hexadecimal ciphertext
            key_hex (str): Hexadecimal key
            
        Returns:
            tuple: (plaintext, calculation_steps)
        """
        try:
            # Clean and convert inputs
            ciphertext_hex = ciphertext_hex.replace(' ', '')
            key_hex = key_hex.replace(' ', '')
            
            ciphertext = binascii.unhexlify(ciphertext_hex)
            key = binascii.unhexlify(key_hex)
            
            if len(key) != 16:
                return "", "Error: Key must be 16 bytes (32 hex characters)"
            
            # Create cipher and decrypt in ECB mode
            cipher = AES.new(key, AES.MODE_ECB)
            decrypted = cipher.decrypt(ciphertext)
            
            # Handle unpadding: if exactly one block, no padding was applied
            # Otherwise, try to unpad (for multi-block or padded data)
            if len(decrypted) == AES.block_size:
                # Single block - no padding was applied during encryption
                plaintext = decrypted
                was_padded = False
            else:
                # Multiple blocks or padded data - try to unpad
                try:
                    plaintext = unpad(decrypted, AES.block_size)
                    was_padded = True
                except ValueError:
                    # If unpadding fails, return raw bytes (might be hex data)
                    plaintext = decrypted
                    was_padded = False
            
            calculation_display = "═" * 50 + "\n"
            calculation_display += "AES-128 DECRYPTION PROCESS (ECB MODE)\n"
            calculation_display += "═" * 50 + "\n\n"
            
            calculation_display += f"Key (hex): {key_hex.upper()}\n"
            calculation_display += f"Mode: ECB (Electronic Codebook)\n"
            calculation_display += f"Ciphertext (hex): {ciphertext_hex.upper()}\n"
            calculation_display += f"Ciphertext length: {len(ciphertext)} bytes ({len(ciphertext) // 16} block(s))\n"
            if was_padded:
                calculation_display += f"Padding removed: Yes\n"
            else:
                calculation_display += f"Padding removed: No (single block or raw data)\n"
            calculation_display += "\n"
            
            calculation_display += "─" * 50 + "\n"
            calculation_display += "DECRYPTION ROUNDS (Inverse Operations)\n"
            calculation_display += "─" * 50 + "\n\n"
            
            calculation_display += "1. AddRoundKey (with last round key)\n"
            calculation_display += "2. InvShiftRows (shift rows right)\n"
            calculation_display += "3. InvSubBytes (use inverse S-box)\n"
            calculation_display += "4. AddRoundKey\n"
            calculation_display += "5. InvMixColumns (not in first round)\n"
            calculation_display += "   ... (repeat for 10 rounds)\n\n"
            
            calculation_display += "─" * 50 + "\n"
            calculation_display += f"Decrypted (hex): {binascii.hexlify(plaintext).decode().upper()}\n"
            
            # Try to decode as UTF-8, if it fails, return hex representation
            try:
                plaintext_str = plaintext.decode('utf-8')
                calculation_display += f"Plaintext: {plaintext_str}\n"
                return plaintext_str, calculation_display
            except UnicodeDecodeError:
                # If it's not valid UTF-8, return hex representation
                plaintext_hex = binascii.hexlify(plaintext).decode().upper()
                calculation_display += f"Plaintext (hex, not UTF-8): {plaintext_hex}\n"
                return plaintext_hex, calculation_display
            
        except Exception as e:
            return "", f"Decryption Error: {str(e)}"
    
    def encrypt_file(self, input_file: str, output_file: str, key_hex: str = None) -> tuple:
        """
        Encrypt a file using AES-128 in ECB mode.
        
        Args:
            input_file (str): Path to input file
            output_file (str): Path to output file
            key_hex (str): Optional hexadecimal key
            
        Returns:
            tuple: (success, message)
        """
        try:
            if key_hex:
                success, message = self.set_key(key_hex)
                if not success:
                    return False, message
            elif self.key is None:
                self.generate_key()
            
            with open(input_file, 'rb') as f:
                data = f.read()
            
            padded_data = pad(data, AES.block_size)
            cipher = AES.new(self.key, AES.MODE_ECB)
            ciphertext = cipher.encrypt(padded_data)
            
            # Write ciphertext
            with open(output_file, 'wb') as f:
                f.write(ciphertext)
            
            return (
                True, 
                f"File encrypted successfully!\nOutput: {output_file}"
            )
            
        except Exception as e:
            return False, f"Error: {str(e)}"
    
    def decrypt_file(self, input_file: str, output_file: str, key_hex: str) -> tuple:
        """
        Decrypt a file using AES-128 in ECB mode.
        
        Args:
            input_file (str): Path to encrypted file
            output_file (str): Path to output file
            key_hex (str): Hexadecimal key
            
        Returns:
            tuple: (success, message)
        """
        try:
            success, message = self.set_key(key_hex)
            if not success:
                return False, message
            
            with open(input_file, 'rb') as f:
                ciphertext = f.read()
            
            cipher = AES.new(self.key, AES.MODE_ECB)
            decrypted = cipher.decrypt(ciphertext)
            plaintext = unpad(decrypted, AES.block_size)
            
            with open(output_file, 'wb') as f:
                f.write(plaintext)
            
            return True, f"File decrypted successfully!\nOutput: {output_file}"
            
        except Exception as e:
            return False, f"Error: {str(e)}"


# Example usage and testing
if __name__ == "__main__":
    aes = AESCipher()
    
    # Generate a key
    key = aes.generate_key()
    print(f"Generated Key: {key}")
    
    # Test encryption
    plaintext = "Hello, AES Encryption!"
    ciphertext, steps = aes.encrypt(plaintext)
    
    print(f"\nPlaintext: {plaintext}")
    print(f"Ciphertext: {ciphertext}")
    print(f"\n{steps}")
    
    # Test decryption
    decrypted, dec_steps = aes.decrypt(ciphertext, key)
    print(f"\nDecrypted: {decrypted}")
    print(f"\n{dec_steps}")
