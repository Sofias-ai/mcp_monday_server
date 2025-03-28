import sys
import os
from pathlib import Path
from .common import logger, mcp

def main():
    logger.info("Starting Monday MCP server...")
    
    try:
        # Import tools and resources
        import src.tools as tools
        import src.resources as resources
        
        logger.info("Running MCP server...")
        mcp.run(transport="stdio")
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
        sys.exit(1)

if __name__ == '__main__':
    main()