def multiplicationTable(N):
    result = []
    for i in range(1, 11):
        result.append(str(i * N))
    return " ".join(result)

# Ensure the function is only called once
if __name__ == "__main__":
    # Print the result of the function call
    print(multiplicationTable(5))
