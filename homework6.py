my_dict = {"Anton": 22, "Alena": 21}
my_set = {1, "Яблоко", 42.314}

print(f"Dict: {my_dict}")
print(f"Existing value: {my_dict.get('Anton')}")
print(f"Not existing value: {my_dict.get('Anton1')}")
my_dict.update({"Anton23": 23, "Anton24": 24})
print(f"Deleted value: {my_dict.pop('Anton')}")
print(f"Dict: {my_dict} \n")

print(my_set)
my_set.update({"Тыблоко", 314.42})
my_set.discard(1)
print(my_set)