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

      # d1 = "'" + (str(request.args.get("start"))) + "'"
      
      
      d0 = "'2020-03-01" #for tea made to start date
      d00 = "'2019-03-01'" #last year tea made start date
      d1 = "'2020-07-02'"
      d11 = "'2019-07-02'" #last years end date

      #[TM TODAY]
      val = "TMTENTRY.TM_VAL "
      tab = "TMENTRY"
      cur.execute(f'''select {val} from {tab} where date = {d1} ''')
      rv = cur.fetchall()

      #[TM TODATE]
      val1 = "sum(TMENTRY.TM_VAL)"
      tab1 = "TMENTRY"
      cur1.execute(f'''select {val1} from {tab1} where DATE >= {d0} AND DATE <= {d1} ''')
      rv1 = cur1.fetchall()

      #[TM TODATE LAST YEAR]
      val2 = "sum(TMENTRY.TM_VAL)"
      tab2 = "TMENTRY"
      cur2.execute(f'''select {val2} from {tab2} where DATE >= {d00} AND DATE <= {d1} ''')
      rv2 = cur2.fetchall()

      #[RECOVERY % TODAY
      val3 = ((SUM(FIELDENTRY.GL_VAL))/(TMENTRY.TM_VAL))
      tab3 = 'TMENTRY , FIELDENTRY'
      joi3 = TMENTRY.DATE = FIELDENTRY.DATE
      cur3.execute(f'''select {val3} from {tab3} where {joi3} DATE = {d1} ''')

      #[RECOVERY % TO DATE
      val4 = ((SUM(FIELDENTRY.GL_VAL))/(sum(TMENTRY.TM_VAL))
      tab4 = 'TMENTRY , FIELDENTRY'
      joi4 = TMENTRY.DATE = FIELDENTRY.DATE
      cur4.execute(f'''select {val4} from {tab4} where {joi4} DATE >= {d0} and DATE <= {d1}''')


      column_headers = ['TM TODAY','TM TODATE', 'TM TODATE LY', 'RECOVERY % TODAY','RECOVERY% TODATE' ]

      
      def sids_converter(o):
            if isinstance(o, datetime.date):
                  return str(o.year) + str("/") + str(o.month) + str("/") + str(o.day)




if __name__ == "__main__":
    app.run(debug=True)

    


