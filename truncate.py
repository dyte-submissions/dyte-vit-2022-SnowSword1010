def truncate(str):
    dependencyName = ""
    dependencyVersion = ""
    idx = 0
    arr = []
    # part before '@' represents dependencyName
    while(str[idx] != '@'):
        dependencyName += str[idx]
        idx+=1

    idx+=1
    # part after '@' represents dependencyVersion
    dependencyVersion += str[idx:]
    arr.append(dependencyName)
    arr.append(dependencyVersion)
    return arr