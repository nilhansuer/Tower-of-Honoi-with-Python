print("tower of honoi:")

def printMove(fr, to):
    print("move from", str(fr), "to", str(to))

def Towers(n, fr, to, spare):
    if (n==1):
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
Towers(3, 'f', 't', 's')

print('\n'+"another alternative for tower of honoi:")

#2nd alternative for tower of honoi

def move(n, start, temp, final):
    if(n>0):
        move(n-1, start, final, temp)
        print("Moved disk", n, "from rod", start, "to rod", final)
        move(n-1, temp, start, final)
move(3, 'f', 's', 't')


#3rd alternativefor tower of honoi:

# removed tail recursion

#def move_tail_removed(n, start, temp, final):
    #if(n>0):
        #move_tail_removed(n-1, start, final, temp)
        #print("Moved disk", n, "from rod", start, "to rod", final)
        #n-=1
        #start, temp = temp, start
#move(3, 'f', 's', 't')
