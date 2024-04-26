cp = input("Ingrese el código postal del lugar de destino: ")
direccion = input("Dirección del lugar de destino: ")
tipo = int(input("Tipo de envío (id entre 0 y 6 - ver tabla 2 en el enunciado): "))
pago = int(input("Forma de pago (1: efectivo - 2: tarjeta): "))

cp = cp.upper()

#Comprobar a que país corresponde el cp
if len(cp) >= 4 and len(cp) <= 9:
    if len(cp) == 8 and cp[0] != 'O' and cp[0] != 'I':
        destino = 'Argentina'
        porcentaje_provincia = 1
        
    elif len(cp) == 4 and not ('A' <= max(cp) <= 'Z'):
        destino = 'Bolivia'
        porcentaje_provincia = 1.20
        
    elif len(cp) == 9 and not ('A' <= max(cp) <= 'Z'):
        destino = 'Brasil'
        if cp[0] == '8' or cp[0] == '9':
            provincia = 8
            porcentaje_provincia = 1.20
        elif cp[0] == '0' or cp[0] == '1' or cp[0] == '2' or cp[0] == '3':
            provincia = 0
            porcentaje_provincia = 1.25
        elif cp[0] == '4' or cp[0] == '5' or cp[0] == '6' or cp[0] == '7':
            provincia = 4
            porcentaje_provincia = 1.30
        
    elif len(cp) == 7 and not ('A' <= max(cp) <= 'Z'):
        destino = 'Chile'
        porcentaje_provincia = 1.25
        
    elif len(cp) == 6 and not ('A' <= max(cp) <= 'Z'):
        destino = 'Paraguay'
        porcentaje_provincia = 1.20
        
    elif len(cp) == 5 and cp[0] == '1' and not ('A' <= max(cp) <= 'Z'):
        destino = 'Uruguay'
        provincia = 1
        porcentaje_provincia = 1.20
    elif len(cp) == 5 and cp[0] != '1' and not ('A' <= max(cp) <= 'Z'):
        destino = 'Uruguay'
        provincia = 2
        porcentaje_provincia = 1.25
        
    else:
        destino = 'Otro'
        porcentaje_provincia = 1.50
    
else:
    destino = 'Otro'
    porcentaje_provincia = 1.50

#Chequeo de provincias Argentina
if destino == 'Argentina':
    if cp[0] == 'A':
        provincia = 'Salta'
    elif cp[0] == 'B':
        provincia = 'Buenos Aires'
    elif cp[0] == 'C':
        provincia = 'Ciudad Autónoma de Buenos Aires'
    elif cp[0] == 'D':
        provincia = 'San Luis'
    elif cp[0] == 'E':
        provincia = 'Entre Rios'
    elif cp[0] == 'F':
        provincia = 'La Rioja'
    elif cp[0] == 'G':
        provincia = 'Santiago Del Estero'
    elif cp[0] == 'H':
        provincia = 'San Luis'
    elif cp[0] == 'K':
        provincia = 'Catamarca'
    elif cp[0] == 'J':
        provincia = 'San Juan'
    elif cp[0] == 'L':
        provincia = 'La Pampa'
    elif cp[0] == 'M':
        provincia = 'Mendoza'
    elif cp[0] == 'N':
        provincia = 'Misiones'
    elif cp[0] == 'P':
        provincia = 'Formosa'
    elif cp[0] == 'Q':
        provincia = 'Neuquén'
    elif cp[0] == 'R':
        provincia = 'Río Negro'
    elif cp[0] == 'S':
        provincia = 'Santa Fe'
    elif cp[0] == 'T':
        provincia = 'Tucumán'
    elif cp[0] == 'U':
        provincia = 'Chubut'
    elif cp[0] == 'V':
        provincia = 'Tierra Del Fuego'
    elif cp[0] == 'W':
        provincia = 'Corrientes'
    elif cp[0] == 'X':
        provincia = 'Córdoba'
    elif cp[0] == 'Y':
        provincia = 'Jujuy'
    elif cp[0] == 'Z':
        provincia = 'Santa Cruz'

else:
    provincia = 'No aplica'
        
#Tipo
lista_precios = (1100,1800,2450,8300,10900,14300,17900)
precio_tipo = lista_precios[tipo]

#Pago
inicial = precio_tipo * porcentaje_provincia

if pago == 1:
    final = inicial * 0.90
elif pago == 2:
    final = inicial
else:
    print('Opcion de pago incorrecta')

#Prints
print("País de destino del envío:", destino)
print("Provincia destino:", provincia)
print("Importe inicial a pagar:", inicial)
print("Importe final a pagar:", final)