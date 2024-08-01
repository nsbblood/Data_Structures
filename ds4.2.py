dataList = [0, 3, 5, 11, 14, 16, 22, 25, 28, 30]

inputNumber = input("Write a number so we can check it! ")

#Convert input to integer
try:
    inputNumber = int(inputNumber)
except ValueError:
    print(f"Invalid input. Please enter a number.")
    exit() 

for i, row in enumerate(dataList):
    for j, value in enumerate(dataList):  # Corrected iteration variable
        if inputNumber == value:
            print(f"{inputNumber} is in dataList at row {i}, index {j}")
            exit()  # when I use break, I got 9-10 same outputs
    else:
        # else block only executes if the inner loop didn't break
        print(f"Sorry, {inputNumber} is not in our list.")
        exit()

#Bad code example...