string1 = input("Enter the first string: ") 
string2 = input("Enter the second string: ") 
string1 = string1.replace(" ", "").lower() 

string2 = string2.replace(" ", "").lower() 

if sorted(string1) == sorted(string2): 

    print("The strings are anagrams of each other.") 

else: 

    print("The strings are not anagrams.") 