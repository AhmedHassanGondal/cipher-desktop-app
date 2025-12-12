"""
Advanced Animation System for CryptoSuite
==========================================
Provides smooth animations, transitions, and visual effects
for a premium user experience.
"""

import time
import threading
from typing import Callable, Any, Optional


class EasingFunctions:
    """Collection of easing functions for smooth animations."""
    
    @staticmethod
    def linear(t: float) -> float:
        """Linear easing - no acceleration."""
        return t
    
    @staticmethod
    def ease_in_quad(t: float) -> float:
        """Quadratic ease-in - accelerating from zero velocity."""
        return t * t
    
    @staticmethod
    def ease_out_quad(t: float) -> float:
        """Quadratic ease-out - decelerating to zero velocity."""
        return t * (2 - t)
    
    @staticmethod
    def ease_in_out_quad(t: float) -> float:
        """Quadratic ease-in-out - acceleration until halfway, then deceleration."""
        if t < 0.5:
            return 2 * t * t
        return -1 + (4 - 2 * t) * t
    
    @staticmethod
    def ease_in_cubic(t: float) -> float:
        """Cubic ease-in."""
        return t * t * t
    
    @staticmethod
    def ease_out_cubic(t: float) -> float:
        """Cubic ease-out."""
        return 1 + (t - 1) ** 3
    
    @staticmethod
    def ease_in_out_cubic(t: float) -> float:
        """Cubic ease-in-out."""
        if t < 0.5:
            return 4 * t * t * t
        return 1 + (t - 1) * (2 * t - 2) ** 2
    
    @staticmethod
    def ease_out_elastic(t: float) -> float:
        """Elastic ease-out - overshoots then settles."""
        if t == 0:
            return 0
        if t == 1:
            return 1
        
        p = 0.3
        s = p / 4
        return pow(2, -10 * t) * pow(2, 10 * (t - 1) / 10) * 1.5 + 1
    
    @staticmethod
    def ease_out_bounce(t: float) -> float:
        """Bounce ease-out."""
        if t < 1 / 2.75:
            return 7.5625 * t * t
        elif t < 2 / 2.75:
            t -= 1.5 / 2.75
            return 7.5625 * t * t + 0.75
        elif t < 2.5 / 2.75:
            t -= 2.25 / 2.75
            return 7.5625 * t * t + 0.9375
        else:
            t -= 2.625 / 2.75
            return 7.5625 * t * t + 0.984375


class Animator:
    """Handles smooth animations for Tkinter widgets."""
    
    def __init__(self, root):
        self.root = root
        self._animations = {}
        self._animation_id = 0
    
    def animate_value(
        self,
        start: float,
        end: float,
        duration: int,
        callback: Callable[[float], None],
        easing: Callable[[float], float] = EasingFunctions.ease_out_cubic,
        on_complete: Optional[Callable[[], None]] = None
    ) -> int:
        """
        Animate a value from start to end over duration milliseconds.
        
        Args:
            start: Starting value
            end: Ending value
            duration: Animation duration in milliseconds
            callback: Function called with current value on each frame
            easing: Easing function to use
            on_complete: Function called when animation completes
            
        Returns:
            Animation ID that can be used to cancel the animation
        """
        self._animation_id += 1
        animation_id = self._animation_id
        
        start_time = time.time()
        duration_sec = duration / 1000.0
        
        def update():
            if animation_id not in self._animations:
                return
                
            elapsed = time.time() - start_time
            progress = min(1.0, elapsed / duration_sec)
            
            eased_progress = easing(progress)
            current_value = start + (end - start) * eased_progress
            
            try:
                callback(current_value)
            except Exception:
                # Widget might have been destroyed
                self._animations.pop(animation_id, None)
                return
            
            if progress < 1.0:
                self.root.after(16, update)  # ~60fps
            else:
                self._animations.pop(animation_id, None)
                if on_complete:
                    on_complete()
        
        self._animations[animation_id] = True
        self.root.after(0, update)
        return animation_id
    
    def cancel(self, animation_id: int):
        """Cancel an animation by ID."""
        self._animations.pop(animation_id, None)
    
    def cancel_all(self):
        """Cancel all running animations."""
        self._animations.clear()
    
    def fade_in(self, widget, duration: int = 300, on_complete: Optional[Callable] = None):
        """Fade in a widget by animating its alpha/color."""
        # Note: CTk doesn't support true alpha, so we simulate with color
        pass
    
    def slide_in(
        self,
        widget,
        direction: str = "left",
        distance: int = 50,
        duration: int = 300,
        easing: Callable = EasingFunctions.ease_out_cubic
    ):
        """Slide a widget in from a direction."""
        if direction == "left":
            start_x = -distance
            end_x = 0
        elif direction == "right":
            start_x = distance
            end_x = 0
        else:
            return
        
        original_x = widget.winfo_x()
        
        def update(value):
            widget.place(x=original_x + value)
        
        self.animate_value(start_x, end_x, duration, update, easing)


class PulseEffect:
    """Creates a pulsing glow effect for widgets."""
    
    def __init__(self, root, widget, base_color: str, glow_color: str):
        self.root = root
        self.widget = widget
        self.base_color = base_color
        self.glow_color = glow_color
        self._running = False
        self._intensity = 0.0
    
    def start(self, frequency: float = 1.0):
        """Start the pulse effect."""
        self._running = True
        self._pulse(frequency)
    
    def stop(self):
        """Stop the pulse effect."""
        self._running = False
    
    def _pulse(self, frequency: float):
        if not self._running:
            return
        
        import math
        self._intensity = (math.sin(time.time() * frequency * 2 * math.pi) + 1) / 2
        
        # Blend colors based on intensity
        try:
            self.widget.configure(fg_color=self.base_color)
        except Exception:
            self._running = False
            return
        
        self.root.after(50, lambda: self._pulse(frequency))


class TypewriterEffect:
    """Creates a typewriter text effect."""
    
    def __init__(self, root, textbox, text: str, speed: int = 50):
        self.root = root
        self.textbox = textbox
        self.text = text
        self.speed = speed
        self._index = 0
        self._running = False
    
    def start(self, on_complete: Optional[Callable] = None):
        """Start the typewriter effect."""
        self._index = 0
        self._running = True
        self.textbox.delete("1.0", "end")
        self._type_next(on_complete)
    
    def stop(self):
        """Stop the effect."""
        self._running = False
    
    def _type_next(self, on_complete):
        if not self._running or self._index >= len(self.text):
            if on_complete:
                on_complete()
            return
        
        try:
            self.textbox.insert("end", self.text[self._index])
            self._index += 1
            self.root.after(self.speed, lambda: self._type_next(on_complete))
        except Exception:
            self._running = False


class CountUpEffect:
    """Animates a number counting up."""
    
    def __init__(self, root, label, start: int, end: int, duration: int = 1000):
        self.root = root
        self.label = label
        self.start = start
        self.end = end
        self.duration = duration
        self.animator = Animator(root)
    
    def start(self, format_string: str = "{:.0f}"):
        """Start the count-up animation."""
        def update(value):
            self.label.configure(text=format_string.format(value))
        
        self.animator.animate_value(
            self.start,
            self.end,
            self.duration,
            update,
            EasingFunctions.ease_out_cubic
        )


# Color utilities for gradients and effects
def hex_to_rgb(hex_color: str) -> tuple:
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb: tuple) -> str:
    """Convert RGB tuple to hex color."""
    return '#{:02x}{:02x}{:02x}'.format(*rgb)


def blend_colors(color1: str, color2: str, ratio: float) -> str:
    """Blend two colors together."""
    rgb1 = hex_to_rgb(color1)
    rgb2 = hex_to_rgb(color2)
    
    blended = tuple(int(rgb1[i] + (rgb2[i] - rgb1[i]) * ratio) for i in range(3))
    return rgb_to_hex(blended)


def generate_gradient_colors(start_color: str, end_color: str, steps: int) -> list:
    """Generate a list of colors forming a gradient."""
    colors = []
    for i in range(steps):
        ratio = i / (steps - 1) if steps > 1 else 0
        colors.append(blend_colors(start_color, end_color, ratio))
    return colors

