from task import add

# Call the task asynchronously
result = add.delay(4, 6)

# Wait for the result and print it
print(f"Task result: {result.get(timeout=10)}")