# app/utils.py


def fetch_data_from_api():
    """Simulate a function that fetches data from an external API."""
    return {"data": "real data"}


def write_to_file(file_path, content):
    """Write content to a file at the given path."""
    with open(file_path, "w") as f:
        f.write(content)


def read_from_file(file_path):
    """Read content from a file at the given path."""
    with open(file_path, "r") as f:
        return f.read()
