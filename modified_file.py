# Question 1: File Read & Write Challenge

# Read from input_file.txt
with open("input_file.txt", "r") as file:
    original_text = file.read()

# Print before modification
print("BEFORE MODIFICATION:")
print(original_text)

# Modify text (convert to uppercase)
modified_text = original_text.upper()

# Write to output_file.txt
with open("output_file.txt", "w") as file:
    file.write(modified_text)

# Read the new file
with open("output_file.txt", "r") as file:
    after_text = file.read()

# Print after modification
print("\n AFTER MODIFICATION:")
print(after_text)


# Question 2: Error Handling Lab 

filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as file:
        content = file.read()
    print("\n File Content:\n")
    print(content)

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
finally:
    print("\n Program finished running.")
