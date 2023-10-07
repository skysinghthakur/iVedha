#Write a simple if statement to check a condition
#it will ask age from user and check their eligibilty to vote 
age = int(input("Enter your age: "))
if(age>=18):
    print("Eligible for Vote")


#Advice / write a code that uses a for loop to iterate over a list or range

#this we are traversing to each element (not index)
l = [10, 20, 30, 40, 50, 60]
for i in l:
    print(i,end=" ")
print()
#traversing over the index
for i in range(len(l)):
    print(f"index: {i} value: {l[i]}")


#Tell us some example of using while loops.

#if we need to break the loop at some condition
#suppose the above list is prices values and you have 100 bucks only and you can only buy from starting

sum = i = 0
while(i<len(l) and sum < 100):
    sum += l[i]
    i+=1
print(f"sum is {sum} at {i}")

