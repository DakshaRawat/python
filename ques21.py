input_list = input("Enter a list of elements separated by spaces: ").split() 

element_to_count = input("Enter the element to count: ") 
count = input_list.count(element_to_count) 

print(f"The element '{element_to_count}' occurs {count} times in the list.") 