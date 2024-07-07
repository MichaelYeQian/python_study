nested_dict = {
    "a" : 1,
    "b" :{"x" : 2 , "y" :3},
    "c" :{"z" : {"p" : 4}}
}
sum = nested_dict["a"] + nested_dict["b"]["x"] + nested_dict["b"]["y"] + nested_dict["c"]["z"]["p"]
print(f"sum of all values : {sum}")