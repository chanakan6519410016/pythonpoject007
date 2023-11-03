#Primutive Data Type
#Number , Boolean , String

# Non-Primitive Data Type / Collection / Data Structure ข้อมูลชนิดไม่พื้นฐาน
#List , Tuple , Set , Dictionary

#Data type จะเอามาใช้กับการเขียนโปรแกรมในเรื่องของ ตัวแปร พารามิเตอร์ ฟังก์ชัน เมธอด

# --- List คือ ข้อมูลหลายข้อมูล ซ้ำกันได้ คนละชนิดได้ แก้ไขได้ เป็นข้อมูลมีลำดับ มี index กำกับ 
        #   0    1   2     3    4         5
my_list1 = [10, 20, True, 10, 'SAU', [20, 'IoT']]
        #   6    5   4    3     2         1       ติด -

# --- Tuple คือ ข้อมูลหลายข้อมูล คนละชนิดได้ ซ้ำก็ได้ มีลำดับ แต่แก้ไขไม่ได้ เพิ่ม/ลบไม่ได้
        #    0   1     2    3    4       5
my_tuple1 = (10, 20, True, 10, 'SAU',(20, 'IoT'))
        #   6    5    4    3     2       1       ติด -

# --- Set คือ ข้อมูลหลายข้อมูล คนละชนิดได้ ซ้ำไม่ได้(หากซ้ำถือว่าเป็นตัวเดียวกัน) ไม่มีลำดับ และแก้ไขไม่ได้ แต่เพิ่ม/ลบได้
# set,list อยู่ภายใน set ไม่ได้ แต่ tuple,sting,number,boolean อยู่ใน Set ได้
my_set1 = {10, 20, True, 10, 'SAU',(20, 'IoT')}

# ******** Dictionary คือ ข้อมูลหลายข้อมูลที่เป็น key:value แก้ไขได้ ไม่มี index กำกับ ไม่มีลำดับ ซ้ำได้
# key เป็น String/Integer ส่วน value เป็นอะไรก็ได้ (number,string,boolean,list,tuple,set,dictionary)
my_diction1 = {'name':'mod', 'age':30, 555:999, 'flag':True, 'wow':[10,20,30]}