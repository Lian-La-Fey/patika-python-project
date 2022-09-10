def reverse(list, index):
    if (len(list) == index): return

    if (type(list[index]) == type([])):
        list[index] = list[index][::-1]
        reverse(list[index], 0)

    return reverse(list, index + 1)

input = [9, [[1, 3], 2, [1, 2]], [3, 4], [5, 6, 7]]
input = input[::-1]
reverse(input, 0)

print(input)