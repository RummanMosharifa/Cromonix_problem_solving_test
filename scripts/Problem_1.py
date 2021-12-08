# Taking input (array)

print('Length of the array : ', end='')
length = int(input())
print()
print("Enter the values of the array (,) separated : ", end='')
print()
temp_list = []

while len(temp_list) < length:
    print(f"Enter {len(temp_list)}th indexed element : ", end='')
    try:
        input_val = int(input())
    except:
        print("Please Enter an Integer!!!")
    if input_val not in temp_list:
        temp_list.append(input_val)
    else:
        print("You can not enter the same value twice!!!")

# sorting the array
temp_list.sort()
print(f"Given sorted array : {temp_list}")

# Taking input (target)
print('Enter the target value : ', end='')
try:
    target_value = int(input())
except:
    print("Please enter an integer value")


# get the elements that sums up to the target value
def get_correct_element(temp_list, target):
    first_index = -1
    second_index = -1
    for i in range(len(temp_list)):
        for j in range(i + 1, len(temp_list)):
            if temp_list[i] + temp_list[j] == target:
                first_index = i
                second_index = j
    return first_index,second_index


# get the indices of the elements that sums up to the target value
def get_indices(temp_list, target):
    first_index, second_index = get_correct_element(temp_list, target)
    if first_index >= 0 and second_index >= 0:
        return first_index, second_index
    else:
        return None


if __name__ == '__main__':
    indices = get_indices(temp_list, target_value)
    if indices is not None:
        print(f"The indices are : {list(indices)}")
    else:
        print("Not found!!")
