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

@app.route('/fuelreport',methods=['GET', 'POST'])
@cross_origin()

def displayfuelreport():
      cur = mysql.connection.cursor()
      cursor = mysql.connection.cursor()
      # d1 = "'" + (str(request.args.get("start"))) + "'"
      # d2 = "'" + (str(request.args.get("end"))) + "'"
      # grp = "'" + (str(request.args.get("grpby"))) + "'"
      d1 = "'2020-07-01'"
      d2 = "'2020-07-02'"
      con = "FUELENTRY.DATE, MACHINETAB.MACH_NAME , FUELTAB.FUEL_NAME"
      val = "FUELENTRY.FUEL_VAL"
      tab = "FUELENTRY, MACHINETAB, FUELTAB"
      joi = "FUELENTRY.FUEL_ID = FUELTAB.FUEL_ID and FUELENTRY.MACH_ID = MACHINETAB.MACH_ID"
      cur.execute(f'''select {con} , {val} from {tab} where {joi} and date >= {d1} and date <= {d2}''')
      rv = cur.fetchone()

      cursor.execute("select sum(FUELENTRY.FUEL_VAL) from FUELENTRY")
      rv1 = cursor.fetchone()

      row_headers = ['Date', 'Machine', 'Fuel', 'Qnty', 'sumfuel']
      json_data = []



      def sids_converter(o):
            if isinstance(o, datetime.date):
                  return str(o.year) + str("/") + str(o.month) + str("/") + str(o.day)

      #for row in rv:
      json_data.append(dict(rv))
      return json.dumps(json_data, default=sids_converter)





if __name__ == "__main__":
    app.run(debug=True)

