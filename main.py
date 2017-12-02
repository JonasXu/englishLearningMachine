import actions as ac
import os
import time


# os.system("mode con cols=100 lines=20")

def sleep(t = 1):
    time.sleep(t)
def clear():
    os.system('cls')


# this is main program

def search():
        print('this is search mode\n\n\n');
        while 1:
            clear()
            st = input('you want to search:')

            ac.search(st)

            save = input('save? y/n\n')
            if save != 'n':
                ac.save(st)
                print('saved')
            st = input('[enter]')

def train():

        print('this is train mode');
        # while 1:


        trainset = ac.gettrainset()
        for i in range(len(trainset)):
            clear()
            print(i, 'word')
            print('\n'*20)
            print(trainset[i])
            ans = input('get? y/n')
            if ans == 'n':
                ac.search()
                save = input('save? y/n')
                if save == 'y':
                    ac.save(y)
        st = input('[enter]')

def exam():
        clear()
        print('this is exam mode');


while 1:
    clear()
    print("------------------------------------")
    print("welcome to lexical learning machine!")
    print("------------------------------------")

    st = input("you want to: (search, train, exam)\n")

    operator = {'search': search, 'train': train, 'exam': exam, '': print}

    operator[st]()
