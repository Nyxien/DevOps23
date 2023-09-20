num_list =[1, 2, 7, 4, 9]

def minimun(num_list):
    min = num_list[0]
    for x in num_list:
        if x < min:
            min = x
    return min

print(minimun(num_list))