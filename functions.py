# Funciones para registro y login de usuarios

# Lista para almacenar temporalmente los datos del usuario actual
user = []

# Diccionario para almacenar usuarios (username: password)
users_dict = {}

def load_users():
    """Carga los usuarios desde el archivo users.txt"""
    try:
        with open('users.txt', 'r') as file:
            for line in file:
                if ':' in line:
                    username, password = line.strip().split(':', 1)
                    users_dict[username] = password
    except FileNotFoundError:
        # Si el archivo no existe, creamos uno con usuarios por defecto
        with open('users.txt', 'w') as file:
            file.write('usuario1:clave123\n')
            file.write('usuario2:clave456\n')
        users_dict.update({'usuario1': 'clave123', 'usuario2': 'clave456'})
    
    return users_dict

def save_user(username, password):
    """Guarda un nuevo usuario en el archivo users.txt"""
    with open('users.txt', 'a') as file:
        file.write(f'{username}:{password}\n')

def user_register():
    """Registra un nuevo usuario pidiendo datos por consola"""
    print("\n--- REGISTRO DE USUARIO ---")
    username = input("Ingrese nombre de usuario: ")
    
    # Verificar si el usuario ya existe
    users = load_users()
    if username in users:
        print("Error: Este nombre de usuario ya existe.")
        return False
    
    # Recolectar datos del usuario
    user.clear()  # Limpiar lista anterior
    user.append(username)
    name = input("Ingrese su nombre: ")
    user.append(name)
    last_name = input("Ingrese su apellido: ")
    user.append(last_name)
    email = input("Ingrese su email: ")
    user.append(email)
    password = input("Cree una contraseña (8 caracteres mínimo): ")
    
    # Validación simple de contraseña
    if len(password) < 8:
        print("Error: La contraseña debe tener al menos 8 caracteres.")
        return False
    
    user.append(password)
    
    # Guardar usuario en el archivo
    save_user(username, password)
    
    print("\n¡Usuario creado correctamente!")
    print(f"Datos: {user}")
    return True
    
def user_login():
    """Función para iniciar sesión"""
    print("\n--- INICIO DE SESIÓN ---")
    username = input("Usuario: ")
    password = input("Contraseña: ")
    
    # Cargar usuarios y verificar credenciales
    users = load_users()
    
    if username in users and users[username] == password:
        print(f"\n¡Bienvenido, {username}!")
        return True
    else:
        print("Error: Usuario o contraseña incorrectos.")
        return False
