
while True:
    try:



        enter_number=int(input("Enter your number:"))
        enter_text=input("Enter the text you want to print")

        break

    except ValueError:
        print("Invalid input")



for x in range(1,enter_number+1):
    print(enter_text)
