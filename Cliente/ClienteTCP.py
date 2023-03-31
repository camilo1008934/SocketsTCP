import socket, hashlib, time, os
from datetime import datetime

IP='192.168.20.58'
PORT=65000
SIZE=1024
ADDR=(IP, PORT)
FORMAT='utf-8'
date=datetime.now().strftime("%Y-%m-%d-%H-%M-%S-")
log=open(("Logs\c"+date+"log.txt"),'a')
conexiones=int(input("Ingrese el numero de conexiones: "))
clientes=[]

for i in range(conexiones+1):
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    if i!=0:
        print("Cliente "+str(i)+" listo para recibir.")
    clientes.append(client)
input("Presione enter para comenzar la recepcion...")
clientes[0].send("START".encode(FORMAT))

for i in range(1,conexiones+1):
    file=open(("ArchivosRecibidos\Cliente"+str(i)+"-Prueba-"+str(conexiones))+".txt", 'a')
    start=time.time()
    while True:
        part=clientes[i].recv(SIZE).decode(FORMAT)
        file.write(part)
        if not part:
            break
    end=time.time()
    print("Archivo del cliente "+str(i)+" recibido.")  
    file=open(("ArchivosRecibidos\Cliente"+str(i)+"-Prueba-"+str(conexiones))+".txt",'rt')
    content=file.read()
    file.seek(0,os.SEEK_END)
    log.write("Nombre del archivo: Cliente"+str(i)+"-Prueba-"+str(conexiones)+".txt\n")
    log.write("Tamano del archivo: "+str(file.tell())+" bytes\n")
    log.write("Archivo del cliente "+str(i)+" recibido en "+str(end-start)+".\n")
    index=content.find("HashHex")
    hashG=content[0:index]
    file=open(("ArchivosRecibidos\Cliente"+str(i)+"-Prueba-"+str(conexiones))+".txt", 'w')
    file.write(content[index+7:len(content)])
    file=open(("ArchivosRecibidos\Cliente"+str(i)+"-Prueba-"+str(conexiones))+".txt",'rt')
    content=file.read()
    hashC=hashlib.md5(content.encode(FORMAT)).hexdigest()
    print("Hash obtenido: "+hashG)
    print("Hash calculado: "+hashC)
    file.close()
    clientes[i].close()
