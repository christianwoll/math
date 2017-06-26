import random

results = []
overshoot = []
num_tests = 10**5
for _ in range(num_tests):
    calories = 2000
    for i in range(100):
        x = (random.random() + 1) / 2
        calories *= x
        if calories <= 400: break
    results.append(i + 1)
    overshoot.append(400 - calories)

print(num_tests)
print('offerings:')
print(sum(results) / len(results))
print(max(results))
print('overshoot:')
print(sum(overshoot) / len(overshoot))
print(min(overshoot))
print(max(overshoot))
