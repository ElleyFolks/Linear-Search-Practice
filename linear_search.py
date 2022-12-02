def linear_search(list_num, key_input):

    for index in range(len(list_num)):
        if (list_num[index] == key_input):
            return index  # breaks out of loop and returns found index position

    return -1  # defaults to false if not found


# main program
list_numbers = [1, 2, 3, 5, 7, 11]

print(list_numbers)

key = int(input("Please enter a number to be searched: \n"))

key_index = linear_search(list_numbers, key)

if (key_index == -1):
    print("entered number {input} not found".format(input=key))
else:
    print("number found in index position: {index} ".format(index=key_index))
