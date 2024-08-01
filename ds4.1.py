dataList = [0, 3, 5, 11, 14, 16, 22, 25, 28, 30]

inputNumber = input("Write a number so we can check it! ")

# Convert input to integer 
try:
    inputNumber = int(inputNumber)
except ValueError:
    print(f"Invalid input. Please enter a number.")
    exit()  # Exit if input isn't a number

found = False
for i, row in enumerate(dataList):
    if inputNumber == row:
        print(f"{inputNumber} is in dataList at {i+1}")
        found = True  # Set a flag to indicate the number was found
        break  # Exit if the number is found

if not found:
    print(f"Sorry, {inputNumber} is not in our list.")
