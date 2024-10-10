# while True:
#     input = input().split()
#     if input[0] == 1:
#         my_list = [None] * 3
#     if input[0] == 2:
#         my_list = []
#     if input[0] == 3:
#         my_list.append(input[1])
#     if input[0] == 4:
#         if len(my_list) == 0:
#             print('nulle')
#         elif input[1] > len(my_list):
#             print('oute')
#         else:
#             print(my_list[input[1] + 1])
#     if input[0] == 5:
#         if input[1] == 0:
#             print('sefre')
#         else:
#             print(input[2] / input[1])
#     if input[0] == 6:
#         break


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