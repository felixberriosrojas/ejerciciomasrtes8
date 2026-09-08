from mysqlconection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.edad = data['edad']
        self.created_at = data['created_at']
        self.update_at = data['update_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (nombre, apellido, edad, created_at, update_at) VALUES (%(nombre)s, %(apellido)s, %(edad)s, NOW(), NOW());"
        return connectToMySQL('tarea4').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        
        results = connectToMySQL('tarea4').query_db(query)
        usuarios = []

        for usuario in results:
            usuarios.append(cls(usuario))
        return usuarios