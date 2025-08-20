f1=open("file7.txt","a+")
while True:
    print("Do You Want to enter a line in file(y/n)")
    ans=input()
    ans=ans.lower()
    if ans=='y':
        print("Enter a Line")
        line=input()
        f1.write(line)
        f1.write("\n")
    else:
        break
f1.seek(0,0)

str1=f1.read()

char_count = len(str1)
word_count = len(str1.split())
line_count = len(str1.splitlines())


print(str1)
print(char_count)
print(word_count)
print(line_count)

f1.close()

