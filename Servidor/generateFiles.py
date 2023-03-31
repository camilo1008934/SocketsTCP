file=open('100MB.txt','w')
file.write('A'*(100*1024*1024))

file1=open('250MB.txt','w')
file1.write('B'*(250*1024*1024))
