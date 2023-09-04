so1 = input("Moi ban nhap so nguyen thu 1: ")
so2 = input("Moi ban nhap so nguyen thu 2: ")

try:
    thu1 = int(so1)
    thu2 = int(so2)
    tong = thu1 + thu2
    print("tong hai so nguyen la: ", tong)
except:
    print("dinh dang dau vao khong hop le!")