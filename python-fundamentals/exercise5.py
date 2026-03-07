def manage_tags(existing_tags: dict, *simple_tags, **key_value_tags) -> dict:
    """
    Applies simple and key-value tags to an existing dictionary of tags.
    """
    # 1. Create a shallow copy to ensure immutability of the original dict
    new_tags = existing_tags.copy()

    # 2. Process the 'simple_tags' (*args)
    # Each positional argument becomes a key with the value 'true'
    for tag in simple_tags:
        new_tags[tag] = 'true'

    # 3. Process the 'key_value_tags' (**kwargs)
    # Using .update() or dictionary unpacking ensures these overwrite 
    # both the initial tags and the simple tags.
    new_tags.update(key_value_tags)

    # 4. Return the new, merged dictionary
    return new_tags