import time

weights = [4, 8, 3, 5, 9, 2, 3, 1, 5, 2, 4, 2, 7, 10, 3, 13, 11, 8]
values = [6, 12, 4, 3, 7, 1, 3, 2, 7, 3, 4, 2, 10, 13, 5, 16, 14, 9]
capacity = 45
n = len(weights)

def brute_force():
    max_value = 0
    best_combination = []
    for i in range(1 << n):
        current_weight = 0
        current_value = 0
        current_combination = []

        for j in range(n):
            if (i >> j) & 1:
                current_weight += weights[j]
                current_value += values[j]
                current_combination.append(j + 1)
        
        if current_weight <= capacity and current_value > max_value:
            max_value = current_value
            best_combination = current_combination
    
    return max_value, best_combination

if __name__ == "__main__":
    print("総当たり法")
    value, combo = brute_force()
    print(f"最大の値段: {value}")
    print(f"品物の組み合わせ: {combo}")