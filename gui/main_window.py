"""
CryptoSuite Pro - Premium Cryptography Desktop Application
============================================================
A stunning, world-class GUI with smooth animations, elegant design,
and professional aesthetics for cryptographic operations.

CS-3002 Information Security Project
"""

import customtkinter as ctk
from tkinter import filedialog, messagebox
import sys
import os
import time
import math

# OCR imports (optional - for extracting text from images)
try:
    from PIL import Image
    import pytesseract
    OCR_AVAILABLE = True
    
    # Try to find Tesseract in common Windows installation paths
    if os.name == 'nt':  # Windows
        common_paths = [
            r'C:\Program Files\Tesseract-OCR\tesseract.exe',
            r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe',
            r'C:\Users\{}\AppData\Local\Tesseract-OCR\tesseract.exe'.format(os.getenv('USERNAME', '')),
        ]
        
        # Check if tesseract_cmd is already set (it might be None or empty)
        tesseract_cmd = getattr(pytesseract.pytesseract, 'tesseract_cmd', None)
        if not tesseract_cmd or not os.path.exists(tesseract_cmd) if tesseract_cmd else True:
            for path in common_paths:
                if os.path.exists(path):
                    pytesseract.pytesseract.tesseract_cmd = path
                    break
        
        # If still not found, try to get it from PATH
        tesseract_cmd = getattr(pytesseract.pytesseract, 'tesseract_cmd', None)
        if not tesseract_cmd or not os.path.exists(tesseract_cmd) if tesseract_cmd else True:
            try:
                import shutil
                tesseract_path = shutil.which('tesseract')
                if tesseract_path and os.path.exists(tesseract_path):
                    pytesseract.pytesseract.tesseract_cmd = tesseract_path
            except:
                pass
except ImportError:
    OCR_AVAILABLE = False

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ciphers.caesar_cipher import CaesarCipher
from ciphers.vigenere_cipher import VigenereCipher
from ciphers.playfair_cipher import PlayfairCipher
from ciphers.hill_cipher import HillCipher
from ciphers.monoalphabetic_cipher import MonoalphabeticCipher
from modern_ciphers.aes_cipher import AESCipher
from modern_ciphers.des_cipher import DESCipher
from modern_ciphers.diffie_hellman import DiffieHellman
from gui.theme import COLORS, CIPHER_THEMES, ICONS, SPACING, RADIUS


class CryptoApp(ctk.CTk):
    """Main application window for the Cryptography Suite."""
    
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("🔐 CryptoSuite Pro - Advanced Cryptography Toolkit")
        self.geometry("1520x980")
        self.minsize(1350, 900)
        
        # Set appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        
        # Configure colors
        self.configure(fg_color=COLORS['bg_dark'])
        
        # Animation state
        self._pulse_running = False
        
        # Initialize cipher instances
        self._init_ciphers()
        
        # Build UI
        self._create_layout()
        self._create_sidebar()
        self._create_main_content()
        
        # Show default tab with animation
        self.after(100, self._show_home_animated)
        
        # Start ambient animations
        self._start_ambient_animations()
    
    def _init_ciphers(self):
        """Initialize all cipher instances."""
        self.caesar = CaesarCipher()
        self.vigenere = VigenereCipher()
        self.playfair = PlayfairCipher()
        self.hill = HillCipher()
        self.monoalphabetic = MonoalphabeticCipher()
        self.aes = AESCipher()
        self.des = DESCipher()
        self.dh = DiffieHellman()
        
        # Track active nav button
        self.active_nav_button = None
        self.nav_buttons = {}
        self.nav_indicators = {}
    
    def _start_ambient_animations(self):
        """Start subtle ambient animations for premium feel."""
        self._pulse_running = True
        self._animate_logo_glow()
    
    def _animate_logo_glow(self):
        """Subtle pulsing animation for logo."""
        if not self._pulse_running:
            return
        
        try:
            # Calculate pulse intensity using sine wave
            intensity = (math.sin(time.time() * 2) + 1) / 2
            
            # Blend between two colors for glow effect
            r1, g1, b1 = int(COLORS['bg_secondary'][1:3], 16), int(COLORS['bg_secondary'][3:5], 16), int(COLORS['bg_secondary'][5:7], 16)
            r2, g2, b2 = int(COLORS['accent_primary'][1:3], 16), int(COLORS['accent_primary'][3:5], 16), int(COLORS['accent_primary'][5:7], 16)
            
            r = int(r1 + (r2 - r1) * intensity * 0.15)
            g = int(g1 + (g2 - g1) * intensity * 0.15)
            b = int(b1 + (b2 - b1) * intensity * 0.15)
            
            color = f'#{r:02x}{g:02x}{b:02x}'
            
            if hasattr(self, 'logo_container'):
                self.logo_container.configure(fg_color=color)
        except Exception:
            pass
        
        self.after(50, self._animate_logo_glow)
    
    def _create_layout(self):
        """Create main layout structure."""
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
    
    def _create_sidebar(self):
        """Create the elegant navigation sidebar with glass-like effect."""
        # Sidebar container
        self.sidebar = ctk.CTkFrame(
            self,
            width=300,
            corner_radius=0,
            fg_color=COLORS['bg_primary']
        )
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(16, weight=1)
        self.sidebar.grid_propagate(False)
        
        # Top accent line
        accent_line = ctk.CTkFrame(
            self.sidebar,
            height=3,
            fg_color=COLORS['accent_primary']
        )
        accent_line.grid(row=0, column=0, sticky="ew", padx=0, pady=0)
        
        # ═══════════════════════════════════════════════════════════════
        # LOGO SECTION with animated glow
        # ═══════════════════════════════════════════════════════════════
        self.logo_container = ctk.CTkFrame(
            self.sidebar,
            fg_color=COLORS['bg_secondary'],
            corner_radius=RADIUS['xl']
        )
        self.logo_container.grid(row=1, column=0, padx=16, pady=(20, 12), sticky="ew")
        
        # Logo with animated shimmer effect container
        logo_inner = ctk.CTkFrame(self.logo_container, fg_color="transparent")
        logo_inner.pack(fill="x", padx=20, pady=20)
        
        # Animated logo icon
        self.logo_icon = ctk.CTkLabel(
            logo_inner,
            text="🔐",
            font=ctk.CTkFont(size=48)
        )
        self.logo_icon.pack()
        
        # App name with gradient-like styling
        app_name = ctk.CTkLabel(
            logo_inner,
            text="CryptoSuite",
            font=ctk.CTkFont(family="Segoe UI", size=28, weight="bold"),
            text_color=COLORS['text_primary']
        )
        app_name.pack(pady=(10, 2))
        
        # Pro badge
        pro_badge = ctk.CTkFrame(
            logo_inner,
            fg_color=COLORS['accent_primary'],
            corner_radius=RADIUS['sm']
        )
        pro_badge.pack(pady=(5, 0))
        
        ctk.CTkLabel(
            pro_badge,
            text="  PRO EDITION  ",
            font=ctk.CTkFont(size=10, weight="bold"),
            text_color="white"
        ).pack(padx=8, pady=3)
        
        # ═══════════════════════════════════════════════════════════════
        # NAVIGATION SECTIONS
        # ═══════════════════════════════════════════════════════════════
        
        # Dashboard
        self._create_nav_button(
            "dashboard", "🏠", "Dashboard", 2,
            self._show_home_animated
        )
        
        # Classical Ciphers Section
        self._create_section_header(3, "CLASSICAL CIPHERS", "📜")
        
        self._create_nav_button("caesar", "🔐", "Caesar Cipher", 4, 
                               lambda: self._show_cipher_animated("caesar"))
        self._create_nav_button("vigenere", "🔑", "Vigenère Cipher", 5,
                               lambda: self._show_cipher_animated("vigenere"))
        self._create_nav_button("playfair", "📋", "Playfair Cipher", 6,
                               lambda: self._show_cipher_animated("playfair"))
        self._create_nav_button("hill", "📊", "Hill Cipher", 7,
                               lambda: self._show_cipher_animated("hill"))
        self._create_nav_button("monoalphabetic", "🔤", "Monoalphabetic", 8,
                               lambda: self._show_cipher_animated("monoalphabetic"))
        
        # Modern Encryption Section
        self._create_section_header(9, "MODERN ENCRYPTION", "🛡️")
        
        self._create_nav_button("aes", "🔒", "AES-128", 10,
                               lambda: self._show_cipher_animated("aes"))
        self._create_nav_button("des", "⚠️", "DES", 11,
                               lambda: self._show_cipher_animated("des"))
        
        # Key Exchange Section
        self._create_section_header(12, "KEY EXCHANGE", "🤝")
        
        self._create_nav_button("diffie_hellman", "🔗", "Diffie-Hellman", 13,
                               lambda: self._show_cipher_animated("diffie_hellman"))
        
        # ═══════════════════════════════════════════════════════════════
        # FOOTER with version info
        # ═══════════════════════════════════════════════════════════════
        footer = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        footer.grid(row=17, column=0, padx=16, pady=16, sticky="sew")
        
        # Course info badge
        info_frame = ctk.CTkFrame(
            footer,
            fg_color=COLORS['bg_tertiary'],
            corner_radius=RADIUS['md']
        )
        info_frame.pack(fill="x")
        
        ctk.CTkLabel(
            info_frame,
            text="📚  CS-3002",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=COLORS['text_secondary']
        ).pack(pady=(10, 2))
        
        ctk.CTkLabel(
            info_frame,
            text="Information Security",
            font=ctk.CTkFont(size=10),
            text_color=COLORS['text_tertiary']
        ).pack(pady=(0, 10))
    
    def _create_section_header(self, row: int, text: str, icon: str):
        """Create an elegant section header."""
        header_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        header_frame.grid(row=row, column=0, padx=20, pady=(20, 6), sticky="ew")
        
        # Icon and text
        ctk.CTkLabel(
            header_frame,
            text=f"{icon}  {text}",
            font=ctk.CTkFont(size=10, weight="bold"),
            text_color=COLORS['text_tertiary']
        ).pack(anchor="w")
    
    def _create_nav_button(self, key: str, icon: str, text: str, row: int, command):
        """Create a premium navigation button with indicator."""
        btn_container = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        btn_container.grid(row=row, column=0, padx=12, pady=2, sticky="ew")
        
        # Active indicator (left border)
        indicator = ctk.CTkFrame(
            btn_container,
            width=4,
            height=36,
            fg_color="transparent",
            corner_radius=2
        )
        indicator.pack(side="left", padx=(0, 0))
        indicator.pack_propagate(False)
        self.nav_indicators[key] = indicator
        
        # Button
        btn = ctk.CTkButton(
            btn_container,
            text=f"  {icon}   {text}",
            font=ctk.CTkFont(size=13),
            fg_color="transparent",
            hover_color=COLORS['bg_tertiary'],
            text_color=COLORS['text_secondary'],
            anchor="w",
            height=42,
            corner_radius=RADIUS['md'],
            command=lambda k=key, c=command: self._nav_click(k, c)
        )
        btn.pack(fill="x", padx=4, side="left", expand=True)
        
        self.nav_buttons[key] = btn
    
    def _nav_click(self, key: str, command):
        """Handle navigation click with smooth visual feedback."""
        # Reset all buttons and indicators
        for k, btn in self.nav_buttons.items():
            btn.configure(
                fg_color="transparent",
                text_color=COLORS['text_secondary']
            )
            if k in self.nav_indicators:
                self.nav_indicators[k].configure(fg_color="transparent")
        
        # Highlight active button with accent color
        if key in self.nav_buttons:
            theme = CIPHER_THEMES.get(key, {'primary': COLORS['accent_primary']})
            accent = theme.get('primary', COLORS['accent_primary'])
            
            self.nav_buttons[key].configure(
                fg_color=COLORS['bg_tertiary'],
                text_color=accent
            )
            if key in self.nav_indicators:
                self.nav_indicators[key].configure(fg_color=accent)
        
        # Execute command
        command()
    
    def _create_main_content(self):
        """Create the main content area with smooth scrolling."""
        self.main_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color=COLORS['bg_dark']
        )
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        
        self.content_frame = None
    
    def _clear_content(self):
        """Clear the main content area."""
        if self.content_frame:
            self.content_frame.destroy()
        
        self.content_frame = ctk.CTkScrollableFrame(
            self.main_frame,
            fg_color="transparent",
            scrollbar_button_color=COLORS['bg_tertiary'],
            scrollbar_button_hover_color=COLORS['accent_primary']
        )
        self.content_frame.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self.content_frame.grid_columnconfigure(0, weight=1)
    
    def _show_home_animated(self):
        """Display the home/dashboard with animation."""
        self._nav_click("dashboard", lambda: None)
        self._show_home()
    
    def _show_cipher_animated(self, cipher_type: str):
        """Display cipher with animation."""
        self._show_cipher(cipher_type)
    
    def _scroll_to_cards(self):
        """Scroll down to show the feature cards section."""
        # Scroll the content frame down to show cards
        if hasattr(self, 'content_frame') and self.content_frame:
            # Scroll down by moving the canvas
            try:
                self.content_frame._parent_canvas.yview_moveto(0.15)
            except Exception:
                pass
    
    def _show_home(self):
        """Display the stunning home/dashboard view."""
        self._clear_content()
        
        # ═══════════════════════════════════════════════════════════════
        # HERO SECTION with gradient background
        # ═══════════════════════════════════════════════════════════════
        hero = ctk.CTkFrame(
            self.content_frame,
            fg_color=COLORS['bg_secondary'],
            corner_radius=RADIUS['xxl']
        )
        hero.grid(row=0, column=0, sticky="ew", padx=40, pady=(30, 20))
        
        # Accent bar at top
        accent_bar = ctk.CTkFrame(
            hero,
            height=4,
            fg_color=COLORS['accent_primary'],
            corner_radius=2
        )
        accent_bar.pack(fill="x", padx=40, pady=(30, 0))
        
        hero_inner = ctk.CTkFrame(hero, fg_color="transparent")
        hero_inner.pack(fill="x", padx=50, pady=(25, 40))
        
        # Welcome greeting
        greeting_row = ctk.CTkFrame(hero_inner, fg_color="transparent")
        greeting_row.pack(fill="x")
        
        ctk.CTkLabel(
            greeting_row,
            text="✨",
            font=ctk.CTkFont(size=40)
        ).pack(side="left")
        
        text_frame = ctk.CTkFrame(greeting_row, fg_color="transparent")
        text_frame.pack(side="left", padx=(15, 0))
        
        ctk.CTkLabel(
            text_frame,
            text="Welcome to CryptoSuite Pro",
            font=ctk.CTkFont(family="Segoe UI", size=36, weight="bold"),
            text_color=COLORS['text_primary']
        ).pack(anchor="w")
        
        ctk.CTkLabel(
            text_frame,
            text="Professional-grade encryption, decryption, and key exchange toolkit",
            font=ctk.CTkFont(size=15),
            text_color=COLORS['text_secondary']
        ).pack(anchor="w", pady=(6, 0))
        
        # Quick action buttons
        btn_row = ctk.CTkFrame(hero_inner, fg_color="transparent")
        btn_row.pack(anchor="w", pady=(25, 0))
        
        start_btn = ctk.CTkButton(
            btn_row,
            text="🚀  Get Started",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color=COLORS['accent_primary'],
            hover_color="#4493e6",
            height=48,
            corner_radius=RADIUS['lg'],
            command=lambda: self._show_cipher_animated("caesar")
        )
        start_btn.pack(side="left", padx=(0, 15))
        
        explore_btn = ctk.CTkButton(
            btn_row,
            text="🔍  Explore Algorithms",
            font=ctk.CTkFont(size=14),
            fg_color=COLORS['bg_tertiary'],
            hover_color=COLORS['bg_hover'],
            text_color=COLORS['text_primary'],
            height=48,
            corner_radius=RADIUS['lg'],
            command=self._scroll_to_cards
        )
        explore_btn.pack(side="left")
        
        # ═══════════════════════════════════════════════════════════════
        # FEATURE CARDS - Three column layout
        # ═══════════════════════════════════════════════════════════════
        cards_container = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        cards_container.grid(row=1, column=0, sticky="ew", padx=40, pady=10)
        cards_container.grid_columnconfigure((0, 1, 2), weight=1, uniform="card")
        
        # Classical Ciphers Card
        self._create_premium_card(
            cards_container, 0,
            "📜", "Classical Ciphers",
            "Caesar, Vigenère, Playfair, Hill & Monoalphabetic",
            COLORS['accent_green'], "#1a2f23",
            ["Caesar Cipher", "Vigenère", "Playfair", "Hill Matrix", "Monoalphabetic"],
            "5 algorithms"
        )
        
        # Modern Encryption Card
        self._create_premium_card(
            cards_container, 1,
            "🔒", "Modern Encryption",
            "Industry-standard AES-128 and DES algorithms",
            COLORS['accent_primary'], "#1a2535",
            ["AES-128 CBC Mode", "DES 16 Rounds", "File Encryption", "Hex Output"],
            "Military Grade"
        )
        
        # Key Exchange Card
        self._create_premium_card(
            cards_container, 2,
            "🤝", "Key Exchange",
            "Diffie-Hellman secure key establishment",
            COLORS['accent_purple'], "#271a35",
            ["Prime Parameters", "Public Keys", "Private Keys", "Shared Secret"],
            "Secure Channel"
        )
        
        # ═══════════════════════════════════════════════════════════════
        # STATS SECTION with animated numbers
        # ═══════════════════════════════════════════════════════════════
        stats_frame = ctk.CTkFrame(
            self.content_frame,
            fg_color=COLORS['bg_secondary'],
            corner_radius=RADIUS['xl']
        )
        stats_frame.grid(row=2, column=0, sticky="ew", padx=40, pady=20)
        
        stats_inner = ctk.CTkFrame(stats_frame, fg_color="transparent")
        stats_inner.pack(fill="x", padx=50, pady=35)
        stats_inner.grid_columnconfigure((0, 1, 2, 3), weight=1)
        
        self._create_animated_stat(stats_inner, 0, "8", "Total Algorithms", COLORS['accent_green'])
        self._create_animated_stat(stats_inner, 1, "128", "Bit Encryption", COLORS['accent_primary'])
        self._create_animated_stat(stats_inner, 2, "16", "Feistel Rounds", COLORS['accent_purple'])
        self._create_animated_stat(stats_inner, 3, "∞", "Possibilities", COLORS['accent_orange'])
        
        # ═══════════════════════════════════════════════════════════════
        # ABOUT SECTION
        # ═══════════════════════════════════════════════════════════════
        about_frame = ctk.CTkFrame(
            self.content_frame,
            fg_color=COLORS['bg_secondary'],
            corner_radius=RADIUS['xl']
        )
        about_frame.grid(row=3, column=0, sticky="ew", padx=40, pady=(10, 40))
        
        about_inner = ctk.CTkFrame(about_frame, fg_color="transparent")
        about_inner.pack(fill="x", padx=50, pady=35)
        
        ctk.CTkLabel(
            about_inner,
            text="📚  About This Project",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color=COLORS['text_primary']
        ).pack(anchor="w")
        
        about_text = """
This comprehensive cryptography application demonstrates the implementation of various 
cryptographic algorithms with detailed step-by-step calculations and visualizations.

Developed for the CS-3002 Information Security course, it covers:

  ✓  Classical Ciphers - Historical encryption techniques and their mathematical foundations
  ✓  Modern Standards - AES-128 and DES encryption with full round demonstrations
  ✓  Key Exchange - Secure Diffie-Hellman key establishment protocol
  ✓  File Encryption - Practical file encryption using AES (bonus feature)
  ✓  Educational Value - Step-by-step explanations of all cryptographic operations
        """
        
        ctk.CTkLabel(
            about_inner,
            text=about_text.strip(),
            font=ctk.CTkFont(size=13),
            text_color=COLORS['text_secondary'],
            justify="left"
        ).pack(anchor="w", pady=(20, 0))
    
    def _create_premium_card(self, parent, col, icon, title, desc, accent, bg_tint, features, badge):
        """Create a premium feature card with hover effects."""
        card = ctk.CTkFrame(
            parent,
            fg_color=bg_tint,
            corner_radius=RADIUS['xl']
        )
        card.grid(row=0, column=col, padx=10, pady=10, sticky="nsew")
        
        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(fill="both", expand=True, padx=28, pady=28)
        
        # Icon container with glow effect
        icon_container = ctk.CTkFrame(
            inner,
            width=60,
            height=60,
            fg_color=accent,
            corner_radius=RADIUS['lg']
        )
        icon_container.pack(anchor="w")
        icon_container.pack_propagate(False)
        
        ctk.CTkLabel(
            icon_container,
            text=icon,
            font=ctk.CTkFont(size=28)
        ).place(relx=0.5, rely=0.5, anchor="center")
        
        # Title
        ctk.CTkLabel(
            inner,
            text=title,
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=COLORS['text_primary']
        ).pack(anchor="w", pady=(18, 4))
        
        # Description
        ctk.CTkLabel(
            inner,
            text=desc,
            font=ctk.CTkFont(size=12),
            text_color=COLORS['text_secondary'],
            wraplength=230,
            justify="left"
        ).pack(anchor="w")
        
        # Features list
        features_frame = ctk.CTkFrame(inner, fg_color="transparent")
        features_frame.pack(anchor="w", pady=(15, 0))
        
        for feature in features[:3]:
            feat_row = ctk.CTkFrame(features_frame, fg_color="transparent")
            feat_row.pack(anchor="w", pady=2)
            
            ctk.CTkLabel(
                feat_row,
                text="•",
                font=ctk.CTkFont(size=12),
                text_color=accent
            ).pack(side="left")
            
            ctk.CTkLabel(
                feat_row,
                text=f"  {feature}",
                font=ctk.CTkFont(size=11),
                text_color=COLORS['text_tertiary']
            ).pack(side="left")
        
        # Badge
        badge_frame = ctk.CTkFrame(
            inner,
            fg_color=COLORS['bg_tertiary'],
            corner_radius=RADIUS['sm']
        )
        badge_frame.pack(anchor="w", pady=(18, 0))
        
        ctk.CTkLabel(
            badge_frame,
            text=f"  ⚡ {badge}  ",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=accent
        ).pack(padx=10, pady=5)
    
    def _create_animated_stat(self, parent, col, value, label, color):
        """Create an animated statistic display."""
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.grid(row=0, column=col, padx=15)
        
        # Value with accent color
        val_label = ctk.CTkLabel(
            frame,
            text=value,
            font=ctk.CTkFont(size=42, weight="bold"),
            text_color=color
        )
        val_label.pack()
        
        # Label
        ctk.CTkLabel(
            frame,
            text=label,
            font=ctk.CTkFont(size=12),
            text_color=COLORS['text_tertiary']
        ).pack(pady=(4, 0))
    
    def _show_cipher(self, cipher_type: str):
        """Display the cipher interface based on type."""
        self._clear_content()
        
        if cipher_type == "caesar":
            self._build_caesar_ui()
        elif cipher_type == "vigenere":
            self._build_vigenere_ui()
        elif cipher_type == "playfair":
            self._build_playfair_ui()
        elif cipher_type == "hill":
            self._build_hill_ui()
        elif cipher_type == "monoalphabetic":
            self._build_monoalphabetic_ui()
        elif cipher_type == "aes":
            self._build_aes_ui()
        elif cipher_type == "des":
            self._build_des_ui()
        elif cipher_type == "diffie_hellman":
            self._build_dh_ui()
    
    # ═══════════════════════════════════════════════════════════════════════════
    # SHARED UI COMPONENTS
    # ═══════════════════════════════════════════════════════════════════════════
    
    def _create_cipher_header(self, title: str, description: str, cipher_key: str):
        """Create a beautiful cipher page header."""
        theme = CIPHER_THEMES.get(cipher_key, CIPHER_THEMES['caesar'])
        accent = theme.get('primary', COLORS['accent_primary'])
        
        # Header container
        header = ctk.CTkFrame(
            self.content_frame,
            fg_color=COLORS['bg_secondary'],
            corner_radius=RADIUS['xxl']
        )
        header.grid(row=0, column=0, sticky="ew", padx=40, pady=(30, 20))
        
        # Accent line
        accent_line = ctk.CTkFrame(
            header,
            height=4,
            fg_color=accent,
            corner_radius=2
        )
        accent_line.pack(fill="x", padx=40, pady=(30, 0))
        
        header_inner = ctk.CTkFrame(header, fg_color="transparent")
        header_inner.pack(fill="x", padx=45, pady=(25, 35))
        
        # Title row with icon
        title_row = ctk.CTkFrame(header_inner, fg_color="transparent")
        title_row.pack(fill="x")
        
        # Icon badge
        icon_frame = ctk.CTkFrame(
            title_row,
            width=56,
            height=56,
            fg_color=accent,
            corner_radius=RADIUS['lg']
        )
        icon_frame.pack(side="left")
        icon_frame.pack_propagate(False)
        
        ctk.CTkLabel(
            icon_frame,
            text=theme.get('icon', '🔐'),
            font=ctk.CTkFont(size=26)
        ).place(relx=0.5, rely=0.5, anchor="center")
        
        # Text content
        text_frame = ctk.CTkFrame(title_row, fg_color="transparent")
        text_frame.pack(side="left", padx=(18, 0))
        
        ctk.CTkLabel(
            text_frame,
            text=title,
            font=ctk.CTkFont(size=30, weight="bold"),
            text_color=COLORS['text_primary']
        ).pack(anchor="w")
        
        ctk.CTkLabel(
            text_frame,
            text=description,
            font=ctk.CTkFont(size=13),
            text_color=COLORS['text_secondary']
        ).pack(anchor="w", pady=(5, 0))
        
        return accent
    
    def _create_section(self, row: int, title: str = "", icon: str = "") -> ctk.CTkFrame:
        """Create a content section with optional title."""
        section = ctk.CTkFrame(
            self.content_frame,
            fg_color=COLORS['bg_secondary'],
            corner_radius=RADIUS['xl']
        )
        section.grid(row=row, column=0, sticky="ew", padx=40, pady=10)
        
        inner = ctk.CTkFrame(section, fg_color="transparent")
        inner.pack(fill="x", padx=35, pady=30)
        
        if title:
            title_frame = ctk.CTkFrame(inner, fg_color="transparent")
            title_frame.pack(fill="x", pady=(0, 15))
            
            ctk.CTkLabel(
                title_frame,
                text=f"{icon}  {title}" if icon else title,
                font=ctk.CTkFont(size=16, weight="bold"),
                text_color=COLORS['text_primary']
            ).pack(anchor="w")
        
        return inner
    
    def _create_input_field(self, parent, label: str, hint: str = "", height: int = 100) -> ctk.CTkTextbox:
        """Create a labeled input textbox."""
        ctk.CTkLabel(
            parent,
            text=label,
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=COLORS['text_primary']
        ).pack(anchor="w")
        
        if hint:
            ctk.CTkLabel(
                parent,
                text=hint,
                font=ctk.CTkFont(size=11),
                text_color=COLORS['text_tertiary']
            ).pack(anchor="w", pady=(2, 0))
        
        textbox = ctk.CTkTextbox(
            parent,
            height=height,
            font=ctk.CTkFont(family="Cascadia Code", size=13),
            fg_color=COLORS['bg_dark'],
            border_color=COLORS['border'],
            border_width=1,
            corner_radius=RADIUS['lg'],
            text_color=COLORS['text_primary']
        )
        textbox.pack(fill="x", pady=(10, 0))
        
        return textbox
    
    def _create_key_input(self, parent, label: str, hint: str, default: str, width: int = 200) -> ctk.CTkEntry:
        """Create a key input field."""
        row = ctk.CTkFrame(parent, fg_color="transparent")
        row.pack(fill="x", pady=(20, 0))
        
        label_frame = ctk.CTkFrame(row, fg_color="transparent")
        label_frame.pack(side="left")
        
        ctk.CTkLabel(
            label_frame,
            text=label,
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=COLORS['text_primary']
        ).pack(anchor="w")
        
        if hint:
            ctk.CTkLabel(
                label_frame,
                text=hint,
                font=ctk.CTkFont(size=11),
                text_color=COLORS['text_tertiary']
            ).pack(anchor="w")
        
        entry = ctk.CTkEntry(
            row,
            width=width,
            height=42,
            font=ctk.CTkFont(family="Cascadia Code", size=13),
            fg_color=COLORS['bg_dark'],
            border_color=COLORS['border'],
            border_width=1,
            corner_radius=RADIUS['md'],
            text_color=COLORS['text_primary']
        )
        entry.pack(side="right")
        entry.insert(0, default)
        
        return entry
    
    def _create_button(self, parent, text: str, command, style: str = "primary", icon: str = ""):
        """Create a styled button."""
        styles = {
            'primary': (COLORS['accent_green'], '#2ea043', COLORS['bg_dark']),
            'secondary': (COLORS['accent_cyan'], '#1b7c83', COLORS['bg_dark']),
            'purple': (COLORS['accent_purple'], '#8957e5', 'white'),
            'orange': (COLORS['accent_orange'], '#9e6a03', COLORS['bg_dark']),
            'danger': (COLORS['accent_red'], '#da3633', 'white'),
            'ghost': (COLORS['bg_tertiary'], COLORS['bg_hover'], COLORS['text_primary']),
        }
        
        fg, hover, text_color = styles.get(style, styles['primary'])
        
        return ctk.CTkButton(
            parent,
            text=f"{icon}  {text}" if icon else text,
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color=fg,
            hover_color=hover,
            text_color=text_color,
            height=44,
            corner_radius=RADIUS['lg'],
            command=command
        )
    
    # ═══════════════════════════════════════════════════════════════════════════
    # CAESAR CIPHER UI
    # ═══════════════════════════════════════════════════════════════════════════
    
    def _build_caesar_ui(self):
        """Build elegant Caesar cipher interface."""
        self._create_cipher_header(
            "Caesar Cipher",
            "Classical shift cipher — each letter shifted by a fixed number of positions in the alphabet",
            "caesar"
        )
        
        # Input section
        input_section = self._create_section(1, "Input", "📝")
        
        self.caesar_input = self._create_input_field(
            input_section, "Plaintext / Ciphertext",
            "Enter text to encrypt or decrypt, or load from file", 100
        )
        
        # File load buttons for input
        file_btn_frame = ctk.CTkFrame(input_section, fg_color="transparent")
        file_btn_frame.pack(fill="x", pady=(10, 0))
        self._create_button(file_btn_frame, "Load from File", lambda: self._load_text_from_file(self.caesar_input), "orange", "📂").pack(side="left", padx=(0, 10))
        self._create_button(file_btn_frame, "Extract from Image (OCR)", lambda: self._extract_text_from_image(self.caesar_input), "purple", "🖼️").pack(side="left")
        
        self.caesar_shift = self._create_key_input(
            input_section, "Shift Key", "Number of positions (0-25)", "3", 120
        )
        
        # Buttons
        btn_frame = ctk.CTkFrame(input_section, fg_color="transparent")
        btn_frame.pack(fill="x", pady=(25, 0))
        
        self._create_button(btn_frame, "Encrypt", self._caesar_encrypt, "primary", "🔐").pack(side="left", padx=(0, 12))
        self._create_button(btn_frame, "Decrypt", self._caesar_decrypt, "secondary", "🔓").pack(side="left", padx=(0, 12))
        self._create_button(btn_frame, "Clear", lambda: self._clear_fields([self.caesar_input, self.caesar_output, self.caesar_steps]), "ghost", "🗑️").pack(side="left")
        
        # Output section
        output_section = self._create_section(2, "Result", "✨")
        self.caesar_output = self._create_input_field(output_section, "Output", "", 80)
        
        # Save output button
        save_btn_frame = ctk.CTkFrame(output_section, fg_color="transparent")
        save_btn_frame.pack(fill="x", pady=(10, 0))
        self._create_button(save_btn_frame, "Save Result to File", lambda: self._save_text_to_file(self.caesar_output), "orange", "💾").pack(side="left")
        
        # Steps section
        steps_section = self._create_section(3, "Calculation Steps", "📊")
        self.caesar_steps = self._create_input_field(steps_section, "", "Step-by-step demonstration", 200)
        
        # Spacer
        ctk.CTkFrame(self.content_frame, fg_color="transparent", height=30).grid(row=4, column=0)
    
    def _caesar_encrypt(self):
        plaintext = self.caesar_input.get("1.0", "end-1c")
        try:
            shift = int(self.caesar_shift.get())
        except ValueError:
            messagebox.showerror("Error", "Shift must be a number (0-25)")
            return
        ciphertext, steps = self.caesar.encrypt(plaintext, shift)
        self.caesar_output.delete("1.0", "end")
        self.caesar_output.insert("1.0", ciphertext)
        self.caesar_steps.delete("1.0", "end")
        self.caesar_steps.insert("1.0", steps)
    
    def _caesar_decrypt(self):
        ciphertext = self.caesar_input.get("1.0", "end-1c")
        try:
            shift = int(self.caesar_shift.get())
        except ValueError:
            messagebox.showerror("Error", "Shift must be a number (0-25)")
            return
        plaintext, steps = self.caesar.decrypt(ciphertext, shift)
        self.caesar_output.delete("1.0", "end")
        self.caesar_output.insert("1.0", plaintext)
        self.caesar_steps.delete("1.0", "end")
        self.caesar_steps.insert("1.0", steps)
    
    # ═══════════════════════════════════════════════════════════════════════════
    # VIGENÈRE CIPHER UI
    # ═══════════════════════════════════════════════════════════════════════════
    
    def _build_vigenere_ui(self):
        """Build Vigenère cipher interface."""
        self._create_cipher_header(
            "Vigenère Cipher",
            "Polyalphabetic substitution cipher using a keyword for encryption",
            "vigenere"
        )
        
        input_section = self._create_section(1, "Input", "📝")
        self.vigenere_input = self._create_input_field(input_section, "Plaintext / Ciphertext", "Enter text or load from file", 100)
        
        file_btn_frame = ctk.CTkFrame(input_section, fg_color="transparent")
        file_btn_frame.pack(fill="x", pady=(10, 0))
        self._create_button(file_btn_frame, "Load from File", lambda: self._load_text_from_file(self.vigenere_input), "orange", "📂").pack(side="left", padx=(0, 10))
        self._create_button(file_btn_frame, "Extract from Image (OCR)", lambda: self._extract_text_from_image(self.vigenere_input), "purple", "🖼️").pack(side="left")
        
        self.vigenere_key = self._create_key_input(input_section, "Keyword", "Letters only", "SECRET", 200)
        
        btn_frame = ctk.CTkFrame(input_section, fg_color="transparent")
        btn_frame.pack(fill="x", pady=(25, 0))
        self._create_button(btn_frame, "Encrypt", self._vigenere_encrypt, "primary", "🔐").pack(side="left", padx=(0, 12))
        self._create_button(btn_frame, "Decrypt", self._vigenere_decrypt, "secondary", "🔓").pack(side="left", padx=(0, 12))
        self._create_button(btn_frame, "Clear", lambda: self._clear_fields([self.vigenere_input, self.vigenere_output, self.vigenere_steps]), "ghost", "🗑️").pack(side="left")
        
        output_section = self._create_section(2, "Result", "✨")
        self.vigenere_output = self._create_input_field(output_section, "Output", "", 80)
        
        save_btn_frame = ctk.CTkFrame(output_section, fg_color="transparent")
        save_btn_frame.pack(fill="x", pady=(10, 0))
        self._create_button(save_btn_frame, "Save Result to File", lambda: self._save_text_to_file(self.vigenere_output), "orange", "💾").pack(side="left")
        
        steps_section = self._create_section(3, "Calculation Steps", "📊")
        self.vigenere_steps = self._create_input_field(steps_section, "", "", 200)
    
    def _vigenere_encrypt(self):
        plaintext = self.vigenere_input.get("1.0", "end-1c")
        keyword = self.vigenere_key.get()
        if not keyword:
            messagebox.showerror("Error", "Please enter a keyword")
            return
        ciphertext, steps = self.vigenere.encrypt(plaintext, keyword)
        self.vigenere_output.delete("1.0", "end")
        self.vigenere_output.insert("1.0", ciphertext)
        self.vigenere_steps.delete("1.0", "end")
        self.vigenere_steps.insert("1.0", steps)
    
    def _vigenere_decrypt(self):
        ciphertext = self.vigenere_input.get("1.0", "end-1c")
        keyword = self.vigenere_key.get()
        if not keyword:
            messagebox.showerror("Error", "Please enter a keyword")
            return
        plaintext, steps = self.vigenere.decrypt(ciphertext, keyword)
        self.vigenere_output.delete("1.0", "end")
        self.vigenere_output.insert("1.0", plaintext)
        self.vigenere_steps.delete("1.0", "end")
        self.vigenere_steps.insert("1.0", steps)
    
    # ═══════════════════════════════════════════════════════════════════════════
    # PLAYFAIR CIPHER UI
    # ═══════════════════════════════════════════════════════════════════════════
    
    def _build_playfair_ui(self):
        """Build Playfair cipher interface."""
        self._create_cipher_header(
            "Playfair Cipher",
            "Digraph substitution cipher using a 5×5 key matrix",
            "playfair"
        )
        
        input_section = self._create_section(1, "Input", "📝")
        self.playfair_input = self._create_input_field(input_section, "Plaintext / Ciphertext", "Enter text or load from file", 100)
        
        file_btn_frame = ctk.CTkFrame(input_section, fg_color="transparent")
        file_btn_frame.pack(fill="x", pady=(10, 0))
        self._create_button(file_btn_frame, "Load from File", lambda: self._load_text_from_file(self.playfair_input), "orange", "📂").pack(side="left", padx=(0, 10))
        self._create_button(file_btn_frame, "Extract from Image (OCR)", lambda: self._extract_text_from_image(self.playfair_input), "purple", "🖼️").pack(side="left")
        
        self.playfair_key = self._create_key_input(input_section, "Keyword", "For 5×5 matrix generation", "MONARCHY", 200)
        
        btn_frame = ctk.CTkFrame(input_section, fg_color="transparent")
        btn_frame.pack(fill="x", pady=(25, 0))
        self._create_button(btn_frame, "Encrypt", self._playfair_encrypt, "primary", "🔐").pack(side="left", padx=(0, 12))
        self._create_button(btn_frame, "Decrypt", self._playfair_decrypt, "secondary", "🔓").pack(side="left", padx=(0, 12))
        self._create_button(btn_frame, "Clear", lambda: self._clear_fields([self.playfair_input, self.playfair_output, self.playfair_steps]), "ghost", "🗑️").pack(side="left")
        
        output_section = self._create_section(2, "Result", "✨")
        self.playfair_output = self._create_input_field(output_section, "Output", "", 80)
        
        save_btn_frame = ctk.CTkFrame(output_section, fg_color="transparent")
        save_btn_frame.pack(fill="x", pady=(10, 0))
        self._create_button(save_btn_frame, "Save Result to File", lambda: self._save_text_to_file(self.playfair_output), "orange", "💾").pack(side="left")
        
        steps_section = self._create_section(3, "Key Matrix & Steps", "📊")
        self.playfair_steps = self._create_input_field(steps_section, "", "", 250)
    
    def _playfair_encrypt(self):
        plaintext = self.playfair_input.get("1.0", "end-1c")
        keyword = self.playfair_key.get()
        if not keyword:
            messagebox.showerror("Error", "Please enter a keyword")
            return
        ciphertext, steps = self.playfair.encrypt(plaintext, keyword)
        self.playfair_output.delete("1.0", "end")
        self.playfair_output.insert("1.0", ciphertext)
        self.playfair_steps.delete("1.0", "end")
        self.playfair_steps.insert("1.0", steps)
    
    def _playfair_decrypt(self):
        ciphertext = self.playfair_input.get("1.0", "end-1c")
        keyword = self.playfair_key.get()
        if not keyword:
            messagebox.showerror("Error", "Please enter a keyword")
            return
        plaintext, steps = self.playfair.decrypt(ciphertext, keyword)
        self.playfair_output.delete("1.0", "end")
        self.playfair_output.insert("1.0", plaintext)
        self.playfair_steps.delete("1.0", "end")
        self.playfair_steps.insert("1.0", steps)
    
    # ═══════════════════════════════════════════════════════════════════════════
    # HILL CIPHER UI
    # ═══════════════════════════════════════════════════════════════════════════
    
    def _build_hill_ui(self):
        """Build Hill cipher interface."""
        self._create_cipher_header(
            "Hill Cipher (2×2 Matrix)",
            "Polygraphic substitution using matrix multiplication modulo 26",
            "hill"
        )
        
        input_section = self._create_section(1, "Input", "📝")
        self.hill_input = self._create_input_field(input_section, "Plaintext / Ciphertext", "Enter text or load from file", 100)
        
        file_btn_frame = ctk.CTkFrame(input_section, fg_color="transparent")
        file_btn_frame.pack(fill="x", pady=(10, 0))
        self._create_button(file_btn_frame, "Load from File", lambda: self._load_text_from_file(self.hill_input), "orange", "📂").pack(side="left", padx=(0, 10))
        self._create_button(file_btn_frame, "Extract from Image (OCR)", lambda: self._extract_text_from_image(self.hill_input), "purple", "🖼️").pack(side="left")
        
        self.hill_key = self._create_key_input(input_section, "Key (4 letters)", "Example: HILL → [[7,8],[11,11]]", "HILL", 140)
        
        btn_frame = ctk.CTkFrame(input_section, fg_color="transparent")
        btn_frame.pack(fill="x", pady=(25, 0))
        self._create_button(btn_frame, "Encrypt", self._hill_encrypt, "primary", "🔐").pack(side="left", padx=(0, 12))
        self._create_button(btn_frame, "Decrypt", self._hill_decrypt, "secondary", "🔓").pack(side="left", padx=(0, 12))
        self._create_button(btn_frame, "Clear", lambda: self._clear_fields([self.hill_input, self.hill_output, self.hill_steps]), "ghost", "🗑️").pack(side="left")
        
        output_section = self._create_section(2, "Result", "✨")
        self.hill_output = self._create_input_field(output_section, "Output", "", 80)
        
        save_btn_frame = ctk.CTkFrame(output_section, fg_color="transparent")
        save_btn_frame.pack(fill="x", pady=(10, 0))
        self._create_button(save_btn_frame, "Save Result to File", lambda: self._save_text_to_file(self.hill_output), "orange", "💾").pack(side="left")
        
        steps_section = self._create_section(3, "Matrix Operations", "📊")
        self.hill_steps = self._create_input_field(steps_section, "", "", 280)
    
    def _hill_encrypt(self):
        plaintext = self.hill_input.get("1.0", "end-1c")
        key = self.hill_key.get()
        if len(key) != 4:
            messagebox.showerror("Error", "Key must be exactly 4 letters")
            return
        ciphertext, steps = self.hill.encrypt(plaintext, key)
        if ciphertext == "":
            messagebox.showerror("Error", steps)
            return
        self.hill_output.delete("1.0", "end")
        self.hill_output.insert("1.0", ciphertext)
        self.hill_steps.delete("1.0", "end")
        self.hill_steps.insert("1.0", steps)
    
    def _hill_decrypt(self):
        ciphertext = self.hill_input.get("1.0", "end-1c")
        key = self.hill_key.get()
        if len(key) != 4:
            messagebox.showerror("Error", "Key must be exactly 4 letters")
            return
        plaintext, steps = self.hill.decrypt(ciphertext, key)
        if plaintext == "":
            messagebox.showerror("Error", steps)
            return
        self.hill_output.delete("1.0", "end")
        self.hill_output.insert("1.0", plaintext)
        self.hill_steps.delete("1.0", "end")
        self.hill_steps.insert("1.0", steps)
    
    # ═══════════════════════════════════════════════════════════════════════════
    # MONOALPHABETIC CIPHER UI
    # ═══════════════════════════════════════════════════════════════════════════
    
    def _build_monoalphabetic_ui(self):
        """Build Monoalphabetic cipher interface."""
        self._create_cipher_header(
            "Monoalphabetic Cipher",
            "Simple substitution with a custom alphabet mapping",
            "monoalphabetic"
        )
        
        input_section = self._create_section(1, "Input", "📝")
        self.mono_input = self._create_input_field(input_section, "Plaintext / Ciphertext", "Enter text or load from file", 100)
        
        file_btn_frame = ctk.CTkFrame(input_section, fg_color="transparent")
        file_btn_frame.pack(fill="x", pady=(10, 0))
        self._create_button(file_btn_frame, "Load from File", lambda: self._load_text_from_file(self.mono_input), "orange", "📂").pack(side="left", padx=(0, 10))
        self._create_button(file_btn_frame, "Extract from Image (OCR)", lambda: self._extract_text_from_image(self.mono_input), "purple", "🖼️").pack(side="left")
        
        # Key input (full width)
        ctk.CTkLabel(
            input_section,
            text="Substitution Key",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=COLORS['text_primary']
        ).pack(anchor="w", pady=(20, 0))
        
        ctk.CTkLabel(
            input_section,
            text="Keyword or full 26-letter substitution alphabet",
            font=ctk.CTkFont(size=11),
            text_color=COLORS['text_tertiary']
        ).pack(anchor="w", pady=(2, 0))
        
        self.mono_key = ctk.CTkEntry(
            input_section,
            height=42,
            font=ctk.CTkFont(family="Cascadia Code", size=13),
            fg_color=COLORS['bg_dark'],
            border_color=COLORS['border'],
            border_width=1,
            corner_radius=RADIUS['md'],
            text_color=COLORS['text_primary']
        )
        self.mono_key.pack(fill="x", pady=(10, 0))
        self.mono_key.insert(0, "SECURITY")
        
        btn_frame = ctk.CTkFrame(input_section, fg_color="transparent")
        btn_frame.pack(fill="x", pady=(25, 0))
        self._create_button(btn_frame, "Encrypt", self._mono_encrypt, "primary", "🔐").pack(side="left", padx=(0, 12))
        self._create_button(btn_frame, "Decrypt", self._mono_decrypt, "secondary", "🔓").pack(side="left", padx=(0, 12))
        self._create_button(btn_frame, "Random Key", self._mono_random_key, "purple", "⚡").pack(side="left", padx=(0, 12))
        self._create_button(btn_frame, "Clear", lambda: self._clear_fields([self.mono_input, self.mono_output, self.mono_steps]), "ghost", "🗑️").pack(side="left")
        
        output_section = self._create_section(2, "Result", "✨")
        self.mono_output = self._create_input_field(output_section, "Output", "", 80)
        
        save_btn_frame = ctk.CTkFrame(output_section, fg_color="transparent")
        save_btn_frame.pack(fill="x", pady=(10, 0))
        self._create_button(save_btn_frame, "Save Result to File", lambda: self._save_text_to_file(self.mono_output), "orange", "💾").pack(side="left")
        
        steps_section = self._create_section(3, "Substitution Mapping", "📊")
        self.mono_steps = self._create_input_field(steps_section, "", "", 220)
    
    def _mono_encrypt(self):
        plaintext = self.mono_input.get("1.0", "end-1c")
        key = self.mono_key.get()
        if not key:
            messagebox.showerror("Error", "Please enter a keyword")
            return
        ciphertext, steps = self.monoalphabetic.encrypt(plaintext, key)
        self.mono_output.delete("1.0", "end")
        self.mono_output.insert("1.0", ciphertext)
        self.mono_steps.delete("1.0", "end")
        self.mono_steps.insert("1.0", steps)
    
    def _mono_decrypt(self):
        ciphertext = self.mono_input.get("1.0", "end-1c")
        key = self.mono_key.get()
        if not key:
            messagebox.showerror("Error", "Please enter a keyword")
            return
        plaintext, steps = self.monoalphabetic.decrypt(ciphertext, key)
        self.mono_output.delete("1.0", "end")
        self.mono_output.insert("1.0", plaintext)
        self.mono_steps.delete("1.0", "end")
        self.mono_steps.insert("1.0", steps)
    
    def _mono_random_key(self):
        random_key = self.monoalphabetic.generate_random_key()
        self.mono_key.delete(0, "end")
        self.mono_key.insert(0, random_key)
    
    # ═══════════════════════════════════════════════════════════════════════════
    # AES-128 UI
    # ═══════════════════════════════════════════════════════════════════════════
    
    def _build_aes_ui(self):
        """Build AES-128 interface."""
        self._create_cipher_header(
            "AES-128 Encryption",
            "Advanced Encryption Standard — Industry-standard 128-bit symmetric block cipher",
            "aes"
        )
        
        input_section = self._create_section(1, "Input", "📝")
        
        self.aes_input = self._create_input_field(
            input_section, "Plaintext (text) or Ciphertext (hex)",
            "Enter text to encrypt or hex ciphertext to decrypt", 80
        )
        
        # File load button for text input
        file_btn_frame = ctk.CTkFrame(input_section, fg_color="transparent")
        file_btn_frame.pack(fill="x", pady=(10, 0))
        self._create_button(file_btn_frame, "Load Text from File", lambda: self._load_text_from_file(self.aes_input), "orange", "📂").pack(side="left", padx=(0, 10))
        self._create_button(file_btn_frame, "Extract from Image (OCR)", lambda: self._extract_text_from_image(self.aes_input), "purple", "🖼️").pack(side="left")
        
        # Key input row
        key_row = ctk.CTkFrame(input_section, fg_color="transparent")
        key_row.pack(fill="x", pady=(20, 0))
        
        ctk.CTkLabel(
            key_row,
            text="Key (32 hex characters = 128 bits)",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=COLORS['text_primary']
        ).pack(anchor="w")
        
        key_input_row = ctk.CTkFrame(input_section, fg_color="transparent")
        key_input_row.pack(fill="x", pady=(10, 0))
        
        self.aes_key = ctk.CTkEntry(
            key_input_row,
            height=42,
            font=ctk.CTkFont(family="Cascadia Code", size=13),
            fg_color=COLORS['bg_dark'],
            border_color=COLORS['border'],
            border_width=1,
            corner_radius=RADIUS['md'],
            text_color=COLORS['text_primary']
        )
        self.aes_key.pack(side="left", fill="x", expand=True, padx=(0, 12))
        
        self._create_button(key_input_row, "Generate", self._aes_generate_key, "purple", "⚡").pack(side="left")
        
        # Buttons
        btn_frame = ctk.CTkFrame(input_section, fg_color="transparent")
        btn_frame.pack(fill="x", pady=(25, 0))
        
        self._create_button(btn_frame, "Encrypt", self._aes_encrypt, "primary", "🔐").pack(side="left", padx=(0, 12))
        self._create_button(btn_frame, "Decrypt", self._aes_decrypt, "secondary", "🔓").pack(side="left", padx=(0, 12))
        self._create_button(btn_frame, "Encrypt File", self._aes_encrypt_file, "orange", "📁").pack(side="left", padx=(0, 12))
        self._create_button(btn_frame, "Decrypt File", self._aes_decrypt_file, "orange", "📂").pack(side="left", padx=(0, 12))
        self._create_button(btn_frame, "Clear", lambda: self._clear_fields([self.aes_input, self.aes_output, self.aes_steps]), "ghost", "🗑️").pack(side="left")
        
        output_section = self._create_section(2, "Result", "✨")
        self.aes_output = self._create_input_field(output_section, "Ciphertext (Hex)", "", 80)
        
        # Save output button
        save_btn_frame = ctk.CTkFrame(output_section, fg_color="transparent")
        save_btn_frame.pack(fill="x", pady=(10, 0))
        self._create_button(save_btn_frame, "Save Result to File", lambda: self._save_text_to_file(self.aes_output), "orange", "💾").pack(side="left")
        
        steps_section = self._create_section(3, "AES Round Demonstration", "📊")
        self.aes_steps = self._create_input_field(steps_section, "", "", 300)
    
    def _aes_generate_key(self):
        key = self.aes.generate_key()
        self.aes_key.delete(0, "end")
        self.aes_key.insert(0, key)
    
    def _aes_encrypt(self):
        plaintext = self.aes_input.get("1.0", "end-1c")
        key = self.aes_key.get()
        if not key:
            key = self.aes.generate_key()
            self.aes_key.delete(0, "end")
            self.aes_key.insert(0, key)
        ciphertext, steps = self.aes.encrypt(plaintext, key)
        if not ciphertext:
            messagebox.showerror("Error", steps)
            return
        self.aes_output.delete("1.0", "end")
        self.aes_output.insert("1.0", ciphertext)
        self.aes_steps.delete("1.0", "end")
        self.aes_steps.insert("1.0", steps)
    
    def _aes_decrypt(self):
        ciphertext = self.aes_input.get("1.0", "end-1c")
        key = self.aes_key.get()
        if not key:
            messagebox.showerror("Error", "Key is required for decryption")
            return
        plaintext, steps = self.aes.decrypt(ciphertext, key)
        if not plaintext and "Error" in steps:
            messagebox.showerror("Error", steps)
            return
        self.aes_output.delete("1.0", "end")
        self.aes_output.insert("1.0", plaintext)
        self.aes_steps.delete("1.0", "end")
        self.aes_steps.insert("1.0", steps)
    
    def _aes_encrypt_file(self):
        input_file = filedialog.askopenfilename(title="Select file to encrypt")
        if not input_file:
            return
        output_file = filedialog.asksaveasfilename(
            title="Save encrypted file as",
            defaultextension=".enc",
            initialfile=os.path.basename(input_file) + ".enc"
        )
        if not output_file:
            return
        key = self.aes_key.get()
        if not key:
            key = self.aes.generate_key()
            self.aes_key.delete(0, "end")
            self.aes_key.insert(0, key)
        success, message = self.aes.encrypt_file(input_file, output_file, key)
        if success:
            messagebox.showinfo("Success", f"{message}\n\n⚠️ Save your key for decryption!")
        else:
            messagebox.showerror("Error", message)
    
    def _aes_decrypt_file(self):
        input_file = filedialog.askopenfilename(
            title="Select encrypted file",
            filetypes=[("Encrypted files", "*.enc"), ("All files", "*.*")]
        )
        if not input_file:
            return
        output_file = filedialog.asksaveasfilename(
            title="Save decrypted file as",
            initialfile=os.path.basename(input_file).replace(".enc", "")
        )
        if not output_file:
            return
        key = self.aes_key.get()
        if not key:
            messagebox.showerror("Error", "Key is required for decryption")
            return
        success, message = self.aes.decrypt_file(input_file, output_file, key)
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)
    
    # ═══════════════════════════════════════════════════════════════════════════
    # DES UI
    # ═══════════════════════════════════════════════════════════════════════════
    
    def _build_des_ui(self):
        """Build DES interface."""
        self._create_cipher_header(
            "DES Encryption",
            "Data Encryption Standard — Classic 64-bit block cipher with 16 Feistel rounds",
            "des"
        )
        
        # Warning banner
        warning = ctk.CTkFrame(
            self.content_frame,
            fg_color="#3d1f24",
            corner_radius=RADIUS['xl']
        )
        warning.grid(row=1, column=0, sticky="ew", padx=40, pady=(0, 10))
        
        warning_inner = ctk.CTkFrame(warning, fg_color="transparent")
        warning_inner.pack(fill="x", padx=25, pady=18)
        
        ctk.CTkLabel(
            warning_inner,
            text="⚠️  Security Notice",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=COLORS['accent_red']
        ).pack(anchor="w")
        
        ctk.CTkLabel(
            warning_inner,
            text="DES is considered insecure due to its 56-bit key length. Use AES for secure applications.",
            font=ctk.CTkFont(size=12),
            text_color=COLORS['text_secondary']
        ).pack(anchor="w", pady=(4, 0))
        
        input_section = self._create_section(2, "Input", "📝")
        
        self.des_input = self._create_input_field(
            input_section, "Plaintext (text) or Ciphertext (hex)",
            "Enter text to encrypt or hex ciphertext to decrypt", 80
        )
        
        # File load button
        file_btn_frame = ctk.CTkFrame(input_section, fg_color="transparent")
        file_btn_frame.pack(fill="x", pady=(10, 0))
        self._create_button(file_btn_frame, "Load Text from File", lambda: self._load_text_from_file(self.des_input), "orange", "📂").pack(side="left", padx=(0, 10))
        self._create_button(file_btn_frame, "Extract from Image (OCR)", lambda: self._extract_text_from_image(self.des_input), "purple", "🖼️").pack(side="left")
        
        # Key row
        key_row = ctk.CTkFrame(input_section, fg_color="transparent")
        key_row.pack(fill="x", pady=(20, 0))
        
        ctk.CTkLabel(
            key_row,
            text="Key (16 hex characters = 64 bits)",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=COLORS['text_primary']
        ).pack(anchor="w")
        
        key_input_row = ctk.CTkFrame(input_section, fg_color="transparent")
        key_input_row.pack(fill="x", pady=(10, 0))
        
        self.des_key = ctk.CTkEntry(
            key_input_row,
            height=42,
            font=ctk.CTkFont(family="Cascadia Code", size=13),
            fg_color=COLORS['bg_dark'],
            border_color=COLORS['border'],
            border_width=1,
            corner_radius=RADIUS['md'],
            text_color=COLORS['text_primary']
        )
        self.des_key.pack(side="left", fill="x", expand=True, padx=(0, 12))
        
        self._create_button(key_input_row, "Generate", self._des_generate_key, "purple", "⚡").pack(side="left")
        
        # Buttons
        btn_frame = ctk.CTkFrame(input_section, fg_color="transparent")
        btn_frame.pack(fill="x", pady=(25, 0))
        
        self._create_button(btn_frame, "Encrypt", self._des_encrypt, "primary", "🔐").pack(side="left", padx=(0, 12))
        self._create_button(btn_frame, "Decrypt", self._des_decrypt, "secondary", "🔓").pack(side="left", padx=(0, 12))
        self._create_button(btn_frame, "Clear", lambda: self._clear_fields([self.des_input, self.des_output, self.des_steps]), "ghost", "🗑️").pack(side="left")
        
        output_section = self._create_section(3, "Result", "✨")
        self.des_output = self._create_input_field(output_section, "Ciphertext (Hex)", "", 80)
        
        # Save output button
        save_btn_frame = ctk.CTkFrame(output_section, fg_color="transparent")
        save_btn_frame.pack(fill="x", pady=(10, 0))
        self._create_button(save_btn_frame, "Save Result to File", lambda: self._save_text_to_file(self.des_output), "orange", "💾").pack(side="left")
        
        steps_section = self._create_section(4, "DES Round Demonstration", "📊")
        self.des_steps = self._create_input_field(steps_section, "", "", 300)
    
    def _des_generate_key(self):
        key = self.des.generate_key()
        self.des_key.delete(0, "end")
        self.des_key.insert(0, key)
    
    def _des_encrypt(self):
        plaintext = self.des_input.get("1.0", "end-1c")
        key = self.des_key.get()
        if not key:
            key = self.des.generate_key()
            self.des_key.delete(0, "end")
            self.des_key.insert(0, key)
        ciphertext, steps = self.des.encrypt(plaintext, key)
        if not ciphertext:
            messagebox.showerror("Error", steps)
            return
        self.des_output.delete("1.0", "end")
        self.des_output.insert("1.0", ciphertext)
        self.des_steps.delete("1.0", "end")
        self.des_steps.insert("1.0", steps)
    
    def _des_decrypt(self):
        ciphertext = self.des_input.get("1.0", "end-1c")
        key = self.des_key.get()
        if not key:
            messagebox.showerror("Error", "Key is required for decryption")
            return
        plaintext, steps = self.des.decrypt(ciphertext, key)
        if not plaintext and "Error" in steps:
            messagebox.showerror("Error", steps)
            return
        self.des_output.delete("1.0", "end")
        self.des_output.insert("1.0", plaintext)
        self.des_steps.delete("1.0", "end")
        self.des_steps.insert("1.0", steps)
    
    # ═══════════════════════════════════════════════════════════════════════════
    # DIFFIE-HELLMAN UI
    # ═══════════════════════════════════════════════════════════════════════════
    
    def _build_dh_ui(self):
        """Build Diffie-Hellman interface."""
        self._create_cipher_header(
            "Diffie-Hellman Key Exchange",
            "Secure key exchange protocol for establishing shared secrets over insecure channels",
            "diffie_hellman"
        )
        
        # Parameters section
        params_section = self._create_section(1, "Public Parameters", "🌐")
        
        params_row = ctk.CTkFrame(params_section, fg_color="transparent")
        params_row.pack(fill="x")
        params_row.grid_columnconfigure((0, 1), weight=1)
        
        # Prime p
        p_frame = ctk.CTkFrame(params_row, fg_color="transparent")
        p_frame.grid(row=0, column=0, sticky="ew", padx=(0, 20))
        
        ctk.CTkLabel(
            p_frame,
            text="Prime Number (p)",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=COLORS['text_primary']
        ).pack(anchor="w")
        
        self.dh_prime = ctk.CTkEntry(
            p_frame,
            height=42,
            font=ctk.CTkFont(family="Cascadia Code", size=13),
            fg_color=COLORS['bg_dark'],
            border_color=COLORS['border'],
            border_width=1,
            corner_radius=RADIUS['md'],
            text_color=COLORS['text_primary']
        )
        self.dh_prime.pack(fill="x", pady=(10, 0))
        self.dh_prime.insert(0, "23")
        
        # Generator g
        g_frame = ctk.CTkFrame(params_row, fg_color="transparent")
        g_frame.grid(row=0, column=1, sticky="ew")
        
        ctk.CTkLabel(
            g_frame,
            text="Generator (g)",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=COLORS['text_primary']
        ).pack(anchor="w")
        
        self.dh_generator = ctk.CTkEntry(
            g_frame,
            height=42,
            font=ctk.CTkFont(family="Cascadia Code", size=13),
            fg_color=COLORS['bg_dark'],
            border_color=COLORS['border'],
            border_width=1,
            corner_radius=RADIUS['md'],
            text_color=COLORS['text_primary']
        )
        self.dh_generator.pack(fill="x", pady=(10, 0))
        self.dh_generator.insert(0, "5")
        
        # Private keys section
        keys_section = self._create_section(2, "Private Keys (Auto-generated if empty)", "🔐")
        
        keys_row = ctk.CTkFrame(keys_section, fg_color="transparent")
        keys_row.pack(fill="x")
        keys_row.grid_columnconfigure((0, 1), weight=1)
        
        # Alice
        alice_frame = ctk.CTkFrame(keys_row, fg_color="transparent")
        alice_frame.grid(row=0, column=0, sticky="ew", padx=(0, 20))
        
        ctk.CTkLabel(
            alice_frame,
            text="🧑‍💼 Alice's Private Key (a)",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=COLORS['accent_green']
        ).pack(anchor="w")
        
        self.dh_alice_private = ctk.CTkEntry(
            alice_frame,
            height=42,
            font=ctk.CTkFont(family="Cascadia Code", size=13),
            fg_color=COLORS['bg_dark'],
            border_color=COLORS['accent_green'],
            border_width=2,
            corner_radius=RADIUS['md'],
            text_color=COLORS['text_primary']
        )
        self.dh_alice_private.pack(fill="x", pady=(10, 0))
        self.dh_alice_private.insert(0, "6")
        
        # Bob
        bob_frame = ctk.CTkFrame(keys_row, fg_color="transparent")
        bob_frame.grid(row=0, column=1, sticky="ew")
        
        ctk.CTkLabel(
            bob_frame,
            text="👨‍💼 Bob's Private Key (b)",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=COLORS['accent_primary']
        ).pack(anchor="w")
        
        self.dh_bob_private = ctk.CTkEntry(
            bob_frame,
            height=42,
            font=ctk.CTkFont(family="Cascadia Code", size=13),
            fg_color=COLORS['bg_dark'],
            border_color=COLORS['accent_primary'],
            border_width=2,
            corner_radius=RADIUS['md'],
            text_color=COLORS['text_primary']
        )
        self.dh_bob_private.pack(fill="x", pady=(10, 0))
        self.dh_bob_private.insert(0, "15")
        
        # Buttons
        btn_frame = ctk.CTkFrame(keys_section, fg_color="transparent")
        btn_frame.pack(fill="x", pady=(25, 0))
        
        self._create_button(btn_frame, "Perform Key Exchange", self._dh_exchange, "purple", "🤝").pack(side="left", padx=(0, 12))
        self._create_button(btn_frame, "Use Large Prime", self._dh_use_large_prime, "orange", "🔢").pack(side="left", padx=(0, 12))
        self._create_button(btn_frame, "Clear", lambda: self._clear_fields([self.dh_result]), "ghost", "🗑️").pack(side="left")
        
        # Result section
        result_section = self._create_section(3, "Key Exchange Process", "📊")
        self.dh_result = self._create_input_field(result_section, "", "", 380)
    
    def _dh_exchange(self):
        try:
            p = int(self.dh_prime.get())
            g = int(self.dh_generator.get())
        except ValueError:
            messagebox.showerror("Error", "Prime and Generator must be integers")
            return
        
        alice_private = None
        bob_private = None
        
        try:
            if self.dh_alice_private.get():
                alice_private = int(self.dh_alice_private.get())
            if self.dh_bob_private.get():
                bob_private = int(self.dh_bob_private.get())
        except ValueError:
            messagebox.showerror("Error", "Private keys must be integers")
            return
        
        shared_key, steps = self.dh.full_key_exchange(p, g, alice_private, bob_private)
        
        self.dh_result.delete("1.0", "end")
        self.dh_result.insert("1.0", steps)
        
        if shared_key:
            messagebox.showinfo("✅ Success", f"Shared secret key established: {shared_key}")
    
    def _dh_use_large_prime(self):
        self.dh_prime.delete(0, "end")
        self.dh_prime.insert(0, "7919")
        self.dh_generator.delete(0, "end")
        self.dh_generator.insert(0, "7")
        self.dh_alice_private.delete(0, "end")
        self.dh_bob_private.delete(0, "end")
    
    # ═══════════════════════════════════════════════════════════════════════════
    # UTILITY METHODS
    # ═══════════════════════════════════════════════════════════════════════════
    
    def _clear_fields(self, fields: list):
        """Clear multiple text fields."""
        for field in fields:
            try:
                if isinstance(field, ctk.CTkTextbox):
                    field.delete("1.0", "end")
                elif isinstance(field, ctk.CTkEntry):
                    field.delete(0, "end")
            except Exception:
                pass
    
    def _load_text_from_file(self, target_textbox: ctk.CTkTextbox):
        """
        Load text content from any file and insert into the target textbox.
        Supports .txt, .csv, .json, .xml, .html, .md, .py, .js, .java, etc.
        """
        filetypes = [
            ("Text files", "*.txt"),
            ("All text files", "*.txt;*.csv;*.json;*.xml;*.html;*.md;*.py;*.js;*.java;*.c;*.cpp;*.h"),
            ("CSV files", "*.csv"),
            ("JSON files", "*.json"),
            ("XML files", "*.xml"),
            ("HTML files", "*.html;*.htm"),
            ("Markdown files", "*.md"),
            ("Source code", "*.py;*.js;*.java;*.c;*.cpp;*.h;*.cs"),
            ("All files", "*.*")
        ]
        
        file_path = filedialog.askopenfilename(
            title="Select File to Load Text From",
            filetypes=filetypes
        )
        
        if not file_path:
            return
        
        try:
            # Try different encodings
            encodings = ['utf-8', 'utf-16', 'latin-1', 'cp1252', 'ascii']
            content = None
            
            for encoding in encodings:
                try:
                    with open(file_path, 'r', encoding=encoding) as f:
                        content = f.read()
                    break
                except UnicodeDecodeError:
                    continue
            
            if content is None:
                # Try binary read as last resort
                with open(file_path, 'rb') as f:
                    content = f.read().decode('utf-8', errors='replace')
            
            # Clear existing content and insert new
            target_textbox.delete("1.0", "end")
            target_textbox.insert("1.0", content)
            
            # Show success message with file info
            file_name = os.path.basename(file_path)
            char_count = len(content)
            line_count = content.count('\n') + 1
            messagebox.showinfo(
                "File Loaded Successfully",
                f"📁 File: {file_name}\n"
                f"📝 Characters: {char_count:,}\n"
                f"📄 Lines: {line_count:,}\n\n"
                f"Text has been loaded into the input field.\n"
                f"You can now apply encryption/decryption."
            )
            
        except Exception as e:
            messagebox.showerror(
                "Error Loading File",
                f"Could not read the file:\n{str(e)}\n\n"
                f"Make sure the file contains readable text."
            )
    
    def _extract_text_from_image(self, target_textbox: ctk.CTkTextbox):
        """
        Extract text from an image using OCR (Optical Character Recognition).
        Supports PNG, JPG, JPEG, BMP, TIFF, GIF images.
        Requires Tesseract OCR to be installed on the system.
        """
        if not OCR_AVAILABLE:
            messagebox.showerror(
                "OCR Not Available",
                "OCR (Optical Character Recognition) requires additional setup:\n\n"
                "1. Install Tesseract OCR from:\n"
                "   https://github.com/UB-Mannheim/tesseract/wiki\n\n"
                "2. Add Tesseract to your system PATH\n\n"
                "3. Install Python packages:\n"
                "   pip install pytesseract pillow\n\n"
                "After installation, restart the application."
            )
            return
        
        filetypes = [
            ("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff;*.gif"),
            ("PNG files", "*.png"),
            ("JPEG files", "*.jpg;*.jpeg"),
            ("BMP files", "*.bmp"),
            ("TIFF files", "*.tiff;*.tif"),
            ("GIF files", "*.gif"),
            ("All files", "*.*")
        ]
        
        file_path = filedialog.askopenfilename(
            title="Select Image to Extract Text From",
            filetypes=filetypes
        )
        
        if not file_path:
            return
        
        try:
            # Open the image
            image = Image.open(file_path)
            
            # Convert to RGB if necessary (for PNG with transparency)
            if image.mode in ('RGBA', 'P'):
                image = image.convert('RGB')
            
            # Extract text using Tesseract OCR
            try:
                # Try to detect Tesseract if not already set or if current path doesn't exist
                if os.name == 'nt':  # Windows
                    tesseract_cmd = getattr(pytesseract.pytesseract, 'tesseract_cmd', None)
                    if not tesseract_cmd or (tesseract_cmd and not os.path.exists(tesseract_cmd)):
                        common_paths = [
                            r'C:\Program Files\Tesseract-OCR\tesseract.exe',
                            r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe',
                            r'C:\Users\{}\AppData\Local\Tesseract-OCR\tesseract.exe'.format(os.getenv('USERNAME', '')),
                        ]
                        for path in common_paths:
                            if os.path.exists(path):
                                pytesseract.pytesseract.tesseract_cmd = path
                                break
                    
                    # Try PATH as fallback
                    tesseract_cmd = getattr(pytesseract.pytesseract, 'tesseract_cmd', None)
                    if not tesseract_cmd or (tesseract_cmd and not os.path.exists(tesseract_cmd)):
                        import shutil
                        tesseract_path = shutil.which('tesseract')
                        if tesseract_path and os.path.exists(tesseract_path):
                            pytesseract.pytesseract.tesseract_cmd = tesseract_path
                
                extracted_text = pytesseract.image_to_string(image)
            except pytesseract.TesseractNotFoundError:
                messagebox.showerror(
                    "Tesseract Not Found",
                    "Tesseract OCR is not installed or not in PATH.\n\n"
                    "Please install Tesseract OCR:\n"
                    "1. Download from: https://github.com/UB-Mannheim/tesseract/wiki\n"
                    "2. Run the installer\n"
                    "3. Add to PATH (usually C:\\Program Files\\Tesseract-OCR)\n"
                    "4. Restart this application"
                )
                return
            except Exception as ocr_error:
                error_msg = str(ocr_error).lower()
                if "tesseract" in error_msg and ("not found" in error_msg or "not installed" in error_msg):
                    messagebox.showerror(
                        "Tesseract Not Found",
                        "Tesseract OCR is not installed or not in PATH.\n\n"
                        "Please install Tesseract OCR:\n"
                        "1. Download from: https://github.com/UB-Mannheim/tesseract/wiki\n"
                        "2. Run the installer\n"
                        "3. Add to PATH (usually C:\\Program Files\\Tesseract-OCR)\n"
                        "4. Restart this application"
                    )
                    return
                else:
                    messagebox.showerror(
                        "OCR Error",
                        f"An error occurred during OCR:\n{str(ocr_error)}"
                    )
                    return
            
            # Clean up the extracted text
            extracted_text = extracted_text.strip()
            
            if not extracted_text:
                messagebox.showwarning(
                    "No Text Found",
                    "No text could be extracted from the image.\n\n"
                    "Tips for better results:\n"
                    "• Use clear, high-resolution images\n"
                    "• Ensure text is not rotated or skewed\n"
                    "• Use images with good contrast\n"
                    "• Avoid handwritten text (printed works better)"
                )
                return
            
            # Clear existing content and insert extracted text
            target_textbox.delete("1.0", "end")
            target_textbox.insert("1.0", extracted_text)
            
            # Show success message
            file_name = os.path.basename(file_path)
            char_count = len(extracted_text)
            word_count = len(extracted_text.split())
            messagebox.showinfo(
                "Text Extracted Successfully! 🎉",
                f"📷 Image: {file_name}\n"
                f"📝 Characters: {char_count:,}\n"
                f"📖 Words: {word_count:,}\n\n"
                f"Text has been extracted and loaded.\n"
                f"You can now apply encryption/decryption!"
            )
            
        except Exception as e:
            messagebox.showerror(
                "Error Extracting Text",
                f"Could not extract text from image:\n{str(e)}\n\n"
                f"Make sure the image is valid and contains readable text."
            )
    
    def _save_text_to_file(self, source_textbox: ctk.CTkTextbox):
        """
        Save text content from a textbox to a file.
        """
        content = source_textbox.get("1.0", "end-1c")
        
        if not content.strip():
            messagebox.showwarning("No Content", "There is no text to save.")
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Save Text to File",
            defaultextension=".txt",
            filetypes=[
                ("Text files", "*.txt"),
                ("All files", "*.*")
            ]
        )
        
        if not file_path:
            return
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            file_name = os.path.basename(file_path)
            messagebox.showinfo(
                "File Saved Successfully",
                f"✅ Text saved to:\n{file_name}"
            )
        except Exception as e:
            messagebox.showerror("Error Saving File", f"Could not save file:\n{str(e)}")
    
    def destroy(self):
        """Clean up before closing."""
        self._pulse_running = False
        super().destroy()


def main():
    """Main entry point for the application."""
    app = CryptoApp()
    app.mainloop()


if __name__ == "__main__":
    main()
