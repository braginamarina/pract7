my_list = [1, 3, 5, 3, 7, 9, 1, 5]
seen = set()
duplicates = set()

for item in my_list:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

if duplicates:
    print(f"Повторяющиеся элементы: {list(duplicates)}")
else:
    print("Повторяющихся элементов нет")