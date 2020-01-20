"""Supply the packages to the rest of the app."""


def get_latest_packages():
    """Return some packages."""
    return [
        {'name': 'flask', 'version': '1.1.1'},
        {'name': 'sqalchemy', 'version': '2.2.0'},
        {'name': 'passlib', 'version': '3.0.0'},
    ]
