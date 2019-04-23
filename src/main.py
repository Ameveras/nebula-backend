# Flask dependencies
from flask import Flask, request, jsonify
app = Flask(__name__)

#TODO: Add Base, Hotel
from database_setup import Base, Hotel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB
#TODO: Add database hotels
engine = create_engine('sqlite:///nebula.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/api/hotels/add-hotel', methods = ['GET'])
def get_message():
    id = request.args.get('id')
    name = request.args.get('name')
    query = session.query(Hotel).filter(Hotel.hNombre == name)
    result = query.all()
    return jsonify({"messages from " + id: ["Hello there " + name]})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
