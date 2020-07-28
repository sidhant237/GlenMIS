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

@app.route('/gradeper',methods=['GET', 'POST'])
@cross_origin()

def displayfuelreport():
      cur = mysql.connection.cursor()
      # d1 = "'" + (str(request.args.get("start"))) + "'"
      # d2 = "'" + (str(request.args.get("end"))) + "'"
      d1 = "'2020-07-01'"
      d2 = "'2020-07-02'"

      con = "TEAGRADETAB.TEAGRADE_NAME , SORTENTRY.SORT_KG"
      fom = "ROUND((SUM(SORTENTRY.SORT_KG))/("
      tab = "SORTENTRY , TEAGRADETAB"
      joi = "SORTENTRY.TEAGRADE_ID = TEAGRADETAB.TEAGRADE_ID"
      cur.execute(f'''select {con} , {fom}  from {tab} where {joi} and date >= {d1} and date <= {d2} group by MACHINETAB.MACH_NAME''')
      rv = cur.fetchall()

      row_headers = ['Machine', 'Fuel Used' , 'TM', 'TM/Fuel']
      json_data = []

      def sids_converter(o):
            if isinstance(o, datetime.date):
                  return str(o.year) + str("/") + str(o.month) + str("/") + str(o.day)

      for row in rv:
          json_data.append(dict(zip(row_headers,row)))
      return json.dumps(json_data, default=sids_converter)




if __name__ == "__main__":
    app.run(debug=True)

