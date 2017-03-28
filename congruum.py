nums = {}
for m in range(2, 2**10):
    for n in range(1, m):
        x = m**2 + n**2
        if not x in nums.keys():
            nums[x] = []
        nums[x].append([m, n])

print('Searching...')
for i, k1 in enumerate(nums.keys()):
    for k2 in list(nums.keys())[:i]:
        k3 = (k1**2 + k2**2)**(1/2)
        if k3 in nums.keys():
            k3 = int(k3)
            c1 = [4*m*n*(m**2-n**2) for m, n in nums[k1]]
            c2 = [4*m*n*(m**2-n**2) for m, n in nums[k2]]
            c3 = [4*m*n*(m**2-n**2) for m, n in nums[k3]]
            if set(c1) & set(c2) or set(c1) & set(c3) or set(c2) & set(c3):
                print(k1, c1)
                print(k2, c2)
                print(k3, c3)
                print()
print('Done')
