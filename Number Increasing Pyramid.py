def Pattern_Print(M):
    for i in range(1, M+1):
        for j in range(1, i+1):
            print(j, end="")
        print()    

A = int(input("Enter The Number => "))

Pattern_Print(A)