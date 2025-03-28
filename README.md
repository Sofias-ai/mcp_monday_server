# MCP Monday Server

An MCP server for Claude Desktop that provides tools to interact with Monday.com boards and items.

## Installation

This package can be installed and executed using UVX or other Python package managers:

```bash
# Install using UVX
uvx install mcp_monday_server

# Or install using pip
pip install .
```

## Claude Desktop Configuration

Add this MCP server to your Claude Desktop configuration:

```json
"mcpServers": {
  "monday": {
    "command": "uvx",
    "args": [
      "mcp_monday_server"
    ],
    "env": {
      "MONDAY_API_KEY": "your-monday-api-key",
      "MONDAY_BOARD_ID": "your-monday-board-id" 
    }
  }
}
```

## Available Tools

- **Get_Board_Schema**: Get schema information from your Monday.com board
- **Get_Item_Details**: Get details of a specific item by ID
- **Get_Items_by_Column_Value**: Find items with specific values in a column
- **Create_Item**: Create a new item in your Monday board
- **Update_Item**: Update an existing item's values
- **Delete_Item**: Remove an item from the board

## Development

After cloning the repository:

```bash
# Install in development mode
pip install -e .

# Run the server manually
mcp_monday_server
```

## Environment Variables

Create a `.env` file in the root directory with:

```
MONDAY_API_KEY=your-monday-api-key
MONDAY_BOARD_ID=your-monday-board-id
```

Or provide these variables in your Claude Desktop configuration.
