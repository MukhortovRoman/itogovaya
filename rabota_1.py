def filter_short_strings(arr):
    result = []
    for string in arr:
        if len(string) <= 3:
            result.append(string)
    return result


input_arr = ["Hello", "2", "world", ":-)"]
output_arr = filter_short_strings(input_arr)
print(output_arr)
