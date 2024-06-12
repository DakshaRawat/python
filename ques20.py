input_numbers = input("Enter a list of numbers separated by spaces: ") 

numbers_list = input_numbers.split() 

numbers_list = [int(num) for num in numbers_list] 

sum_of_numbers = sum(numbers_list) 

print("The sum of the numbers is:", sum_of_numbers) 