def load_users():
    """Carga los usuarios desde el archivo users.txt"""
    users = {}
    try:
        with open('users.txt', 'r') as file:
            for line in file:
                if ':' in line:
                    username, password = line.strip().split(':', 1)
                    users[username] = password
    except FileNotFoundError:
        # Si el archivo no existe, creamos uno con usuarios por defecto
        with open('users.txt', 'w') as file:
            file.write('usuario1:clave123\n')
            file.write('usuario2:clave456\n')
        users = {'usuario1': 'clave123', 'usuario2': 'clave456'}
    
    return users

def authenticate(username, password):
    """Verifica si las credenciales son correctas"""
    users = load_users()
    return username in users and users[username] == password

def add_user(username, password):
    """Añade un nuevo usuario al archivo"""
    users = load_users()
    if username in users:
        return False  # Usuario ya existe
    
    with open('users.txt', 'a') as file:
        file.write(f'{username}:{password}\n')
    
    return True