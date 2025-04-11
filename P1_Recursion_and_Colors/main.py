"""
Problema de la Torre de Hanói, teniendo en cuenta la restricción de que no se pueden colocar dos discos del mismo color consecutivamente en ningún poste.
Realicé la solución dividiéndola estratégicamente en distintas variables para así garantizar un uso optimo y recursivo del código.
El algoritmo utiliza recursión y backtracking para explorar los movimientos válidos hasta que todos los discos están en el poste "C".
"""

def move(disk, target):
    """
    Verifica si es posible mover el disco específico a una pila objetivo, respetando las siguientes reglas:
    - Si la pila de destino está vacía, el movimiento es permitido.
    - Si la pila de destino no está vacía:
        - El disco a mover debe ser de menor tamaño que el disco en la cima de la pila de destino.
        - El disco a mover debe tener un color diferente al disco en la cima de la pila de destino.

    Parámetros:
      disk: Es el disco que se va a mover con sus datos (tamaño, color).
      target: Lista de discos que estan en la pila de destino.

    """
    if not target:
        # La pila de destino está vacía, se permite el movimiento.
        return True
    top_disk = target[-1]
    # Verifica que el disco a mover sea más pequeño y de diferente color que el disco en la cima de la pila de destino.
    return disk[0] < top_disk[0] and disk[1] != top_disk[1]


def solution(rods, moves, visited, total_disks):
    """
    Ya que el ejercicio propone un problema que puede contener reglas iterativas para llegar a la solución, 
    cree esta función intermedia que busca la solución usando la técnica de backtracking para así tratar 
    de hacerlo de manera recursiva
    """
    # Si todos los discos estan ordenados debidamente en C ya se logro el objetivo, se retorna y sale de la funcion.
    if len(rods["C"]) == total_disks:
        return moves

    # Convierte el estado actual de los postes en una tupla de tuplas, lo que permite almacenarlo en un conjunto, 
    # usar la variable visited para evitar ciclos durante la repeticion.
    state_key = (tuple(rods["A"]), tuple(rods["B"]), tuple(rods["C"]))
    if state_key in visited:
        # Si este estado es repetido, se retorna None para evitar ciclos.
        return None
    visited.add(state_key)
    
    # Este for es para mover el disco superior de cada poste.
    for source in ["A", "B", "C"]:
        if rods[source]:
            disk = rods[source][-1]
            '''
            En un principio cree la solución revisando cada poste desde A hasta C [A, B, C], 
            sin embargo, debido a que el poste target de la solución final es C me di cuenta que si itero la revés, 
            empezado desde C [C, B, A] se puede llegar a la solución con muchos menos movimientos y de forma más rápida. 
            '''
            for target in ["C", "B", "A"]:
                if source == target:
                    # Como estamos en un for, hay que verificar cada bucle para evitar realizar una operacion
                    # se intenta mover hacia el mismo poste de origen.
                    continue
                if move(disk, rods[target]):
                    # Aca cree copias usando .copy() de los postes para no alterar el estado actual.
                    new_rods = {
                        "A": rods["A"].copy(),
                        "B": rods["B"].copy(),
                        "C": rods["C"].copy()
                    }
                    moved_disk = new_rods[source].pop()  # Quita el disco del poste de origen.
                    new_rods[target].append(moved_disk)  # Coloca el disco en el poste de destino.
                    # moves lo que hace es guardar el resultado final de las tuplas que se mostraran
                    # como esto es un ciclo entonces va creando nuevos movimientos hasta llegar a la solucion
                    new_moves = moves + [(moved_disk[0], source, target)] 
                    
                    # Aaca se actualiza el estado para reiterar la funcion.
                    result = solution(new_rods, new_moves, visited, total_disks)
                    if result is not None:
                        return result
                    
    # Si no se encuentra una solución en este camino, se retorna None.
    return None


def preparation(disks, n):
    """
    Cree esta función para preparar la solución, asignando los siguientes parámetros 

    (Postes) / rods: Diccionario que representa el estado actual de los postes, hice que 
    inicialmente en el poste que representa la llave A contuviera el estado inicial de la tupla que se recibe en el input.
    moves: Lista de movimientos realizados hasta el momento, cada movimiento es una tupla (tamaño_del_disco, origen, destino).
    visited: Conjunto que contiene los estados ya visitados, para evitar ciclos.
    n: Número total de discos.
    """
    rods = {
        "A": disks,
        "B": [],
        "C": []
    }
    visited = set()
    result = solution(rods, [], visited, n)
    # Si no se pudo solucionar devuelve -1
    return result if result is not None else -1


if __name__ == "__main__":
    #Ejemplo 1:
    disks = [(3, "rojo"), (2, "azul"), (1, "rojo")]
    # Hice que n fuera igual a len(disk) debido a que n siempre la cantidad de discos, de esta forma se evita la redundancia y posibles errores al digitar n manualmente
    n = len(disks)
    if n >= 1 and n <= 8:
        result = preparation(disks, n)
        print("Ejemplo 1:")
        print(result)
    else:
        print("La cantidad de discos esta fuera de los parametros")

    # Ejemplo 2: Caso sin solución.
    disks = [(4, "rojo"), (3, "azul"), (2, "rojo"), (1, "rojo")]
    n = len(disks)
    if n >= 1 and n <= 8:
        result = preparation(disks, n)
        print("Ejemplo 2:")
        print(result)
    else:
        print("La cantidad de discos esta fuera de los parametros")