# File Read & Write Challenge + Error Handling Lab

def main():
    # Ask user for the filename
    filename = input("Enter the filename to read: ")

    try:
        # Try opening and reading the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"✅ Modified content has been written to '{new_filename}'")

    except FileNotFoundError:
        # Handles the case when file is not found
        print("❌ Error: The file does not exist. Please check the name and try again.")
    except IOError:
        # Handles other I/O errors
        print("❌ Error: The file cannot be read or written.")

# Run the program
if __name__ == "__main__":
    main()
