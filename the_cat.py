items = [int(num) for num in input().split(', ')]
entry_point = int(input())
item_type = input()

right = []
left = []

for i in range(0, entry_point):
    left.append(items[i])
for i in range(entry_point + 1, len(items)):
    right.append(items[i])

left_value = 0
right_value = 0

for elem in left:
    if item_type == "cheap" and elem < items[entry_point]:
        left_value += elem
    if item_type == "expensive" and elem >= items[entry_point]:
        left_value += elem

for elem in right:
    if item_type == "cheap" and elem < items[entry_point]:
        right_value += elem
    if item_type == "expensive" and elem >= items[entry_point]:
        right_value += elem

if right_value > left_value:
    print(f"Right - {right_value}")
else:
    print(f"Left - {left_value}")