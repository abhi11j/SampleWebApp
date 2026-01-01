class RepositoryError(Exception):
    """Base exception for repository errors."""
    pass

class ValidationError(RepositoryError):
    pass

class OperationError(RepositoryError):
    pass

def validate_input(data):
    try:
        if not isinstance(data, dict):
            raise ValidationError("Input data must be a dictionary.")
        # Additional validation logic...
    except ValidationError as e:
        print(f"Validation error: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error during validation: {e}")
        raise OperationError from e


def perform_operation():
    try:
        # Example operation
        validate_input({})
    except RepositoryError as e:
        print(f"Repository error: {e}")
        # Handle or propagate
    except Exception as e:
        print(f"Unknown error: {e}")
        raise
