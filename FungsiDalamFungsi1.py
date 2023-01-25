def foo():
    name = "ayam"

    def bar():
        nonlocal name
        name = 'Ayam tidak bulat'

        print(name)

    bar()

    print(name)

foo()
