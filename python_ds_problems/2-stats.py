import random
from fractions import Fraction

"""
Objective 1
In this challenge, we practice calculating probability.

Task
In a single toss of  fair (evenly-weighted) -sided dice, find the probability of that their sum will be at most 9
"""

N = 1000000
track = 0

for _ in range(N):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    if d1 + d2 > 9:
        track += 1

print(str(Fraction(round(1 - track / N, 2)).limit_denominator()))  # 0.833

"""
Objective 2
In this challenge, we practice calculating probability.

Task
For a single toss of  fair (evenly-weighted) dice, find the probability that the values rolled by each die will be different and their sum is .

Output Format

In the editor below, submit your answer as Plain Text in the form of an irreducible fraction , where  and  are both integers.
"""


N = 1000000
track = 0

for _ in range(N):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    if d1 != d2 and d1 + d2 == 6:
        track += 1

print(round(track / N, 3))
print(str(Fraction(round(track / N, 2)).limit_denominator()))

"""
Objective
In this challenge, we practice calculating probability.

Task
There are  urns: ,  and .

Urn  X contains  red balls and  black balls.
Urn  Y contains  red balls and  black balls.
Urn  Z contains  red balls and  black balls.
One ball is drawn from each urn. What is the probability that the  balls drawn consist of 2 red balls and 1 black ball?

Output Format

In the editor below, submit your answer as Plain Text in the form of an irreducible fraction , where  and  are both integers.
"""

N = 1000000
track = 0

for _ in range(N):
    # pick 1:
    #
    b1 = random.randint(1, 6)
    b2 = random.randint(1, 6)
    b3 = random.randint(1, 6)
    if d1 != d2 and d1 + d2 == 6:
        track += 1

print(round(track / N, 3))
print(str(Fraction(round(track / N, 2)).limit_denominator()))
