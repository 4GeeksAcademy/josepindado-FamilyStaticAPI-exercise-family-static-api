
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {"id": 1, "first_name": "John", "age": 33, "lucky_numbers": [7, 13, 22]},
            {"id": 2, "first_name": "Jane", "age": 35, "lucky_numbers": [10, 14, 3]},
            {"id": 3, "first_name": "Jimmy", "age": 5, "lucky_numbers": [1]}
        ]

    # Método para generar una ID única cuando se añade un nuevo miembro a la lista
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    # Método para añadir un nuevo miembro a la lista
    def add_member(self, member):
        if "id" not in member:  
            member['id'] = self._generate_id()  # Genera un ID si no se proporciona
        member['last_name'] = self.last_name  # El apellido siempre será 'Jackson'
        self._members.append(member)  # Añade el miembro a la lista

    # Método para eliminar un miembro por su ID
    def delete_member(self, id):
        for i, member in enumerate(self._members):
            if member["id"] == id:
                del self._members[i]
                return True
        return False
        
    # Método para obtener un miembro por su ID
    def get_member(self, id):
        for member in self._members:
            if member['id'] == id:
                return member
        return None

    # Método para obtener todos los miembros de la familia
    def get_all_members(self):
        return self._members