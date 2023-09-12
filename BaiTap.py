# bài tập thứ 1
so1 = int(input("Moi ban nhap so nguyen thu 1: "))
so2 = int(input("Moi ban nhap so nguyen thu 2: "))
SumNguyen = so1 + so2

print("Tong hai so nguyen la: ",SumNguyen)
# bài tập thứ 2

so1 = input("Moi ban nhap so nguyen thu 1: ")
so2 = input("Moi ban nhap so nguyen thu 2: ")

try:
    thu1 = int(so1)
    thu2 = int(so2)
    tong = thu1 + thu2
    print("tong hai so nguyen la: ", tong)
except:
    print("dinh dang dau vao khong hop le!")

# bài tập thứ 3

ten = input('Mời bạn điền tên của bạn: ')
print('Xin','chào!','Tôi','tên','là',ten,sep = '--')

# bài tập thứ 4
# "Oct(): là dùng để đổi 1 số nguyên bất kỳ sang 1 số bát phân"
# 25 | 8
#  1 | 3 | 8
#      3 | 0 
# => 31(8)
soThapPhan = int(input())
print('So thap phan %d trong he bat phan la %o' % (soThapPhan, soThapPhan)) 

# cách 2
P1 = int(input("Input một số hệ thâp phân:"))
P2 = oct(P1)[2:]
print('So thap phan %d trong he bat phan la' % (P1), P2)


# Bài tập thứ 5

P1 = input("Input một số hệ thâp phân:")
try:
    soThapPhan = int(P1)
    P2 = oct(soThapPhan)[2:]
    print('So thap phan %d trong he bat phan la' % (soThapPhan), P2)
except:
    print('dinh dang dau vao khong hop le!')

# Bài tập thứ 6
# làm tròn đến n chữ số 
giaTriA = float(input())
giaTriB = int(input())
print('Dùng format: {0:.{1}f}'.format(giaTriA,giaTriB))

# nó chỉ làm tròn để chữ số mà nó có
formatNum = round(giaTriA,giaTriB)
print('Dùng round: ', formatNum)

# bài tập 7
# Cách 1:
gtA = input()
gtB = input()
try:
    soThapPhanA = float(gtA)
    soThapPhanB = int(gtB)
    print('Dùng format: {0:.{1}f}'.format(soThapPhanA,soThapPhanB))
except:
    print('dinh dang dau vao khong hop le!')

# Cách 2: (đỡ tốn tài nguyên hơn)
gtA2 = input()
gtB2 = input()
flag = False
try:
    soThapPhanA2 = float(gtA2)
    soThapPhanB2 = int(gtB2)
    flag = True
except:
    print('dinh dang dau vao khong hop le!')

if flag:
    print('Dùng format: {0:.{1}f}'.format(soThapPhanA2,soThapPhanB2))


# Bài 8:

my_list=input().split()

my_list=[int(x) for x in my_list]

print(sum(my_list))

#Nhap dong du lieu chua day gia tri tu ban phim
dayGiaTri = input()

#Su dung ham split() de cat day gia tri thanh cac chuoi con
danhSachGiaTri = dayGiaTri.split()

#Su dung ham map() de thuc hien viec chuyen cac chuoi con sang kieu so nguyen
danhSachSo = map(int, danhSachGiaTri)

#Su dung ham sum() de tinh tong day so
tongDaySo = sum(danhSachSo)

#In ket qua ra man hinh
print(tongDaySo)



