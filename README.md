# 🔐 CryptoSuite Pro

<div align="center">

![CryptoSuite Pro](https://img.shields.io/badge/CryptoSuite-Pro%20Edition-0d1117?style=for-the-badge&logo=lock&logoColor=58a6ff)
![Python](https://img.shields.io/badge/Python-3.8+-3fb950?style=for-the-badge&logo=python&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-8957e5?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-58a6ff?style=for-the-badge)

### **Advanced Cryptography Desktop Application**
#### CS-3002 Information Security Project

*A stunning, professional-grade toolkit for encryption, decryption, and key exchange*

**Submission Date: December 2, 2025**

</div>

---

## ✨ Features Overview

### 📜 Classical Ciphers (5 Algorithms - Exceeds Requirement!)
| Cipher | Description | Status |
|--------|-------------|--------|
| **Caesar Cipher** | Shift-based substitution with configurable key (0-25) | ✅ |
| **Vigenère Cipher** | Polyalphabetic substitution using keyword encryption | ✅ |
| **Playfair Cipher** | Digraph substitution with 5×5 key matrix | ✅ |
| **Hill Cipher** | Matrix-based (2×2) polygraphic encryption | ✅ |
| **Monoalphabetic** | Custom alphabet mapping with random key generation | ✅ |

### 🛡️ Modern Encryption (Industry Standards)
| Algorithm | Key Size | Description | Status |
|-----------|----------|-------------|--------|
| **AES-128** | 128-bit | Advanced Encryption Standard (CBC mode) | ✅ |
| **DES** | 56-bit | Data Encryption Standard (16 Feistel rounds) | ✅ |

### 🤝 Key Exchange
| Protocol | Description | Status |
|----------|-------------|--------|
| **Diffie-Hellman** | Secure key establishment over insecure channels | ✅ |

### 🎁 Bonus & Extra Features
| Feature | Description | Status |
|---------|-------------|--------|
| **File Encryption** | AES-128 file encryption/decryption | ⭐ Bonus |
| **Step-by-Step Calculations** | Educational calculation display for ALL algorithms | ⭐ Bonus |
| **Load from File** | Load text from any file type (all 7 algorithms) | 🆕 Extra |
| **Save to File** | Save encrypted/decrypted results (all 7 algorithms) | 🆕 Extra |
| **OCR Text Extraction** | Extract text from images using Tesseract (all 7 algorithms) | 🆕 Extra |
| **Hexadecimal Output** | Hex display for modern ciphers | ✅ |
| **Premium Dark Theme UI** | GitHub-inspired dark theme with animations | ✅ |

---

## 🎨 Premium User Interface

CryptoSuite Pro features a stunning, professional-grade GUI designed for optimal user experience:

- 🌑 **Deep Dark Theme** - GitHub-inspired dark color palette (#0d1117)
- ✨ **Animated Elements** - Subtle pulsing effects and smooth transitions
- 🎯 **Intuitive Navigation** - Clean sidebar with visual indicators
- 📊 **Beautiful Cards** - Feature cards with hover effects
- 🔤 **Modern Typography** - Carefully selected fonts for readability
- 📱 **Responsive Design** - Adapts to different window sizes

### Color Palette
| Element | Color | Hex |
|---------|-------|-----|
| Background | Deep Dark | `#0d1117` |
| Surface | Dark Gray | `#161b22` |
| Primary | Blue | `#58a6ff` |
| Success | Green | `#3fb950` |
| Warning | Gold | `#d29922` |
| Error | Red | `#f85149` |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Tesseract OCR (optional, for OCR feature)

### Installation

1. **Clone or download the project**
```bash
cd IS_SEMESTER_PROJECT
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python main.py
```

4. **(Optional) Install Tesseract OCR for image text extraction**
   - Download from: https://github.com/UB-Mannheim/tesseract/wiki
   - Add to system PATH (e.g., `C:\Program Files\Tesseract-OCR`)

---

## 📦 Project Structure

```
cipher-desktop-app/
├── main.py                    # Entry point with premium banner
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── PROJECT_REPORT.html        # Detailed project report (HTML)
├── PROJECT_REPORT.md          # Project report (Markdown)
│
├── ciphers/                   # Classical cipher implementations
│   ├── __init__.py
│   ├── caesar_cipher.py       # Caesar cipher with steps
│   ├── vigenere_cipher.py     # Vigenère cipher with tableau
│   ├── playfair_cipher.py     # Playfair with matrix display
│   ├── hill_cipher.py         # Hill 2×2 matrix cipher
│   └── monoalphabetic_cipher.py
│
├── modern_ciphers/            # Modern encryption algorithms
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
└── build_exe.py               # Executable builder script (run to generate dist/CryptoSuite.exe)
```

> The compiled `dist/CryptoSuite.exe` is not committed — run `python build_exe.py`
> to produce it locally.

---

## 🔧 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| customtkinter | 5.2.1 | Modern dark-themed GUI framework |
| pycryptodome | 3.19.0 | AES and DES implementations |
| numpy | 1.26.2 | Matrix operations (Hill cipher) |
| Pillow | 10.1.0 | Image handling for OCR |
| pytesseract | 0.3.13 | OCR text extraction from images |
| darkdetect | 0.8.0 | System theme detection |

---

## 📖 Algorithm Details

### Caesar Cipher
- **Type**: Monoalphabetic substitution
- **Key**: Single integer (0-25)
- **Formula**: `C = (P + K) mod 26`

### Vigenère Cipher  
- **Type**: Polyalphabetic substitution
- **Key**: Keyword of any length
- **Uses**: Tabula recta (Vigenère tableau)

### Playfair Cipher
- **Type**: Digraph substitution
- **Key**: Keyword → 5×5 matrix (I/J combined)
- **Rules**: Same row, same column, rectangle

### Hill Cipher
- **Type**: Polygraphic substitution
- **Key**: 2×2 matrix with inverse mod 26
- **Formula**: `C = K × P mod 26`

### AES-128
- **Type**: Symmetric block cipher
- **Key Size**: 128 bits (16 bytes)
- **Block Size**: 128 bits
- **Rounds**: 10
- **Operations**: SubBytes, ShiftRows, MixColumns, AddRoundKey

### DES
- **Type**: Symmetric block cipher (legacy)
- **Key Size**: 56 bits (64 with parity)
- **Block Size**: 64 bits
- **Rounds**: 16 Feistel rounds
- **⚠️ Note**: Included for educational purposes only

### Diffie-Hellman
- **Type**: Key exchange protocol
- **Parameters**: Prime (p), Generator (g)
- **Formula**: `A = g^a mod p`, `B = g^b mod p`, `K = B^a = A^b mod p`

---

## 📁 File Operations

### Load from File
Supports multiple file types with automatic encoding detection:
- Text files (`.txt`)
- Data files (`.csv`, `.json`, `.xml`)
- Web files (`.html`, `.htm`)
- Documentation (`.md`)
- Source code (`.py`, `.js`, `.java`, `.c`, `.cpp`, `.h`, `.cs`)

### Save to File
Save encrypted/decrypted results to text files for all algorithms.

### OCR Text Extraction
Extract text from images using Tesseract OCR:
- PNG, JPG, JPEG, BMP, TIFF, GIF support
- Automatic text extraction
- Direct encryption of extracted text

---

## 🏗️ Building Executable

Create a standalone executable:

```bash
python build_exe.py
```

The executable will be in the `dist/` folder (~28 MB).

---

## 📝 Requirements Fulfilled

| Requirement | Required | Implemented | Status |
|-------------|----------|-------------|--------|
| Desktop GUI Application | Yes | CustomTkinter | ✅ |
| Classical Ciphers | At least 2 | **5 Implemented** | ⭐ Exceeded |
| AES Implementation | Yes | AES-128 CBC | ✅ |
| DES Implementation | Yes | 16 Feistel rounds | ✅ |
| Diffie-Hellman | Yes | Full implementation | ✅ |
| Display Plaintext/Ciphertext | Yes | All views | ✅ |
| Display Keys | Yes | All ciphers | ✅ |
| Calculation Steps (Optional) | Optional | All algorithms | ⭐ Bonus |
| File Encryption (Bonus) | Bonus | AES file support | ⭐ Bonus |
| Load from File | Not required | All 7 algorithms | 🆕 Extra |
| Save to File | Not required | All 7 algorithms | 🆕 Extra |
| OCR Extraction | Not required | All 7 algorithms | 🆕 Extra |
| Standalone Executable | Yes | CryptoSuite.exe | ✅ |

---

## 👨‍💻 Usage Examples

### Caesar Cipher
1. Enter plaintext: `HELLO WORLD`
2. Set shift key: `3`
3. Click **Encrypt**
4. Result: `KHOOR ZRUOG`

### AES-128 Encryption
1. Enter plaintext: `Secret Message`
2. Click **Generate** for key
3. Click **Encrypt**
4. Copy the hex ciphertext and IV

### Diffie-Hellman Key Exchange
1. Set prime: `23`, generator: `5`
2. Set Alice's private key: `6`
3. Set Bob's private key: `15`
4. Click **Perform Key Exchange**
5. Both compute the same shared secret!

### Load from File & Encrypt
1. Click **Load from File** button
2. Select any text file
3. Text is loaded into input field
4. Apply any encryption algorithm
5. Click **Save Result to File** to save

### OCR Text Extraction
1. Click **Extract from Image (OCR)** button
2. Select an image file (PNG, JPG, etc.)
3. Text is extracted and loaded
4. Apply any encryption algorithm

---

## 🎓 Academic Information

- **Course**: CS-3002 Information Security
- **Project**: Desktop Cryptography Application
- **Semester**: Fall 2024
- **Submission Date**: December 2, 2025
- **Institution**: FAST-NUCES

### Group Members
| Roll Number | Name |
|-------------|------|
| 22F-3848 | Ahmed Hassan Gondal |
| 22F-3340 | Muhammad Uzair |
| 22F-3386 | Abdul Rafay |

---

## 📄 License

This project is developed for educational purposes as part of the CS-3002 course curriculum.

---

<div align="center">

**Made with ❤️ for Information Security**

*CryptoSuite Pro - Securing Your Data, One Encryption at a Time*

![Footer](https://img.shields.io/badge/Version-2.0_Pro-58a6ff?style=flat-square)
![Footer](https://img.shields.io/badge/Algorithms-8_Total-3fb950?style=flat-square)
![Footer](https://img.shields.io/badge/Features-21_Buttons-d29922?style=flat-square)

</div>
