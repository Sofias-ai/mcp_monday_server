import sys
import os
from pathlib import Path
from common import logger, mcp

def main():
    logger.info("Starting Monday MCP server...")
    
    try:
        # Add the project root to the path if needed
        if __name__ == "__main__":
            project_root = str(Path(__file__).parent.parent)
            if project_root not in sys.path:
                sys.path.insert(0, project_root)
                
        # Import tools and resources
        import tools
        import resources
        
        logger.info("Running MCP server...")
        mcp.run(transport="stdio")
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
        sys.exit(1)

if __name__ == '__main__':
    main()