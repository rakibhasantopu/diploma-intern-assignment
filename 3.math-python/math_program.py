def sum(first,second):
    print(f"The value of {first}+{second}= {first+second}")

sum(10,15)


def subtraction(first,second):
    return(first-second)
result = subtraction(10,5)
print(f"substraction result is {result}")


def multiplication(first,second,third,forth):
    multiply=(first*second*third*forth)
    print(f"Multiplication of {first} * {second} * {third} * {forth} = {multiply}")
    return(multiply)

multiplication(5,5,2,2)


def division(first,second):
    devide=(first/second)
    print(f'devision Result is {devide}')
    modulus=(first%second)
    if modulus!=0:
        print(f"modulus result is {modulus}" )
    else :
        return
    


division(30,4)