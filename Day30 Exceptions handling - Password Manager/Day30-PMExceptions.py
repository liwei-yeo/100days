
try:
    file = open("a_file.txt")
except FileNotFoundError as error_message:
    print("There was an error")
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"{error_message}: That key does not exist")
else:
    content = file.read()
    print(content)
finally:
    print("run this no matter what")
    file.close()
    raise KeyError("This is an error that I made up")

