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
      cursor = mysql.connection.cursor()
      d1 = "'2020-07-01'"
      d2 = "'2020-07-01'"
      #d1 = "'" + (str(request.args.get("start"))) + "'"
      #d2 = "'" + (str(request.args.get("end"))) + "'"
      # d2 = "'" + (request.args.get('end')) + "'"
      con = "fieldentry.date,jobtab.job_Name,sectab.sec_name,squtab.squ_name"
      val = "mnd_val, area_val"
      fom = "(mnd_val/Area_Val)"
      con2 = "divtab.div_name"
      tab = "FIELDENTRY,SQUTAB,JOBTAB,SECTAB,DIVTAB"
      joi = "FIELDENTRY.SQU_ID = SQUTAB.SQU_ID AND FIELDENTRY.JOB_ID=JOBTAB.JOB_ID AND FIELDENTRY.SEC_ID=SECTAB.SEC_ID AND DIVTAB.DIV_ID=SECTAB.DIV_ID"
      job = "(FIELDENTRY.JOB_ID = 2 or FIELDENTRY.JOB_ID = 3)"
      cur.execute(f'''select {con} , {val} , {fom} , {con2} from {tab} where {joi} and date >={d1} and date <={d2} and {job}''')
      cursor.execute(f'''select {con} , {val} , {fom} , {con2} from {tab} where {joi} and date >={d1} and date <={d2} and {job}''')

      row_headers = ['Date', 'Job_Name', 'Section_Name', 'Squad_Name', 'Mandays', 'AreaCovered', 'mnd_Area', 'Division']
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

