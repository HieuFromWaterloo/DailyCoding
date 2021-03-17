# requirement: reverse INPLAC, inplace means without using extra memory
# O(N) linear running time where N is the number of elemnts

def reverse(nums):

    # pointing to the first item
    start_index = 0
    # index pointing to the last item
    end_index = len(nums) - 1

    while end_index > start_index:
        # keep swapping the items
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        start_index = start_index + 1
        end_index = end_index - 1
    return nums


if __name__ == '__main__':

    n = [1, 2, 3, 4]
    n2 = reverse(n)
    print(n2)
