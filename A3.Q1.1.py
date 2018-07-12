#Test function that finds the sum of two numbers
def sum(a,b):
    c = a+b
    return c

#Input sequence
lst = [1,2,3,4,5,6,7,8,9,10]

#myreduce  function
def myreduce(func,seq):
    a = func(seq[0],seq[1])
    for i in range(1,len(seq)-1):
        b = func(a,seq[i+1])
        a = b


    return a

res = myreduce(sum,lst)
print(res)
