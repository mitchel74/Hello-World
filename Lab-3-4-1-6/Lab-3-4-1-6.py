hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

middle = int(input("Enter an integer to replace middle number: "))
hat_list[2] = middle
# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
del hat_list[-1]
# Step 2: write a line of code that removes the last element from the list.
print("New list legnth: ", len(hat_list))
# Step 3: write a line of code that prints the length of the existing list.

print(hat_list)