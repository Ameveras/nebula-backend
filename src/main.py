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
    try:
        result = query.one()
    except:
        return jsonify({"error": "id not found"})
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
    return jsonify({"OK": "200"})


@app.route('/api/users/update_cliente/<id>', methods=['PUT'])
def update_users(id):
     query = session.query(Usuario).filter(Usuario.IdCliente==id)
     result = query.one()
     request.get_json(force=True)
     IdCliente = request.json['Id_Cliente']
     TipoDoc= request.json['Tipo_Documento']
     Documento = request.json['Documento']
     CNombre = request.json['Nombre']
     CApellido = request.json['Apellido']
     Sexo = request.json['Sexo']
     Pais= request.json['Pais']
     FechaNacimiento = request.json['Dirrecion']
     Telefono = request.json['Pais']
     Email = request.json['Telefono']
     Foto = request.json['Foto']
     FechaRegistro = request.json['Fecha_Registro']


     result.IdCliente = IdCliente
     result.TipoDoc = TipoDoc
     result.Documento = Documento
     result.CNombre = CNombre
     result.CApellido = CApellido
     result.Sexo = Sexo
     result.direccion = direccion
     result.pais = pais
     result.FechaNacimiento = FechaNacimiento
     result.Telefono = Telefono
     result.Email = Email
     result.Foto = Foto
     result.FechaRegistro = FechaRegistro
     session.merge(result)
     session.flush()
     session.commit()
     return jsonify({"OK": "200"})

    
 @app.route('/api/users/delete_user/<id>', methods=['DELETE'])
 def delete_hotels(id):
     query = session.query.get(id)
     delete_users = query.filter_by(Usuario.IdCliente==id).first()
     session.delete(delete_users)
     session.commit()
     return jsonify({"Mgs": "is Correct"})

@app.route('/api/hotels/update_hotel/<id>', methods=['PUT'])
def update_hotels(id):
    query = session.query(Hotel).filter(Hotel.idHotel==id)
     result = query.one()
     request.get_json(force=True)
     name = request.json['name']
     dirH = request.json['Dirrecion']
     pais = request.json['Pais']
     tel = request.json['Telefono']
     mail = request.json['Email']
     result.hNombre = name
     result.direccion = dirH
     result.pais = pais
     result.telefono = tel
     result.email = mail
     session.merge(result)
     session.flush()
     session.commit()
     return jsonify({"OK": "200"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
