# import packages
from crypt import methods
from flask import Flask, jsonify, request, redirect
from flask import jsonify
import mariadb
from config import config
from config import conn_params


app = Flask(__name__)

@app.route('/')
def home():
    """This function temporarily redirect to the /api/greeting route."""
    return redirect('/api/greeting')

@app.route('/api/greeting', methods=['GET'])
def number_of_rows():
    """This function shows the total number of rows in the DB when /api/greeting is invoked."""

    try:
        conn = mariadb.connect(**conn_params)
        sql = "SELECT COUNT(*) FROM cryptocurrencys"
        cur = conn.cursor()
        cur.execute(sql)
        number_rows = cur.fetchone()
        # print(number_rows)
        conn.close()
        return jsonify({"number of rows": number_rows[0]})
    except mariadb.Error as e:
        print(f'Error GET ALL: {e}')
        return jsonify({"message": "Error" })

@app.route('/api/messages', methods=['POST'])
def create_cryptocurrency():
    """This function creates a new row in the DB when /api/messages is invoked."""

    try:
        #print(request.json)
        conn = mariadb.connect(**conn_params)
        sql = """INSERT INTO cryptocurrencys(
                    cryptocurrency_id,
                    cryptocurrency_name, 
                    cryptocurrency_symbol)
                VALUES('{0}','{1}', '{2}')""".format(
                    request.json['cryptocurrency_id'],
                    request.json['cryptocurrency_name'],
                    request.json['cryptocurrency_symbol']
                )
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.execute("SELECT * FROM cryptocurrencys WHERE cryptocurrency_id = '{0}'".format(request.json['cryptocurrency_id']))
        currency = cur.fetchone()
        conn.close()
        return jsonify({"currency": currency, "message": "cryptocurrency created"}), 201
    except mariadb.Error as e:
        print(f'Error with POST: {e}')
        return jsonify({"message": "Error" })

@app.route('/api/cryptocurrencies/<id>', methods=['GET'])
def get_cryptocurrency(id):
    try:
        conn = mariadb.connect(**conn_params)
        sql = "SELECT * FROM cryptocurrencys WHERE cryptocurrency_id = '{0}'".format(id)
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchone()
        if data != None:
            currency = {'cryptocurrency_id': data[0], 'cryptocurrency_name': data[1], 'cryptocurrency_symbol': data[2], 'created_at': data[3]}
            print(currency)
            conn.close()
            return jsonify({"currency": currency })
        else:
            return jsonify({"message": "currency not found"})
    except mariadb.Error as e:
        print(f'Error with GET: {e}')
        return jsonify({"message": "Error" })

@app.route('/api/cryptocurrencies/<id>', methods=['DELETE'])
def delete_cryptocurrency(id):
    try:
        #print(request.json)
        conn = mariadb.connect(**conn_params)
        sql = """DELETE FROM cryptocurrencys 
                WHERE cryptocurrency_id = '{0}'""".format(id)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()
        return jsonify({"message": "cryptocurrency deleted" })
    except mariadb.Error as e:
        print(f'Error with DELETE: {e}')
        return jsonify({"message": "Error" })

def resource_not_found(error):
    return jsonify({"message": "sorry, resource not foud :(" }), 404

# TODO securing the API

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, resource_not_found)
    app.run(host='0.0.0.0')