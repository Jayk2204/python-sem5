# wap to read and write binary file
f1=open("file1.bin","wb+")

data=b"This is Binary Data.\n Second line of binary"
f1.write(data)
data1=f1.readline()
data2=f1.readline()
print("Data is",data1,"  ",data2)

