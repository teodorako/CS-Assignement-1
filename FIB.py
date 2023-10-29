#FIB- Rabbits and Recurrence Relations by Teodora Kovacevic

def fib(n, k):
    number1 = 1
    number2 = 1
    for i in range(2, n):
        temporary_number = number1
        number1 = number2
        number2 = temporary_number *k + number2
    return number2
    
fib(35,4)