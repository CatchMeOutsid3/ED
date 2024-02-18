import re

ef = input("Enter File Location: ")

# Open the file for reading
with open(ef, 'r') as file:
    # Read the contents of the file into a variable
    file_contents = file.read()

# Use regex to match email addresses in the file contents
email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
emails = email_regex.findall(file_contents)

# Use regex to match URLs in the file contents
url_regex = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
urls = url_regex.findall(file_contents)

# Print the results
print("Email addresses found:")
for email in emails:
    print("- " + email)

print("\nURLs found:")
for url in urls:
    print("- " + url)
