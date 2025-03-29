import mcp.server.stdio, sys, asyncio
from mcp.server import NotificationOptions, Server
from mcp.server.models import InitializationOptions
from .common import monday_client, server, logger
from .tools import register_tools

async def main():
    logger.info("Starting Monday MCP server")

    # Register tools with the server
    register_tools(server, monday_client)

    try:
        async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
            await server.run(
                read_stream,
                write_stream,
                InitializationOptions(
                    server_name="monday",
                    server_version="1.0.0",
                    capabilities=server.get_capabilities(
                        notification_options=NotificationOptions(),
                        experimental_capabilities={},
                    ),
                ),
            )
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())