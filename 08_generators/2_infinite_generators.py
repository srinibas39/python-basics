
def infinit_chai():
    count = 1
    while True:
        yield f"Refill #{count}"
        count = count + 1

refill = infinit_chai()

for _ in range(5):
    print(next(refill))

for _ in range(6):
    print(next(refill))