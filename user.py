# user.py

from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Définir une classe User pour représenter l'entité utilisateur
class User:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

# Établir la connexion à MongoDB et la collection
client = MongoClient('mongodb+srv://admin:louay@cluster0.g7oulyh.mongodb.net/')
db = client['PFE']
collection = db['User']

# Route racine
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Ajouter une route pour ajouter des données utilisateur à MongoDB
@app.route('/add_user', methods=['POST'])
def add_user_route():
    # Obtenir les données de la requête au format JSON
    user_data = request.json

    # Extraire les champs de l'utilisateur
    firstname = user_data.get('firstname')
    lastname = user_data.get('lastname')
    age = user_data.get('age')

    # Créer une instance de la classe User avec les données extraites
    new_user = User(firstname, lastname, age)

    # Insérer les données de l'utilisateur dans MongoDB
    collection.insert_one(new_user.__dict__)

    return 'User added to MongoDB'
@app.route('/get_users', methods=['GET'])
def get_users():
    # Récupérer tous les utilisateurs de la collection
    users = list(collection.find({}, {'_id': 0}))

    # Convertir les résultats en JSON et les renvoyer
    return jsonify(users)

if __name__ == '__main__':
    app.run()
