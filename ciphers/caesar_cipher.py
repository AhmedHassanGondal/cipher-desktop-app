"""
Caesar Cipher Implementation
============================
The Caesar cipher is one of the earliest known encryption techniques.
It works by shifting each letter in the plaintext by a fixed number of positions
in the alphabet.

Mathematical Formula:
- Encryption: E(x) = (x + k) mod 26
- Decryption: D(x) = (x - k) mod 26

Where:
- x = position of the letter (A=0, B=1, ..., Z=25)
- k = shift key (0-25)
"""


class CaesarCipher:
    """
    Caesar Cipher class implementing encryption and decryption.
    
    Attributes:
        alphabet (str): The standard English alphabet
    """
    
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    def encrypt(self, plaintext: str, shift: int) -> tuple:
        """
        Encrypt plaintext using Caesar cipher.
        
        Args:
            plaintext (str): The text to encrypt
            shift (int): The shift key (0-25)
            
        Returns:
            tuple: (ciphertext, calculation_steps)
        """
        plaintext = plaintext.upper()
        shift = shift % 26  # Normalize shift to 0-25
        ciphertext = []
        steps = []
        
        for i, char in enumerate(plaintext):
            if char in self.alphabet:
                # Get position of character
                x = self.alphabet.index(char)
                # Apply encryption formula: E(x) = (x + k) mod 26
                encrypted_pos = (x + shift) % 26
                encrypted_char = self.alphabet[encrypted_pos]
                ciphertext.append(encrypted_char)
                
                # Record calculation step for first 5 characters
                if i < 5:
                    steps.append(
                        f"'{char}' (pos {x}) → ({x} + {shift}) mod 26 = {encrypted_pos} → '{encrypted_char}'"
                    )
            else:
                # Non-alphabetic characters remain unchanged
                ciphertext.append(char)
        
        calculation_display = "Encryption Steps (showing first 5 chars):\n"
        calculation_display += "Formula: E(x) = (x + k) mod 26\n\n"
        calculation_display += "\n".join(steps) if steps else "No alphabetic characters to encrypt"
        
        return ''.join(ciphertext), calculation_display
    
    def decrypt(self, ciphertext: str, shift: int) -> tuple:
        """
        Decrypt ciphertext using Caesar cipher.
        
        Args:
            ciphertext (str): The text to decrypt
            shift (int): The shift key used for encryption
            
        Returns:
            tuple: (plaintext, calculation_steps)
        """
        ciphertext = ciphertext.upper()
        shift = shift % 26
        plaintext = []
        steps = []
        
        for i, char in enumerate(ciphertext):
            if char in self.alphabet:
                # Get position of character
                x = self.alphabet.index(char)
                # Apply decryption formula: D(x) = (x - k) mod 26
                decrypted_pos = (x - shift) % 26
                decrypted_char = self.alphabet[decrypted_pos]
                plaintext.append(decrypted_char)
                
                # Record calculation step for first 5 characters
                if i < 5:
                    steps.append(
                        f"'{char}' (pos {x}) → ({x} - {shift}) mod 26 = {decrypted_pos} → '{decrypted_char}'"
                    )
            else:
                plaintext.append(char)
        
        calculation_display = "Decryption Steps (showing first 5 chars):\n"
        calculation_display += "Formula: D(x) = (x - k) mod 26\n\n"
        calculation_display += "\n".join(steps) if steps else "No alphabetic characters to decrypt"
        
        return ''.join(plaintext), calculation_display
    
    def brute_force(self, ciphertext: str) -> list:
        """
        Try all possible shifts (0-25) for cryptanalysis.
        
        Args:
            ciphertext (str): The encrypted text
            
        Returns:
            list: All possible decryptions with their shift values
        """
        results = []
        for shift in range(26):
            decrypted, _ = self.decrypt(ciphertext, shift)
            results.append((shift, decrypted))
        return results


# Example usage and testing
if __name__ == "__main__":
    cipher = CaesarCipher()
    
    # Test encryption
    plaintext = "HELLO WORLD"
    shift = 3
    
    encrypted, enc_steps = cipher.encrypt(plaintext, shift)
    print(f"Plaintext: {plaintext}")
    print(f"Shift: {shift}")
    print(f"Ciphertext: {encrypted}")
    print(f"\n{enc_steps}")
    
    # Test decryption
    decrypted, dec_steps = cipher.decrypt(encrypted, shift)
    print(f"\nDecrypted: {decrypted}")
    print(f"\n{dec_steps}")

