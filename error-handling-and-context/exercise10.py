def manage_tags(existing_tags: dict, *simple_tags, **key_value_tags) -> dict:
    """
    Applies simple and key-value tags to an existing dictionary of tags.

    Args:
        existing_tags: The initial dictionary of tags.
        *simple_tags: Positional string arguments to be added as tags with a
                      value of 'true'. Duplicates are ignored.
        **key_value_tags: Keyword arguments to be added or used to overwrite
                          existing tags.

    Returns:
        A new dictionary with all tags merged.

    Raises:
        TypeError: If existing_tags is not a dictionary.
    """
    # --- Input Validation ---
    # We use isinstance() to check if the variable matches the dict type.
    if not isinstance(existing_tags, dict):
        raise TypeError(f"existing_tags must be a dictionary, but got {type(existing_tags).__name__}")

    # --- Core logic from previous part ---
    # Create a shallow copy to avoid mutating the original input
    new_tags = existing_tags.copy()

    # Process positional tags (simple_tags)
    for tag in set(simple_tags):
        new_tags[tag] = 'true'

    # Process keyword tags using the dictionary union operator (|)
    new_tags = new_tags | key_value_tags

    return new_tags