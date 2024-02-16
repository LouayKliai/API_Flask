# user.py

from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Définir une classe User pour représenter l'entité utilisateur
class User:
    def __init__(self, firstname, lastname, age,cin):
        self.firstName = firstname
        self.lastName = lastname
        self.age = age
        self.cin=cin

# Établir la connexion à MongoDB et la collection
client = MongoClient('mongodb+srv://admin:louay@cluster0.g7oulyh.mongodb.net/')
db = client['PFE']
collection = db['users']

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
    firstname = user_data.get('firstName')
    lastname = user_data.get('lastName')
    age = user_data.get('age')
    cin = user_data.get('cin')

    # Créer une instance de la classe User avec les données extraites
    new_user = User(firstname, lastname, age,cin)

    # Insérer les données de l'utilisateur dans MongoDB
    collection.insert_one(new_user.__dict__)

    return 'User added to MongoDB'


@app.route('/get_users', methods=['GET'])
def get_users():
    # Récupérer tous les utilisateurs de la collection
    users = list(collection.find({}, {'_id': 0}))

    # Convertir les résultats en JSON et les renvoyer
    return jsonify(users)



@app.route('/get_one_user/<num>', methods=['GET'])
def get_one_user(num):     
    users = list(collection.find({}, {'_id': 0}))  
    for user in users:            
        user=collection.find({},{'_id': 0, 'cin': 1, 
                    'firstname': 1})
        if user.cin==num:                               
            return jsonify({'message': 'User with CIN {} exists .'.format(num)})                
        else:
            return jsonify({'message': 'User with CIN {} does not exist.'.format(num)})
        

    
@app.route('/delete_all_users', methods=['DELETE'])
def delete_all_users():
    # Supprimer tous les utilisateurs de la base de données
    result = collection.delete_many({})
    
    if result.deleted_count > 0:
        return jsonify({'message': 'All users deleted successfully.'})
    else:        
        return jsonify({'message': 'No users found to delete.'})
    

  
@app.route('/delete_user_with_cin/<cin>', methods=['DELETE'])
def delete_user_with_cin(cin):
    # Supprimer l'utilisateur de la base de données en fonction de son CIN
    result = collection.delete_one({'cin': cin})    
    if result.deleted_count > 0:
        return jsonify({'message': 'User with CIN {} deleted successfully.'.format(cin)})
    else:
        return jsonify({'message': 'User with CIN {} not found.'.format(cin)})

  
@app.route('/delete_one_user/<cin>', methods=['DELETE'])
def delete_user_cin(cin):

    myQuery ={'cin':cin}
    result=collection.delete_one(myQuery)
    if result:
        print("bien supprimer")
        return jsonify({'message': 'User with CIN {} deleted successfully.'.format(cin)})
    else:
        print("erreur")
        return jsonify({'message': 'User with CIN {} not found.'.format(cin)})



@app.route('/get_one', methods=['GET'])
def get_one():  
    x = collection.find_one()
    return jsonify(x)
   
if __name__ == '__main__':
    
    app.run()
