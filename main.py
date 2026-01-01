import sys

class RepositoryError(Exception):
    """Base exception for repository errors."""
    pass

class FileNotFoundError(RepositoryError):
    pass

class InvalidInputError(RepositoryError):
    pass

def process_repository():
    try:
        # Example operation that may fail
        with open('config.yaml') as f:
            config = f.read()
        # Further processing...
    except FileNotFoundError as e:
        print(f"Error: Configuration file not found. {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(2)

def main():
    try:
        process_repository()
    except RepositoryError as e:
        print(f"Repository error: {e}", file=sys.stderr)
        sys.exit(3)
    except Exception as e:
        print(f"Fatal error: {e}", file=sys.stderr)
        sys.exit(99)

if __name__ == "__main__":
    main()
