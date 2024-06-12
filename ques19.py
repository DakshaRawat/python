import string 
input_string = input("Enter a string: ") 

translator = str.maketrans('', '', string.punctuation) 

cleaned_string = input_string.translate(translator) 

print("String without punctuation:", cleaned_string) 