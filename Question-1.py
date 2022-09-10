def flat(list, index, extended):
    if ( len(list) == index ): return

    if type(list[index]) == type([]) or type(list[index]) == type(()):
        flat(list[index], 0, extended)
    else:
        extended.append(list[index])

    return flat(list, index+1, extended)

input = [[1,'a',('cat'),2],[[[3]],'dog'],4,5]

flatten = []

for item in input:
    if type(item) == type([]) or type(item) == type({}) or type(item) == type(()):
        extended = []
        flat(item, 0, extended)
        flatten.extend(extended)
    else:
        flatten.append(item)

print(flatten)