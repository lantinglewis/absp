def separator(unedited_list):
    if len(unedited_list) != 0:
        for i in range(len(unedited_list) - 1):
            print(unedited_list[i] + ', ', end='')

        print('and ' + unedited_list[len(unedited_list)-1])
    else:
        print("You can't separate a empty list")


spam = ['apples', 'bananas', 'tofu', 'cats']
empty_list = []

separator(spam)
separator(empty_list)
