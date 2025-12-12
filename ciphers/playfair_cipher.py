"""
Playfair Cipher Implementation
==============================
The Playfair cipher encrypts pairs of letters (digraphs) using a 5x5 key matrix.
It was the first practical digraph substitution cipher and was used for 
tactical purposes by British forces in the Boer War and World War I.

Key Matrix Generation:
1. Remove duplicate letters from the keyword
2. Fill remaining positions with unused letters (I and J are combined)
3. Arrange in a 5x5 grid

Encryption Rules:
1. Same row: Replace each with letter to its right (wrap around)
2. Same column: Replace each with letter below (wrap around)
3. Rectangle: Replace each with letter in same row but other corner

Special Handling:
- If both letters are the same, insert 'X' between them
- If plaintext length is odd, append 'X'
"""


class PlayfairCipher:
    """
    Playfair Cipher class implementing digraph encryption and decryption.
    
    Attributes:
        matrix (list): 5x5 key matrix
        char_positions (dict): Maps each character to its position
    """
    
    def __init__(self):
        self.matrix = None
        self.char_positions = {}
    
    def _generate_matrix(self, keyword: str) -> list:
        """
        Generate the 5x5 key matrix from the keyword.
        
        Args:
            keyword (str): The encryption keyword
            
        Returns:
            list: 5x5 matrix of characters
        """
        # Prepare keyword: uppercase, remove non-alpha, replace J with I
        keyword = keyword.upper()
        keyword = ''.join(c for c in keyword if c.isalpha())
        keyword = keyword.replace('J', 'I')
        
        # Build matrix with unique characters
        seen = set()
        matrix_chars = []
        
        # Add keyword characters first
        for char in keyword:
            if char not in seen:
                seen.add(char)
                matrix_chars.append(char)
        
        # Add remaining alphabet letters (excluding J)
        alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # No J
        for char in alphabet:
            if char not in seen:
                seen.add(char)
                matrix_chars.append(char)
        
        # Create 5x5 matrix
        matrix = []
        for i in range(0, 25, 5):
            matrix.append(matrix_chars[i:i+5])
        
        # Store character positions for quick lookup
        self.char_positions = {}
        for row in range(5):
            for col in range(5):
                self.char_positions[matrix[row][col]] = (row, col)
        
        self.matrix = matrix
        return matrix
    
    def _display_matrix(self) -> str:
        """Generate a visual representation of the key matrix."""
        if not self.matrix:
            return "Matrix not generated"
        
        display = "5×5 Playfair Key Matrix:\n"
        display += "+" + "-" * 11 + "+\n"
        for row in self.matrix:
            display += "| " + " ".join(row) + " |\n"
        display += "+" + "-" * 11 + "+\n"
        display += "(Note: I and J are treated as the same letter)\n"
        return display
    
    def _prepare_plaintext(self, plaintext: str) -> list:
        """
        Prepare plaintext by creating digraphs.
        
        Args:
            plaintext (str): The text to prepare
            
        Returns:
            list: List of character pairs (digraphs)
        """
        # Clean and prepare text
        plaintext = plaintext.upper()
        plaintext = ''.join(c for c in plaintext if c.isalpha())
        plaintext = plaintext.replace('J', 'I')
        
        # Create digraphs
        digraphs = []
        i = 0
        while i < len(plaintext):
            if i == len(plaintext) - 1:
                # Odd length: add X at end
                digraphs.append(plaintext[i] + 'X')
                i += 1
            elif plaintext[i] == plaintext[i + 1]:
                # Same letters: insert X between
                digraphs.append(plaintext[i] + 'X')
                i += 1
            else:
                digraphs.append(plaintext[i] + plaintext[i + 1])
                i += 2
        
        return digraphs
    
    def _encrypt_digraph(self, digraph: str) -> tuple:
        """
        Encrypt a single digraph.
        
        Args:
            digraph (str): Two-character string
            
        Returns:
            tuple: (encrypted_digraph, rule_used, step_details)
        """
        char1, char2 = digraph[0], digraph[1]
        row1, col1 = self.char_positions[char1]
        row2, col2 = self.char_positions[char2]
        
        if row1 == row2:
            # Same row: shift right
            new_col1 = (col1 + 1) % 5
            new_col2 = (col2 + 1) % 5
            enc_char1 = self.matrix[row1][new_col1]
            enc_char2 = self.matrix[row2][new_col2]
            rule = "Same Row"
            step = f"'{char1}'({row1},{col1}) → ({row1},{new_col1})='{enc_char1}', '{char2}'({row2},{col2}) → ({row2},{new_col2})='{enc_char2}'"
        elif col1 == col2:
            # Same column: shift down
            new_row1 = (row1 + 1) % 5
            new_row2 = (row2 + 1) % 5
            enc_char1 = self.matrix[new_row1][col1]
            enc_char2 = self.matrix[new_row2][col2]
            rule = "Same Column"
            step = f"'{char1}'({row1},{col1}) → ({new_row1},{col1})='{enc_char1}', '{char2}'({row2},{col2}) → ({new_row2},{col2})='{enc_char2}'"
        else:
            # Rectangle: swap columns
            enc_char1 = self.matrix[row1][col2]
            enc_char2 = self.matrix[row2][col1]
            rule = "Rectangle"
            step = f"'{char1}'({row1},{col1}) → ({row1},{col2})='{enc_char1}', '{char2}'({row2},{col2}) → ({row2},{col1})='{enc_char2}'"
        
        return enc_char1 + enc_char2, rule, step
    
    def _decrypt_digraph(self, digraph: str) -> tuple:
        """
        Decrypt a single digraph.
        
        Args:
            digraph (str): Two-character encrypted string
            
        Returns:
            tuple: (decrypted_digraph, rule_used, step_details)
        """
        char1, char2 = digraph[0], digraph[1]
        row1, col1 = self.char_positions[char1]
        row2, col2 = self.char_positions[char2]
        
        if row1 == row2:
            # Same row: shift left
            new_col1 = (col1 - 1) % 5
            new_col2 = (col2 - 1) % 5
            dec_char1 = self.matrix[row1][new_col1]
            dec_char2 = self.matrix[row2][new_col2]
            rule = "Same Row"
            step = f"'{char1}'({row1},{col1}) ← ({row1},{new_col1})='{dec_char1}', '{char2}'({row2},{col2}) ← ({row2},{new_col2})='{dec_char2}'"
        elif col1 == col2:
            # Same column: shift up
            new_row1 = (row1 - 1) % 5
            new_row2 = (row2 - 1) % 5
            dec_char1 = self.matrix[new_row1][col1]
            dec_char2 = self.matrix[new_row2][col2]
            rule = "Same Column"
            step = f"'{char1}'({row1},{col1}) ← ({new_row1},{col1})='{dec_char1}', '{char2}'({row2},{col2}) ← ({new_row2},{col2})='{dec_char2}'"
        else:
            # Rectangle: swap columns (same as encryption)
            dec_char1 = self.matrix[row1][col2]
            dec_char2 = self.matrix[row2][col1]
            rule = "Rectangle"
            step = f"'{char1}'({row1},{col1}) → ({row1},{col2})='{dec_char1}', '{char2}'({row2},{col2}) → ({row2},{col1})='{dec_char2}'"
        
        return dec_char1 + dec_char2, rule, step
    
    def encrypt(self, plaintext: str, keyword: str) -> tuple:
        """
        Encrypt plaintext using Playfair cipher.
        
        Args:
            plaintext (str): The text to encrypt
            keyword (str): The encryption keyword
            
        Returns:
            tuple: (ciphertext, calculation_steps)
        """
        self._generate_matrix(keyword)
        digraphs = self._prepare_plaintext(plaintext)
        
        ciphertext = []
        steps = []
        
        for i, digraph in enumerate(digraphs):
            encrypted, rule, step = self._encrypt_digraph(digraph)
            ciphertext.append(encrypted)
            if i < 5:  # Show first 5 steps
                steps.append(f"'{digraph}' → '{encrypted}' [{rule}]\n   {step}")
        
        calculation_display = self._display_matrix()
        calculation_display += f"\nDigraphs formed: {' '.join(digraphs)}\n\n"
        calculation_display += "Encryption Steps (first 5 digraphs):\n"
        calculation_display += "\n".join(steps) if steps else "No digraphs to encrypt"
        
        return ''.join(ciphertext), calculation_display
    
    def decrypt(self, ciphertext: str, keyword: str) -> tuple:
        """
        Decrypt ciphertext using Playfair cipher.
        
        Args:
            ciphertext (str): The text to decrypt
            keyword (str): The decryption keyword
            
        Returns:
            tuple: (plaintext, calculation_steps)
        """
        self._generate_matrix(keyword)
        
        # Clean ciphertext
        ciphertext = ciphertext.upper()
        ciphertext = ''.join(c for c in ciphertext if c.isalpha())
        ciphertext = ciphertext.replace('J', 'I')
        
        # Create digraphs
        digraphs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
        
        plaintext = []
        steps = []
        
        for i, digraph in enumerate(digraphs):
            if len(digraph) == 2:
                decrypted, rule, step = self._decrypt_digraph(digraph)
                plaintext.append(decrypted)
                if i < 5:  # Show first 5 steps
                    steps.append(f"'{digraph}' → '{decrypted}' [{rule}]\n   {step}")
        
        calculation_display = self._display_matrix()
        calculation_display += f"\nDigraphs to decrypt: {' '.join(digraphs)}\n\n"
        calculation_display += "Decryption Steps (first 5 digraphs):\n"
        calculation_display += "\n".join(steps) if steps else "No digraphs to decrypt"
        
        return ''.join(plaintext), calculation_display


# Example usage and testing
if __name__ == "__main__":
    cipher = PlayfairCipher()
    
    # Test encryption
    plaintext = "HELLO WORLD"
    keyword = "MONARCHY"
    
    encrypted, enc_steps = cipher.encrypt(plaintext, keyword)
    print(f"Plaintext: {plaintext}")
    print(f"Keyword: {keyword}")
    print(f"Ciphertext: {encrypted}")
    print(f"\n{enc_steps}")
    
    # Test decryption
    decrypted, dec_steps = cipher.decrypt(encrypted, keyword)
    print(f"\nDecrypted: {decrypted}")
    print(f"\n{dec_steps}")

