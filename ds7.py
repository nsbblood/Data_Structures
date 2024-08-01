def find_second_smallest(numbers):
  # Convert the input string to a list of integers
  try:
    numbers = [int(num) for num in numbers.split()]
  except ValueError:
    print("Please enter only integers separated by spaces.")
    return

  #Check 4 numbers
  if len(numbers) < 4:
    print("List must contain at least four numbers.")
    return

  #Sort the list
  sorted_numbers = sorted(numbers)

  #Return the second smallest number
  return sorted_numbers[1]

#Get input
user_input = input("Write 5 numbers separated by spaces: ")

# all the function
result = find_second_smallest(user_input)

#Print the result if it's not None
if result is not None:
  print("The second smallest number is:", result)

