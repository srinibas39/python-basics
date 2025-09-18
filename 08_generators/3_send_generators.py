
# yield generates data
# we can also send data to yield

def chai_customer():
    print("Welcome")
    order = yield # stops the program flow
    while True:
        print(f"Preparing: {order}")
        order = yield #

stall = chai_customer()

next(stall) #doing this to get inside the while lopp

stall.send("Lemon Tea")
stall.send("coffee")

