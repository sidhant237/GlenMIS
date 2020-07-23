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

@app.route('/invoicelist',methods=['GET', 'POST'])
@cross_origin()

def displayfuelreport():
      cur = mysql.connection.cursor()

      con = "FACTORYENTRY.INV_NO, TEAGRADETAB.TEAGRADE_NAME"
      val = "FACTORYENTRY.KG_VAL , FACTORYENTRY.PACKDATE"
      tab = "FACTORYENTRY,TEAGRADETAB,TEATYPETAB"
      joi = "FACTORYENTRY.TEAGRADE_ID=TEAGRADETAB.TEAGRADE_ID and FACTORYENTRY.TEATYPE_ID = TEATYPETAB.TEATYPE_ID"
      cur.execute(f'''select {con} , {val} from {tab} where {joi} and (FACTORYENTRY.TEATYPE_ID = 1)''')
      row_headers = ['Inv No','Grade', 'Qnty','Pack Date']
      rv = cur.fetchall()
      json_data = []

      def sids_converter(o):
            if isinstance(o, datetime.date):
                  return str(o.year) + str("/") + str(o.month) + str("/") + str(o.day)

      for result in rv:
            json_data.append(dict(zip(row_headers, result)))
      return json.dumps(json_data, default=sids_converter)






if __name__ == "__main__":
    app.run(debug=True)

