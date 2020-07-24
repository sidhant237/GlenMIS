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
      cur2 = mysql.connection.cursor()
      cur3 = mysql.connection.cursor()
      cur4 = mysql.connection.cursor()
      rv=[]

      # d1 = "'" + (str(request.args.get("start"))) + "'"
      

      d0 = "'2020-03-01'"  #start date current year
      d00 = "'2019-03-01'" #start date last year
      d1 = "'2020-07-02'" #current date
      d11 = "'2019-07-02'" #end date last year

      #[TM TODAY]
      val = "TMENTRY.TM_VAL "
      tab = "TMENTRY"
      cur.execute(f'''select {val} from {tab} where TM_DATE = {d1} ''')
      rv.append (cur.fetchall()[0][0])

      #[TM TODATE]
      val1 = "sum(TMENTRY.TM_VAL)"
      tab1 = "TMENTRY"
      cur1.execute(f'''select {val1} from {tab1} where TM_DATE >= {d0} AND TM_DATE <= {d1} ''')
      rv.append (cur1.fetchall()[0][0])

      #[TM TODATE LAST YEAR]
      val2 = "sum(TMENTRY.TM_VAL)"
      tab2 = "TMENTRY"
      cur2.execute(f'''select {val2} from {tab2} where TM_DATE >= {d00} AND TM_DATE <= {d11} ''')
      rv.append (cur2.fetchall()[0][0])

      #[RECOVERY % TODAY
      val3 = " ROUND(SUM(FIELDENTRY.GL_VAL)/SUM(TMENTRY.TM_VAL),4) * 100 "
      tab3 = "TMENTRY , FIELDENTRY"
      joi3 = "(TMENTRY.TM_DATE = FIELDENTRY.DATE) and (TMENTRY.TM_DATE="
      cur3.execute(f'''select {val3} from {tab3} where {joi3}{d1})''')
      rv.append (cur3.fetchall()[0][0])

      #[RECOVERY % TO DATE
      val4 = " ROUND(SUM(FIELDENTRY.GL_VAL)/SUM(TMENTRY.TM_VAL),4) * 100 "
      tab4 = 'TMENTRY , FIELDENTRY'
      joi4 = "(TMENTRY.TM_DATE = FIELDENTRY.DATE) and (TMENTRY.TM_DATE>="
      cur4.execute(f'''select {val4} from {tab4} where {joi4}{d0}) and (TMENTRY.TM_DATE<={d1})''')
      rv.append(cur4.fetchall()[0][0])


      def sids_converter(o):
            if isinstance(o, datetime.date):
                  return str(o.year) + str("/") + str(o.month) + str("/") + str(o.day)

      column_headers = ['TM TODAY', 'TM TODATE', 'TM TODATE LY', 'RECOVERY % TODAY', 'RECOVERY% TODATE']
      json_data=[]
      json_data.append(dict(zip(column_headers, rv)))
      return json.dumps(json_data, default=sids_converter)

if __name__ == "__main__":
    app.run(debug=True)

    


