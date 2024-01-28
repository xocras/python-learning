# Absolute File Paths:

# /Project_Folder/File_Inside_Project_Folder.txt

with open("C:/Users/oscar/OneDrive/Documents/Hello.txt", mode="w") as file:
    file.write("Hello World!")

# Relative File Paths:

# ./File_Inside_Project_Folder.txt

# ../Another_Folder/Another_File.txt

with open("../../../../../Hello.txt") as file:
    print(file.read())
