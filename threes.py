# this is a program intended to return the number of values up to and
# including a given integer which contain the digit three at least one time
n = int(input("Enter a value:"))
a_list = list(range(0, n+1))
string_to_test = str(a_list)
chars_to_check = ["3"]
count = 0
for char in chars_to_check:
    if char in string_to_test:
        count = count+1

print ("Number of threes found in range = " + str((count)))