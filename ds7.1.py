def find_second_smallest(numbers):
  # Convert the input string to a list of integers
  try:
    numbers = [int(num) for num in numbers.split()]
    
  except ValueError:
    print("Please enter only integers separated by spaces.")
    return

  if len(numbers) < 4:
    print("List must contain at least four numbers.")
    return


  #Sort the list
  sorted_numbers = sorted(numbers)

  #Return the {user_input2} smallest number
  return sorted_numbers[user_input2-1]

#Get input
user_input = input("Write 5 numbers separated by spaces: ")
user_input2=input("sorted from smallest to the biggest, You want to get smallest value(Between 1-5): ")

user_input2=int(user_input2)
if user_input2>5:
    print("You should give us lower value")

# all the function
result = find_second_smallest(user_input)

#Print the result if it's not None
if result is not None:
  print(f"The {user_input2} smallest number is:", result)

