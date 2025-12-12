#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                                ║
║   ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗ ███████╗██╗   ██╗██╗████████╗███████╗   ║
║  ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝██║   ██║██║╚══██╔══╝██╔════╝   ║
║  ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║███████╗██║   ██║██║   ██║   █████╗     ║
║  ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║╚════██║██║   ██║██║   ██║   ██╔══╝     ║
║  ╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝███████║╚██████╔╝██║   ██║   ███████╗   ║
║   ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   ╚══════╝   ║
║                                                                                ║
║                         PRO EDITION - VERSION 2.0                             ║
║                                                                                ║
║   🔐 Advanced Cryptography Desktop Application                                 ║
║   📚 CS-3002 Information Security                                             ║
║                                                                                ║
╚═══════════════════════════════════════════════════════════════════════════════╝

CryptoSuite Pro - A comprehensive cryptography toolkit featuring:

✨ CLASSICAL CIPHERS
   • Caesar Cipher - Shift-based substitution
   • Vigenère Cipher - Polyalphabetic substitution
   • Playfair Cipher - Digraph substitution with 5×5 matrix
   • Hill Cipher - Matrix-based polygraphic encryption
   • Monoalphabetic Cipher - Custom alphabet mapping

🛡️ MODERN ENCRYPTION
   • AES-128 - Advanced Encryption Standard (128-bit)
   • DES - Data Encryption Standard (educational)

🤝 KEY EXCHANGE
   • Diffie-Hellman - Secure key establishment protocol

📁 BONUS FEATURES
   • File Encryption/Decryption using AES
   • Step-by-step calculation demonstrations
   • Beautiful, professional GUI

Copyright © 2025 - CS-3002 Information Security Project
"""

import sys
import os

# Ensure the project root is in the path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


def print_banner():
    """Print the startup banner."""
    banner = """
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║    ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗                     ║
║   ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗                    ║
║   ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║                    ║
║   ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║                    ║
║   ╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝                    ║
║    ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝                     ║
║                                                                          ║
║   ███████╗██╗   ██╗██╗████████╗███████╗    ██████╗ ██████╗  ██████╗      ║
║   ██╔════╝██║   ██║██║╚══██╔══╝██╔════╝    ██╔══██╗██╔══██╗██╔═══██╗     ║
║   ███████╗██║   ██║██║   ██║   █████╗      ██████╔╝██████╔╝██║   ██║     ║
║   ╚════██║██║   ██║██║   ██║   ██╔══╝      ██╔═══╝ ██╔══██╗██║   ██║     ║
║   ███████║╚██████╔╝██║   ██║   ███████╗    ██║     ██║  ██║╚██████╔╝     ║
║   ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   ╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝      ║
║                                                                          ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║   🔐 ADVANCED CRYPTOGRAPHY DESKTOP APPLICATION                           ║
║   📚 CS-3002 Information Security Project                                ║
║                                                                          ║
║   Version 2.0 Pro Edition                                                ║
║                                                                          ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║   ✨ Features:                                                           ║
║      • 5 Classical Ciphers (Caesar, Vigenère, Playfair, Hill, Mono)     ║
║      • 2 Modern Standards (AES-128, DES)                                 ║
║      • Diffie-Hellman Key Exchange                                       ║
║      • File Encryption/Decryption                                        ║
║      • Step-by-Step Calculations                                         ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
"""
    print(banner)


def main():
    """Main entry point for CryptoSuite Pro."""
    try:
        # Print startup banner
        print_banner()
        print("   🚀 Starting CryptoSuite Pro...")
        print("   📍 Please wait while the application loads...\n")
        
        # Import and run the GUI
        from gui.main_window import CryptoApp
        
        print("   ✅ All modules loaded successfully!")
        print("   🎨 Launching graphical interface...\n")
        print("   ℹ️  Close this window to exit the application.\n")
        print("=" * 76)
        
        # Create and run the application
        app = CryptoApp()
        app.mainloop()
        
        print("\n   👋 Thank you for using CryptoSuite Pro!")
        print("   📚 CS-3002 Information Security\n")
        
    except ImportError as e:
        print(f"\n   ❌ Error: Missing required module - {e}")
        print("   💡 Try running: pip install -r requirements.txt\n")
        sys.exit(1)
        
    except Exception as e:
        print(f"\n   ❌ Error: {e}")
        print("   💡 Please check the error and try again.\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
