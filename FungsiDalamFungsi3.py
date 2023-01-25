def f(n):
    if n == 0:
        print("Go!")
        return 
        
    print(n,",", end="")
    f(n-1)

f(10)


f(27)

#karena menggunakan hp modul time gak ada, jadi langsung full output tanpa delay 
