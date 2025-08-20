#wap two integers and a float to a binary file
import struct
with open('numbers.bin','wb')as f:
    f.write(struct.pack('iif',42,256,3.14))
#Read them Back
with open('numbers.bin','rb')as f:
    data=f.read()
    a,b,c=struct.unpack('iif',data)
    
print(a,b,c)