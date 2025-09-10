def add_stat_to_db(stat_name: str, value: str, user_id) -> str:
    # Simulate adding a stat to a database
    print(f"Adding stat to DB: {stat_name} = {value}", flush=True)
    return f"Stat {stat_name} with value {value} added to database."


def get_user_from_db(user_name: str) -> str:
    # Simulate retrieving a user from a database
    print(f"Retrieving user from DB: {user_name}", flush=True)
    return f"User {user_name} found in database. with ID 12345"


def get_users_from_db() -> str:
    # Simulate retrieving all users from a database
    print("Retrieving all users from DB", flush=True)
    return "User1, User2, User3"
