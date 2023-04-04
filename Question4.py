#a
Dict = {}

print("Question 4.a")

for i in range(1, 31):
    if i == 1:
        Dict[i] = 0
    else:
        Dict[i] = (i-1) * i

print(Dict)

#b

print("Question 4.b")
for key in Dict:
    print(key, Dict[key])

#c

print("Question 4.c")
sum = 0

for key in Dict:
    sum += Dict[key]

print(sum)


#d
print("Question 4.d")

removingKey = int(input("Enter a number to be removed from the Dict : "))

if Dict.get(removingKey):
    Dict.pop(removingKey)
else:
    print("There is not a matching key with a number your entered")

print(Dict)