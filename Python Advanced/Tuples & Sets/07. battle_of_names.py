
def create_list_names(n_lines):
    names = []
    for _ in range(n_lines):
        names.append(input())
    return names

def even_or_odd(sum_values, odd_nums, even_nums):
    if sum_values % 2 == 0:
        even_nums.add(sum_values)
    else:
        odd_nums.add(sum_values)

def operations(odd_nums, even_nums):
    if sum(odd_nums) == sum(even_nums):
        result = odd_nums.union(even_nums) #use the union() method or "|" operator find the union of the 2 sets
    elif sum(odd_nums) > sum(even_nums):
        result = odd_nums - even_nums # use the difference() method or "-" operator to find the difference between the 2 sets
    else:
        result = odd_nums ^ even_nums # use symmetric_difference() method oor "^" to find the symmetric diff between 2 sets
    return result

lines = int(input())
names = create_list_names(lines)

current_line = 0
odd_nums = set([])
even_nums = set({})

for name in names:
    current_line += 1
    sum_char_values = 0
    for char in name:
        sum_char_values += ord(char)
    sum_char_values //= current_line
    even_or_odd(sum_char_values, odd_nums, even_nums)

print(*operations(odd_nums, even_nums), sep=", ") #unpack the sets and sep by ", "
