# Generator: >>>>>>>
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result


my_nums = square_numbers([1, 2, 3, 4, 5])
# print(my_nums) [1, 4, 9, 16, 25]

# Now our result is a list, how do we make it a generator?


def square_numbers_generator(nums):
    # result = []
    for i in nums:
        # here we no longer have a list as our final output
        # Generator DO NOT hold the entire result in memory, INSTEAD,
        # it yields one result at a time
        # NOTE: we can still use for loop to call the next generator
        # Save memory
        yield (i * i)


my_nums_generator = square_numbers_generator([1, 2, 3, 4, 5])

# print(next(my_nums_generator))
# for i in my_nums_generator:
#     print(i)

# WHAT ABOUT as List Comprehension???? HOW TO CREATE A GENERATOR?
my_nums = [x**2 for x in [1, 2, 3, 4, 5]]
# use () instead of []
my_nums_generator = (x**2 for x in [1, 2, 3, 4, 5])
# print(my_nums_generator)
# for i in my_nums_generator:
#     print(i)

# Convert Generator into a list: This will remove all memory advantage
# list(my_nums_generator)

##### Example: ####
# from pympler import summary, muppy
# import psutil
# import resource
import os
import sys
import time
import random


# def memory_usage_psutil():
#     # return the memory usage in MB
#     process = psutil.Process(os.getpid())
#     mem = process.get_memory_info()[0] / float(2 ** 20)
#     return mem


# def memory_usage_resource():
#     rusage_denom = 1024.
#     if sys.platform == 'darwin':
#         # ... it seems that in OSX the output is different units ...
#         rusage_denom = rusage_denom * rusage_denom
#     mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / rusage_denom
#     return mem


names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

# print 'Memory (Before): {}Mb'.format(mem_profile.memory_usage_psutil())


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        # yield i # return 0,1,2,3,4,...
        yield person


t1 = time.clock()
people_gen = people_generator(3)
t2 = time.clock()
t3_gen = t2 - t1
print('Took {} Seconds'.format(t3_gen))


t1 = time.clock()
people_list = people_list(3)
t2 = time.clock()
t3_list = t2 - t1

# print 'Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil())
print('Took {} Seconds'.format(t3_list))

print("generator is {:.3f} faster".format(t3_list / t3_gen))

print(people_list)

for i in people_gen:
    print(i)
