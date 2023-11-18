


menu = {'sandwich' : 10, 'tea': 3, 'cola': 4, 'beer': 5}

#print(menu)

def valgykla():
    user_input = input('Please order: ')
    user_order = str(user_input)
    menu = {'sandwich' : 10, 'tea': 3, 'cola': 4, 'beer': 5}
    total_sum = 0
    while True:
        if user_order in menu:
            total_sum += menu[user_order] 
            print(f'{user_order} costs {menu[user_order]}, total is {total_sum}')
            user_input = input('Order: ')
            user_order = str(user_input)
        elif user_order == '':
            print(f'Your total is {total_sum}')
            break
        else:
            print('We do not have this, sir.')
            user_input = input('Can I bring you anything else? ')
            user_order = str(user_input)

        


#print(menu['sandwich'])
valgykla()