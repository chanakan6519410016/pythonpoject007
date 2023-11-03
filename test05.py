# --- Tuple คือ ข้อมูลหลายข้อมูล คนละชนิดได้ ซ้ำก็ได้ มีลำดับ แต่แก้ไขไม่ได้ เพิ่ม/ลบไม่ได้
        #    0   1     2    3    4       5
my_tuple1 = (10, 20, True, 10, 'SAU',(20, 'IoT'))
        #   6    5    4    3     2       1       ติด -
# การเข้าถึงข้อมูลใน Tupleเพื่อเอาข้อมูลมาใช้ หรือแก้ไขค่าข้อมูลให้มันใหม่
# เข้าถึงแต่ละข้อมูล
print(my_tuple1[4]) # SAU
print(my_tuple1[-2]) # SAU
print(my_tuple1[5]) # (20,'IoT')
print(my_tuple1[-1]) # (20,'IoT')
print(my_tuple1[5][1]) # IoT
print(my_tuple1[-1][-1]) # IoT

# เข้าถึงทีละหลายข้อมูล : Slicing ผลลัพธ์จะเป็น Tuple ไม่มีข้างหน้า : คือเอาตั้งแต่หน้าสุด ไม่มีข้างหลัง : คือเอาถึงหลังสุด
print(my_tuple1[1:4] ) # 20, True, 10
print(my_tuple1[3:] ) # 10,'SAU', (20,'IoT')
print(my_tuple1[:3] ) # 10, 20, True

# เข้าถึงทุกข้อมูล ทุกข้อมูลจะถูกเก็บข้างหน้า in
for info in my_tuple1 :
    print(info, end=', ')

print()

# หากอยากจะแก้ข้อมูลใน Tuple ก็ทำได้แต่ต้องทำอ้อมๆ
my_list = list( my_tuple1 )
my_list[4] = 'IoT'
my_tuple1 = tuple (my_list)
print(my_tuple1)

#Tuple Method
# นับจำนวนข้อมูล
print(my_tuple1.count(10) ) # 2
# บอกว่าอยู่ลำดับ index เบอร์ไหน
print(my_tuple1.index(True) )


# Tuple Function -> len(), min()ต้องเป็นชนิดเดียวกันหมด, max()ต้องเป็นชนิดเดียวกันหมด ยกเว้น number กับ boolean เทียบกันได้
my_tuple2 = [10, 20, 10, 30, True]
print(len(my_tuple2))
print(min(my_tuple2))
print(max(my_tuple2))