def load_schema(file):
    """
    Reads a schema file (.sql or .txt) and returns its content as a string.
    """
    content = file.read().decode("utf-8")
    return content
