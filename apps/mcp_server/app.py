from fastmcp import FastMCP
from services.mcp_server.db_functions import (
    add_stat_to_db,
    get_user_id_by_username,
    get_users_from_db,
)

mcp = FastMCP("StatsLoader")


@mcp.tool(
    name="add_stat_to_db",
    description="Add a game stat to the database. using the user_id (not the user_name) of the user",
)
def add_stat_to_db_tool(stat_name: str, value: str, user_id: str) -> str:
    return add_stat_to_db(stat_name, value, user_id)


@mcp.tool(
    name="get_user_id_by_username",
    description="Retrieve user id from the database, by providing the username.",
)
def get_user_id_by_username_tool(user_name: str) -> int:
    return get_user_id_by_username(user_name)


@mcp.tool(
    name="get_users_from_db",
    description="Retrieve all users from the database.",
)
def get_users_from_db_tool() -> str:
    return get_users_from_db()


if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8000)
