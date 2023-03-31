# SocketsTCP

En este repositorio se encuentra la aplicacion de un Cliente y Servidor de Sockets TCP para la transmision de archivos.

En primer lugar se accede a la carpeta Servidor y se ejecuta el archivo generateFiles.py para generar los archivos 100MB.txt y 250MB.txt los cuales se utilizan para la transmision.

En la misma carpeta Servidor se abre el archivo ServidorTCP.py y se cambia la variable HOST por la IP del equipo en donde se este ejecutando dicho servidor y posteriormente en este servidor se ejecuta el archivo ServidorTCP.py

OJO: ES MUY IMPORTANTE QUE A LA HORA DE EJECUTAR CADA ARCHIVO SE ESTE DENTRO DE LA CARPETA QUE CONTIENE A ESTE (En este caso dentro de la carpeta Servidor)

Una vez se esta ejecutando el servidor y se ingreso el nombre del archivo a enviar y el numero de clientes se procede a la parte del cliente, aqui nuevamente es de suma importancia que se este dentro de la carpeta Cliente.

En primer lugar se entra al archivo ClienteTCP.py y se cambia la variable IP por la IP del servidor que se asigno anteriormente, una vez se realiza esto se puede ejecutar el archivo.

Cuando se ejecute el archivo se ingresa el numero de conexiones que se desean (Tal como se hizo con el servidor) y posteriormente se presiona ENTER para empezar la transferencia de los archivos.

Dichos archivos se guardan en la carpeta Cliente/ArchivosRecibidos y tanto para el servidor como para el cliente se tiene su correspondiente carpeta de Logs donde se guarda la informacion de cada transmision.
