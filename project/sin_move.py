import math
import os

factor(key)
factor2(key)
rand_gen_x(p)
rand_gen_y(p)

def main(argc, argv[]):
    key = 70
    fil = open("test.txt", 'r+')
    tmp = ""
    num_lines = 0
    longest_line = 0
    while (  ):
    # need help for the python3 version of input from file
        num_lines++
        if len(tmp>longest_line):
            longest_line = len(tmp)
        
    #what is char ** board?

    #need help since there are no pointers
    # also what is seekg and beg
    fil = 
    curr_line=0
    
    while( ):
    # need help for the python3 version of input from file
        board[curr_line] = some[longest_line]
        for i in longes_line:
            board[curr_line][i] ='o'
        for i in len(tmp):
            board[curr_line][i] = tmp[i]
        
        curr_line++

    for i in range(num_lines):
        for j in range(longest_line):
            print(board[i][j], end='')

    print("  ",end ='')

    tmp_key = key
    while tmp_key != 0:
        tmp_fac = factor(tmp_key)
        for i in range(longest_line):
            for j in range(longest_line):
                tmp_char='o'
                tmp_char = board[i][j]
                x_pos = (longest_line-1)*rand_gen_x(tmp_fact*j)
                print(x_pos+ " ")
                y_pos = num_lines*rand_gen_y(tmp_fac*j)
                print(y_pos + " " + tmp_fac, end ="")
                board[i][j] = board[y_pos][x_pos]
                board[y_pos][x_pos] = tmp_char
    
    for i in range(num_lines):
        for j in range(longest_line):
            print(board[i][j], end ="")
        print(" ", end="")

    print("div", end = "")
    tmp_key = key
    while(tmp_key != 1):
        tmp_fac = factor2(tmp_key)
        i = num_lines-1
        # I converted the following for loops for while loops
        while i >=0:
            j = longest_line-1
            while j >=0:
                tmp_char = board[i][j]
                x_pos = (longest_line-1)*rand_gen_x(tmp_fac*j)
                print(x_pos + " ")
                y_pos = num_lines*rand_gen_y(tmp_fac*j)
                print(y_pos+" "+tmp_fac+" ")
                board[i][j] = board[y_pos][x_pos]
                board[y_pos][x_pos] = tmp_char
                j-=1
            i-=1
    for i in range(num_lines):
        for j in range(longest_line):
            print(board[i][j])
        print(" ", end="")
    print(" ", end= "")

    print("it works")

def factor2(key):
    if (key == 1):
        return 1
    i = 2 
    tmp_i = i
    tmp_key = key 
    while i<=tmp_key:
        if tmp_key%i==0:
            tmp_key = tmp_key/i
            tmp_i = i
        i++
    key = key/tmp_i
    return tmp_i

def factor(key):
    i = 2
    if key==1:
        return 1
    while i<=key:
        if key%i==0:
            key = key/i
            return i
        i++
    return 1

def rand_gen_x(p):
    w = cos(p)
    return w*w

def rand_gen_y(p):
    w = sin(p)
    return w*w
