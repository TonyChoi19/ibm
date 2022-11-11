def main():
    size_avail = []
    req = []

    num_shirt = input()
    size_shirt = input()

    size_shirt_list = size_shirt.split(" ")
    for i in range(int(num_shirt)):
        size_avail.append(size_shirt_list[i])

    requests = input()
    size_req = input()

    size_req_list = size_req.split(" ")
    for i in range(int(requests)):
        req.append(size_req_list[i])

    if int(num_shirt) >= int(requests):
        size_avail = rank(size_avail) 
        req = rank(req) 

        if len(size_avail[0]) > 0:
            if len(req[0]) > 0:
                for i in size_avail[0].copy():
                    for j in req[0].copy():
                        if len(i) <= len(j):
                            size_avail[0].remove(i)
                            req[0].remove(j)
        
        if len(size_avail[1])>0:
            if len(req[0]) > 0:
                for j in req[0].copy():
                    if len(size_avail[1]) != 0:
                        size_avail[1].remove(size_avail[1][0])
                        req[0].remove(j)

            if len(req[1]) > 0:
                    for j in req[1].copy():
                        if len(size_avail[1]) != 0:
                            size_avail[1].remove(size_avail[1][0])
                            req[1].remove(j)

        if len(size_avail[2])>0:
            if len(req[0]) > 0:
                for j in req[0].copy():
                    if len(size_avail[2]) != 0:
                        size_avail[2].remove(size_avail[2][0])
                        req[0].remove(j)
            
            if len(req[1]) > 0:
                for j in req[1].copy():
                    if len(size_avail[2]) != 0:
                        size_avail[2].remove(size_avail[2][0])
                        req[1].remove(j)

            if len(req[2]) > 0:           
                for i in size_avail[2].copy():
                    for j in req[2].copy():
                        if len(i) >= len(j):
                            size_avail[2].remove(i)
                            req[2].remove(j)
                            break
    
        if len(req[0]) == 0 and len(req[1]) == 0 and len(req[2]) == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")



def rank(list):
    S =[]
    M = []
    L = []
    for i in list:
        if 'S' in i:
            S.append(i)
        if 'M' in i:
            M.append(i)
        if 'L' in i:
            L.append(i)


    result =[[],[],[]]

    for i in S:
        result[0].append(i)
    result[0].sort()
    
    for i in M:
        result[1].append(i)
    result[1].sort()

    for i in L:
        result[2].append(i)
    result[2].sort()
    return result



main()
    
