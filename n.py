# Diemtoan = float(input("nhap diem toan"))
# Diemvan = float(input('nhap diem van'))
# Diemanh = float(input('nhap diem anh'))
# n = (Diemanh + Diemtoan + Diemvan)/3
# print (n)
# if n>8:
#     print ('hoc sinh gioi')
# elif n>7: 
#     print ('hoc sinh kha')
# elif 6 <= n <= 7:
#     print ('hoc sinh trung binh kha')
# else:
#     print ('hoc sinh trung binh')
# n = float(input('nhap mot so bat ki '))
# print (n)
# if n%2 == 0:
#     print('so chan')
# else:
#     print('so le')
# % chia lay du 
# / chia binh thuong 
# // chia lay phan nguyen 
# control + ? : boi den va disable 
# lenh vong lap: for va while

# import math 
# i = input('nhap mot so bat ki ')
# x = i + 1
# for i in range (1,x,1):
#     if 

# float: so thuc 
# int: so nguyen
# tim tong day so 

# import math 
# x = int(input())
# sum = 0
# for i in range (1,x+1,1): 
#     sum += i
# print(sum)

# import math
# n = int(input())
# i = 1 
# tong = 0
# while i <= n: 
#     tong += i
#     i += 1 
# print(tong)



# check co phai so nguyen to ko 
# import math 
# n = int(input())
# check = True 
# for i in range (2, math.isqrt(n) + 1): 
#     if n % i == 0:
#         check = False 
# if check == True:
#     print('n la so nguyen to')
# else: 
#     print('n ko phai la so nguyen to')



# check so chinh phuong 

# import math 
# n = int(input ('nhap mot so bat ki '))
# i = math.sqrt(n)
# print (i)
# print (n, 'la binh phuong cua' ,i )
# if int(i) == i:
#     print ('day la so chinh phuong')
# else:
#     print ('day ko phai la so chinh phuong')

# x = float(input('Nhập điểm Toán '))
# y = float(input('Nhập điểm Văn '))
# z = float(input('Nhập điểm Anh '))
# i = ( x + y )*2 + z 
# print(i)

# x = float(input(' Nhập số thứ nhất '))
# y = float(input(' Nhập số thứ hai '))
# if x>y + x%y == 0: 
#     print( y, 'là ước của', x )
# elif x<y + y%x == 0:
#     print( x, 'là ước của', y)
# elif x>y + x%y != 0:
#     print(y, 'không phải ước của', x )
# elif x<y + y%x != 0:
#     print( x, ' không phải ước của ', y )

# a = '8.9' 
# print(type(a))


# x = int(input( 'nhap mot so bat ki '))
# sum = 0
# for i in range (1,x+1,1):
#     sum += i 
# print(sum)

# x = int(input(' nhap mot so bat ki '))
# i = 1 
# sum = 0 
# while i <= x :
#     sum += i
#     i += 1 
# print(sum)

# chuyen kí tư thanh số 
# print(ord('!'))
# print(ord('a'))

# chuyen so thanh ki tự 
# print(chr(97))

# check xem so hay ki tu: 
# import math
# print('ab'.isdigit())
# print('97'.isdigit())

# tính tổng n số thỏa mãn sau:
#nếu n lẻ thì sum = 1 + 3 + 5 + .. + n
#nếu n chẵn thì sum = 2 + 4 + 6 + .. + n

# x = int(input('nhap mot so bat ki '))
# sum = 0
# if x % 2 == 0:
#     for i in range(0,x+1,2):
#         sum += i
# else:
#     for i in range(1,x+1,2):
#         sum += i

# print(sum)

# dùng hàm bậc: 
# import math 
# isqrt: phần nguyên của căn bậc 2 
# sqrt: raw căn bậc 2
# print(pow(3,2))    ----- 3 mũ 2


# import math
# a = input('nhap so thu nhat ')
# b = input('nhap so thu hai ')
# if a.isdigit() and b.isdigit() : 
#     i = input('nhap 1 trong 4 phep tinh + ; - ; * ; /: ')
#     if i == '+':
#         c = int(a) + int(b) 
#         print(c)
#     elif i == '-': 
#         c = int(a) - int(b)
#         print(c)
#     elif i == '*': 
#         c = int(a) * int(b)
#         print(c)
#     elif i == '/':
#         if b != 0:
#             c = int(a)/int(b)
#             print(c)
#         else:
#             print('loi he thong')
#             print('nhap lai', b )
#             continue 

# else:
#     print('loi he thong ')



# x = int(input('Nhap so thu nhat '))
# y= int(input('Nhap so thu hai '))
# z= int(input('Nhap so thu ba '))
# g= int(input('Nhap so thu tu '))
# if x>y and x>z and x>g: 
#     print(x,'la so lon nhat')
# elif y>x and y>z and y>g: 
#     print(y,'la so lon nhat')
# elif z>x and z>y and z>g: 
#     print(z,'la so lon nhat')
# elif g>x and g>y and g>z: 
#     print(g,'la so lon nhat')


# thiếu trường hợp x=y or x=z or x=g .... 

l = [1,2,3,4,5,6]

i = 0 
max_l = l[0]
while i < len(l):
    if l[i] > max_l:
        max_l = l[i]
    i += 1 

print(max_l)