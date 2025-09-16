import code;
import pdb;
import asyncio
print("Hello python")

# Variables

# Numbers
a = 10
pi = 3.14

# Strings
name = "srinibas"

# Boolean
is_active = True

# Lists
fruits = ["apple", "banana", "mango"]

# Dictionaries
person = {"name":"srinibas", "age":30}

print(f"Hi, My name is {person['name']} and I like {fruits[0]}")

# Functions

def greet(name):
    return f"Hello {name}!"

print (greet(person["name"]))

#Loops

for fruit in fruits:
    print(fruit)

for i in range(100):
    print(i, end=' ')

for x in range(30,0,-5):
    print(x , end=' ')

j = 0
while j < 10:
    print(j, end=" ")
    j += 5
    
# Code.interact --> interactive console
def debug_point():
    x = 42
    y = "hello"
    # This opens a REPL where you can play with variables x and y
    code.interact(local=locals())

debug_point()

# Pdb =>
#  to print p f"i: {i} a: {a} b: {b} result: {result}"
def calculate(a, b):
    my_list = []
    for i in range(10):
        pdb.set_trace()  
        result = i + a + b
        my_list.append(result)
    return list

# print(calculate(5, 10))

#  async and await

async def fetch_data(n):
    print(f"fecthing {n}...")
    asyncio.sleep(2)
    print("fecthing done")
    return f"Data {n}"

async def main():
    result = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3),
        fetch_data(4)
    )
    print(result)

asyncio.run(main())