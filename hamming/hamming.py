def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("String lengths should match")
    if strand_a == strand_b:
        return 0
    list_a = list(strand_a)
    list_b = list(strand_b)
    distance = 0
    for index_a, element_a in enumerate(list_a):
        if element_a != list_b[index_a]:
            distance += 1
    return distance
