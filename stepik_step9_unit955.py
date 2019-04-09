def modify_list(l):
    for i in range(len(l)-1,-1,-1):
        if l[i] % 2 != 0:
            l.remove(l[i])
        else:
            l[i] = int(l[i] / 2)