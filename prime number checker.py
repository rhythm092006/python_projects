print("WELCOME TO THE PRIME CHECKER")
while True:
    try:
        input_number=int(input("Enter your number :"))
        break
    except ValueError:
        print("Invalid Input")

if input_number ==0:
    print("0 is not a prime number")

elif input_number ==1:
    print("1 is not a prime number")

elif input_number <0:
    print("Negative numbers are not considered as primes")


else:
    count=0
    divisor=1
    while divisor<=input_number:
        if input_number%divisor==0:
            count +=1
        if count>=3:
            break
        else:
           divisor +=1

        

    if count ==2:
        print("the number is a prime")
    else:
        print("the number is not a prime")


    



            




