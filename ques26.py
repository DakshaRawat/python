string = input("Enter a string: ")
prefix = input("Enter a prefix to check: ")
suffix = input("Enter a suffix to check: ")

if string.startswith(prefix):
    print("The string starts with the prefix ")
else:
    print("The string does not start with the prefix")

if string.endswith(suffix):
    print("The string ends with the suffix")
else: 
    print("The string does not end with the suffix ")