# Example of memoization

def add_to_80(n):
    return n + 80

# using closures, the outer function "memoised_add_to_80" save the dictonary called "cache" which save previous solutions
# cache is saved due to it is used on the inner function "add_to_80"
def memoized_add_to_80():
    cache = {}

    def add_to_80(n):
        if n in cache:
            return cache[n]
        else:
            print("long")
            cache[n] = n + 80
            return cache[n]
    return add_to_80

memoized = memoized_add_to_80()

print(memoized(5))
print(memoized(5))