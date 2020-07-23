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

@app.route('/pluckgroup',methods=['GET', 'POST'])
@cross_origin()

def displaypluckgroup():
      cur = mysql.connection.cursor()
      #d1 = "'" + (str(request.args.get("start"))) + "'"
      #d2 = "'" + (str(request.args.get("end"))) + "'"
      #grp = "'" + (str(request.args.get("grpby"))) + "'"
      d1 = "'2020-07-01'"
      d2 = "'2020-07-03'"
      #grp = "Section"
      grp = "Squad"
      #grp = "Squad"

      if grp == 'Section':
            con = "SECTAB.SEC_NAME"
            val = "sum(FIELDENTRY.MND_VAL), sum(FIELDENTRY.GL_VAL), sum(FIELDENTRY.AREA_VAL)"
            fom = "(sum(GL_VAL)/sum(MND_VAL)), (sum(GL_VAL)/sum(AREA_VAL)),(sum(MND_VAL)/sum(AREA_VAL))"
            #con2 = "DIVTAB.DIV_NAME, SECTAB.SEC_PRUNE , SECTAB.SEC_JAT"
            tab = "FIELDENTRY,SQUTAB,JOBTAB,SECTAB,DIVTAB"
            joi = "FIELDENTRY.SQU_ID = SQUTAB.SQU_ID AND FIELDENTRY.JOB_ID=JOBTAB.JOB_ID AND FIELDENTRY.SEC_ID=SECTAB.SEC_ID AND DIVTAB.DIV_ID=SECTAB.DIV_ID"
            job = "(FIELDENTRY.JOB_ID = 1 )"
            cur.execute(f'''select {con} , {val} , {fom} from {tab} where {joi} and date >={d1} and date <={d2} and {job} group by fieldentry.sec_id''')

            row_headers = ['Section_Name', 'Mandays', 'Greenleaf', 'AreaCovered', 'GL/Mnd', 'GL/Area', 'Mnd/Area']
            rv = cur.fetchall()


      if grp == 'Division':
            con = "DIVTAB.DIV_NAME"
            val = "sum(FIELDENTRY.MND_VAL), sum(FIELDENTRY.GL_VAL), sum(FIELDENTRY.AREA_VAL)"
            fom = "(sum(GL_VAL)/sum(MND_VAL)), (sum(GL_VAL)/sum(AREA_VAL)),(sum(MND_VAL)/sum(AREA_VAL))"
            # con2 = "DIVTAB.DIV_NAME, SECTAB.SEC_PRUNE , SECTAB.SEC_JAT"
            tab = "FIELDENTRY,SQUTAB,JOBTAB,SECTAB,DIVTAB"
            joi = "FIELDENTRY.SQU_ID = SQUTAB.SQU_ID AND FIELDENTRY.JOB_ID=JOBTAB.JOB_ID AND FIELDENTRY.SEC_ID=SECTAB.SEC_ID AND DIVTAB.DIV_ID=SECTAB.DIV_ID"
            job = "(FIELDENTRY.JOB_ID = 1 )"
            cur.execute(f'''select {con} , {val} , {fom} from {tab} where {joi} and date >={d1} and date <={d2} and {job} group by SECTAB.DIV_ID''')

            row_headers = ['Division', 'Mandays', 'Greenleaf', 'AreaCovered', 'GL/Mnd', 'GL/Area', 'Mnd/Area']
            rv = cur.fetchall()


      if grp == 'Squad':
            con = "SQUTAB.SQU_NAME"
            val = "sum(FIELDENTRY.MND_VAL), sum(FIELDENTRY.GL_VAL), sum(FIELDENTRY.AREA_VAL)"
            fom = "(sum(GL_VAL)/sum(MND_VAL)), (sum(GL_VAL)/sum(AREA_VAL)),(sum(MND_VAL)/sum(AREA_VAL))"
            # con2 = "DIVTAB.DIV_NAME, SECTAB.SEC_PRUNE , SECTAB.SEC_JAT"
            tab = "FIELDENTRY,SQUTAB,JOBTAB,SECTAB,DIVTAB"
            joi = "FIELDENTRY.SQU_ID = SQUTAB.SQU_ID AND FIELDENTRY.JOB_ID=JOBTAB.JOB_ID AND FIELDENTRY.SEC_ID=SECTAB.SEC_ID AND DIVTAB.DIV_ID=SECTAB.DIV_ID"
            job = "(FIELDENTRY.JOB_ID = 1 )"
            cur.execute(f'''select {con} , {val} , {fom} from {tab} where {joi} and date >={d1} and date <={d2} and {job} group by SQUTAB.SQU_ID''')

            row_headers = ['Squad', 'Mandays', 'Greenleaf', 'AreaCovered', 'GL/Mnd', 'GL/Area', 'Mnd/Area']
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

