# r la read
# w la write (xoa het va ghi lai)
# a la append (ghi noi dung cu va ghi them cai moi)



# lam file text trong notepad 

# Đường dẫn
import random
_PATH = 'D:/ailatrieuphu'

# Tên file
CAU_HOI_FILE_NAME = 'cauhoi.txt'
CAU_TRA_LOI_FILE_NAME = 'cautraloi.txt'
GIAI_THUONG_FILE_NAME = 'giaithuong.txt'

# Đường dẫn đến file
CAU_HOI = _PATH + '/'+ CAU_HOI_FILE_NAME
CAU_TRA_LOI = _PATH + '/' + CAU_TRA_LOI_FILE_NAME
GIAI_THUONG = _PATH + '/' + GIAI_THUONG_FILE_NAME

# Đọc file
with open(CAU_HOI, 'r' ,encoding = 'utf-8') as f:
    CAU_HOI_LIST = f.readlines()
with open(CAU_TRA_LOI, 'r',encoding = 'utf-8') as f:
    CAU_TRA_LOI_LIST = f.readlines()
with open(GIAI_THUONG, 'r' ,encoding = 'utf-8') as f:
    GIAI_THUONG_LIST = f.readlines()

# VI_TRI = random.randint(1,19)
VI_TRI = 0
# print(VI_TRI)
# In câu hỏi
name = input('Nhập vào tên thí sinh: ')
print("Chào mừng", name ,"đã đến với chương trình AI LÀ TRIỆU PHÚ")
cont = True


while cont == True:
    print("Câu hỏi thứ", VI_TRI,":",CAU_HOI_LIST[VI_TRI])
    user_answer = input('Nhập vào câu trả lời: ') 
    if user_answer.strip().lower() == (CAU_TRA_LOI_LIST[VI_TRI]).strip().lower():
        print ('Chính xác')
        if VI_TRI == 14:
            print("Xin chúc mừng, bạn đã trả lời đúng toàn bộ câu hỏi")
            print("Cảm ơn bạn vì đã tham gia chương trình, hẹn gặp lại")
            break
        print('Xin chúc mừng, bạn đã nhận được:',GIAI_THUONG_LIST[VI_TRI])
        VI_TRI += 1
        g = input('Bạn có muốn tiếp tục không: Có/Không: ')
        if g == "Có":
            cont = True
        elif g == "Không":
            cont = False 
            print('Bạn sẽ ra về với:', GIAI_THUONG_LIST[VI_TRI - 1])
            print('Trò chơi kết thúc, hẹn gặp lại')
            break 
        else:
            print('Câu trả lời không xác định, vui lòng nhập lại')
            g = input('Bạn có muốn tiếp tục không: Có/Không ')

    else:
        print ('Sai')
        print ('Câu trả lời đúng là: ', CAU_TRA_LOI_LIST[VI_TRI])
        if VI_TRI == 0:
            print ('Vì bạn sai câu hỏi đầu tiên nên sẽ không có phần thưởng')
            print('Hẹn gặp lại lần sau')
            cont = False 
            break
        else:
            print ('Bạn nhận được phần thưởng là 100.000 đồng')
            print('Hẹn gặp lại lần sau')
            cont = False 
            break 





# if (1 in QUYEN_TRO_GIUP) & (2 in QUYEN_TRO_GIUP):
#         quyen_tro_giup = int(input("""
#         Ban co muon nhan duoc quyen tro giup duoi day:
#             1. 50/50
#             2. Khao sat khan gia tu truong quay
#             3. Khong can tro giup
#         """))
#         if quyen_tro_giup == 1:
#             print("Ban da chon quyen tro giup so 1.")
#             QUYEN_TRO_GIUP.remove(1)
#         elif quyen_tro_giup == 2:
#             print("Ban da chon quyen tro giup so 2.")
#             QUYEN_TRO_GIUP.remove(2)
#         else:
#             print("Ban da khong chon quyen tro giup nao.")
#             pass
#     elif (2 in QUYEN_TRO_GIUP):
#         quyen_tro_giup = int(input("""
#         Ban co muon nhan duoc quyen tro giup duoi day:
#             2. Khao sat khan gia tu truong quay
#             3. Khong can tro giup
#         """))
#         if quyen_tro_giup == 2:
#             print("Ban da chon quyen tro giup so 2.")
#             QUYEN_TRO_GIUP.remove(2)
#         else:
#             print("Ban da khong chon quyen tro giup nao.")
#             pass
#     elif (1 in QUYEN_TRO_GIUP):
#         quyen_tro_giup = int(input("""
#         Ban co muon nhan duoc quyen tro giup duoi day:
#             1. 50/50
#             3. Khong can tro giup
#         """))
#         if quyen_tro_giup == 1:
#             print("Ban da chon quyen tro giup so 1.")
#             QUYEN_TRO_GIUP.remove(1)
#         else:
#             print("Ban da khong chon quyen tro giup nao.")
#             pass
#     elif len(QUYEN_TRO_GIUP) == 0:
#         print("Ban khong con quyen tro giup nao nua!")
#     else:
#         print("Ban da khong chon quyen tro giup nao.")
#         pass


# if quyen_tro_giup == 1:
#             print("Ban da chon quyen tro giup so 1.")
#             dap_an_1 = CAU_TRA_LOI_LIST_ADJUST[VI_TRI_CAU_HOI]
#             dap_an_2 = chr(random.randint(65,68))
#             while dap_an_2.lower() == dap_an_1.lower():
#                 dap_an_2 = chr(random.randint(65,68))
           
#             dap_an_list = [dap_an_1, dap_an_2]
#             dap_an_1_display = random.randint(0,1)
#             dap_an_2_display = 1 - dap_an_1_display
#             print('{} --- {}'.format(dap_an_list[dap_an_1_display], dap_an_list[dap_an_2_display]))
#             QUYEN_TRO_GIUP.remove(1)






#    CAU_TRA_LOI_LIST_ADJUST.append(i.strip())




# GIAI_THUONG_LIST_ADJUST = []
# for j in GIAI_THUONG_LIST:
#     GIAI_THUONG_LIST_ADJUST.append(j.strip())

# CAU_HOI_DA_RA = []
# SO_THU_TU = 0
# for i in range(5):
#     print("Cau hoi thu {}".format(SO_THU_TU + 1))
#     VI_TRI_CAU_HOI = random.randint(1, 18)

#     while VI_TRI_CAU_HOI in CAU_HOI_DA_RA:
#         VI_TRI_CAU_HOI = random.randint(1, 18)

#     print(BO_CAU_HOI_LIST[VI_TRI_CAU_HOI])
#     user_answer = input("Nhap vao cau tra loi cua ban: ")
#     if user_answer.lower() == (CAU_TRA_LOI_LIST_ADJUST[VI_TRI_CAU_HOI]).lower():
#         print("""
#     Xin chuc mung, ban da tra loi dung!
#     ---> Giai thuong cua ban luc nay la {}d !!!
#                 """.format(GIAI_THUONG_LIST_ADJUST[SO_THU_TU]))

#         if SO_THU_TU == 4:
#             print("Chuc mung ban da hoan thanh tro choi voi tong giai thuong la {} dong!!!".format(GIAI_THUONG_LIST_ADJUST[SO_THU_TU]))
#         else:
#             SO_THU_TU += 1
#             CHOI_TIEP = input("Ban co muon tiep tuc?  (Yes/No): ")
#             if CHOI_TIEP.lower() == 'yes':
#                 CAU_HOI_DA_RA.append(VI_TRI_CAU_HOI)
#                 continue
#             else:
#                 print("Chuc mung ban da hoan thanh tro choi voi tong giai thuong la {} dong!!!".format(GIAI_THUONG_LIST_ADJUST[SO_THU_TU - 1]))
#                 break
#     else:
#         if SO_THU_TU == 0:
#             print("""
#         That dang tiec, ban da tra loi sai cau hoi nay!
#         ---> Vi sai cau hoi dau tien, ban khong nhan duoc giai thuong!
#                   """)
#             break
#         else:
#             print("""
#         That dang tiec, ban da tra loi sai cau hoi nay!
#         ---> Giai thuong cua ban luc nay tro ve {} dong !!!
#                     """.format(GIAI_THUONG_LIST_ADJUST[0]))
#             break