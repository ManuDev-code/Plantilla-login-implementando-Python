# Sistema de login simple por consola
import functions

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n===== SISTEMA DE USUARIOS =====")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")
    return input("Seleccione una opción (1-3): ")

def main():
    """Función principal del programa"""
    # Cargar usuarios al inicio
    functions.load_users()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            # Iniciar sesión
            if functions.user_login():
                # Si el login es exitoso, mostrar alguna funcionalidad
                print("Has accedido al sistema.")
                input("Presiona Enter para volver al menú principal...")
        
        elif opcion == "2":
            # Registrar nuevo usuario
            functions.user_register()
            input("Presiona Enter para continuar...")
        
        elif opcion == "3":
            # Salir del programa
            print("¡Hasta pronto!")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()