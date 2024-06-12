str=input("enter the sentence")
samplefile=open('c:/Users/DAKSHA RAWAT/demo.txt','w')
print(str,file=samplefile)
with open('c:/Users/DAKSHA RAWAT/demo.txt', 'r') as samplefile:
    content = samplefile.read()
    print(content)



