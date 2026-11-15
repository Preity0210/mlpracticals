
n = int(input("Enter number of items: "))

items = []

for i in range(n):
    w = int(input("Enter weight: "))
    p = int(input("Enter profit: "))
    items.append((p/w, w, p))

capacity = int(input("Enter knapsack capacity: "))

items.sort(reverse=True)

total = 0

for ratio, w, p in items:
    if capacity >= w:
        total += p
        capacity -= w
    else:
        total += ratio * capacity
        break

print("Maximum Profit:", total)
