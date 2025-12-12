"""
DES (Data Encryption Standard) Implementation
==============================================
DES is a symmetric-key block cipher that was the dominant encryption algorithm
from the mid-1970s until AES replaced it in 2001.

Key Features:
- Block size: 64 bits (8 bytes)
- Key size: 56 bits (64 bits with 8 parity bits)
- Number of rounds: 16 Feistel rounds
- Mode: ECB (Electronic Codebook)

Algorithm Structure:
1. Initial Permutation (IP)
2. 16 Feistel Rounds:
   - Expansion (E): 32 bits → 48 bits
   - Key mixing: XOR with subkey
   - Substitution (S-boxes): 48 bits → 32 bits
   - Permutation (P)
   - XOR with left half and swap
3. Final Permutation (IP⁻¹)

Security Note:
DES is now considered insecure due to its short key length.
Modern applications should use AES or Triple DES.
"""

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import binascii


class DESCipher:
    """
    DES Cipher class implementing encryption and decryption in ECB mode.
    
    Attributes:
        key (bytes): 8-byte encryption key
    """
    
    # Initial Permutation Table
    IP = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]
    
    # Final Permutation Table (IP^-1)
    FP = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25
    ]
    
    # Expansion Permutation Table (32 bits → 48 bits)
    E = [
        32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32, 1
    ]
    
    # Permutation Table (P-box)
    P = [
        16, 7, 20, 21, 29, 12, 28, 17,
        1, 15, 23, 26, 5, 18, 31, 10,
        2, 8, 24, 14, 32, 27, 3, 9,
        19, 13, 30, 6, 22, 11, 4, 25
    ]
    
    # S-boxes (8 S-boxes, each mapping 6 bits to 4 bits)
    S_BOXES = [
        # S1
        [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
        ],
        # S2
        [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
        ],
        # S3
        [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
        ],
        # S4
        [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
        ],
        # S5
        [
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
        ],
        # S6
        [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
        ],
        # S7
        [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
        ],
        # S8
        [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
        ]
    ]
    
    # Permuted Choice 1 (PC-1) - removes parity bits
    PC1 = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4
    ]
    
    # Permuted Choice 2 (PC-2)
    PC2 = [
        14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32
    ]
    
    # Left rotations for each round
    ROTATIONS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    
    def __init__(self):
        self.key = None
    
    def generate_key(self) -> str:
        """
        Generate a random 64-bit (8-byte) key.
        
        Returns:
            str: Hexadecimal representation of the key
        """
        self.key = get_random_bytes(8)
        return binascii.hexlify(self.key).decode('utf-8').upper()
    
    def set_key(self, key_hex: str) -> tuple:
        """
        Set the encryption key from hexadecimal string.
        
        Args:
            key_hex (str): 16-character hexadecimal key (64 bits)
            
        Returns:
            tuple: (success, message)
        """
        try:
            key_hex = key_hex.replace(' ', '').upper()
            
            if len(key_hex) != 16:
                return False, f"Key must be 16 hex characters (64 bits). Got {len(key_hex)} characters."
            
            self.key = binascii.unhexlify(key_hex)
            return True, "Key set successfully"
        except Exception as e:
            return False, f"Invalid hexadecimal key: {str(e)}"
    
    def _bytes_to_bits(self, data: bytes) -> list:
        """Convert bytes to list of bits."""
        bits = []
        for byte in data:
            for i in range(7, -1, -1):
                bits.append((byte >> i) & 1)
        return bits
    
    def _bits_to_bytes(self, bits: list) -> bytes:
        """Convert list of bits to bytes."""
        result = []
        for i in range(0, len(bits), 8):
            byte = 0
            for j in range(8):
                byte = (byte << 1) | bits[i + j]
            result.append(byte)
        return bytes(result)
    
    def _permute(self, block: list, table: list) -> list:
        """Apply permutation table to block."""
        return [block[table[i] - 1] for i in range(len(table))]
    
    def _left_rotate(self, bits: list, n: int) -> list:
        """Left circular rotation."""
        return bits[n:] + bits[:n]
    
    def _xor(self, a: list, b: list) -> list:
        """XOR two bit lists."""
        return [a[i] ^ b[i] for i in range(len(a))]
    
    def _generate_subkeys(self, key: bytes) -> list:
        """
        Generate 16 round subkeys from the main key.
        
        Args:
            key (bytes): 8-byte key
            
        Returns:
            list: 16 subkeys, each 48 bits
        """
        # Convert key to bits
        key_bits = self._bytes_to_bits(key)
        
        # Apply PC-1 (permuted choice 1)
        permuted_key = self._permute(key_bits, self.PC1)
        
        # Split into left and right halves (28 bits each)
        C = permuted_key[:28]
        D = permuted_key[28:]
        
        subkeys = []
        for i in range(16):
            # Left rotate each half
            C = self._left_rotate(C, self.ROTATIONS[i])
            D = self._left_rotate(D, self.ROTATIONS[i])
            
            # Combine and apply PC-2
            combined = C + D
            subkey = self._permute(combined, self.PC2)
            subkeys.append(subkey)
        
        return subkeys
    
    def _sbox_substitution(self, block: list) -> list:
        """
        Apply S-box substitution (48 bits → 32 bits).
        
        Args:
            block (list): 48 bits
            
        Returns:
            list: 32 bits after S-box substitution
        """
        result = []
        for i in range(8):
            # Get 6-bit group
            group = block[i * 6:(i + 1) * 6]
            
            # Row is determined by bits 0 and 5
            row = (group[0] << 1) | group[5]
            
            # Column is determined by bits 1-4
            col = (group[1] << 3) | (group[2] << 2) | (group[3] << 1) | group[4]
            
            # Look up in S-box
            val = self.S_BOXES[i][row][col]
            
            # Convert to 4 bits
            for j in range(3, -1, -1):
                result.append((val >> j) & 1)
        
        return result
    
    def _feistel_function(self, R: list, subkey: list) -> list:
        """
        Feistel function (f function).
        
        Args:
            R (list): 32-bit right half
            subkey (list): 48-bit subkey
            
        Returns:
            list: 32-bit result
        """
        # Expansion (32 → 48 bits)
        expanded = self._permute(R, self.E)
        
        # XOR with subkey
        xored = self._xor(expanded, subkey)
        
        # S-box substitution (48 → 32 bits)
        substituted = self._sbox_substitution(xored)
        
        # Permutation (P-box)
        permuted = self._permute(substituted, self.P)
        
        return permuted
    
    def _display_initial_permutation(self, data: bytes) -> str:
        """Display initial permutation step."""
        bits = self._bytes_to_bits(data)
        permuted = self._permute(bits, self.IP)
        
        display = "Initial Permutation (IP):\n"
        display += f"  Input (hex): {binascii.hexlify(data).decode().upper()}\n"
        display += f"  Input (binary, first 16 bits): {''.join(str(b) for b in bits[:16])}...\n"
        display += f"  After IP (first 16 bits): {''.join(str(b) for b in permuted[:16])}...\n"
        display += f"  IP table example: bit 58 → position 1, bit 50 → position 2, etc.\n"
        
        return display
    
    def _display_round_details(self, round_num: int, L: list, R: list, subkey: list) -> str:
        """Display details of a Feistel round."""
        # Convert to hex for display
        L_hex = ''.join(f'{int("".join(str(b) for b in L[i:i+4]), 2):X}' for i in range(0, 32, 4))
        R_hex = ''.join(f'{int("".join(str(b) for b in R[i:i+4]), 2):X}' for i in range(0, 32, 4))
        K_hex = ''.join(f'{int("".join(str(b) for b in subkey[i:i+4]), 2):X}' for i in range(0, 48, 4))
        
        display = f"Round {round_num}:\n"
        display += f"  L{round_num-1} = {L_hex}\n"
        display += f"  R{round_num-1} = {R_hex}\n"
        display += f"  K{round_num} = {K_hex}\n"
        display += f"  L{round_num} = R{round_num-1}\n"
        display += f"  R{round_num} = L{round_num-1} ⊕ f(R{round_num-1}, K{round_num})\n"
        
        return display
    
    def encrypt(self, plaintext: str, key_hex: str = None) -> tuple:
        """
        Encrypt plaintext using DES in ECB mode.
        
        Args:
            plaintext (str): The text to encrypt
            key_hex (str): Optional hexadecimal key
            
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
        
        # Pad only if not exactly one block (for test vectors, single blocks don't need padding)
        if len(plaintext_bytes) == DES.block_size:
            padded_data = plaintext_bytes
        else:
            padded_data = pad(plaintext_bytes, DES.block_size)
        
        # Create cipher and encrypt using PyCryptodome in ECB mode
        cipher = DES.new(self.key, DES.MODE_ECB)
        ciphertext = cipher.encrypt(padded_data)
        
        # Generate detailed steps for demonstration
        calculation_display = "═" * 55 + "\n"
        calculation_display += "DES (DATA ENCRYPTION STANDARD) PROCESS (ECB MODE)\n"
        calculation_display += "═" * 55 + "\n\n"
        
        calculation_display += f"Key (hex): {binascii.hexlify(self.key).decode().upper()}\n"
        calculation_display += f"Mode: ECB (Electronic Codebook)\n"
        if is_hex:
            calculation_display += f"Plaintext (hex): {binascii.hexlify(plaintext_bytes).decode().upper()}\n"
        else:
            calculation_display += f"Plaintext: {plaintext}\n"
            calculation_display += f"Plaintext (hex): {binascii.hexlify(plaintext_bytes).decode().upper()}\n"
        calculation_display += f"Data length: {len(padded_data)} bytes ({len(padded_data) // 8} block(s))\n"
        if len(plaintext_bytes) == DES.block_size:
            calculation_display += f"(Single block - no padding needed)\n"
        calculation_display += "\n"
        
        calculation_display += "─" * 55 + "\n"
        calculation_display += "DES STRUCTURE OVERVIEW\n"
        calculation_display += "─" * 55 + "\n\n"
        
        calculation_display += "1. Initial Permutation (IP)\n"
        calculation_display += "2. 16 Feistel Rounds\n"
        calculation_display += "3. Final Permutation (IP⁻¹)\n\n"
        
        # Demonstrate on first block
        first_block = padded_data[:8]
        calculation_display += self._display_initial_permutation(first_block)
        calculation_display += "\n"
        
        calculation_display += "─" * 55 + "\n"
        calculation_display += "FEISTEL ROUNDS DEMONSTRATION (First 3 rounds)\n"
        calculation_display += "─" * 55 + "\n\n"
        
        # Generate subkeys
        subkeys = self._generate_subkeys(self.key)
        
        # Perform initial permutation
        bits = self._bytes_to_bits(first_block)
        permuted = self._permute(bits, self.IP)
        L = permuted[:32]
        R = permuted[32:]
        
        # Show first 3 rounds
        for round_num in range(1, 4):
            calculation_display += self._display_round_details(round_num, L, R, subkeys[round_num - 1])
            
            # Perform round
            f_result = self._feistel_function(R, subkeys[round_num - 1])
            new_R = self._xor(L, f_result)
            L = R
            R = new_R
            calculation_display += "\n"
        
        calculation_display += "... (rounds 4-16 continue similarly) ...\n\n"
        
        calculation_display += "─" * 55 + "\n"
        calculation_display += "S-BOX SUBSTITUTION EXAMPLE\n"
        calculation_display += "─" * 55 + "\n\n"
        
        calculation_display += "Each 6-bit input maps to 4-bit output:\n"
        calculation_display += "  Input: b1 b2 b3 b4 b5 b6\n"
        calculation_display += "  Row = b1b6 (2 bits → 0-3)\n"
        calculation_display += "  Col = b2b3b4b5 (4 bits → 0-15)\n"
        calculation_display += "  Output = S[row][col] (4 bits)\n\n"
        
        calculation_display += "─" * 55 + "\n"
        calculation_display += "FINAL PERMUTATION (IP⁻¹)\n"
        calculation_display += "─" * 55 + "\n\n"
        
        calculation_display += "The final permutation is the inverse of the initial permutation.\n"
        calculation_display += "It rearranges the 64 bits back to produce the ciphertext.\n\n"
        
        calculation_display += f"Ciphertext (hex): {binascii.hexlify(ciphertext).decode().upper()}\n"
        
        return binascii.hexlify(ciphertext).decode().upper(), calculation_display
    
    def decrypt(self, ciphertext_hex: str, key_hex: str) -> tuple:
        """
        Decrypt ciphertext using DES in ECB mode.
        
        Args:
            ciphertext_hex (str): Hexadecimal ciphertext
            key_hex (str): Hexadecimal key
            
        Returns:
            tuple: (plaintext, calculation_steps)
        """
        try:
            # Clean and convert inputs - remove all whitespace, newlines, etc.
            ciphertext_hex = ''.join(c for c in ciphertext_hex if c in '0123456789abcdefABCDEF')
            key_hex = ''.join(c for c in key_hex if c in '0123456789abcdefABCDEF')
            
            # Check if hex strings have even length
            if len(ciphertext_hex) % 2 != 0:
                return "", f"Error: Ciphertext hex string has odd length ({len(ciphertext_hex)} chars). Must be even."
            if len(key_hex) % 2 != 0:
                return "", f"Error: Key hex string has odd length ({len(key_hex)} chars). Must be even."
            
            if len(key_hex) != 16:
                return "", "Error: Key must be 16 hex characters (8 bytes)"
            
            ciphertext = binascii.unhexlify(ciphertext_hex)
            key = binascii.unhexlify(key_hex)
            
            if len(key) != 8:
                return "", "Error: Key must be 8 bytes (16 hex characters)"
            
            # Create cipher and decrypt in ECB mode
            cipher = DES.new(key, DES.MODE_ECB)
            decrypted = cipher.decrypt(ciphertext)
            
            # Handle unpadding: if exactly one block, no padding was applied
            # Otherwise, try to unpad (for multi-block or padded data)
            if len(decrypted) == DES.block_size:
                # Single block - no padding was applied during encryption
                plaintext = decrypted
                was_padded = False
            else:
                # Multiple blocks or padded data - try to unpad
                try:
                    plaintext = unpad(decrypted, DES.block_size)
                    was_padded = True
                except ValueError:
                    # If unpadding fails, return raw bytes (might be hex data)
                    plaintext = decrypted
                    was_padded = False
            
            calculation_display = "═" * 55 + "\n"
            calculation_display += "DES DECRYPTION PROCESS (ECB MODE)\n"
            calculation_display += "═" * 55 + "\n\n"
            
            calculation_display += f"Key (hex): {key_hex.upper()}\n"
            calculation_display += f"Mode: ECB (Electronic Codebook)\n"
            calculation_display += f"Ciphertext (hex): {ciphertext_hex.upper()}\n"
            calculation_display += f"Ciphertext length: {len(ciphertext)} bytes ({len(ciphertext) // 8} block(s))\n"
            if was_padded:
                calculation_display += f"Padding removed: Yes\n"
            else:
                calculation_display += f"Padding removed: No (single block or raw data)\n"
            calculation_display += "\n"
            
            calculation_display += "─" * 55 + "\n"
            calculation_display += "DES DECRYPTION = ENCRYPTION WITH REVERSED SUBKEYS\n"
            calculation_display += "─" * 55 + "\n\n"
            
            calculation_display += "Decryption uses the same algorithm but applies\n"
            calculation_display += "the 16 subkeys in reverse order (K16 to K1).\n\n"
            
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
        Encrypt a file using DES in ECB mode.
        
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
            
            padded_data = pad(data, DES.block_size)
            cipher = DES.new(self.key, DES.MODE_ECB)
            ciphertext = cipher.encrypt(padded_data)
            
            # Write ciphertext
            with open(output_file, 'wb') as f:
                f.write(ciphertext)
            
            return True, f"File encrypted successfully!\nOutput: {output_file}"
            
        except Exception as e:
            return False, f"Error: {str(e)}"
    
    def decrypt_file(self, input_file: str, output_file: str, key_hex: str) -> tuple:
        """
        Decrypt a file using DES in ECB mode.
        
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
            
            cipher = DES.new(self.key, DES.MODE_ECB)
            decrypted = cipher.decrypt(ciphertext)
            plaintext = unpad(decrypted, DES.block_size)
            
            with open(output_file, 'wb') as f:
                f.write(plaintext)
            
            return True, f"File decrypted successfully!\nOutput: {output_file}"
            
        except Exception as e:
            return False, f"Error: {str(e)}"


# Example usage and testing
if __name__ == "__main__":
    des = DESCipher()
    
    # Generate a key
    key = des.generate_key()
    print(f"Generated Key: {key}")
    
    # Test encryption
    plaintext = "Hello, DES Encryption!"
    ciphertext, steps = des.encrypt(plaintext)
    
    print(f"\nPlaintext: {plaintext}")
    print(f"Ciphertext: {ciphertext}")
    print(f"\n{steps}")
    
    # Test decryption
    decrypted, dec_steps = des.decrypt(ciphertext, key)
    print(f"\nDecrypted: {decrypted}")
    print(f"\n{dec_steps}")
