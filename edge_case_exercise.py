def move(my_list, direction):
    index = my_list.index(1)  # find where the 1 is
    
    # Move right
    if direction == "right" and index < len(my_list) - 1:
        my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]
    
    # Move left
    elif direction == "left" and index > 0:
        my_list[index], my_list[index - 1] = my_list[index - 1], my_list[index]
    
    # Return updated list
    return my_list
