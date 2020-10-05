from PIL import Image as im
encoded = im.open('Encoded.bmp')
enc = encoded.load()

n1=encoded.size[0]
n=int(n1/3)

def check(p):
    st=""
    for i in range(len(p)):
        if(p[i]%2==0):
            st+='0'
        else:
            st+='1'
    return st

binn=[]
dec_text=""
for i in range(n):
    data=""
    for j in range(3):
        data+=check(list(enc[i,j]))
    data=data[:len(data)-1]
    binn.append(data)
    dec_text+=chr(int(data,2))
print(dec_text)