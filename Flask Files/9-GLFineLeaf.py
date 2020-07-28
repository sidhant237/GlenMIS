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

@app.route('/GL',methods=['GET', 'POST'])
@cross_origin()

def displayteamade():
      cur = mysql.connection.cursor()
      cur1 = mysql.connection.cursor()
      cur2 = mysql.connection.cursor()
      # d1 = "'" + (str(request.args.get("start"))) + "'"
      # d11 = "'" + (str(request.args.get("end"))) + "'"
      # grp = "'" + (str(request.args.get("grpby"))) + "'"
      d1 = "'2020-07-02'"
      d11 = "'2019-07-02'"
      rv = []
      column_headers = ['1', '2', '3', '4']

      #GL TODAY
      val = "DIVTAB.DIV_NAME, sum(GL_VAL)"
      tab = "FIELDENTRY, DIVTAB, SECTAB"
      joi = "(FIELDENTRY.SEC_ID=SECTAB.SEC_ID) AND (SECTAB.DIV_ID = DIVTAB.DIV_ID)"
      job = "FIELDENTRY.JOB_ID = 1"
      cur.execute(f'''select {val} from {tab} where {joi} AND {job} and date = {d1} GROUP BY DIVTAB.DIV_NAME''')
      rv.append (cur.fetchall()[0[0]])

      #GLTODAY LY
      val1 = "sum(GL_VAL)"
      tab1 = "FIELDENTRY, DIVTAB, SECTAB"
      joi1 = "(FIELDENTRY.SEC_ID=SECTAB.SEC_ID) AND (SECTAB.DIV_ID = DIVTAB.DIV_ID)"
      job1 = "FIELDENTRY.JOB_ID = 1"
      cur1.execute(f'''select {val1} from {tab1} where {joi1} AND {job1} and date = {d11} GROUP BY DIVTAB.DIV_NAME''')
      rv.append (cur1.fetchall()[0[0]])

      # FINE LEAF% TODAYS GL
      val2 = 'sum(FL_PER)'
      tab2 = "FLENTRY, DIVTAB"
      joi2 = "(FLENTRY.DIV_ID = DIVTAB.DIV_ID)"
      cur2.execute(f'''select {val2} from {tab2} where {joi2} and date = {d1} GROUP BY DIVTAB.DIV_ID''')
      rv.append(cur2.fetchall()[0[0]])


      def sids_converter(o):
            if isinstance(o, datetime.date):
                  return str(o.year) + str("/") + str(o.month) + str("/") + str(o.day)

      json_data = []
      json_data.append(dict(zip(column_headers, rv)))
      return json.dumps(json_data, default=sids_converter)


if __name__ == "__main__":
    app.run(debug=True)




