from modules import state_management
from interface import main_interface

def main():
    # Inicializa o gerenciamento de estado
    state_management.init_state()

    # Inicia a interface gráfica
    main_interface.start_interface()

if __name__ == "__main__":
    main()