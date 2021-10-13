f=open("test.txt",'r')
lines=f.readlines()
for l in lines:
  print(l,end=' ')
f.close()  
