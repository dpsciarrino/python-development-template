# src/main.py

"""Provides a Python project template suitable for Desktop GUI projects.
"""

from gui.windows import HelloWindow
from app import Application

def main():
    """Runs the main application.
    """
    # Build the application
    app = Application()
    
    # Instantiate the main GUI Window
    HelloWindow(app)




if __name__ == '__main__':
    main()

