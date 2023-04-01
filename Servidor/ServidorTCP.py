import socket, os, time, hashlib
from datetime import datetime

HOST='192.168.20.58' #Se asigna la direccion IP actual de la maquina
PORT=65000
SIZE=1024
ADDR=(HOST, PORT)
FORMAT="utf-8"

date=datetime.now().strftime("%Y-%m-%d-%H-%M-%S-")
log=open("Logs/"+date+"log.txt",'a')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Se inicia el socket del servidor
s.bind(ADDR)
s.listen(30) # Un maximo de 30 conexiones en cola
while True: #Bucle infinito para escuchar conexiones de forma constante
    filename=input("Ingrese el nombre del archivo a enviar: ")
    log.write("Nombre del archivo: "+filename+"\n")
    file=open(filename,"r")

    data=file.read()
    file.seek(0,os.SEEK_END)

    log.write("Tamano del archivo: "+str(file.tell())+" bytes\n")

    clientes=int(input("Ingrese el numero de clientes: "))
    conexiones=0
    conns=[]
    print("Esperando que los clientes se conecten...")

    while conexiones<clientes+1: #Se aceptan el numero de conexiones establecidas
       conn, addr = s.accept()
       cliente=(conn, addr)
       conns.append(cliente)
       conexiones+=1
       if conexiones!=1:
           print("Conectado a ", addr)

    print("Esperando la confirmacion del cliente...") # Se espera la confirmacion para la transferencia

    if conns[0][0].recv(SIZE).decode(FORMAT)=="START":

        for i in range(1,clientes+1): #Se envia el archivo para cada conexion

            print("Calculando valor de hash...")
            hashV=hashlib.sha256(data.encode(FORMAT))
            conns[i][0].send(hashV.hexdigest().encode(FORMAT))
            conns[i][0].send("HashHex".encode(FORMAT))

            print("Enviando el archivo...")

            start=time.time()
            conns[i][0].send(data.encode(FORMAT)) # Se envia el archivo
            end=time.time()
            
            print("Archivo enviado.")
            log.write("Archivo exitosamente enviado al cliente "+str(i)+" en "+str(end-start)+" segundos\n")
            conns[i][0].close()# Se cierra cada conexion
            print("Desconexion ", addr)
    file.close()