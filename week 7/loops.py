# loops

'''

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
    
numbers = [1, 2, 3, 5, 7]

for number in numbers:
    print(number)
    


# using a while loop to count from 1 to 5

count = 1

while count <= 5:
    print(count)
    count += 1 # increments the count by 1
    
'''

# loop control statements

'''

fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    if fruit == "cherry":
        break # exits the loop if cherry is found
    print(fruit)
    
print()

for fruit in fruits:
    if fruit == "cherry":
        continue # skips cherry and moves to the next iteration
    print(fruit)
    
print()

for fruit in fruits:
    if fruit == "cherry":
        pass # placeholder, no action is needed for cherry
    print(fruit)
    
'''

count = 0

while count < 5:
    print(count)
    count += 1
    if count == 3:
        break # exits the loop when the count is reached - 3