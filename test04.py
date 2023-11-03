# --- List คือ ข้อมูลหลายข้อมูล ซ้ำกันได้ คนละชนิดได้ แก้ไขได้ เป็นข้อมูลมีลำดับ มี index กำกับ 
                                    #  0    1
        #   0    1   2     3    4         5
my_list1 = [10, 20, True, 10, 'SAU', [20, 'IoT']]
        #   6    5   4    3     2         1       ติด -
                                    #  2    1     ติด -
# การเข้าถึงข้อมูลใน List เพื่อเอาข้อมูลมาใช้ หรือแก้ไขค่าข้อมูลให้มันใหม่
# เข้าถึงแต่ละข้อมูล
print(my_list1[4]) # SAU
print(my_list1[-2]) # SAU
print(my_list1[5]) # [20,'IoT']
print(my_list1[-1]) # [20,'IoT']
print(my_list1[5][1]) # IoT
print(my_list1[-1][-1]) # IoT

# เข้าถึงทีละหลายข้อมูล : Slicing ผลลัพธ์จะเป็น List ไม่มีข้างหน้า : คือเอาตั้งแต่หน้าสุด ไม่มีข้างหลัง : คือเอาถึงหลังสุด
print(my_list1[1:4] ) # 20, True, 10
print(my_list1[3:] ) # 10,'SAU', [20,'IoT']
print(my_list1[:3] ) # 10, 20, True

# เข้าถึงทุกข้อมูล ทุกข้อมูลจะถูกเก็บข้างหน้า in
for info in my_list1 :
    print(info, end=', ')

print()

print(my_list1)
my_list1[4] = 'Thailand'
print(my_list1)

# List Method
my_list2 = [10, 20, True, 10, 'SAU', [20, 'IoT']]
#append เพิ่มข้อมูลต่อท้าย 1 ชุดใน List
my_list2.append('Wow')
print(my_list2)
my_list2.append([111,222,333])
print(my_list2)
#extend เพิ่มข้อมูลต่อท้ายหลายชุดใน List
my_list2.extend([444,555])
print(my_list2)
# เอาข้อมูลออก เอาออกตัวเดียวตัวแรกที่เจอออก จากซ้ายไปขวา
my_list2.remove(10)
my_list2.remove('SAU')
my_list2.remove([111,222,333])
print(my_list2)
# pop เอาสุดท้ายออก
my_list2.pop()
my_list2.pop()
my_list2.pop()
print(my_list2)
my_list2.pop(2) # 2 คือ index
print(my_list2)

# List Function -> len(), min()ต้องเป็นชนิดเดียวกันหมด, max()ต้องเป็นชนิดเดียวกันหมด ยกเว้น number กับ boolean เทียบกันได้
my_list3 = [10, 20, 10, 30, True]
print(len(my_list3))
print(min(my_list3))
print(max(my_list3))