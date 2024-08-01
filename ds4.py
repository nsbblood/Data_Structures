dataList=[0,3,5,11,14,16,22,25,28,30]

inputNumber=input("Write a number so we can check it!")
for i, row in enumerate(dataList):
    for j,dataList in enumerate(row):
        if inputNumber in dataList:
            print(f"{inputNumber} is in datalist and it's row {row} index {j}")
        else :
            print(f"Sorry {inputNumber} is not our list")

# Go to ds4.2 for the fixed nested version