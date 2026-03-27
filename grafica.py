import matplotlib.pyplot as plt
import numpy as np

def grafico():
    x = np.arange(1, 9) 
    y = 36**x 

    #por el abecedario

    plt.figure(figsize=(10, 6))
    #para la figuta 
   
    plt.plot(x, y, marker='o', color='red', linestyle='-', linewidth=2, label='Combinaciones posibles')
    
    
    plt.yscale('log') 
    
    
    plt.legend() 

    plt.title('Crecimiento Exponencial de la Fuerza Bruta', fontsize=14)

    plt.xlabel('Longitud de la Contraseña (Caracteres)', fontsize=12)

    plt.ylabel('Combinaciones (Escala Logarítmica)', fontsize=12)


    plt.grid(True, which="both", ls="-", alpha=0.5)

    plt.show()

grafico()
