def isValid ():
    allValid = True
    errorCodes = []
    input = open('input.txt', 'r')
    lines = input.readlines()

    for i, line in enumerate (lines):
        if i == 0:
            continue
        else:
            if line.split(" ")[1] == "false":
                errorCodes.append(line.split(" ")[2])
    
    if not errorCodes:
        print("Yes")
    else:
        print("No")
        for err in errorCodes:
            if err != errorCodes[-1]:
                print(err, end=" ")
            else:
                print(err, end="")

isValid()
  