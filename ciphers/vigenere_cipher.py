"""
Vigenère Cipher Implementation
==============================
The Vigenère cipher is a polyalphabetic substitution cipher that uses a keyword
to shift letters differently at each position, making it more secure than 
simple substitution ciphers.

Mathematical Formula:
- Encryption: Ci = (Pi + Ki) mod 26
- Decryption: Pi = (Ci - Ki) mod 26

Where:
- Pi = position of the i-th plaintext letter
- Ki = position of the i-th key letter (key repeats cyclically)
- Ci = position of the i-th ciphertext letter

Historical Note:
This cipher was considered "unbreakable" for 300 years and was known as 
"le chiffre indéchiffrable" (the indecipherable cipher).
"""


class VigenereCipher:
    """
    Vigenère Cipher class implementing keyword-based encryption and decryption.
    
    Attributes:
        alphabet (str): The standard English alphabet
    """
    
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    def _prepare_key(self, plaintext: str, keyword: str) -> str:
        """
        Extend the keyword to match the length of plaintext.
        
        Args:
            plaintext (str): The text to encrypt
            keyword (str): The encryption keyword
            
        Returns:
            str: Extended key matching plaintext length
        """
        keyword = keyword.upper()
        # Remove non-alphabetic characters from keyword
        keyword = ''.join(c for c in keyword if c in self.alphabet)
        
        if not keyword:
            raise ValueError("Keyword must contain at least one alphabetic character")
        
        extended_key = []
        key_index = 0
        
        for char in plaintext.upper():
            if char in self.alphabet:
                extended_key.append(keyword[key_index % len(keyword)])
                key_index += 1
            else:
                extended_key.append(char)
        
        return ''.join(extended_key)
    
    def encrypt(self, plaintext: str, keyword: str) -> tuple:
        """
        Encrypt plaintext using Vigenère cipher.
        
        Args:
            plaintext (str): The text to encrypt
            keyword (str): The encryption keyword
            
        Returns:
            tuple: (ciphertext, calculation_steps)
        """
        plaintext = plaintext.upper()
        extended_key = self._prepare_key(plaintext, keyword)
        ciphertext = []
        steps = []
        step_count = 0
        
        for i, (p_char, k_char) in enumerate(zip(plaintext, extended_key)):
            if p_char in self.alphabet:
                # Get positions
                p_pos = self.alphabet.index(p_char)
                k_pos = self.alphabet.index(k_char)
                
                # Apply encryption formula: Ci = (Pi + Ki) mod 26
                c_pos = (p_pos + k_pos) % 26
                c_char = self.alphabet[c_pos]
                ciphertext.append(c_char)
                
                # Record calculation step for first 5 alphabetic characters
                if step_count < 5:
                    steps.append(
                        f"'{p_char}'(P={p_pos}) + '{k_char}'(K={k_pos}) = ({p_pos}+{k_pos}) mod 26 = {c_pos} → '{c_char}'"
                    )
                    step_count += 1
            else:
                ciphertext.append(p_char)
        
        calculation_display = "Vigenère Encryption Steps (first 5 chars):\n"
        calculation_display += f"Keyword: {keyword.upper()}\n"
        calculation_display += f"Extended Key: {extended_key[:30]}{'...' if len(extended_key) > 30 else ''}\n"
        calculation_display += "Formula: Ci = (Pi + Ki) mod 26\n\n"
        calculation_display += "\n".join(steps) if steps else "No alphabetic characters"
        
        return ''.join(ciphertext), calculation_display
    
    def decrypt(self, ciphertext: str, keyword: str) -> tuple:
        """
        Decrypt ciphertext using Vigenère cipher.
        
        Args:
            ciphertext (str): The text to decrypt
            keyword (str): The decryption keyword
            
        Returns:
            tuple: (plaintext, calculation_steps)
        """
        ciphertext = ciphertext.upper()
        extended_key = self._prepare_key(ciphertext, keyword)
        plaintext = []
        steps = []
        step_count = 0
        
        for i, (c_char, k_char) in enumerate(zip(ciphertext, extended_key)):
            if c_char in self.alphabet:
                # Get positions
                c_pos = self.alphabet.index(c_char)
                k_pos = self.alphabet.index(k_char)
                
                # Apply decryption formula: Pi = (Ci - Ki) mod 26
                p_pos = (c_pos - k_pos) % 26
                p_char = self.alphabet[p_pos]
                plaintext.append(p_char)
                
                # Record calculation step for first 5 alphabetic characters
                if step_count < 5:
                    steps.append(
                        f"'{c_char}'(C={c_pos}) - '{k_char}'(K={k_pos}) = ({c_pos}-{k_pos}) mod 26 = {p_pos} → '{p_char}'"
                    )
                    step_count += 1
            else:
                plaintext.append(c_char)
        
        calculation_display = "Vigenère Decryption Steps (first 5 chars):\n"
        calculation_display += f"Keyword: {keyword.upper()}\n"
        calculation_display += f"Extended Key: {extended_key[:30]}{'...' if len(extended_key) > 30 else ''}\n"
        calculation_display += "Formula: Pi = (Ci - Ki) mod 26\n\n"
        calculation_display += "\n".join(steps) if steps else "No alphabetic characters"
        
        return ''.join(plaintext), calculation_display
    
    def generate_tableau(self) -> str:
        """
        Generate the Vigenère tableau (tabula recta).
        
        Returns:
            str: Visual representation of the tableau
        """
        tableau = "Vigenère Tableau (Tabula Recta):\n\n"
        tableau += "    " + " ".join(self.alphabet) + "\n"
        tableau += "   " + "-" * 52 + "\n"
        
        for i, letter in enumerate(self.alphabet):
            shifted = self.alphabet[i:] + self.alphabet[:i]
            tableau += f" {letter} | " + " ".join(shifted) + "\n"
        
        return tableau


# Example usage and testing
if __name__ == "__main__":
    cipher = VigenereCipher()
    
    # Test encryption
    plaintext = "ATTACK AT DAWN"
    keyword = "LEMON"
    
    encrypted, enc_steps = cipher.encrypt(plaintext, keyword)
    print(f"Plaintext: {plaintext}")
    print(f"Keyword: {keyword}")
    print(f"Ciphertext: {encrypted}")
    print(f"\n{enc_steps}")
    
    # Test decryption
    decrypted, dec_steps = cipher.decrypt(encrypted, keyword)
    print(f"\nDecrypted: {decrypted}")
    print(f"\n{dec_steps}")

