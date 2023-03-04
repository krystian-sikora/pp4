file = input("Enter name of the file: ")

with open(file, 'a') as file:
    append_text = input("Enter text to be appended to text file: ")
    file.write('\n' + append_text)