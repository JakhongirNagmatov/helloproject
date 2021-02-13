word=input("So'z kiriting: ")
count=0
for letter in word:
    if letter==" " :
        continue
    count+=1
print("Siz kiritgan so'zning harflar soni " + str(count) + "ta")
