# Flask dependencies
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database_setup import Base, Hotel
from flask import Flask, request, jsonify
app = Flask(__name__)


# Create session and connect to DB
engine = create_engine('sqlite:///nebula.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/api/hotels/get_hotel', methods=['GET'])
def get_hotel():
    if not 'id' in request.args:
        return jsonify({"error": "ID not specified"})
    id = request.args.get('id')
    query = session.query(Hotel).filter(Hotel.idHotel == id)
    result = query.one()
    return jsonify({"messages from " + id: ["Hello there " + result.hNombre]})


@app.route('/api/hotels/add_hotel', methods=['POST'])
def add_hotel():
    if 'id' not in request.args:
        return jsonify({"error": "id not specified"})
    if 'name' not in request.args:
        return jsonify({"error": "name not specified"})
    if 'dir' not in request.args:
        return jsonify({"error": "dir not specified"})

    if 'country' not in request.args:
        country = None
    else:
        country = request.args.get("country")
    if 'tel' not in request.args:
        tel = None
    else:
        tel = request.args.get("tel")
    if 'mail' not in request.args:
        mail = None
    else:
        mail = request.args.get("mail")

    idH = request.args.get("id")
    name = request.args.get("name")
    dirH = request.args.get("dir")
    newHotel = Hotel(idHotel=idH, hNombre=name, direccion=dirH,
                     pais=country, telefono=tel, email=mail)
    session.add(newHotel)
    session.commit()


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
