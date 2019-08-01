employees = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']

gym_members = ['April', 'John', 'Corey']

developers = ['Judy', 'Corey', 'Steven', 'Jane', 'April']

if 'Corey' in developers:
    print('Found!')

# O(n) for list
# O(1) for a set

s1 = {1, 2, 3, 4, 5}
# for empty set: s = set(), NOT {}: bc this is an empty dict
s2 = {5, 6, 7, 8, 9}
s3 = {8, 9, 10}
s4 = {8}

# add/remove 1 item into a set: use add()/remove()/discard()
# note: usng remove() will throws error if the item is not in the set
s1.add(6)
print(s1)
# add/remove more than 1 item into a set: use update()
s1.update([7, 8], s3)  # we can update using list and set
print(s1)

# ----  We can use intersection, union, difference ---

# intersection
print(s2.intersection(s3))  # 8 and 9
print(s2.intersection(s3, s4))  # 8

# difference & symmetric difference
# value in s2 but not in s3
print(s2.difference(s3))  # 5,6,7
# value in s2 but not in (s1 or s3)
print(s2.difference(s3, s1))  # set()
# values in s2 but not in s3 AND VICE VERSA >>
print(s2.symmetric_difference(s3))  # 5,6,7,10

# union
print(s2.union(s3))  # 5, 6, 7, 8, 9, 10

### Use cases of set: ####

# 1. remove duplicates of a list

# CHECK SUBSET:
firstSet = {57, 83, 29}
secondSet = {57, 83, 29, 67, 73, 43, 48}

print("First set is subset of second set -", firstSet.issubset(secondSet))
print("Second set is subset of First set - ", secondSet.issubset(firstSet))
