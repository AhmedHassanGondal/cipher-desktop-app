"""
Diffie-Hellman Key Exchange Implementation
===========================================
Diffie-Hellman is a method for securely exchanging cryptographic keys over
a public channel. Published in 1976 by Whitfield Diffie and Martin Hellman,
it was one of the first practical implementations of public key exchange.

Mathematical Foundation:
1. Alice and Bob agree on public values:
   - p: A large prime number
   - g: A primitive root modulo p

2. Private and Public Key Generation:
   - Alice chooses private key 'a', computes A = g^a mod p
   - Bob chooses private key 'b', computes B = g^b mod p

3. Shared Secret Computation:
   - Alice computes: K = B^a mod p = g^(ab) mod p
   - Bob computes: K = A^b mod p = g^(ab) mod p
   - Both arrive at the same shared secret K!

Security:
The security relies on the Discrete Logarithm Problem (DLP), which is
computationally infeasible to solve for large prime numbers.
"""

import random
import secrets


class DiffieHellman:
    """
    Diffie-Hellman Key Exchange implementation.
    
    Attributes:
        p (int): Prime modulus
        g (int): Primitive root (generator)
        private_key (int): Private key
        public_key (int): Public key
    """
    
    # Some well-known safe primes for demonstration
    SAFE_PRIMES = {
        'small': 23,      # For educational demonstration
        'medium': 7919,   # Slightly larger
        'large': 104729,  # Even larger
        'very_large': 15485863  # Large prime
    }
    
    def __init__(self):
        self.p = None          # Prime modulus
        self.g = None          # Generator (primitive root)
        self.private_key = None
        self.public_key = None
    
    def is_prime(self, n: int) -> bool:
        """
        Check if a number is prime using Miller-Rabin primality test.
        
        Args:
            n (int): Number to test
            
        Returns:
            bool: True if probably prime
        """
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        # Write n-1 as 2^r * d
        r, d = 0, n - 1
        while d % 2 == 0:
            r += 1
            d //= 2
        
        # Witnesses to test
        witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
        
        for a in witnesses:
            if a >= n:
                continue
            
            x = pow(a, d, n)
            
            if x == 1 or x == n - 1:
                continue
            
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        
        return True
    
    def is_primitive_root(self, g: int, p: int) -> bool:
        """
        Check if g is a primitive root modulo p.
        
        A primitive root g generates all integers from 1 to p-1
        when raised to powers 1, 2, ..., p-1 modulo p.
        
        Args:
            g (int): Candidate primitive root
            p (int): Prime modulus
            
        Returns:
            bool: True if g is a primitive root mod p
        """
        if p < 2:
            return False
        
        # Calculate Euler's totient φ(p) = p-1 for prime p
        phi = p - 1
        
        # Find prime factors of φ(p)
        factors = set()
        n = phi
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.add(d)
                n //= d
            d += 1
        if n > 1:
            factors.add(n)
        
        # g is a primitive root if g^(φ(p)/q) ≠ 1 (mod p) for all prime factors q
        for q in factors:
            if pow(g, phi // q, p) == 1:
                return False
        
        return True
    
    def find_primitive_root(self, p: int) -> int:
        """
        Find a primitive root modulo p.
        
        Args:
            p (int): Prime modulus
            
        Returns:
            int: A primitive root, or -1 if not found
        """
        for g in range(2, p):
            if self.is_primitive_root(g, p):
                return g
        return -1
    
    def set_parameters(self, p: int, g: int) -> tuple:
        """
        Set the public parameters (prime p and generator g).
        
        Args:
            p (int): Prime modulus
            g (int): Primitive root (generator)
            
        Returns:
            tuple: (success, message, validation_details)
        """
        validation = []
        
        # Validate prime
        if not self.is_prime(p):
            return False, "p is not a prime number", ""
        validation.append(f"✓ p = {p} is prime")
        
        # Validate primitive root
        if not self.is_primitive_root(g, p):
            return False, f"g = {g} is not a primitive root modulo {p}", ""
        validation.append(f"✓ g = {g} is a primitive root modulo {p}")
        
        self.p = p
        self.g = g
        
        return True, "Parameters set successfully", "\n".join(validation)
    
    def generate_private_key(self, max_bits: int = 16) -> int:
        """
        Generate a random private key.
        
        Args:
            max_bits (int): Maximum bits for the key
            
        Returns:
            int: Private key
        """
        # Generate random private key in range [2, p-2]
        if self.p:
            self.private_key = secrets.randbelow(self.p - 3) + 2
        else:
            self.private_key = secrets.randbits(max_bits)
        
        return self.private_key
    
    def compute_public_key(self, private_key: int = None) -> int:
        """
        Compute public key from private key.
        
        Public Key = g^private_key mod p
        
        Args:
            private_key (int): Optional private key (uses stored if not provided)
            
        Returns:
            int: Public key
        """
        if private_key is not None:
            self.private_key = private_key
        
        if self.p is None or self.g is None:
            raise ValueError("Parameters (p, g) not set")
        if self.private_key is None:
            raise ValueError("Private key not set")
        
        self.public_key = pow(self.g, self.private_key, self.p)
        return self.public_key
    
    def compute_shared_secret(self, other_public_key: int) -> int:
        """
        Compute the shared secret using the other party's public key.
        
        Shared Secret = other_public_key^private_key mod p
        
        Args:
            other_public_key (int): The other party's public key
            
        Returns:
            int: Shared secret
        """
        if self.p is None:
            raise ValueError("Prime p not set")
        if self.private_key is None:
            raise ValueError("Private key not set")
        
        return pow(other_public_key, self.private_key, self.p)
    
    def full_key_exchange(self, p: int, g: int, 
                          alice_private: int = None, 
                          bob_private: int = None) -> tuple:
        """
        Perform a complete Diffie-Hellman key exchange demonstration.
        
        Args:
            p (int): Prime modulus
            g (int): Primitive root
            alice_private (int): Alice's private key (optional, auto-generated)
            bob_private (int): Bob's private key (optional, auto-generated)
            
        Returns:
            tuple: (shared_key, detailed_steps)
        """
        steps = []
        steps.append("═" * 60)
        steps.append("DIFFIE-HELLMAN KEY EXCHANGE")
        steps.append("═" * 60)
        steps.append("")
        
        # Set parameters
        success, message, validation = self.set_parameters(p, g)
        if not success:
            return None, f"Error: {message}"
        
        steps.append("STEP 1: PUBLIC PARAMETERS (agreed upon publicly)")
        steps.append("─" * 60)
        steps.append(f"  Prime (p) = {p}")
        steps.append(f"  Generator (g) = {g}")
        steps.append(f"  {validation}")
        steps.append("")
        
        # Alice's keys
        if alice_private is None:
            alice_private = secrets.randbelow(p - 3) + 2
        
        alice_public = pow(g, alice_private, p)
        
        steps.append("STEP 2: ALICE'S KEY GENERATION")
        steps.append("─" * 60)
        steps.append(f"  Private key (a) = {alice_private} (kept secret)")
        steps.append(f"  Public key (A) = g^a mod p")
        steps.append(f"                 = {g}^{alice_private} mod {p}")
        steps.append(f"                 = {alice_public}")
        steps.append("")
        
        # Bob's keys
        if bob_private is None:
            bob_private = secrets.randbelow(p - 3) + 2
        
        bob_public = pow(g, bob_private, p)
        
        steps.append("STEP 3: BOB'S KEY GENERATION")
        steps.append("─" * 60)
        steps.append(f"  Private key (b) = {bob_private} (kept secret)")
        steps.append(f"  Public key (B) = g^b mod p")
        steps.append(f"                 = {g}^{bob_private} mod {p}")
        steps.append(f"                 = {bob_public}")
        steps.append("")
        
        # Public key exchange
        steps.append("STEP 4: PUBLIC KEY EXCHANGE")
        steps.append("─" * 60)
        steps.append(f"  Alice sends A = {alice_public} to Bob (over public channel)")
        steps.append(f"  Bob sends B = {bob_public} to Alice (over public channel)")
        steps.append("")
        
        # Shared secret computation
        alice_shared = pow(bob_public, alice_private, p)
        bob_shared = pow(alice_public, bob_private, p)
        
        steps.append("STEP 5: SHARED SECRET COMPUTATION")
        steps.append("─" * 60)
        steps.append("")
        steps.append("  Alice computes:")
        steps.append(f"    K = B^a mod p")
        steps.append(f"      = {bob_public}^{alice_private} mod {p}")
        steps.append(f"      = {alice_shared}")
        steps.append("")
        steps.append("  Bob computes:")
        steps.append(f"    K = A^b mod p")
        steps.append(f"      = {alice_public}^{bob_private} mod {p}")
        steps.append(f"      = {bob_shared}")
        steps.append("")
        
        # Verification
        steps.append("STEP 6: VERIFICATION")
        steps.append("─" * 60)
        if alice_shared == bob_shared:
            steps.append(f"  ✓ Both computed the SAME shared secret!")
            steps.append(f"  ✓ Shared Secret (K) = {alice_shared}")
            steps.append("")
            steps.append("  Mathematical proof:")
            steps.append(f"    Alice: K = B^a = (g^b)^a = g^(ab) mod p")
            steps.append(f"    Bob:   K = A^b = (g^a)^b = g^(ab) mod p")
            steps.append(f"    Since ab = ba, both get g^(ab) = {alice_shared}")
        else:
            steps.append(f"  ✗ Error: Shared secrets don't match!")
            steps.append(f"    Alice's K = {alice_shared}")
            steps.append(f"    Bob's K = {bob_shared}")
        
        steps.append("")
        steps.append("═" * 60)
        steps.append("SECURITY NOTE")
        steps.append("═" * 60)
        steps.append("")
        steps.append("An eavesdropper knows: p, g, A, B")
        steps.append("To find K, they need 'a' or 'b', which requires solving:")
        steps.append(f"  a = log_g(A) mod p  (Discrete Logarithm Problem)")
        steps.append("")
        steps.append("For large primes (2048+ bits), this is computationally infeasible!")
        
        return alice_shared, "\n".join(steps)
    
    def demonstrate_with_values(self, p: int, g: int, a: int, b: int) -> str:
        """
        Demonstrate key exchange with specific values.
        
        Args:
            p (int): Prime modulus
            g (int): Generator
            a (int): Alice's private key
            b (int): Bob's private key
            
        Returns:
            str: Detailed demonstration
        """
        shared_key, steps = self.full_key_exchange(p, g, a, b)
        return steps


# Example usage and testing
if __name__ == "__main__":
    dh = DiffieHellman()
    
    # Simple demonstration with small numbers
    print("Small Numbers Demo (for educational purposes):")
    print("=" * 60)
    
    p = 23  # Prime
    g = 5   # Primitive root
    a = 6   # Alice's private key
    b = 15  # Bob's private key
    
    shared_key, steps = dh.full_key_exchange(p, g, a, b)
    print(steps)
    
    print("\n\nLarger Prime Demo:")
    print("=" * 60)
    
    p = 7919
    g = 7
    shared_key, steps = dh.full_key_exchange(p, g)
    print(steps)

