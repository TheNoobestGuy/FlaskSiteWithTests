from flask import Flask, render_template, jsonify, request
import json

# Create a Flask application
app = Flask(__name__, template_folder='templates')

# Define a routes
@app.route('/')
def home():
    return render_template('Index.html')

@app.route('/CreateRecipes')
def CreateRecipes():
    return render_template('CreateRecipes.html')

@app.route('/FavoriteRecipes')
def FavoriteRecipes():
    return render_template('FavoriteRecipes.html')

# Shared array
data = {
    "Logged": [],
    "RegisteredUsers": [],
    "FavoriteList": []
}

@app.route('/Data', methods=['GET'])
def get_data():
    return jsonify(data)

@app.route('/AddToFavorite', methods=['POST'])
def add_data():
    new_item = request.json
    data['FavoriteList'].append(new_item)
    return jsonify({"message": "Recipe successfully added!", "status": "success"}), 200

@app.route('/RemoveFavorite', methods=['DELETE'])
def remove_data():
    return jsonify(data)

@app.route('/Register', methods=['POST'])
def register():
    new_item = request.json
    data['RegisteredUsers'].append(new_item)
    return jsonify({"message": "Registered successfully!", "status": "success"}), 200

@app.route('/LogIn', methods=['POST'])
def login():
    new_item = request.json
    data['Logged'].append(new_item)
    return jsonify({"message": "Logged successfully!", "status": "success"}), 200

@app.route('/LogOut', methods=['DELETE'])
def logout():
    data['Logged'].clear()
    return jsonify({"message": "User successfully loged out!", "status": "success"}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)