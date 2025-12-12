"""
Hill Cipher Implementation (2×2 Matrix)
=======================================
The Hill cipher is a polygraphic substitution cipher that uses linear algebra
(matrix multiplication) for encryption. It was invented by Lester S. Hill in 1929.

Mathematical Foundation:
- Encryption: C = K × P (mod 26)
- Decryption: P = K⁻¹ × C (mod 26)

Where:
- K = 2×2 key matrix
- P = column vector of plaintext letter positions
- C = column vector of ciphertext letter positions
- K⁻¹ = modular multiplicative inverse of key matrix

Key Matrix Requirements:
- Must be invertible (det(K) ≠ 0)
- gcd(det(K), 26) = 1 (determinant must be coprime with 26)
"""

import numpy as np


class HillCipher:
    """
    Hill Cipher class implementing 2×2 matrix-based encryption and decryption.
    
    Attributes:
        alphabet (str): The standard English alphabet
        key_matrix (numpy.ndarray): 2×2 key matrix
    """
    
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.key_matrix = None
    
    def _mod_inverse(self, a: int, m: int) -> int:
        """
        Calculate the modular multiplicative inverse of a mod m.
        Uses Extended Euclidean Algorithm.
        
        Args:
            a (int): The number to find inverse for
            m (int): The modulus
            
        Returns:
            int: The modular inverse, or -1 if not exists
        """
        a = a % m
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return -1
    
    def _gcd(self, a: int, b: int) -> int:
        """Calculate GCD using Euclidean algorithm."""
        while b:
            a, b = b, a % b
        return a
    
    def set_key(self, key_string: str) -> tuple:
        """
        Set the 2×2 key matrix from a 4-character string.
        
        Args:
            key_string (str): 4 alphabetic characters for the key matrix
            
        Returns:
            tuple: (success, message, matrix_display)
        """
        key_string = key_string.upper()
        key_string = ''.join(c for c in key_string if c.isalpha())
        
        if len(key_string) != 4:
            return False, "Key must contain exactly 4 alphabetic characters", ""
        
        # Create 2×2 matrix
        values = [self.alphabet.index(c) for c in key_string]
        self.key_matrix = np.array([[values[0], values[1]], 
                                     [values[2], values[3]]])
        
        # Check if matrix is valid (invertible mod 26)
        det = int(np.round(np.linalg.det(self.key_matrix))) % 26
        
        if det == 0:
            return False, "Invalid key: Determinant is 0 (matrix not invertible)", ""
        
        if self._gcd(det, 26) != 1:
            return False, f"Invalid key: gcd({det}, 26) = {self._gcd(det, 26)} ≠ 1", ""
        
        # Generate matrix display
        matrix_display = "Key Matrix (K):\n"
        matrix_display += f"┌         ┐\n"
        matrix_display += f"│ {values[0]:2d}  {values[1]:2d} │  =  │ {key_string[0]}  {key_string[1]} │\n"
        matrix_display += f"│ {values[2]:2d}  {values[3]:2d} │      │ {key_string[2]}  {key_string[3]} │\n"
        matrix_display += f"└         ┘\n"
        matrix_display += f"\nDeterminant = ({values[0]}×{values[3]}) - ({values[1]}×{values[2]}) = {det} (mod 26)"
        
        return True, "Key matrix set successfully", matrix_display
    
    def _get_inverse_matrix(self) -> tuple:
        """
        Calculate the inverse of the key matrix mod 26.
        
        Returns:
            tuple: (inverse_matrix, calculation_steps)
        """
        a, b = self.key_matrix[0]
        c, d = self.key_matrix[1]
        
        # Calculate determinant mod 26
        det = int((a * d - b * c) % 26)
        
        # Find modular inverse of determinant
        det_inv = self._mod_inverse(det, 26)
        
        # Adjugate matrix (swap a,d and negate b,c)
        adjugate = np.array([[d, -b], [-c, a]])
        
        # Inverse = det_inv * adjugate (mod 26)
        inverse = (det_inv * adjugate) % 26
        
        steps = f"Inverse Matrix Calculation:\n"
        steps += f"det(K) = {det}\n"
        steps += f"det⁻¹ mod 26 = {det_inv}\n"
        steps += f"Adjugate matrix = [[{d}, {-b}], [{-c}, {a}]]\n"
        steps += f"K⁻¹ = {det_inv} × Adjugate (mod 26)\n"
        steps += f"K⁻¹ = [[{int(inverse[0][0])}, {int(inverse[0][1])}], [{int(inverse[1][0])}, {int(inverse[1][1])}]]"
        
        return inverse.astype(int), steps
    
    def encrypt(self, plaintext: str, key_string: str) -> tuple:
        """
        Encrypt plaintext using Hill cipher.
        
        Args:
            plaintext (str): The text to encrypt
            key_string (str): 4 characters for 2×2 key matrix
            
        Returns:
            tuple: (ciphertext, calculation_steps)
        """
        # Set up key matrix
        success, message, matrix_display = self.set_key(key_string)
        if not success:
            return "", f"Error: {message}"
        
        # Prepare plaintext
        plaintext = plaintext.upper()
        plaintext = ''.join(c for c in plaintext if c.isalpha())
        
        # Pad if necessary
        if len(plaintext) % 2 != 0:
            plaintext += 'X'
        
        ciphertext = []
        steps = []
        step_count = 0
        
        # Process pairs of characters
        for i in range(0, len(plaintext), 2):
            # Create column vector
            p1 = self.alphabet.index(plaintext[i])
            p2 = self.alphabet.index(plaintext[i + 1])
            P = np.array([[p1], [p2]])
            
            # Matrix multiplication: C = K × P (mod 26)
            C = np.dot(self.key_matrix, P) % 26
            
            c1 = int(C[0][0])
            c2 = int(C[1][0])
            
            ciphertext.append(self.alphabet[c1])
            ciphertext.append(self.alphabet[c2])
            
            if step_count < 3:  # Show first 3 pairs
                steps.append(
                    f"'{plaintext[i]}{plaintext[i+1]}' ({p1},{p2}):\n"
                    f"   C = K × P = [[{self.key_matrix[0][0]},{self.key_matrix[0][1]}],[{self.key_matrix[1][0]},{self.key_matrix[1][1]}]] × [[{p1}],[{p2}]]\n"
                    f"   C = [[{c1}],[{c2}]] → '{self.alphabet[c1]}{self.alphabet[c2]}'"
                )
                step_count += 1
        
        calculation_display = matrix_display + "\n\n"
        calculation_display += f"Prepared plaintext: {plaintext}\n\n"
        calculation_display += "Encryption: C = K × P (mod 26)\n\n"
        calculation_display += "\n\n".join(steps) if steps else "No characters to encrypt"
        
        return ''.join(ciphertext), calculation_display
    
    def decrypt(self, ciphertext: str, key_string: str) -> tuple:
        """
        Decrypt ciphertext using Hill cipher.
        
        Args:
            ciphertext (str): The text to decrypt
            key_string (str): 4 characters for 2×2 key matrix
            
        Returns:
            tuple: (plaintext, calculation_steps)
        """
        # Set up key matrix
        success, message, matrix_display = self.set_key(key_string)
        if not success:
            return "", f"Error: {message}"
        
        # Get inverse matrix
        inv_matrix, inv_steps = self._get_inverse_matrix()
        
        # Prepare ciphertext
        ciphertext = ciphertext.upper()
        ciphertext = ''.join(c for c in ciphertext if c.isalpha())
        
        if len(ciphertext) % 2 != 0:
            return "", "Error: Ciphertext length must be even"
        
        plaintext = []
        steps = []
        step_count = 0
        
        # Process pairs of characters
        for i in range(0, len(ciphertext), 2):
            # Create column vector
            c1 = self.alphabet.index(ciphertext[i])
            c2 = self.alphabet.index(ciphertext[i + 1])
            C = np.array([[c1], [c2]])
            
            # Matrix multiplication: P = K⁻¹ × C (mod 26)
            P = np.dot(inv_matrix, C) % 26
            
            p1 = int(P[0][0])
            p2 = int(P[1][0])
            
            plaintext.append(self.alphabet[p1])
            plaintext.append(self.alphabet[p2])
            
            if step_count < 3:  # Show first 3 pairs
                steps.append(
                    f"'{ciphertext[i]}{ciphertext[i+1]}' ({c1},{c2}):\n"
                    f"   P = K⁻¹ × C = [[{inv_matrix[0][0]},{inv_matrix[0][1]}],[{inv_matrix[1][0]},{inv_matrix[1][1]}]] × [[{c1}],[{c2}]]\n"
                    f"   P = [[{p1}],[{p2}]] → '{self.alphabet[p1]}{self.alphabet[p2]}'"
                )
                step_count += 1
        
        calculation_display = matrix_display + "\n\n"
        calculation_display += inv_steps + "\n\n"
        calculation_display += "Decryption: P = K⁻¹ × C (mod 26)\n\n"
        calculation_display += "\n\n".join(steps) if steps else "No characters to decrypt"
        
        return ''.join(plaintext), calculation_display


# Example usage and testing
if __name__ == "__main__":
    cipher = HillCipher()
    
    # Test encryption
    plaintext = "HELLO"
    key = "GYBN"  # Valid 2×2 key matrix
    
    encrypted, enc_steps = cipher.encrypt(plaintext, key)
    print(f"Plaintext: {plaintext}")
    print(f"Key: {key}")
    print(f"Ciphertext: {encrypted}")
    print(f"\n{enc_steps}")
    
    # Test decryption
    decrypted, dec_steps = cipher.decrypt(encrypted, key)
    print(f"\nDecrypted: {decrypted}")
    print(f"\n{dec_steps}")

