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

@app.route('/teamade',methods=['GET', 'POST'])
@cross_origin()

def displayteamade():
      cur = mysql.connection.cursor()
      cur1 = mysql.connection.cursor()
      # d1 = "'" + (str(request.args.get("start"))) + "'"
      # d2 = "'" + (str(request.args.get("end"))) + "'"
      # grp = "'" + (str(request.args.get("grpby"))) + "'"
      d1 = "'2020-07-02'"
      val = "FACTORYENTRY.KG_VAL "
      tab = "FACTORYENTRY,TEATYPETAB"
      joi = "FACTORYENTRY.TEATYPE_ID=TEATYPETAB.TEATYPE_ID"
      cur.execute(f'''select {val} from {tab} where {joi} and FACTORYENTRY.TEATYPE_ID=3 and date = {d1} ''')
      rv = cur.fetchall()

      val1 = "sum(FACTORYENTRY.KG_VAL)"
      tab1 = "FACTORYENTRY,TEATYPETAB"
      joi1 = "FACTORYENTRY.TEATYPE_ID=TEATYPETAB.TEATYPE_ID"
      cur1.execute(f'''select {val1} from {tab1} where {joi1} and FACTORYENTRY.TEATYPE_ID=3 ''')
      rv1 = cur1.fetchall()
      row_headers = ['TM Today', 'TM Todate']
      json_data = []
      for row in rv:
            x = row
      for row1 in rv1:
            y = row1
      rv2 = x + y
      json_data.append(dict(zip(row_headers,rv2)))

      return json.dumps(json_data)




      #rv2 = (rv + rv1)
      #json_data.append(rv2)
      #return json.dumps(dict(zip(row_headers,rv2)))



if __name__ == "__main__":
    app.run(debug=True)

      #def sids_converter(o):
            #if isinstance(o, datetime.date):
                  #return str(o.year) + str("/") + str(o.month) + str("/") + str(o.day)

      #for result in rv:
            #json_data.append(dict(zip(row_headers, result)))
      #return json.dumps(json_data, default=sids_converter)



