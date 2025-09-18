def local_chai():
    yield "chai 1"
    yield "chai 2"

def imported_chai():
    yield "chai 3"
    yield "chai 4"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)

# stall = full_menu()

# print(next(stall))
# print(next(stall))

def chai_stall():
    try:
        while True:
            yield "Waiting"
    except:
        print("Stall closed,No more")

stall = chai_stall()

print(next(stall))
print(next(stall))
print(next(stall))
print(next(stall))
stall.close() #cleans up memory