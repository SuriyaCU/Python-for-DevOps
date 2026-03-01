def greet_users(names):
    """Greets a list of users by name.

    Args:
        names (list(str)): The list of users to greet.
    """

    for name in names:
        print(f"Hello, {name}!")

greet_users(["Alice", "Bob", "Charlie"])