#1170503101  罗猛

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

#machine = {"机器1":machine_1,"机器2":machine_2,"机器4":machine_4,"机器6":machine_6,"机器7":machine_7,"机器8":machine_8,"机器9":machine_9}
#machine = {"机器2":machine_2,"机器4":machine_4,"机器7":machine_7,"机器6":machine_6,"机器8":machine_8,"机器9":machine_9,"机器1":machine_1}
machine = {"机器1":machine_1,"机器9":machine_9,"机器8":machine_8,"机器6":machine_6,"机器7":machine_7,"机器4":machine_4,"机器2":machine_2}
A = {}
B = {}
C = {}

A["机器3"] = machine_3
B["机器5"] = machine_5
C["机器10"] = machine_10


for key,value in machine.items():
    a = list(chain(*A.values()))
    b = list(chain(*B.values()))
    c = list(chain(*C.values()))

    temp = list(machine[key])

    different_1 = difference(a,temp)
    different_2 = difference(b,temp)
    different_3 = difference(c,temp)

    if different_1 == max(different_1,different_2,different_3): 
        A[key] = value
    elif different_2 == max(different_1,different_2,different_3): 
        B[key] = value
    elif different_3 == max(different_1,different_2,different_3):
        C[key] = value

a = set(list(chain(*A.values())))
b = set(list(chain(*B.values())))
c = set(list(chain(*C.values())))

print("分组A：",A.keys())
print("分组B：",B.keys())
print("分组C：",C.keys())
print("分组A所能生产零件的种类：",a)
print("分组B所能生产零件的种类：",b)
print("分组C所能生产零件的种类：",c)

different = difference(a,b) + difference(a,c) + difference(b,c)
print("A,B直接的差异：",difference(a,b))
print("A,C直接的差异：",difference(a,c))
print("B,C直接的差异：",difference(b,c))
print("A,B,C各组之间差异和：",different)