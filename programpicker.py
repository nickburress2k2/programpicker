#Picking programs

import os

#def getInput(arg):

    #switcher = {
        #'payrate': import payrate
        #'first program': import firstprogram
#    }

    #return switcher.get(arg, "Invalid choices")

if __name__ == "__main__":
    inp = input('Which program would you like to run? ')
    #getInput(inp)

    if (inp == 'payrate') or (inp == 'Payrate'):
        import payrate
    elif (inp == 'first program') or (inp == 'First Program') or (inp == 'First program'):
        import firstprog
    else:
        print("No such program exists. Try again.")


    os.system("pause")
