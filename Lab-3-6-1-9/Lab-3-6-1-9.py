my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

new_list = []
#       Solution 1 using in
#for element in my_list:
#    if element in new_list:
#        continue
#    else:
#        new_list.append(element)

#       Solution 2 using not in
for element in my_list:
    if element not in new_list:
        new_list.append(element)

#       Solution 3 outside of lab using dictionary keys as list
#new_list = list(dict.fromkeys(my_list))

#       Solution 4 outside of lab using set object
#new_list = list(set(my_list))

print("The list with unique elements only:")
print(my_list)
print(new_list)