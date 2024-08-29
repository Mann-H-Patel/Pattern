def Pattern_Print(M):  
    for i in range(1, M+1):
        for j in range(1, i+1):
            if (i+j)%2 == 0:
                print(1, end="")
            else:
                print(0, end="")    
        print()    

A = int(input("Enter The Number => "))

Pattern_Print(A)
