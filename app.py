"""Flask app for Cupcakes"""
from flask import Flask, jsonify, request, render_template
from models import db, Cupcake, serialize

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"]  = True

db.init_app(app)
app.app_context().push()

"""Part Two: Listing, Getting & Creating Cupcakes"""

@app.route('/api/cupcakes', methods=["GET"])
def all_cupcakes_data():
    ''' Get data about all the cupcakes. Respond with JSON '''
    cupcakes = Cupcake.query.all()
    serialized = [serialize(cupcake) for cupcake in cupcakes]
    
    return jsonify(cupcakes=serialized)

@app.route('/api/cupcakes/<int:id>', methods=["GET"])
def cupcake_data(id):
    '''Get data on specific cupcake based on ID '''
    cupcake = Cupcake.query.get_or_404(id)
    serialized = serialize(cupcake)

    return jsonify(cupcake=serialized)

@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    ''' Create a cupcake and its data from request '''
    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"]

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = serialize(new_cupcake)

    return (jsonify(cupcake=serialized), 201)

@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_cupcake(id):
    ''' Updating cupcake details '''
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)

    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    ''' Deleting Cupcake '''
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Deleted")

@app.route('/', methods=["GET"])
def index_page():
    cupcakes = Cupcake.query.all()
    return render_template("index.html", cupcakes=cupcakes)


  



