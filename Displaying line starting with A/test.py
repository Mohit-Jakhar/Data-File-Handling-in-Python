def letterA():
      file=open("sample.txt","r")
      line=file.readline()
      while line:
            if line[0]=="A":
                  print(line)
            line=file.readline()
      file.close()
