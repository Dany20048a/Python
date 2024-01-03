try:  #switch de excepciones, haz esto a pesar de...
    x=10
    y=28
    z=x+y
    print(a)
except TypeError:
    print('Error de tipado')
except ZeroDivisionError: #cualquier otra excepcion arroja este otro mensaje
    print('Error de division')
except Exception as e: 
    print(e)

print('El codigo continua')


#c# try(){ } catch(a){ }