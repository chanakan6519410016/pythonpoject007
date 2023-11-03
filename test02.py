#String ทุกตัวจะมี index number กำกับ 0-13
        #01234567890123
infoA = 'Hello SAU 2023'
        #43210987654321 ติด -

print(infoA[6]) # S
print(infoA[-8]) # S

# เข้าถึงตัวอักษรหลายๆตัวใน String เราจะใช้วิธี Slicing ด้วย index number ต้องการ[ตัวไหน:ก่อนถึงตัวไหน]
# SAU
print(infoA[6:9])
print(infoA[-8:-5])

# o SAU 20
print(infoA[4:12])

#String Method 
#ขึ้นต้นด้วย is คือการพิสูจน์ True/False
print( infoA.upper() )
print( infoA.lower() )
print( infoA.capitalize() )
print( infoA.title() )
print( infoA.count('l') )
print( infoA.isdigit() )
print( infoA.islower() )
infoB = infoA.replace('SAU', 'IoT')
print(infoA)
print(infoB)
print(infoB.replace('Hello' ,'Hi...'))

#String Function
print( len(infoA) )


print('SAU',35) # SAU 35
print('SAU',35,end='') #ไม่ขึ้นบรรทัดใหม่ ใช้ end
print('SAU'+str(35)) #SAU35
print('SAU',35,sep='') #SAU35
print('20','02','2023',sep='/')
print('20','มกราคม',2023,sep='-')