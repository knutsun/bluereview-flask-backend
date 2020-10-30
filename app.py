from flask import Flask, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123god1;'
app.config['MYSQL_DB'] = 'officers'

mysql = MySQL(app)


@app.route('/department/newyorkcityny', methods=["GET"])
def get_departments():

    output = {
        "racialParityIndex": 0.0,
        "whiteParityIndex": 0.0,
        "nativeAmericanParityIndex": 0.0,
        "blackParityIndex": 0.0,
        "hispanicParityIndex": 0.0,
        "asianParityIndex": 0.0,
        "policeWhite": 46.7,
        "policeNativeAmerican": 0.1,
        "policeBlack": 15.2,
        "policeHispanic": 29.1,
        "policeAsian": 8.9,
        "policeSource": "https://app.powerbigov.us/view?r=eyJrIjoiZTI4OTRjZTYtNTYwOC00NzcxLThhYTItOTU5NGNkMzIzYjVlIiwidCI6IjJiOWY1N2ViLTc4ZDEtNDZmYi1iZTgzLWEyYWZkZDdjNjA0MyJ9&pageName=ReportSection",
        "policeSourceLastUpdated": "20201026",
        "communityWhite": 32.1,
        "communityNativeAmerican": 0.4,
        "communityBlack": 24.3,
        "communityHispanic": 29.1,
        "communityAsian": 13.9,
        "communitySource": "https://app.powerbigov.us/view?r=eyJrIjoiZTI4OTRjZTYtNTYwOC00NzcxLThhYTItOTU5NGNkMzIzYjVlIiwidCI6IjJiOWY1N2ViLTc4ZDEtNDZmYi1iZTgzLWEyYWZkZDdjNjA0MyJ9&pageName=ReportSection",
        "communitySourceLastUpdated": "20201026",
    }

    response = jsonify(response=output)

    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


# @app.route('/officers')
# def get_officers():
#     cur = mysql.connection.cursor()
#     cur.execute('''SELECT first_name, last_name, mid_initial, locality FROM nycnyofficers''')
#     rv = cur.fetchall()

#     # f.write("[")
#     # output += json.dumps(officer.__dict__) + ","
#     # f.write(output[:-1])
#     # f.write("]")

#     return str(rv)

if __name__ == '__main__':
    app.run(debug=True)
