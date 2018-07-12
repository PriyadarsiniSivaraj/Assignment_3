#List Comprehensions
lst_1 = []
for i in 'ACADGILD':
    lst_1.append(i)
print(lst_1)

p = ['x','y','z']
lst_2 = [ P*i for P in p for i in range(1,5)]
print(lst_2)

p = ['x','y','z']
lst_3 = [ P*i for i in range(1,4) for P in p]
print(lst_3)

l = [[2,3,4],[3,4,5],[4,5,6]]
lst_4 = [[l[i][j]] for i in range(3) for j in range(3)]
print(lst_4)

m = [[2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7]]
n = [5, 6, 7, 8]
for i in range(4):
    m[i].append(n[i])
print(m)

a = [1,2,3]
b = [1,2,3]
lst_6 = [(B,A) for A in a for B in b]
print(lst_6)

