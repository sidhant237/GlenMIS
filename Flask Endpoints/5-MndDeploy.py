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

@app.route('/mnddeploy',methods=['GET', 'POST'])
@cross_origin()

def displaymnddeploy():
      cur = mysql.connection.cursor()
      # d1 = "'" + (str(request.args.get("start"))) + "'"
      # d2 = "'" + (str(request.args.get("end"))) + "'"
      d1 = "'2020-07-01'"
      d2 = "'2020-07-12'"
      con = "JOBTAB.JOB_NAME"
      val = "sum(FIELDENTRY.MND_VAL)"
      tab = "FIELDENTRY,JOBTAB"
      joi = "FIELDENTRY.JOB_ID=JOBTAB.JOB_ID"
      cur.execute(f'''select {con} , {val} from {tab} where {joi} and date >={d1} and date <={d2} group by FIELDENTRY.JOB_ID''')
      row_headers = ['Job Name', 'Mandays']
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

