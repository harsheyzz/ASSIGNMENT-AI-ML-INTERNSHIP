string = "Hello, world!"

prefix = "Hello"
suffix = "world!"

starts_with_prefix = string[:len(prefix)] == prefix

ends_with_suffix = string[-len(suffix):] == suffix

if starts_with_prefix or ends_with_suffix:
    print(f"The string '{string}' starts with '{prefix}' or ends with '{suffix}'.")
else:
    print(f"The string '{string}' does not start with '{prefix}' or end with '{suffix}'.")