from gmail import *
from random import *

a = "Em xin nghi om vi"
b = "Em xin nghi viec vi"
c = "Em xin phep di choi vi"
template_list = [a, b, c]
choice(template_list)
a1 = " bi om"
b1 = " em thich"
reason_list = [a1, b1]
choice(reason_list)
# print(choice(template_list)+choice(reason_list))
gmail = GMail('c4e.13.baoluong@gmail.com','pvcb@123')

msg = Message('Don xin nghi viec_random',to='c4e13.lab.huynq@gmail.com',html=choice(template_list)+choice(reason_list))

gmail.send(msg)
