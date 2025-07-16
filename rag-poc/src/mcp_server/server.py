\"\"\"MCP server for MSSQL operations (ADK Python)\"\"\"
from adk import MCPServer, Tool

# TODO: import pyodbc and define execute_sql_tool, get_schema_tool, fetch_data_tool

def main():
    server = MCPServer()
    # server.register_tool(Tool(...))
    server.serve()

if __name__ == '__main__':
    main()
