from PIL import Image as im 
text = "Name:Tom Account number: 6522 2863 9100 2525 Balance: 10,00,000 Pin: 8787 Account: Savings"
n = len(text)
bin_text = []
for i in  range(len(text)):
    bin_text.append(format(ord(text[i]),'08b'))
cover = im.open('spidy.jpg')
cover = cover.resize([n*3,n*3]) 
pixelc = cover.load()

def change(pix,binary):
    p=pix
    p=list(p)
    for i in range(len(binary)):
        if(binary[i]=='1'):
            if(p[i]%2==0):
                p[i]-=1
        elif(binary[i]=='0'):
            if(p[i]%2!=0):
                p[i]-=1
    return (p[0],p[1],p[2])

encoded = im.new(cover.mode,cover.size)
enc = encoded.load()

inc=0
for i in range(cover.size[0]):
    if(i<n):
        if(inc==len(bin_text)):
            break
        st=bin_text[inc]
        k=0
        for j in range(cover.size[1]):
            enc[i,j]=pixelc[i,j]
            if(j<3):
                enc[i,j] = change(pixelc[i,j],st[k:k+3])     
                k+=3
        inc+=1
    else:
        for j in range(cover.size[1]):
            enc[i,j]=pixelc[i,j]

encoded.save('Encoded.bmp')
