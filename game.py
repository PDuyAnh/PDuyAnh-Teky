
import random
_PATH = 'D:/ailatrieuphu'


CAU_HOI_FILE_NAME = 'cauhoi.txt'
CAU_TRA_LOI_FILE_NAME = 'cautraloi.txt'
GIAI_THUONG_FILE_NAME = 'giaithuong.txt'


CAU_HOI = _PATH + '/'+ CAU_HOI_FILE_NAME
CAU_TRA_LOI = _PATH + '/' + CAU_TRA_LOI_FILE_NAME
GIAI_THUONG = _PATH + '/' + GIAI_THUONG_FILE_NAME


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
