def o():
    ms = "Local"

    def i():
        nonlocal ms

        ms = "Global"
        print("inner:", ms)

    i()
    print("outer:", ms)
    
o()
