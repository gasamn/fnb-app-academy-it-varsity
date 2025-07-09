# sets - we use {}

'''

my_set = {1, 2, 3, 4, 5}

print(my_set)

my_set.add(6)
print(my_set)

my_set.remove(3)
print(my_set)

'''

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# union - adds both sets together and removes duplicate data

union_set = set1.union(set2)
print(union_set)

# intersection - finds common elements between sets

inter_set = set1.intersection(set2)
print(inter_set)

# difference - finds the elements that are present in one set but not the other

diff_set = set1.difference(set2)
print(diff_set)