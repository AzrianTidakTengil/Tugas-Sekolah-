def outer(ha):
    def inner():
        print("yooo,", ha)
    inner()

outer("meeeee")
