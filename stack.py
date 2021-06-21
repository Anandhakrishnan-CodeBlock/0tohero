def add(array):
    print('Enter item to add:')
    itm = int(input())
    array.append(itm)
    return array

def delete(array):
    if len(array) == 0:
        print('Stack Empty')
    else:
        ind = len(array)
        array.pop(ind-1)
        return array

def display(array):
    print(array)

print('Stack Operation:')
print('Select your Option:')
print('1.Push')
print('2.POP')
print('3.Display Stack')
stk = []
while True:
    print('-1.Push, 2.POP, 3.Display Stack, 0.Quit-')
    opt = input()
    if opt in ('1', '2', '3', '0'):
        if opt == '1':
            add(stk)
        elif opt == '2':
            delete(stk)
        elif opt == '3':
            display(stk)
        elif opt == '0':
            break
    else:
        print('Invalid Option')