point=(8,2)

x=point[0]
y=point[1]


def calculate_square_properties(side_lenght):
    area=side_lenght*side_lenght
    perimeter=4*side_lenght
    return(area,perimeter)

result=calculate_square_properties(5)
print("Area: ",result[0])
print("Perimeter: ",result[1])