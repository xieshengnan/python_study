import copy

baby = [1, 2, 3, [4, 5]]
baby1 = baby
baby1[3][0] = 100
print("baby1:", baby1)
print("baby:", baby)
print("--------------------------")
baby2 = baby.copy()
baby2[1] = 9999
baby2[3][0] = 8888
print("baby2:", baby2)
print("baby", baby)
print("-------------------------")
baby3 = copy.deepcopy(baby)
baby3[1] = "deep"
baby3[3][0] = "deep"
print("baby3:", baby3)
print("baby:", baby)


