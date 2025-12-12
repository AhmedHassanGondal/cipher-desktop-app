# 🔐 CRYPTOGRAPHY DESKTOP APPLICATION

## CS-3002 Information Security - Project Report

---

**Course:** CS-3002 Information Security  
**Instructor:** Miss Juhinah Batool  
**Semester:** Fall 2025

**Group Members:**

| Roll Number | Name |
|-------------|------|
| 22F-3848 | Ahmed Hassan Gondal |
| 22F-3340 | Muhammad Uzair |
| 22F-3386 | Abdul Rafay |

**Submission Date:** December 12, 2025

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Project Overview](#2-project-overview)
3. [System Requirements](#3-system-requirements)
4. [Algorithms Implemented](#4-algorithms-implemented)
   - 4.1 [Classical Ciphers](#41-classical-ciphers)
   - 4.2 [Modern Ciphers](#42-modern-ciphers)
   - 4.3 [Key Exchange](#43-key-exchange)
5. [Implementation Details](#5-implementation-details)
6. [User Interface](#6-user-interface)
7. [Extra Features](#7-extra-features)
8. [Testing & Results](#8-testing--results)
9. [Conclusion](#9-conclusion)
10. [References](#10-references)

---

## 1. Introduction

Cryptography is the science of securing communication and data through the use of codes and ciphers. In today's digital age, cryptography plays a crucial role in protecting sensitive information from unauthorized access. This project implements a comprehensive desktop application that demonstrates various cryptographic algorithms, from classical ciphers to modern encryption standards.

The application serves as both an educational tool and a practical demonstration of cryptographic concepts covered in the CS-3002 Information Security course. It provides hands-on experience with:

- **Symmetric encryption techniques** (AES-128, DES)
- **Classical substitution and transposition ciphers** (Caesar, Vigenère, Playfair, Hill, Monoalphabetic)
- **Key exchange protocols** (Diffie-Hellman)
- **Mathematical foundations** of cryptography
- **File encryption/decryption** for practical applications
- **OCR text extraction** from images for encryption

> **💡 Project Highlight:** This application exceeds the minimum requirements by implementing 5 classical ciphers (only 2 required), providing step-by-step calculations for all algorithms, and including bonus features like file encryption and OCR text extraction.

---

## 2. Project Overview

### 2.1 Objectives

The primary objectives of this project are:

1. **Implement Classical Ciphers:** Develop working implementations of historical encryption algorithms including Caesar, Vigenère, Playfair, Hill, and Monoalphabetic ciphers.
2. **Implement Modern Encryption:** Create AES-128 and DES encryption/decryption modules with proper key handling and hexadecimal I/O.
3. **Implement Key Exchange:** Demonstrate the Diffie-Hellman key exchange protocol with step-by-step calculations.
4. **Create User-Friendly GUI:** Design an intuitive graphical interface with modern aesthetics and premium dark theme.
5. **Provide Educational Value:** Display step-by-step calculations for each algorithm to aid understanding.
6. **Enable File Operations:** Support loading text from files and saving encrypted results.
7. **Support OCR:** Extract text from images for encryption using Tesseract OCR.

### 2.2 Features

| Feature | Description | Status |
|---------|-------------|--------|
| Classical Ciphers | 5 classical ciphers implemented | ⭐ EXCEEDED |
| Modern Encryption | AES-128 (CBC mode) and DES | ✅ Complete |
| Key Exchange | Complete Diffie-Hellman implementation | ✅ Complete |
| File Encryption | AES file encryption/decryption | ⭐ Bonus |
| Step-by-Step Display | Calculation visualization for ALL algorithms | ✅ Complete |
| Load from File | Load text from any file type (all 7 algorithms) | 🆕 Extra |
| Save to File | Save encrypted/decrypted results (all 7 algorithms) | 🆕 Extra |
| OCR Extraction | Extract text from images (all 7 algorithms) | 🆕 Extra |
| Premium GUI | Dark theme interface with animations | ✅ Complete |
| Standalone Executable | CryptoSuite.exe - No Python required | ✅ Complete |

### 2.3 Technology Stack

| Component | Technology | Version |
|-----------|------------|---------|
| Programming Language | Python | 3.11 |
| GUI Framework | CustomTkinter | 5.2.1 |
| Cryptography Library | PyCryptodome | 3.19.0 |
| Numerical Library | NumPy | 1.26.2 |
| Image Processing | Pillow | 10.1.0 |
| OCR Engine | pytesseract | 0.3.13 |
| Build Tool | PyInstaller | 6.3.0 |

---

## 3. System Requirements

### 3.1 Minimum Requirements

| Component | Requirement |
|-----------|-------------|
| Operating System | Windows 10/11 |
| RAM | 4 GB |
| Storage | 100 MB |
| Display | 1280x720 resolution |

### 3.2 For Running from Source

| Component | Version |
|-----------|---------|
| Python | 3.8 or higher |
| pip | Latest version |
| Tesseract OCR (optional) | 5.0+ (for OCR feature) |

### 3.3 Dependencies

```
# GUI Framework
customtkinter==5.2.1

# Cryptography
pycryptodome==3.19.0

# Numerical Operations
numpy==1.26.2

# Image Processing
Pillow==10.1.0

# OCR Support
pytesseract==0.3.13

# Theme Detection
darkdetect==0.8.0
```

---

## 4. Algorithms Implemented

### 4.1 Classical Ciphers

#### 4.1.1 Caesar Cipher

**Description:** The Caesar cipher is one of the simplest and oldest encryption techniques. It works by shifting each letter in the plaintext by a fixed number of positions in the alphabet.

**Mathematical Formula:**
- Encryption: `E(x) = (x + k) mod 26`
- Decryption: `D(x) = (x - k) mod 26`

Where:
- `x` = position of the letter (A=0, B=1, ..., Z=25)
- `k` = shift key (0-25)

**Example:**
```
Plaintext:  HELLO
Shift:      3
Ciphertext: KHOOR
```

**Calculation Steps:**
| Letter | Position | +3 | mod 26 | Result |
|--------|----------|-----|--------|--------|
| H | 7 | 10 | 10 | K |
| E | 4 | 7 | 7 | H |
| L | 11 | 14 | 14 | O |
| L | 11 | 14 | 14 | O |
| O | 14 | 17 | 17 | R |

---

#### 4.1.2 Vigenère Cipher

**Description:** A polyalphabetic substitution cipher that uses a keyword to encrypt the message. Each letter uses a different shift based on the corresponding keyword letter.

**Mathematical Formula:**
- Encryption: `Cᵢ = (Pᵢ + Kᵢ) mod 26`
- Decryption: `Pᵢ = (Cᵢ - Kᵢ) mod 26`

**Example:**
```
Plaintext:  HELLO
Keyword:    KEY (extended to KEYKE)
Ciphertext: RIJVS
```

---

#### 4.1.3 Playfair Cipher

**Description:** A digraph substitution cipher that encrypts pairs of letters using a 5×5 key matrix. I and J are combined into one cell.

**Key Matrix Generation:**
1. Remove duplicate letters from keyword
2. Fill remaining cells with unused letters
3. I and J share the same cell

**Encryption Rules:**
1. **Same Row:** Replace each letter with the letter to its right
2. **Same Column:** Replace each letter with the letter below
3. **Rectangle:** Swap columns within the same row

**Example with keyword "MONARCHY":**
```
Key Matrix:
M O N A R
C H Y B D
E F G I/J K
L P Q S T
U V W X Z
```

---

#### 4.1.4 Hill Cipher (2×2 Matrix)

**Description:** A polygraphic cipher using linear algebra. It encrypts blocks of letters using matrix multiplication.

**Mathematical Formula:**
- Encryption: `C = K × P (mod 26)`
- Decryption: `P = K⁻¹ × C (mod 26)`

**Key Requirements:**
- Matrix must be invertible
- `gcd(det(K), 26) = 1`

**Example:**
```
Key: "HILL" → Matrix [[7,8],[11,11]]
Plaintext: "HE" → [7,4]
Ciphertext computed via matrix multiplication mod 26
```

---

#### 4.1.5 Monoalphabetic Cipher

**Description:** A substitution cipher where each letter is replaced by a fixed substitute letter throughout the message.

**Key Space:** 26! ≈ 4.03 × 10²⁶ possible keys

**Example:**
```
Plain:  ABCDEFGHIJKLMNOPQRSTUVWXYZ
Cipher: SECURITYABDFGHJKLMNOPQVWXZ

Plaintext:  HELLO
Ciphertext: Substituted based on key
```

---

### 4.2 Modern Ciphers

#### 4.2.1 AES-128 (Advanced Encryption Standard)

**Description:** AES is a symmetric block cipher established by NIST in 2001. Our implementation uses AES-128 with CBC mode.

**Specifications:**
| Parameter | Value |
|-----------|-------|
| Block Size | 128 bits (16 bytes) |
| Key Size | 128 bits (16 bytes) |
| Number of Rounds | 10 |
| Mode | CBC (Cipher Block Chaining) |

**Round Operations:**
1. **SubBytes:** Non-linear byte substitution using S-box
2. **ShiftRows:** Cyclic row shifting
3. **MixColumns:** Column mixing (except final round)
4. **AddRoundKey:** XOR with round key

**Implementation Features:**
- CBC mode for secure chaining
- PKCS7 padding
- Random IV generation
- File encryption support

---

#### 4.2.2 DES (Data Encryption Standard)

**Description:** DES is a symmetric block cipher using the Feistel structure with 16 rounds.

**Specifications:**
| Parameter | Value |
|-----------|-------|
| Block Size | 64 bits (8 bytes) |
| Key Size | 56 bits (64 with parity) |
| Number of Rounds | 16 Feistel rounds |

**Algorithm Structure:**
1. Initial Permutation (IP)
2. 16 Feistel Rounds:
   - Expansion (32→48 bits)
   - Key XOR
   - S-box substitution (48→32 bits)
   - Permutation (P-box)
   - XOR with left half
   - Swap halves
3. Final Permutation (IP⁻¹)

> **⚠️ Security Note:** DES is now considered insecure due to its 56-bit key length. It is included for educational purposes only.

---

### 4.3 Key Exchange

#### 4.3.1 Diffie-Hellman Key Exchange

**Description:** A method for securely exchanging cryptographic keys over a public channel, published in 1976.

**Mathematical Foundation:**

1. **Public Parameters:**
   - `p` = Large prime number
   - `g` = Primitive root modulo p

2. **Key Generation:**
   - Alice: Private key `a`, Public key `A = gᵃ mod p`
   - Bob: Private key `b`, Public key `B = gᵇ mod p`

3. **Shared Secret:**
   - Alice computes: `K = Bᵃ mod p`
   - Bob computes: `K = Aᵇ mod p`
   - Both get: `K = gᵃᵇ mod p`

**Example:**
```
p = 23 (prime)
g = 5 (primitive root)

Alice: a = 6 (private)
       A = 5⁶ mod 23 = 8 (public)

Bob:   b = 15 (private)
       B = 5¹⁵ mod 23 = 19 (public)

Shared Secret:
Alice: K = 19⁶ mod 23 = 2
Bob:   K = 8¹⁵ mod 23 = 2
```

> **🔒 Security:** Based on the Discrete Logarithm Problem (DLP)

---

## 5. Implementation Details

### 5.1 Project Structure

```
IS_SEMESTER_PROJECT/
│
├── main.py                    # Entry point with premium banner
├── requirements.txt           # Dependencies
├── README.md                  # Documentation
├── PROJECT_REPORT.md          # This report
├── PROJECT_REPORT.html        # HTML version of report
│
├── ciphers/                   # Classical ciphers
│   ├── __init__.py
│   ├── caesar_cipher.py       # Caesar cipher with steps
│   ├── vigenere_cipher.py     # Vigenère cipher with tableau
│   ├── playfair_cipher.py     # Playfair with matrix display
│   ├── hill_cipher.py         # Hill 2×2 matrix cipher
│   └── monoalphabetic_cipher.py
│
├── modern_ciphers/            # Modern encryption
│   ├── __init__.py
│   ├── aes_cipher.py          # AES-128 CBC with file support
│   ├── des_cipher.py          # DES with round demonstration
│   └── diffie_hellman.py      # DH key exchange
│
├── gui/                       # Premium GUI components
│   ├── __init__.py
│   ├── main_window.py         # Main application window (4000+ lines)
│   ├── theme.py               # Color scheme and styling
│   └── animations.py          # Animation utilities
│
├── build_exe.py               # Executable builder script
└── dist/                      # Compiled executable
    └── CryptoSuite.exe        # Standalone application (28 MB)
```

### 5.2 Code Quality

- **Documentation:** All functions include docstrings
- **Type Hints:** Function parameters use type annotations
- **Error Handling:** Input validation and exception handling
- **Modularity:** Separate modules for each cipher
- **UI/UX:** Premium dark theme with smooth animations

### 5.3 Key Implementation Highlights

#### Caesar Cipher - Encryption Function
```python
def encrypt(self, plaintext: str, shift: int) -> tuple:
    for char in plaintext.upper():
        if char in self.alphabet:
            x = self.alphabet.index(char)
            encrypted_pos = (x + shift) % 26
            ciphertext.append(self.alphabet[encrypted_pos])
    return ''.join(ciphertext), calculation_steps
```

#### AES - Key Generation
```python
def generate_key(self) -> str:
    self.key = get_random_bytes(16)  # 128 bits
    return binascii.hexlify(self.key).decode('utf-8').upper()
```

#### File Loading with Multiple Encodings
```python
def _load_text_from_file(self, target_textbox):
    encodings = ['utf-8', 'utf-16', 'latin-1', 'cp1252', 'ascii']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                content = f.read()
            break
        except UnicodeDecodeError:
            continue
```

---

## 6. User Interface

### 6.1 Design Philosophy

The application features a modern premium dark theme with professional aesthetics:

- **Deep dark background:** Reduces eye strain during extended use
- **Vibrant accent colors:** Highlights important elements and actions
- **Clear typography:** Monospace fonts for code and hex values
- **Intuitive layout:** Sidebar navigation with content area
- **Smooth animations:** Pulsing effects and color transitions

### 6.2 Main Components

1. **Dashboard:** Overview of all features with animated cards
2. **Classical Ciphers Section:** All 5 classical cipher implementations
3. **Modern Ciphers Section:** AES-128 and DES with file support
4. **Key Exchange Section:** Diffie-Hellman demonstration
5. **Calculation Display:** Step-by-step visualization for each operation
6. **File Operations:** Load from file, save to file buttons
7. **OCR Integration:** Extract text from images button

### 6.3 Color Scheme

| Element | Color | Hex |
|---------|-------|-----|
| Background | Deep Dark | #0d1117 |
| Surface | Dark Gray | #161b22 |
| Primary | Blue | #58a6ff |
| Success | Green | #3fb950 |
| Warning | Gold | #d29922 |
| Error | Red | #f85149 |
| Text Primary | Light | #f0f6fc |

---

## 7. Extra Features

### 7.1 File Operations

The application supports comprehensive file operations for all 7 encryption algorithms:

**Load from File:**
- Load text from any file type (.txt, .csv, .json, .xml, .html, .md, .py, .js, etc.)
- Automatic encoding detection (UTF-8, UTF-16, Latin-1, CP1252, ASCII)
- Direct loading into input field for encryption

**Save to File:**
- Save encrypted or decrypted results to text files
- Preserves formatting and special characters
- Available for all 7 algorithms

### 7.2 OCR Text Extraction

Extract text from images using Tesseract OCR:

**Supported Image Formats:**
- PNG (.png)
- JPEG (.jpg, .jpeg)
- BMP (.bmp)
- TIFF (.tiff)
- GIF (.gif)

**Features:**
- Automatic text extraction
- Direct loading into input field
- Works with all 7 encryption algorithms
- User-friendly error messages if Tesseract not installed

---

## 8. Testing & Results

### 8.1 Test Cases - Classical Ciphers

| Cipher | Input | Key | Expected Output | Result |
|--------|-------|-----|-----------------|--------|
| Caesar | HELLO | 3 | KHOOR | ✅ Pass |
| Caesar | WORLD | 5 | BTWQI | ✅ Pass |
| Vigenère | HELLO | KEY | RIJVS | ✅ Pass |
| Playfair | HELLO | MONARCHY | CFSUPM | ✅ Pass |
| Hill | HELLO | HILL | Valid output | ✅ Pass |
| Monoalphabetic | HELLO | SECRET | Substituted | ✅ Pass |

### 8.2 Test Cases - Modern Ciphers

| Algorithm | Test | Result |
|-----------|------|--------|
| AES-128 | Encrypt "Hello World" → Decrypt | ✅ Pass |
| AES-128 | File encryption → decryption | ✅ Pass |
| AES-128 | Hex output verification | ✅ Pass |
| DES | Encrypt "Test123" → Decrypt | ✅ Pass |
| DES | 16 rounds execution | ✅ Pass |

### 8.3 Test Cases - Diffie-Hellman

| p | g | a | b | Shared Key | Result |
|---|---|---|---|------------|--------|
| 23 | 5 | 6 | 15 | 2 | ✅ Pass |
| 7919 | 7 | 123 | 456 | Same for both | ✅ Pass |

### 8.4 Test Cases - Extra Features

| Feature | Test | Result |
|---------|------|--------|
| Load from File | Load .txt, .json, .py files | ✅ Pass |
| Save to File | Save encrypted result to .txt | ✅ Pass |
| OCR | Extract text from PNG image | ✅ Pass |
| Encoding Detection | UTF-8, UTF-16, Latin-1 files | ✅ Pass |

---

## 9. Conclusion

### 9.1 Achievements

This project successfully implements all required components and significantly exceeds the minimum requirements:

| Requirement | Required | Implemented | Status |
|-------------|----------|-------------|--------|
| Classical Ciphers | At least 2 | 5 | ⭐ EXCEEDED |
| AES Module | AES-128 | AES-128 + file encryption | ✅ Complete |
| DES Module | 16 Feistel rounds | Full implementation | ✅ Complete |
| Diffie-Hellman | Key exchange | Full with calculations | ✅ Complete |
| GUI Application | Desktop GUI | Premium dark theme | ✅ Complete |
| Hex I/O | For modern ciphers | Implemented | ✅ Complete |
| Calculation Steps | Optional | Included for all | ⭐ Bonus |
| File Encryption | Optional (Bonus) | AES file encryption | ⭐ Bonus |
| Load from File | Not required | All 7 algorithms | 🆕 Extra |
| Save to File | Not required | All 7 algorithms | 🆕 Extra |
| OCR Extraction | Not required | All 7 algorithms | 🆕 Extra |
| Executable | Required | CryptoSuite.exe (28 MB) | ✅ Complete |

### 9.2 Learning Outcomes

Through this project, we gained:

- Deep understanding of classical and modern cryptographic algorithms
- Practical experience with symmetric encryption (AES, DES)
- Knowledge of key exchange protocols (Diffie-Hellman)
- GUI development skills using Python and CustomTkinter
- Software engineering best practices including documentation and testing
- File handling with multiple encoding support
- Integration of OCR technology for text extraction

### 9.3 Future Enhancements

Potential improvements for future versions:

- Triple DES (3DES) implementation
- RSA public-key encryption
- Digital signature support
- Hash function implementations (SHA-256, MD5)
- Steganography features
- Cloud integration for secure file sharing

---

## 10. References

1. Stallings, W. (2017). *Cryptography and Network Security: Principles and Practice* (7th ed.). Pearson.

2. National Institute of Standards and Technology. (2001). *FIPS 197: Advanced Encryption Standard (AES)*. U.S. Department of Commerce.

3. National Institute of Standards and Technology. (1999). *FIPS 46-3: Data Encryption Standard (DES)*. U.S. Department of Commerce.

4. Diffie, W., & Hellman, M. (1976). New directions in cryptography. *IEEE Transactions on Information Theory*, 22(6), 644-654.

5. Kahn, D. (1996). *The Codebreakers: The Comprehensive History of Secret Communication from Ancient Times to the Internet*. Scribner.

6. CustomTkinter Documentation. https://customtkinter.tomschimansky.com/

7. PyCryptodome Documentation. https://pycryptodome.readthedocs.io/

8. Tesseract OCR Documentation. https://github.com/tesseract-ocr/tesseract

---

## Appendix A: How to Run

### Option 1: Using Executable (Recommended)
1. Navigate to `dist/` folder
2. Double-click `CryptoSuite.exe`
3. The application will launch without requiring Python

### Option 2: From Source
```bash
# Install dependencies
pip install -r requirements.txt

# Run application
python main.py
```

### Option 3: For OCR Feature (Optional)
```bash
# Install Tesseract OCR from:
# https://github.com/UB-Mannheim/tesseract/wiki

# Add to system PATH (e.g., C:\Program Files\Tesseract-OCR)

# The application will automatically detect Tesseract
```

---

## Appendix B: Screenshots

[Insert screenshots of the application here]

1. Dashboard/Home Screen - Overview with animated cards
2. Caesar Cipher - Encryption with step-by-step calculation
3. Vigenère Cipher - Keyword-based encryption with tableau
4. Playfair Cipher - Key matrix display
5. Hill Cipher - Matrix multiplication demonstration
6. AES-128 - Hexadecimal output with round demonstration
7. DES - Feistel round visualization
8. Diffie-Hellman - Key exchange process
9. File Operations - Load from file, save to file dialogs
10. OCR Extraction - Text extraction from image

---

**— End of Report —**

*This report was prepared for CS-3002 Information Security course project submission.*

**FAST-NUCES**  
Submitted: December 12, 2025
