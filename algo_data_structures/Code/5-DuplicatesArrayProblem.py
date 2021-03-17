"""
1. bruce force: O(N^2)
2. hashmap:
    - traverse the given array
    - try to insert each item in a hashtable (dictionary) with value as key
    - if cannot insert (len(dict) does not increase) -> duplicate
    - issue: this is not an `inplace` soln so it would require some extra memory for the hashtable
3. use absolute values - O(N) and inplace
    - issue: this method is fucked with negative elements in a list
"""


def find_duplicates(nums):
    # **HARD**
    # we can achieve O(N) linear running time where N=len(nums)
    for num in nums:
        if nums[abs(num)] >= 0:
            nums[abs(num)] = -nums[abs(num)]
        else:
            print('Repetition found: %s' % str(abs(num)))

def find_duplicates2(nums):

    # we can achieve O(N) linear running time where N=len(nums)
    adict = dict()
    current_dict_size = 0
    for num in nums:
        adict[num] = 1
        if len(adict) > current_dict_size:
            current_dict_size = len(adict)
        else:
            print('Repetition found: %s' % str(abs(num)))


if __name__ == '__main__':

    # THIS METHOD CANNOT HANDLE VALUES < 0 !!!
    # the maximum item is smaller than the size of the list

    n = [2, 6, 5, 1, 4, 3, 2]
    find_duplicates(n)
    # find_duplicates2(n)
