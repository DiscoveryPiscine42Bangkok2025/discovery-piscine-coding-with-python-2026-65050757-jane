#!/usr/bin/env python3
#รับ argument สองตัว แล้วสร้างลิสต์ตัวเลขในช่วงนั้น
import sys

if len(sys.argv) - 1 > 0:
    first_number = int(sys.argv[1])
    second_number = int(sys.argv[2]) 
    arr = []

    for number in range(first_number, second_number + 1):
        arr.append(number)
    print(arr)    
else:
    print("none")