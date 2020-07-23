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
      # d1 = "'" + (str(request.args.get("start"))) + "'"
      # d2 = "'" + (str(request.args.get("end"))) + "'"
      # grp = "'" + (str(request.args.get("grpby"))) + "'"
      d1 = "'2020-07-01'"

      #1
      val = "FINEPERENTRY.FL_ID,DIVTAB2.DIV_NAME2, FINEPERENTRY.GL19_VAL, FINEPERENTRY.FL_PER "
      tab = "FINEPERENTRY ,DIVTAB2"
      joi = "FINEPERENTRY.DIV_ID2=DIVTAB2.DIV_ID2"
      cur.execute(f'''select {val} from {tab} where {joi} and date = {d1}''')
      rv = cur.fetchall()

      #2
      val = "sum(FINEPERENTRY.GL19_VAL)"
      tab = "FINEPERENTRY ,DIVTAB2"
      joi = "FINEPERENTRY.DIV_ID2=DIVTAB2.DIV_ID2"
      cur1.execute(f'''select {val} from {tab} where {joi} group by FINEPERENTRY.DIV_ID2 ''')
      rv1 = cur1.fetchall()

      #for row1 in rv1:
      #       json_data.append(dict(zip(row_headers, row1)))
      #return json.dumps(json_data)
      json_data = []
      json_data1 = []

      row_headers = ['fl id', 'Division', 'GL Today', 'FL% ToDay' ]
      row_headers1 = [ 'GL ToDate']
      for row in rv:
            json_data.append(dict(zip(row_headers,row)))
      return json.dumps(json_data)

            for row1 in rv1:
                  json_data1.append(dict(zip(row_headers1, row1)))
            return json.dumps(json_data1)







if __name__ == "__main__":
    app.run(debug=True)

      #def sids_converter(o):
            #if isinstance(o, datetime.date):
                  #return str(o.year) + str("/") + str(o.month) + str("/") + str(o.day)

      #for result in rv:
            #json_data.append(dict(zip(row_headers, result)))
      #return json.dumps(json_data, default=sids_converter)



