from fastmcp import FastMCP

mcp = FastMCP("StatsLoader")


def add_stat_to_db(name: str, value: str, user_name) -> str:
    # Simulate adding a stat to a database
    print(f"Adding stat to DB: {name} = {value}", flush=True)
    return f"Stat {name} with value {value} added to database."


def get_user_from_db(user_name: str) -> str:
    # Simulate retrieving a user from a database
    print(f"Retrieving user from DB: {user_name}", flush=True)
    return f"User {user_name} found in database."


def get_users_from_db() -> str:
    # Simulate retrieving all users from a database
    print("Retrieving all users from DB", flush=True)
    return "User1, User2, User3"


@mcp.tool(
    name="add_stat_to_db",
    description="Add a game stat to the database.",
)
def add_stat_to_db_tool(name: str, value: str, user_name: str) -> str:
    return add_stat_to_db(name, value, user_name)


@mcp.tool(
    name="get_user_from_db",
    description="Retrieve a user from the database.",
)
def get_user_from_db_tool(user_name: str) -> str:
    return get_user_from_db(user_name)


@mcp.tool(
    name="get_users_from_db",
    description="Retrieve all users from the database.",
)
def get_users_from_db_tool() -> str:
    return get_users_from_db()


if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="localhost", port=6275)
