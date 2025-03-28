import asyncio
from .src import server

def main():
    """Main entry point for the package."""
    server.main()

__all__ = ["main", "server"]
