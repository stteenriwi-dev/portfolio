x = 17
y = 12

edad = int(input("Edad: "))
lugar = input("De donde eres: 1. medellin O 2. bogota ?: ")

if(edad>=18):
    print('Ok continuemos')
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    correo = input("Correo: ")
    telefono = input("Telefono: ")
elif(lugar == "medellin" or lugar == "1"):
    
    
    print(
    'Hola '+nombres + apellidos+'. Eres afortunado de tener: '+str(edad)+
    ' Te comunicaremos al número: '+telefono+' y al correo: '+correo
    )
else:
    print(f'No puedes entrar por tener: {edad}')

