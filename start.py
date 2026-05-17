numbers = [1, 2, 3, 4]

print(numbers)
numbers.insert(1, 100) #index works as placeholder that is place and number so oitput is [1,100,3,4]

print(numbers)

numbers.remove(3) # removes matching value output is [1,100,2,4]

print(numbers)
print(numbers[0])      # first element
print(numbers[-1])     # last element

numbers.pop() #pop removes last element

print(numbers)

numbers[0] = 999

print(numbers)
print(numbers[1:3])#Start from index 1 and go up to index 3 excluding 3, prints index 1 and 2 


numbers.sort()

print(numbers)
numbers.sort(reverse=True)

print(numbers)

numbers.reverse()

print(numbers)



#loop in list 
for item in numbers:
    print(item)
    
    
