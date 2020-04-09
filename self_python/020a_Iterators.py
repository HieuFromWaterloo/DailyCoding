"""
- Iteratorable: sth that can be looped over (list, dict, tuple, generator, etc)

- Iterator: is an object with states so it remembers where it is during iteration.

Note that a list is iterable BUT NOT an iterator

- Very helpful because we can add these methods to our classes and make them iterable as well

- Memory efficient: iterator does not require storing a big list/tuple with tons of items while iterating through them. it simple loop over one value at a time until it exhausted. (password crackers as for examples)
"""

nums = [1, 2, 3]
# Check if sth is iterable
# print(dir(nums))
"""
'__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

'__iter__'
"""

# Iterator allows us to call "next" to get the next value "__next__"
# turn a list into an iterator
i_nums = iter(nums)  # now if we run dir(i_nums), we see __next__
print(next(i_nums))  # 1
print(next(i_nums))  # 2
print(next(i_nums))  # 3

# NOTE: we cannot go backwards or reset with iterator. if wanna reset, need to create an iterator object from scratch and run again

#### HELPFUL #####


class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    # now gotta make stuff interable using object __iter__
    def __iter__(self):
        return self

    # add __next__
    def __next__(self):
        # define states is needed
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.current += 1
        return current


nums = MyRange(1, 10)
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))

# GENERATOR EQUIVALENT TO THE ABOVE CLASS: very ez to read version of iterators, which already take care of __iter__, __next__


def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


########### EXERCISE: #########
"""
Create an iterator and generator theat loops through every word in a sentence
"""
sentence = "This is a test sentence"

# Iterator


class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        idx = self.index
        self.index += 1
        return self.words[idx]


my_sentence = Sentence(sentence)


def my_sentence(sentence):
    words = sentence.split()
    idx = 0
    while idx < len(words):
        yield words[idx]
        idx += 1


def my_sentence(sentence):
    words = sentence.split()
    for w in words:
        yield w
