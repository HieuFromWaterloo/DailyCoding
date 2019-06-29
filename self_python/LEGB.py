# LEGB: Local, Enclosing, Global, Built-in

for a in range(2):
    x = 'global {}'.format(a)


def outer():
    # x = 'outer x'  # local
    for b in range(3):
        x = 'outer {}'.format(b) # this x is local to the outer()

    def inner():
        # nonlocal x # this will affect the the local x in the enclosing function
        # "nonlocal" is useful to change the state of the closure and decorator
        # x = 'inner x'
        for c in range(4):
            x = 'inner {}'.format(c) # this x is local to the inner()
            # if cannot find local then it will following LEGB rules
        print(x)
        print(a, b, c)

    inner()
    print(x)
    print(a, b)


outer()
print(x)
print(a)

# Built-in: do not over write build in functions
# import builtins
# print(dir(builtins))
