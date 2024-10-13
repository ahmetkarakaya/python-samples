class ManagedResource:
    def __enter__(self):
        print("Resource acquired")
        return self  # Can return an object to be used within the block

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource released")
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        # Return False to propagate the exception, True to suppress it
        return False

# Usage
with ManagedResource() as resource:
    print("Using the resource")
    # Uncomment the next line to see exception handling
    # raise ValueError("Something went wrong")

