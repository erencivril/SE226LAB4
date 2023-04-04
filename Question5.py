divided = {'Tony': 41, 'Rhodey': 43, 'Nat': 35}
we_fall = {'Steve': 39, 'Clint': 35, 'Wanda': 28}

#5.a
print("Question 5.a")

united_we_stand = {}
united_we_stand.update(divided)
united_we_stand.update(we_fall)

print("Name", "Age")
for key in united_we_stand:
    print(key, united_we_stand[key])

#5.b
print("Question 5.b")

united_we_stand.pop("Nat")
print("Name", "Age")
for key in united_we_stand:
    print(key, united_we_stand[key])


#5.c
print("Question 5.c")

print("Name", "Age")
for key in sorted(united_we_stand):
    print(key, united_we_stand[key])

#5.d
print("Question 5.d")

maximum_value = 0
minimum_value = 9999999999

for (key,val) in united_we_stand.items():
    if val > maximum_value:
        maximum_value = val
    if val < minimum_value:
        minimum_value = val


print("Maximum Age is :", maximum_value)
print("Minimum Age is :", minimum_value)