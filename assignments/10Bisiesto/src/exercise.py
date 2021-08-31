
#Año bisiesto

def main():
  #escribe tu código abajo de esta línea
    año = int(input('Ingresa el año:'))
    if año % 4 != 0:
     año = print(str('False'))
    elif año % 4 == 0 and año % 100 != 0:
     año = print(str('True'))
    elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
     año = print(str('False'))
    elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
     año = print(str('True'))

    
    
    

if __name__ == '__main__':
    main()
