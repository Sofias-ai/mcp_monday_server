# Import only what's needed to make the package usable
# Don't define functions that already exist in server.py

# Export the main entry point
from .server import main

__all__ = ["main"]