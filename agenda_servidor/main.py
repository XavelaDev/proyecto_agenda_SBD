from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

bd = mysql.connector.connect(host='localhost', user='alumno',
passwd='12345',
database='agenda')

cursor = bd.cursor()

@app.route('/agenda/', methods=["GET","POST"])
def agenda():
	if request.method == "GET":
		contactos = []
		query = "SELECT * FROM contacto"
		cursor.execute(query)

		for contacto in cursor.fetchall():
			d = {
				'id': contacto[0],
				'nombre': contacto[1],
				'avatar': contacto[2],
				'correo': contacto[3],
				'telefono': contacto[4],
				'facebook': contacto[5],
				'twitter': contacto[6],
				'instagram': contacto[7],
			}
			contactos.append(d)
			# print(d)
		print(contactos)
		return jsonify(contactos)
	else:
		data = request.get_json()
		print(data)

		query = "INSERT INTO contacto(nombre, avatar, correo, telefono, facebook, twitter, instagram, id_usuario) VALUES(%s, %s, %s, %s, %s, %s, %s, 1)"

		cursor.execute(query, ((data['nombre']), (data['avatar']), (data['correo']), (data['telefono']), (data['facebook']), (data['twitter']), (data['instagram'])))
		bd.commit()

		if cursor.rowcount:
			return jsonify({'data': 'Ok'})
		else:
			return jsonify({'data': 'Error'})

		return jsonify({'data': 'Ok'})

app.run(debug=True)