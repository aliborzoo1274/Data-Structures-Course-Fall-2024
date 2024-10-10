while True:
    user_input = input().split()
    command = int(user_input[0])
    
    if command == 1:
        my_list = []
    elif command == 2:
        my_list = None
    elif command == 3:
        if my_list == None:
            print('nulle')
        else:
            my_list.append(user_input[1])
    elif command == 4:
        if my_list == None:
            print('nulle')
        elif int(user_input[1]) >= len(my_list):
            print('oute')
        else:
            print(my_list[int(user_input[1])])
    elif command == 5:
        if int(user_input[1]) == 0:
            print('sefre')
        else:
            print(int(user_input[2]) / int(user_input[1]))
    elif command == 6:
        break