"""
Premium Theme Configuration for Cryptography Application
==========================================================
A sophisticated, modern dark theme with elegant gradients,
smooth animations, and professional aesthetics.

Design Philosophy:
- Clean, minimal interface with purposeful whitespace
- Subtle gradients and depth through shadows
- Consistent visual hierarchy
- Smooth micro-interactions
- Professional color palette inspired by premium software
"""

# ═══════════════════════════════════════════════════════════════════════════════
# PREMIUM COLOR PALETTE - Inspired by high-end software and dark mode best practices
# ═══════════════════════════════════════════════════════════════════════════════

COLORS = {
    # ─────────────────────────────────────────────────────────────────────────
    # BASE COLORS - Deep, rich backgrounds with subtle blue undertones
    # ─────────────────────────────────────────────────────────────────────────
    'bg_dark': '#0d1117',           # GitHub-style deep dark
    'bg_primary': '#161b22',        # Primary surface
    'bg_secondary': '#21262d',      # Elevated surface
    'bg_tertiary': '#30363d',       # Cards and containers
    'bg_card': '#1c2128',           # Card background
    'bg_input': '#0d1117',          # Input fields
    'bg_hover': '#292e36',          # Hover states
    
    # ─────────────────────────────────────────────────────────────────────────
    # ACCENT COLORS - Vibrant yet sophisticated
    # ─────────────────────────────────────────────────────────────────────────
    'accent_primary': '#58a6ff',    # Primary blue (links, primary actions)
    'accent_green': '#3fb950',      # Success, encrypt
    'accent_purple': '#a371f7',     # Special actions, Diffie-Hellman
    'accent_orange': '#d29922',     # Warnings, file operations
    'accent_red': '#f85149',        # Errors, DES warning
    'accent_cyan': '#39c5cf',       # Secondary actions, decrypt
    'accent_pink': '#db61a2',       # Highlights
    'accent_yellow': '#e3b341',     # Gold accents
    
    # ─────────────────────────────────────────────────────────────────────────
    # GRADIENT COLORS - For beautiful gradient effects
    # ─────────────────────────────────────────────────────────────────────────
    'gradient_start': '#58a6ff',
    'gradient_mid': '#a371f7',
    'gradient_end': '#db61a2',
    
    # ─────────────────────────────────────────────────────────────────────────
    # TEXT COLORS - Carefully balanced for readability
    # ─────────────────────────────────────────────────────────────────────────
    'text_primary': '#f0f6fc',      # Primary text (high contrast)
    'text_secondary': '#8b949e',    # Secondary text
    'text_tertiary': '#6e7681',     # Muted text
    'text_link': '#58a6ff',         # Links
    'text_success': '#3fb950',      # Success messages
    'text_error': '#f85149',        # Error messages
    
    # ─────────────────────────────────────────────────────────────────────────
    # BORDER COLORS - Subtle separation
    # ─────────────────────────────────────────────────────────────────────────
    'border': '#30363d',            # Default border
    'border_light': '#21262d',      # Subtle border
    'border_focus': '#58a6ff',      # Focus state
    'border_success': '#3fb950',    # Success border
    
    # ─────────────────────────────────────────────────────────────────────────
    # SPECIAL EFFECT COLORS
    # ─────────────────────────────────────────────────────────────────────────
    'glow_blue': '#58a6ff',
    'glow_green': '#3fb950',
    'glow_purple': '#a371f7',
    'shadow': '#010409',
}

# ═══════════════════════════════════════════════════════════════════════════════
# CIPHER-SPECIFIC COLOR THEMES
# ═══════════════════════════════════════════════════════════════════════════════

CIPHER_THEMES = {
    'caesar': {
        'primary': '#3fb950',
        'secondary': '#238636',
        'icon': '🔐'
    },
    'vigenere': {
        'primary': '#58a6ff',
        'secondary': '#1f6feb',
        'icon': '🔑'
    },
    'playfair': {
        'primary': '#a371f7',
        'secondary': '#8957e5',
        'icon': '📋'
    },
    'hill': {
        'primary': '#39c5cf',
        'secondary': '#1b7c83',
        'icon': '📊'
    },
    'monoalphabetic': {
        'primary': '#db61a2',
        'secondary': '#bf4b8a',
        'icon': '🔤'
    },
    'aes': {
        'primary': '#58a6ff',
        'secondary': '#1f6feb',
        'icon': '🛡️'
    },
    'des': {
        'primary': '#d29922',
        'secondary': '#9e6a03',
        'icon': '🔒'
    },
    'diffie_hellman': {
        'primary': '#a371f7',
        'secondary': '#8957e5',
        'icon': '🤝'
    }
}

# ═══════════════════════════════════════════════════════════════════════════════
# TYPOGRAPHY - Modern, readable fonts
# ═══════════════════════════════════════════════════════════════════════════════

FONTS = {
    'heading_xl': ('Segoe UI', 32, 'bold'),
    'heading_lg': ('Segoe UI', 24, 'bold'),
    'heading_md': ('Segoe UI', 18, 'bold'),
    'heading_sm': ('Segoe UI', 14, 'bold'),
    'body': ('Segoe UI', 13),
    'body_bold': ('Segoe UI', 13, 'bold'),
    'code': ('Cascadia Code', 12),
    'code_sm': ('Cascadia Code', 11),
    'small': ('Segoe UI', 11),
    'tiny': ('Segoe UI', 10),
    'button': ('Segoe UI', 13, 'bold'),
    'nav': ('Segoe UI', 13),
}

# Fallback fonts for systems without Cascadia Code
FONTS_FALLBACK = {
    'code': ('Consolas', 12),
    'code_sm': ('Consolas', 11),
}

# ═══════════════════════════════════════════════════════════════════════════════
# SPACING SYSTEM - Consistent spacing throughout the app
# ═══════════════════════════════════════════════════════════════════════════════

SPACING = {
    'xs': 4,
    'sm': 8,
    'md': 16,
    'lg': 24,
    'xl': 32,
    'xxl': 48,
    'section': 40,
}

# ═══════════════════════════════════════════════════════════════════════════════
# BORDER RADIUS - Rounded corners for modern look
# ═══════════════════════════════════════════════════════════════════════════════

RADIUS = {
    'xs': 4,
    'sm': 6,
    'md': 8,
    'lg': 12,
    'xl': 16,
    'xxl': 24,
    'full': 9999,
}

# ═══════════════════════════════════════════════════════════════════════════════
# ANIMATION TIMINGS
# ═══════════════════════════════════════════════════════════════════════════════

ANIMATION = {
    'instant': 50,
    'fast': 150,
    'normal': 250,
    'slow': 400,
    'slower': 600,
}

# ═══════════════════════════════════════════════════════════════════════════════
# ICONS - Unicode symbols for consistent iconography
# ═══════════════════════════════════════════════════════════════════════════════

ICONS = {
    # Navigation
    'home': '🏠',
    'dashboard': '📊',
    
    # Ciphers
    'caesar': '🔐',
    'vigenere': '🔑',
    'playfair': '📋',
    'hill': '📈',
    'monoalphabetic': '🔤',
    'aes': '🛡️',
    'des': '🔒',
    'diffie_hellman': '🤝',
    
    # Actions
    'encrypt': '🔐',
    'decrypt': '🔓',
    'generate': '⚡',
    'clear': '🗑️',
    'copy': '📋',
    'file': '📁',
    'file_open': '📂',
    'swap': '🔄',
    'refresh': '🔄',
    
    # Status
    'success': '✅',
    'error': '❌',
    'warning': '⚠️',
    'info': 'ℹ️',
    
    # Misc
    'key': '🔑',
    'lock': '🔒',
    'unlock': '🔓',
    'shield': '🛡️',
    'star': '⭐',
    'sparkle': '✨',
    'lightning': '⚡',
    'rocket': '🚀',
}

# ═══════════════════════════════════════════════════════════════════════════════
# COMPONENT STYLES
# ═══════════════════════════════════════════════════════════════════════════════

BUTTON_STYLES = {
    'primary': {
        'fg_color': COLORS['accent_primary'],
        'hover_color': '#4493e6',
        'text_color': '#ffffff',
    },
    'success': {
        'fg_color': COLORS['accent_green'],
        'hover_color': '#2ea043',
        'text_color': '#ffffff',
    },
    'danger': {
        'fg_color': COLORS['accent_red'],
        'hover_color': '#da3633',
        'text_color': '#ffffff',
    },
    'secondary': {
        'fg_color': COLORS['bg_tertiary'],
        'hover_color': COLORS['bg_hover'],
        'text_color': COLORS['text_primary'],
    },
    'ghost': {
        'fg_color': 'transparent',
        'hover_color': COLORS['bg_tertiary'],
        'text_color': COLORS['text_secondary'],
    },
}

# ═══════════════════════════════════════════════════════════════════════════════
# ASCII ART LOGOS
# ═══════════════════════════════════════════════════════════════════════════════

LOGO_ASCII = """
╔═══════════════════════════════════════════════════════════════╗
║   ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗            ║
║  ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗           ║
║  ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║           ║
║  ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║           ║
║  ╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝           ║
║   ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝            ║
║                                                                 ║
║         INFORMATION SECURITY - CS-3002                          ║
║         CRYPTOGRAPHY DESKTOP APPLICATION                        ║
╚═══════════════════════════════════════════════════════════════╝
"""

LOGO_COMPACT = "⟨ CRYPTO SUITE ⟩"
LOGO_MINIMAL = "🔐"
