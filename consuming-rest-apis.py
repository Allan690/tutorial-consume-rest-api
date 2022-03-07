import requests
import os


class Todos:
    """
    this class will consume the todos rest api
    """
    def __init__(self) -> None:
        self.url = os.getenv('API_URL')

    def get_todos(self) -> list:
        """
        this method will consume the todos rest api
        """
        response = requests.get(self.url)
        return response.json()
    
    def post_todos(self, body) -> None:
        """
        this method will post to the todo rest api
        """
        response = requests.post(self.url, body)
        return response.json()
    
    def put_todos(self, id: str, body) -> None:
        """
        this method will put to the todo rest api
        """
        response = requests.put(self.url + id, body)
        return response.json()
    
    def delete_todos(self, id: str) -> None:
        """
        this method will delete to the todo rest api
        """
        response = requests.delete(self.url + id)
        return response.json()
"""
Homework:
1. modify these methods so that the returned object of the method contains { title, completed } 
2. use these methods from these class - incorporate them into a simple REST API

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(data=Todos.get_todos())

get_todos() => [{ title: "example", completed: true }, { title: "example2", completed: false }]
"""