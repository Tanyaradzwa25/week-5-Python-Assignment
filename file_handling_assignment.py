
# file_handling_assignment.py

def create_file():
    """Create a new text file and write initial content."""
    try:
        # Open file in write mode
        with open('my_file.txt', 'w') as file:
            # Write at least three lines of text, including a mix of strings and numbers
            file.write("This is the first line with some text.\n")
            file.write("Here's the second line, which includes a number: 12345.\n")
            file.write("Finally, the third line with a different number: 67890.\n")
        print("File 'my_file.txt' created and initial content written.")
    except (PermissionError, IOError) as e:
        print(f"Error creating or writing to file: {e}")

def read_file():
    """Read and display the content of the file."""
    try:
        # Open file in read mode
        with open('my_file.txt', 'r') as file:
            # Read the entire content of the file
            content = file.read()
            # Display the content on the console
            print("\nContents of 'my_file.txt':")
            print(content)
    except FileNotFoundError:
        print("File not found.")
    except (PermissionError, IOError) as e:
        print(f"Error reading the file: {e}")
    finally:
        print("Finished attempting to read the file.")

def append_to_file():
    """Append additional lines of text to the file."""
    try:
        with open('my_file.txt', 'a') as file:
            file.write("Appending the fourth line with some more text.\n")
            file.write("Here is the fifth line, adding even more text.\n")
            file.write("This is the sixth line appended to the file.\n")
        print("Additional lines appended to 'my_file.txt'.")
    except (PermissionError, IOError) as e:
        print(f"Error appending to the file: {e}")
    finally:
        print("Finished attempting to read the file.")
      

def main():
    """Main function to execute the tasks."""
    create_file()
    read_file()
    append_to_file()
    read_file()


# Run the main function
if __name__ == "__main__":
    main()

