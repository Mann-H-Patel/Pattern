def Pattern_Print(M):
    num = 1
    for i in range(1, M+1):
        for k in range(M - i):
            print(" ", end="")

        for j in range(1, i+1):
            print(num, " ", end="")
            num+=1
        print("")    

A = int(input("Enter The Number => "))

Pattern_Print(A)
