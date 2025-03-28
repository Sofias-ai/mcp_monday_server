import sys
import os
from pathlib import Path
from common import logger, mcp

def main():
    logger.info("Starting Monday MCP server...")
    
    try:

        if __file__.endswith('src/server.py') or __file__.endswith('src\\server.py'):
            project_root = str(Path(__file__).parent.parent)
            if project_root not in sys.path:
                sys.path.insert(0, project_root)
                
        from src import tools, resources
        
        logger.info("Running MCP server...")
        mcp.run(transport="stdio")
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
        sys.exit(1)

if __name__ == '__main__':
    main()