# yield
# when we dont want results immediately
# lazy evaluation
def serve():
    yield 1
    yield 2 
    yield 3

stall = serve() #serve keep the refernce of all the yields in the memory

for num in stall:
    print(num)

def get_num_list():
    return [1,2,3]

def get_gen_list():
    yield 1
    yield 2
    yield 3

print(get_num_list())
print(get_gen_list())

nums = get_gen_list()

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums)) # gives error beacause we have only three results


