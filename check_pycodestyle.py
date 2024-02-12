#!/usr/bin/bash
# A beautiful code that passes pycodestyle

# Define a class
class e_Class:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def e_thod(self):
        # Perform some action
        result = self.a + self.b
    return result


# Main function
def main():
    instance = e_Class(a=1, b=2)
    result = instance.e_thod()


print(f"Result: {result}")

# Call the main function if the script is executed
if __name__ == "__main__":
    main()
