from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
import json, datetime
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = "GlenDB"

mysql = MySQL(app)

@app.route('/cultdaily',methods=['GET', 'POST'])
@cross_origin()

def displaycultdaily():
      cur = mysql.connection.cursor()
      d1 = "'2020-07-01'"

      #con = "FINEPERENTRY.DIV_ID, FINEPERENTRY.FL_PER, "
      #tab = "FINEPERENTRY, DIVTAB"
      #joi = "FINEPERENTRY.DIV_ID = DIVTAB.DIV_ID"

      cur.execute(f'''select FINEPERENTRY.FL_ID, DIVTAB.DIV_NAME, FINEPERENTRY.FL_PER from FINEPERENTRY, DIVTAB WHERE (DATE = '2020-07-01') AND (FINEPERENTRY.DIV_ID = DIVTAB.DIV_ID) ''')
      row_headers = ['1','2','3']
      rv = cur.fetchall()
      json_data = []

      def sids_converter(o):
            if isinstance(o, datetime.date):
                  return str(o.year) + str("/") + str(o.month) + str("/") + str(o.day)

      for result in rv:
            json_data.append(dict(zip(row_headers , result)))
      return json.dumps(json_data, default=sids_converter)



if __name__ == "__main__":
    app.run(debug=True)

