import random

def add_stat_to_db(stat_name: str, value: str, user_id) -> str:
    # Simulate adding a stat to a database
    print(f"Adding stat to DB: {stat_name} = {value}", flush=True)
    return f"Stat {stat_name} with value {value} added to database."


def get_user_id_by_username(user_name: str) -> int:
    # Simulate retrieving a user from a database
    print(f"Retrieving user_id from DB: {user_name}", flush=True)
    return random.randint(1, 1000)


def get_users_from_db() -> str:
    # Simulate retrieving all users from a database
    print("Retrieving all users from DB", flush=True)
    return "User1, User2, User3"
