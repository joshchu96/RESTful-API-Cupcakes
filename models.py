"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cupcake(db.Model):
    """Model for making cupcakes"""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    flavor = db.Column(db.Text, nullable = False)
    size = db.Column(db.Text, nullable = False)
    rating = db.Column(db.Float, nullable = False)
    image = db.Column(db.Text, nullable = False, default = "https://tinyurl.com/demo-cupcake")

    def __repr__(self):
        return f"< id={self.id}, flavor={self.flavor}, size={self.size}, rating={self.rating}, image={self.image} >"


def serialize(cupcake):
        '''Serialize a cupcake SQLAlchemy obj to a dictionary'''
        return {
            "id": cupcake.id,
            "flavor": cupcake.flavor,
            "size": cupcake.size,
            "rating": cupcake.rating,
            "image": cupcake.image
        }
    

    