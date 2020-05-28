def pickingNumbers(a):
    set_list = set(a)
    max_len = 1
    for i in set_list:
        count_i = a.count(i)
        if (count_i >= 1) and (i+1 in set_list):
            if count_i + a.count(i+1) > max_len:
                max_len =  count_i + a.count(i+1)
        elif a.count(i) > 1 :
            if count_i > max_len:
                max_len = count_i

    return max_len
        
print(pickingNumbers([98, 3, 99, 1, 97, 2]))