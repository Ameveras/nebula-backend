# Flask dependencies
from flask import Flask, request, jsonify
app = Flask(__name__)

from database_setup import Base, Hotel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB
engine = create_engine('sqlite:///nebula.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/api/hotels/add_hotel', methods = ['GET'])
def get_hotel():
    if not 'id' in request.args:
        return jsonify({"error": "ID not specified"})
    id = request.args.get('id')
    query = session.query(Hotel).filter(Hotel.idHotel == id)
    result = query.one()
    return jsonify({"messages from " + id: ["Hello there " + result.hNombre]})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
