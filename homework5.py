immutable_var = 1, "str", False
print(f"Immutable tuple: {immutable_var}")
# immutable_var[0] = 2
# immutable_var is a tuple that is immutable
mutable_list = [1, "str", False]
mutable_list[0] = 2
mutable_list[1] = "int"
mutable_list[2] = False
print(f"Mutable list: {mutable_list}")