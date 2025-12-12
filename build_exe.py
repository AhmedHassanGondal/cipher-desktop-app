"""
Build Script for Creating Executable
=====================================
This script creates a standalone .exe file for the Cryptography Application.

Usage:
    python build_exe.py

Output:
    dist/CryptoSuite.exe
"""

import subprocess
import sys
import os

def build():
    """Build the executable using PyInstaller."""
    
    # PyInstaller command with options
    cmd = [
        sys.executable,
        '-m', 'PyInstaller',
        '--name=CryptoSuite',
        '--onefile',                    # Single executable file
        '--windowed',                   # No console window
        '--icon=NONE',                  # No custom icon (you can add one later)
        '--add-data=ciphers;ciphers',   # Include ciphers package
        '--add-data=modern_ciphers;modern_ciphers',  # Include modern_ciphers package
        '--add-data=gui;gui',           # Include gui package
        '--hidden-import=customtkinter',
        '--hidden-import=Crypto',
        '--hidden-import=Crypto.Cipher',
        '--hidden-import=Crypto.Cipher.AES',
        '--hidden-import=Crypto.Cipher.DES',
        '--hidden-import=Crypto.Random',
        '--hidden-import=Crypto.Util.Padding',
        '--hidden-import=numpy',
        '--hidden-import=PIL',
        '--collect-all=customtkinter',
        '--noconfirm',                  # Replace existing build
        'main.py'
    ]
    
    print("=" * 60)
    print("BUILDING CRYPTOGRAPHY SUITE EXECUTABLE")
    print("=" * 60)
    print("\nThis may take a few minutes...")
    print("\nRunning PyInstaller with the following settings:")
    print("  - Output: CryptoSuite.exe")
    print("  - Type: Single file executable")
    print("  - Window mode: No console")
    print("\n")
    
    # Run PyInstaller
    result = subprocess.run(cmd, cwd=os.path.dirname(os.path.abspath(__file__)))
    
    if result.returncode == 0:
        print("\n" + "=" * 60)
        print("BUILD SUCCESSFUL!")
        print("=" * 60)
        print("\nExecutable created at: dist/CryptoSuite.exe")
        print("\nYou can now distribute this file to run the application")
        print("without requiring Python to be installed.")
    else:
        print("\n" + "=" * 60)
        print("BUILD FAILED!")
        print("=" * 60)
        print("\nPlease check the error messages above.")
    
    return result.returncode

if __name__ == "__main__":
    sys.exit(build())

