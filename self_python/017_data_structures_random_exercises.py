# Data structures Exercises:

"""
Exercise Question 1: Given a two list. Create a third list by picking an odd-index element from the first list and even index elements from second.
"""

listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
listThree = list()
oddElements = listOne[1::2]
print("Element at odd-index positions from list one")
print(oddElements)
EvenElement = listTwo[0::2]
print("Element at odd-index positions from list two")
print(EvenElement)
print("Printing Final third list")
listThree.extend(oddElements)
listThree.extend(EvenElement)
print(listThree)


"""
Exercise Question 2: Given an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list
"""

sampleList = [34, 54, 67, 89, 11, 43, 94]
print("Origigal list ", sampleList)
element = sampleList.pop(4)
print("List After removing element at index 4 ", sampleList)
sampleList.insert(2, element)
print("List after Adding element at index 2 ", sampleList)
sampleList.append(element)
print("List after Adding element at last ", sampleList)

"""
Exercise Question 3: Given a list slice it into a 3 equal chunks and rever each list
"""

sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
# print("Origigal list ", sampleList)
length = len(sampleList)
chunkSize = int(length / 3)
start = 0
end = chunkSize
for i in range(1, 4):
    indexes = slice(start, end, 1)
    # print(indexes): slice(0, 3, 1), slice(3, 6, 1), slice(6, 12, 1)
    listChunk = sampleList[indexes]
    print("Chunk ", i, listChunk)
    print("After reversing it ", list(reversed(listChunk)))
    start = end
    if(i != 2):
        end += chunkSize
    else:
        end += length - chunkSize

"""
Exercise Question 4: Given a list iterate it and count the occurrence of each element and create a dictionary to show the count of each element
"""

sampleList = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Origigal list ", sampleList)
countDict = dict()
for item in sampleList:
    if(item in countDict):
        countDict[item] += 1
    else:
        countDict[item] = 1

print("Printing count of each item  ", countDict)

"""
Exercise Question 5: Given a two list of equal size create a set such that it shows the element from both lists in the pair
"""
firstList = [2, 3, 4, 5, 6, 7, 8]
# print("First List ", firstList)
secondList = [4, 9, 16, 25, 36, 49, 64]
# print("Second List ", secondList)
result = zip(firstList, secondList)
resultSet = set(result)
print(resultSet)


"""
Exercise Question 6: Given a following two sets find the intersection and remove those elements from the first set
"""
firstSet = {23, 42, 65, 57, 78, 83, 29}
secondSet = {57, 83, 29, 67, 73, 43, 48}
print("First Set ", firstSet)
print("Second Set ", secondSet)
intersection = firstSet.intersection(secondSet)
print("Intersection is ", intersection)

# for item in intersection:
#   firstSet.remove(item)
print("First Set after removing common element ", firstSet.difference(intersection))

"""
Exercise Question 7: Given two sets, Checks if One Set is Subset or superset of Another Set. if the subset is found delete all elements from that set
"""

firstSet = {57, 83, 29}
secondSet = {57, 83, 29, 67, 73, 43, 48}

print("First set is subset of second set -", firstSet.issubset(secondSet))
print("Second set is subset of First set - ", secondSet.issubset(firstSet))

"""
Question 8: Iterate a given list and Check if a given element already exists in a dictionary as a key's value if not delete it from the list
"""
rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

rollNumber = [item for item in rollNumber if item in sampleDict.values()]
print("after removing unwanted elemnts from list ", rollNumber)

"""
QUestion 9: Given a dictionary get all values from the dictionary and
add it in a list but don't add duplicates
"""

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53,
         'july': 54, 'Aug': 44, 'Sept': 54}

speedList = sorted(list(set([val for val in speed.values()])))

print("unique list", speedList)  # unique list [47, 52, 44, 53, 54]
