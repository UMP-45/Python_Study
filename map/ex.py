from itertools import combinations

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

machine_dic = ["machine_1","machine_2","machine_3","machine_4","machine_5","machine_6","machine_7","machine_8","machine_9","machine_10"]
machine_list = [machine_1,machine_2,machine_3,machine_4,machine_5,machine_6,machine_7,machine_8,machine_9,machine_10]

if __name__ == '__main__':
    machine = dict(zip(machine_dic,machine_list))
    machine_arrangement = list(combinations(machine, 3)) #机器的组合
    for i in range(len(machine_arrangement)):
        for j in range(len(machine_arrangement)):
            if i == j:
                continue
            else:
                print(machine_arrangement[i],machine_arrangement[j]) 