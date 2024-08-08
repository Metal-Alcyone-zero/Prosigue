
from prosigue.command import Prosigue


class Mi_script:
    
    def empieza(self, entrada, retorno):
        
        print("La entrada es: " + str(entrada))
        
        retorno.put(None)
        

code= Mi_script()

if __name__ == '__main__':

    sinonimo= Prosigue(code)

    sinonimo.entry(3); sinonimo.tiempo(4)
    paso= sinonimo.close(True)

    print(paso)
    print(sinonimo.answer)

    print()

