def formula_func(length_of_parallel_side_1,length_of_parallel_side_2,distance_between_them):
    
    formula= .5 * (length_of_parallel_side_1+length_of_parallel_side_2) * distance_between_them
    return formula

while True:
    try:
        input_for_l1=float(input("Input the length of 1st parallel side:"))
        input_for_l2=float(input("Input the length of 2nd parallel side:"))
        input_for_dis=float(input("Input the length of distance between them:"))

        break

        

    
    except ValueError:
        print("Invalid Input")
result= formula_func(input_for_l1,input_for_l2,input_for_dis)
print("the area of the trapezium is: ",result)
    
