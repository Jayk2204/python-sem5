#wap to count no of Lines,words and Characters in a File.
#Count number of characters

f=open("f3.txt","r")
str1=f.read()

char_count = len(str1)
word_count = len(str1.split())
line_count = len(str1.splitlines())


print(str1)
print(char_count)
print(word_count)
print(line_count)

f.close()

