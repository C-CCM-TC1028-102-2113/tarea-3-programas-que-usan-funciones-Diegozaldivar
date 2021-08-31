
#Volumen de un prisma rectangular

def rectangulo(base,altura):
    area = base * altura
    return area
    


def prisma(AREA_TOTAL, ancho):
    volumen = AREA_TOTAL * ancho
    print( 'El volumen del prisma es: '+ str(volumen))



def main():
  #escribe tu código abajo de esta línea+
    base = float(input('Dame la base:'))
    altura = float(input('Dame la altura:'))
    ancho = float(input('Dame el ancho:'))
    
    AREA_TOTAL = rectangulo(base,altura)
    print('El area del rectángulo es:' + str(AREA_TOTAL))

    prisma(AREA_TOTAL, ancho)





if __name__ == '__main__':
    main()
    
    
