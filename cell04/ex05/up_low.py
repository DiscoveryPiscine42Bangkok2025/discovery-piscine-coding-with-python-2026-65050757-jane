str = input("")
str_changed = ""

for chr in str:
    if(chr.isupper()): 
        str_changed += chr.lower()
    else:
        str_changed += chr.upper()

print(str_changed)