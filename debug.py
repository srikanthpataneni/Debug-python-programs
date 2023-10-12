def reverse_string(s):
    # Reversing a string using slicing
    return s[::-1]

def main():
    input_string = "Hello, world!"
    reversed_string = reverse_string(input_string)
    print(f"Reversed string: {reversed_string}")

if __name__ == "__main__":
    main()
