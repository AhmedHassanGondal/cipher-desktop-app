"""
Monoalphabetic Substitution Cipher Implementation
==================================================
The monoalphabetic cipher is a substitution cipher where each letter in the 
plaintext is replaced by a fixed corresponding letter from a substitution alphabet.

Unlike the Caesar cipher which uses a fixed shift, monoalphabetic ciphers allow
any permutation of the alphabet as the key, providing 26! ≈ 4×10²⁶ possible keys.

Security Note:
Despite the large key space, this cipher is vulnerable to frequency analysis
because each letter always maps to the same substitute letter.

Key Types:
1. Random Permutation: A complete scrambled alphabet
2. Keyword-based: Generate substitution from a keyword
"""

import random


class MonoalphabeticCipher:
    """
    Monoalphabetic Substitution Cipher class.
    
    Attributes:
        alphabet (str): The standard English alphabet
        substitution_alphabet (str): The substitution mapping
    """
    
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.substitution_alphabet = None
    
    def generate_key_from_keyword(self, keyword: str) -> str:
        """
        Generate a substitution alphabet from a keyword.
        
        The keyword letters come first (without duplicates), followed by
        the remaining alphabet letters in order.
        
        Args:
            keyword (str): The keyword to generate substitution from
            
        Returns:
            str: 26-character substitution alphabet
        """
        keyword = keyword.upper()
        keyword = ''.join(c for c in keyword if c.isalpha())
        
        # Build substitution: keyword letters first (unique), then remaining
        seen = set()
        substitution = []
        
        for char in keyword:
            if char not in seen:
                seen.add(char)
                substitution.append(char)
        
        for char in self.alphabet:
            if char not in seen:
                seen.add(char)
                substitution.append(char)
        
        return ''.join(substitution)
    
    def generate_random_key(self) -> str:
        """
        Generate a random substitution alphabet.
        
        Returns:
            str: 26-character random substitution alphabet
        """
        chars = list(self.alphabet)
        random.shuffle(chars)
        return ''.join(chars)
    
    def validate_key(self, key: str) -> tuple:
        """
        Validate a substitution key.
        
        Args:
            key (str): The substitution alphabet to validate
            
        Returns:
            tuple: (is_valid, error_message)
        """
        key = key.upper()
        key = ''.join(c for c in key if c.isalpha())
        
        if len(key) != 26:
            return False, f"Key must contain exactly 26 letters (got {len(key)})"
        
        if len(set(key)) != 26:
            return False, "Key must contain each letter exactly once (no duplicates)"
        
        return True, "Valid key"
    
    def _display_mapping(self) -> str:
        """Generate a visual representation of the substitution mapping."""
        if not self.substitution_alphabet:
            return "Substitution alphabet not set"
        
        display = "Substitution Mapping:\n"
        display += "┌" + "─" * 54 + "┐\n"
        display += "│ Plain:  " + " ".join(self.alphabet) + " │\n"
        display += "│ Cipher: " + " ".join(self.substitution_alphabet) + " │\n"
        display += "└" + "─" * 54 + "┘"
        
        return display
    
    def encrypt(self, plaintext: str, key: str) -> tuple:
        """
        Encrypt plaintext using monoalphabetic substitution.
        
        Args:
            plaintext (str): The text to encrypt
            key (str): The substitution alphabet (26 chars) or keyword
            
        Returns:
            tuple: (ciphertext, calculation_steps)
        """
        key = key.upper()
        
        # Check if key is a full substitution alphabet or a keyword
        if len(key) == 26 and len(set(key)) == 26:
            self.substitution_alphabet = key
            key_type = "Full Substitution Alphabet"
        else:
            self.substitution_alphabet = self.generate_key_from_keyword(key)
            key_type = f"Generated from keyword '{key}'"
        
        # Create substitution dictionary
        sub_dict = {self.alphabet[i]: self.substitution_alphabet[i] for i in range(26)}
        
        plaintext_upper = plaintext.upper()
        ciphertext = []
        steps = []
        step_count = 0
        
        for char in plaintext_upper:
            if char in self.alphabet:
                encrypted_char = sub_dict[char]
                ciphertext.append(encrypted_char)
                
                if step_count < 10:  # Show first 10 substitutions
                    pos = self.alphabet.index(char)
                    steps.append(f"'{char}' (pos {pos}) → '{encrypted_char}'")
                    step_count += 1
            else:
                ciphertext.append(char)
        
        calculation_display = f"Key Type: {key_type}\n\n"
        calculation_display += self._display_mapping() + "\n\n"
        calculation_display += "Encryption Steps (first 10 chars):\n"
        calculation_display += "\n".join(steps) if steps else "No alphabetic characters"
        calculation_display += f"\n\nKey Space: 26! ≈ 4.03 × 10²⁶ possible keys"
        
        return ''.join(ciphertext), calculation_display
    
    def decrypt(self, ciphertext: str, key: str) -> tuple:
        """
        Decrypt ciphertext using monoalphabetic substitution.
        
        Args:
            ciphertext (str): The text to decrypt
            key (str): The substitution alphabet (26 chars) or keyword
            
        Returns:
            tuple: (plaintext, calculation_steps)
        """
        key = key.upper()
        
        # Check if key is a full substitution alphabet or a keyword
        if len(key) == 26 and len(set(key)) == 26:
            self.substitution_alphabet = key
            key_type = "Full Substitution Alphabet"
        else:
            self.substitution_alphabet = self.generate_key_from_keyword(key)
            key_type = f"Generated from keyword '{key}'"
        
        # Create reverse substitution dictionary
        rev_dict = {self.substitution_alphabet[i]: self.alphabet[i] for i in range(26)}
        
        ciphertext_upper = ciphertext.upper()
        plaintext = []
        steps = []
        step_count = 0
        
        for char in ciphertext_upper:
            if char in self.substitution_alphabet:
                decrypted_char = rev_dict[char]
                plaintext.append(decrypted_char)
                
                if step_count < 10:  # Show first 10 substitutions
                    pos = self.substitution_alphabet.index(char)
                    steps.append(f"'{char}' (pos {pos}) → '{decrypted_char}'")
                    step_count += 1
            else:
                plaintext.append(char)
        
        calculation_display = f"Key Type: {key_type}\n\n"
        calculation_display += self._display_mapping() + "\n\n"
        calculation_display += "Decryption Steps (first 10 chars):\n"
        calculation_display += "\n".join(steps) if steps else "No alphabetic characters"
        
        return ''.join(plaintext), calculation_display
    
    def frequency_analysis(self, text: str) -> str:
        """
        Perform frequency analysis on text (useful for cryptanalysis).
        
        Args:
            text (str): The text to analyze
            
        Returns:
            str: Frequency analysis results
        """
        text = text.upper()
        text = ''.join(c for c in text if c.isalpha())
        
        if not text:
            return "No alphabetic characters to analyze"
        
        # Count frequencies
        freq = {}
        for char in text:
            freq[char] = freq.get(char, 0) + 1
        
        # Sort by frequency
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        # Standard English letter frequencies (for comparison)
        english_freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
        
        result = "Frequency Analysis:\n"
        result += "=" * 40 + "\n"
        result += f"{'Letter':<8} {'Count':<8} {'Frequency':<12}\n"
        result += "-" * 40 + "\n"
        
        for letter, count in sorted_freq:
            percentage = (count / len(text)) * 100
            result += f"{letter:<8} {count:<8} {percentage:.2f}%\n"
        
        result += "\n" + "=" * 40 + "\n"
        result += "Standard English frequency order: ETAOINSHRDLCUMWFGYPBVKJXQZ\n"
        result += f"This text's frequency order: {''.join(c[0] for c in sorted_freq)}"
        
        return result


# Example usage and testing
if __name__ == "__main__":
    cipher = MonoalphabeticCipher()
    
    # Test with keyword
    plaintext = "HELLO WORLD"
    keyword = "SECURITY"
    
    encrypted, enc_steps = cipher.encrypt(plaintext, keyword)
    print(f"Plaintext: {plaintext}")
    print(f"Keyword: {keyword}")
    print(f"Ciphertext: {encrypted}")
    print(f"\n{enc_steps}")
    
    # Test decryption
    decrypted, dec_steps = cipher.decrypt(encrypted, keyword)
    print(f"\nDecrypted: {decrypted}")
    print(f"\n{dec_steps}")
    
    # Test frequency analysis
    sample_text = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
    print(f"\n{cipher.frequency_analysis(sample_text)}")

