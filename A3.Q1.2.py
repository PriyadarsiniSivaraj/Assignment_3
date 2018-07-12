#Test function that returns True for Even number
def even(num):
    if num % 2 == 0:
            return True
    else:
            return False
#Input Sequence
lst = [2,13,16,88,90,67,73,65,18]

#myfilter function
def myfilter(func,seq):
    result = []
    for i in seq:
        if func(i) == True :
            result.append(i)

    return result

print(myfilter(even,lst))
