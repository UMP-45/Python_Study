from itertools import chain

def difference(l_1,l_2):
    n = len(list(set(l_1).union(set(l_2))))
    m = len(list(set(l_1).intersection(set(l_2))))
    return 1 - n/(n+m)

machine_1 = [1,6]
machine_2 = [2,3,7,8,9,12,13,15]
machine_3 = [3,5,10,14]
machine_4 = [2,7,8,11,12,13]
machine_5 = [3,5,10,11,14]
machine_6 = [1,4,5,9,10]
machine_7 = [2,5,7,8,9,10]
machine_8 = [3,4,15]
machine_9 = [4,10]
machine_10 = [3,8,10,14,15]

#machine = {"machine_1":machine_1,"machine_2":machine_2,"machine_4":machine_4,"machine_6":machine_6,"machine_7":machine_7,"machine_8":machine_8,"machine_9":machine_9}
#machine = {"machine_1":machine_1,"machine_2":machine_2,"machine_4":machine_4,"machine_6":machine_6,"machine_7":machine_7,"machine_8":machine_8,"machine_9":machine_9}
#machine = {"machine_2":machine_2,"machine_4":machine_4,"machine_7":machine_7,"machine_6":machine_6,"machine_8":machine_8,"machine_9":machine_9,"machine_1":machine_1}
machine = {"machine_3":machine_3,"machine_5":machine_5,"machine_10":machine_10,"machine_6":machine_6,"machine_7":machine_7,"machine_4":machine_4,"machine_2":machine_2}
A = {}
B = {}
C = {}

A["machine_3"] = machine_1
B["machine_5"] = machine_9
C["machine_10"] = machine_8

for key,value in machine.items():
    a = list(chain(*A.values()))
    b = list(chain(*B.values()))
    c = list(chain(*C.values()))

    A_copy = a.copy()
    A_copy.extend(list(machine[key]))
    different_1 = difference(A_copy,b) + difference(A_copy,c) + difference(b,c)
    
    B_copy = b.copy()
    B_copy.extend(list(machine[key]))
    different_2 = difference(a,B_copy) + difference(a,c) + difference(B_copy,c)
    
    C_copy = c.copy()
    C_copy.extend(list(machine[key]))
    different_3 = difference(a,b) + difference(a,C_copy) + difference(b,C_copy)

    if different_1 == min(different_1,different_2,different_3): 
        A[key] = value
    elif different_2 == min(different_1,different_2,different_3): 
        B[key] = value
    elif different_3 == min(different_1,different_2,different_3):
        C[key] = value

# for key,value in machine.items():
    # a = list(chain(*A.values()))
    # b = list(chain(*B.values()))
    # c = list(chain(*C.values()))

    # temp = list(machine[key])

    # different_1 = difference(a,temp)
    # different_2 = difference(b,temp)
    # different_3 = difference(c,temp)

    # if different_1 == max(different_1,different_2,different_3): 
        # A[key] = value
    # elif different_2 == max(different_1,different_2,different_3): 
        # B[key] = value
    # elif different_3 == max(different_1,different_2,different_3):
        # C[key] = value

a = set(list(chain(*A.values())))
b = set(list(chain(*B.values())))
c = set(list(chain(*C.values())))

print(A.keys())
print(B.keys())
print(C.keys())
print(a)
print(b)
print(c)

different = difference(a,b) + difference(a,c) + difference(b,c)
print("A,B:",difference(a,b))
print("A,C:",difference(a,c))
print("B,C:",difference(b,c))
print(different)