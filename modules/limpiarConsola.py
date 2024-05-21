import os
def limpiarPantalla():
    sistema_operativo = os.name

    if sistema_operativo == 'posix':  # Linux y macOS
        os.system('clear')
    elif sistema_operativo == 'nt':   # Windows
        os.system('cls')
    else:
        os.system('clear')
        os.system('cls')