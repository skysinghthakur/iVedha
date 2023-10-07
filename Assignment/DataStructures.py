l = [10, 20, 30]
l.append(40)
#add value 40 at the end of the list

#if there are multiple values to add we can use extend
l.extend([50,60])
#if will also add at the end of list

l.insert(1,100)
#insert element at specific location

l.remove(20)
#remove the first occurence of the given value

l.pop(1)
#if we specify index then the element be popped out else by default last element get popped out

index = l.index(30)
#return the fist occurence index of the value

count = l.count(30)
#return the number of times element appear in the list

l.sort()
# to sort the list

l.reverse()
# to reverse the list

candidate = {'name': 'Akash', 'experience': 2.2}
# accessing candidate name
print(f"Name of the Candidate is {candidate['name']}")

# get won't throw any error if key doesn't exist value is None
print(f"Age of candidate is {candidate.get('age')}")

# modifying
candidate['age'] = 24
candidate['experience'] = 2.3

del candidate['age']
val = candidate.pop('age','Not Found') #remove and return age if exist else return "Not Found"
print(f"Age {val}")

print(f"All the keys in dictionary: {candidate.keys()}")
print(f"All the values in dictionary:  {candidate.values()}")
print(f"All the key and values in dictionary: {candidate.items()}")