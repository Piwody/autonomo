import time


intentos = 0



def prueba(prefijo, longitud, alfabeto, objetivo):
    global intentos
    
  
    if len(prefijo) == longitud:
        intentos += 1
        if prefijo == objetivo:
            return prefijo
        return None

    
    for char in alfabeto:
        resultado = prueba(prefijo + char, longitud, alfabeto, objetivo)

        if resultado: 
            return resultado
    
    return None

# tiene dos parte la primera la logica y la segunda la parte de medir el tiempo y los intentos y la contrasena 


def bruteforce(alfabeto, password):
    global intentos
    intentos = 0
    tiempo = time.time()
    
   
    
    
    for largo in range(1, 10): 

        print("viendo los caracteres " + str(largo) + "...")
        encontrada = prueba("", largo, alfabeto, password)
        
        if encontrada:

            final = time.time()
            tiempo_total = final - tiempo
           
            print("te cachamos tu pass es: " + str(encontrada))
            print("intentos: " + str(intentos))
            print("tiempo en segundos: " + str((tiempo_total)) )
            
            return encontrada

    print("No se encontró la contraseña con el alfabeto.")
    return None



caracterdeuser= "abcdefghijklmnopqrstuvwxyz0123456789"
contra = "carro" 

bruteforce(caracterdeuser, contra)