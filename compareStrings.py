def compareStrings(str1, str2):
    # splitting the string on period symbol
    arr1 = str1.split('.')
    arr2 = str2.split('.')
    for i in range(0, len(arr1)):
        # only corresponding integers are compared
        a = int(arr1[i])
        b = int(arr2[i])
        if(a == b):
            continue
        elif(a > b):
            return True
        else:
            return False
    return True
