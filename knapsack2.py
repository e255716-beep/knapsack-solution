import pulp
import time

start = time.perf_counter()

problem = pulp.LpProblem("knapsack", pulp.LpMaximize)

x_1 = pulp.LpVariable("1", lowBound=0, upBound=1, cat=pulp.LpInteger)
x_2 = pulp.LpVariable("2", lowBound=0, upBound=1, cat=pulp.LpInteger)
x_3 = pulp.LpVariable("3", lowBound=0, upBound=1, cat=pulp.LpInteger)
x_4 = pulp.LpVariable("4", lowBound=0, upBound=1, cat=pulp.LpInteger)
x_5 = pulp.LpVariable("5", lowBound=0, upBound=1, cat=pulp.LpInteger)
x_6 = pulp.LpVariable("6", lowBound=0, upBound=1, cat=pulp.LpInteger)
x_7 = pulp.LpVariable("7", lowBound=0, upBound=1, cat=pulp.LpInteger)
x_8 = pulp.LpVariable("8", lowBound=0, upBound=1, cat=pulp.LpInteger)
x_9 = pulp.LpVariable("9", lowBound=0, upBound=1, cat=pulp.LpInteger)
x_10 = pulp.LpVariable("10", lowBound=0, upBound=1, cat=pulp.LpInteger)
x_11 = pulp.LpVariable("11", lowBound=0, upBound=1, cat=pulp.LpInteger)
x_12 = pulp.LpVariable("12", lowBound=0, upBound=1, cat=pulp.LpInteger)
x_13 = pulp.LpVariable("13", lowBound=0, upBound=1, cat=pulp.LpInteger)
x_14 = pulp.LpVariable("14", lowBound=0, upBound=1, cat=pulp.LpInteger)
x_15 = pulp.LpVariable("15", lowBound=0, upBound=1, cat=pulp.LpInteger)
x_16 = pulp.LpVariable("16", lowBound=0, upBound=1, cat=pulp.LpInteger)
x_17 = pulp.LpVariable("17", lowBound=0, upBound=1, cat=pulp.LpInteger)
x_18 = pulp.LpVariable("18", lowBound=0, upBound=1, cat=pulp.LpInteger)

problem += (6 * x_1 + 12 * x_2 + 4 * x_3 + 3 * x_4 + 7 * x_5 + 1 * x_6 
+ 3 * x_7 + 2 * x_8 + 7 * x_9 + 3 * x_10 + 4 * x_11 + 2 * x_12 + 10 * x_13 
+ 13 * x_14 + 5 * x_15 + 16 * x_16 + 14 * x_17 + 9 * x_18)

problem += (4 * x_1 + 8 * x_2 + 3 * x_3 + 5 * x_4 + 9 * x_5 + 2 * x_6 
+ 3 * x_7 + 1 * x_8 + 5 * x_9 + 2 * x_10 + 4 * x_11 + 2 * x_12 + 7 * x_13 
+ 10 * x_14 + 3 * x_15 + 13 * x_16 + 11 * x_17 + 8 * x_18 <= 45)

problem.solve()

end = time.perf_counter()

print("Status", pulp.LpStatus[problem.status])
print("Combination")
print(f"1: {pulp.value(x_1)}個")
print(f"2: {pulp.value(x_2)}個")
print(f"3: {pulp.value(x_3)}個")
print(f"4: {pulp.value(x_4)}個")
print(f"5: {pulp.value(x_5)}個")
print(f"6: {pulp.value(x_6)}個")
print(f"7: {pulp.value(x_7)}個")
print(f"8: {pulp.value(x_8)}個")
print(f"9: {pulp.value(x_9)}個")
print(f"10: {pulp.value(x_10)}個")
print(f"11: {pulp.value(x_11)}個")
print(f"12: {pulp.value(x_12)}個")
print(f"13: {pulp.value(x_13)}個")
print(f"14: {pulp.value(x_14)}個")
print(f"15: {pulp.value(x_15)}個")
print(f"16: {pulp.value(x_16)}個")
print(f"17: {pulp.value(x_17)}個")
print(f"18: {pulp.value(x_18)}個")
print("Total value", pulp.value(problem.objective))
print("処理時間: {:.6f} 秒".format(end - start))