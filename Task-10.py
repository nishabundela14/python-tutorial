list1 = list(range(1,11))
print(f"original list: {list1}")

new_list = list1[:5]
print(f"Extracted first five elements: {new_list}")

new_list.reverse()
print(f"Reversed extracted elements: {new_list}")