def name_cat(lst):
    k = ""
    counter = 0
    while counter <= len(lst) - 1:
        if counter == 0:
            k += lst[counter]
        else:
            k += f", {lst[counter]}"
        counter += 1
    return k
