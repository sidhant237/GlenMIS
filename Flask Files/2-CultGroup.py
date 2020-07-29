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

@app.route('/cultgroup',methods=['GET', 'POST'])
@cross_origin()

def displaycultdaily():
      cur = mysql.connection.cursor()
      # d1 = "'" + (str(request.args.get("start"))) + "'"
      # d2 = "'" + (str(request.args.get("end"))) + "'"
      # grp = "'" + (str(request.args.get("grpby"))) + "'"
      d1 = "'2020-07-01'"
      d2 = "'2020-07-14'"
      grp = "section"

      if grp == 'job':
            con = "JOBTAB.JOB_NAME"
            val = "sum(FIELDENTRY.MND_VAL)"
            val1 = "sum(FIELDENTRY.AREA_VAL)"
            fom = "ROUND((sum(FIELDENTRY.MND_VAL))/(sum(FIELDENTRY.AREA_VAL)),2)"
            tab = "FIELDENTRY,SQUTAB,JOBTAB,SECTAB,DIVTAB"
            joi = "FIELDENTRY.SQU_ID = SQUTAB.SQU_ID AND FIELDENTRY.JOB_ID=JOBTAB.JOB_ID AND FIELDENTRY.SEC_ID=SECTAB.SEC_ID AND DIVTAB.DIV_ID=SECTAB.DIV_ID"
            job = "(FIELDENTRY.JOB_ID = 2 or FIELDENTRY.JOB_ID = 3 or FIELDENTRY.JOB_ID = 4)"
            cur.execute(f'''select {con} , {val} , {val1} , {fom}  from {tab} where {joi} and date >={d1} and date <={d2} and {job} group by FIELDENTRY.JOB_ID''')
            rv = cur.fetchall()
            row_headers = ['Job Name', 'Mandays', 'Area Covered', 'Mnd/Area']

      elif grp == 'section':
            con = "SECTAB.SEC_NAME"
            val = "sum(FIELDENTRY.MND_VAL)"
            val1 = "sum(FIELDENTRY.AREA_VAL)"
            fom = "ROUND((SUM(FIELDENTRY.MND_VAL))/(SUM(FIELDENTRY.AREA_VAL)),2)"
            tab = "FIELDENTRY,SQUTAB,JOBTAB,SECTAB,DIVTAB"
            joi = "FIELDENTRY.SQU_ID = SQUTAB.SQU_ID AND FIELDENTRY.JOB_ID=JOBTAB.JOB_ID AND FIELDENTRY.SEC_ID=SECTAB.SEC_ID AND DIVTAB.DIV_ID=SECTAB.DIV_ID"
            cur.execute(f'''select {con} , {val} , {val1} , {fom}  from {tab} where {joi} and date >={d1} and date <={d2} group by FIELDENTRY.SEC_ID''')
            rv = cur.fetchall()
            row_headers = ['Section Name', 'Mandays', 'Area Covered', 'Mnd/Area']

      json_data = []

      def sids_converter(o):
            if isinstance(o, datetime.date):
                  return str(o.year) + str("/") + str(o.month) + str("/") + str(o.day)

      for result in rv:
            json_data.append(dict(zip(row_headers,result)))
      return json.dumps(json_data, default=sids_converter)


if __name__ == "__main__":
    app.run(debug=True)

