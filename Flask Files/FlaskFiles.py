from flask import Flask
from flask_mysqldb import MySQL
import json, datetime
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
mysql = MySQL(app)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = "GlenDB"


@app.route('/cultdaily',methods=['GET', 'POST'])
@cross_origin()
def cultivationdaily():
      cur = mysql.connection.cursor()
      d1 = "'2020-07-01'"
      d2 = "'2020-07-14'"
      #d1 = "'" + (str(request.args.get("start"))) + "'"
      #d2 = "'" + (str(request.args.get("end"))) + "'"

      con = "FIELDENTRY.DATE, JOBTAB.JOB_NAME, SECTAB.SEC_NAME, SQUTAB.SQU_NAME"
      val = "MND_VAL, AREA_VAL"
      fom = "ROUND((MND_VAL/AREA_VAL),2)"
      con2 = "DIVTAB.DIV_NAME"
      tab = "FIELDENTRY,SQUTAB,JOBTAB,SECTAB,DIVTAB"
      joi = "FIELDENTRY.SQU_ID = SQUTAB.SQU_ID AND FIELDENTRY.JOB_ID=JOBTAB.JOB_ID AND FIELDENTRY.SEC_ID=SECTAB.SEC_ID AND DIVTAB.DIV_ID=SECTAB.DIV_ID"
      job = "(FIELDENTRY.JOB_ID = 2 or FIELDENTRY.JOB_ID = 3 or FIELDENTRY.JOB_ID = 4)"
      cur.execute(f'''select {con} , {val} , {fom} , {con2} from {tab} where {joi} and date >={d1} and date <={d2} and {job}''')
      rv = cur.fetchall()

      row_headers = ['Date', 'Job_Name', 'Section_Name', 'Squad_Name', 'Mandays', 'AreaCovered', 'Mnd/Area', 'Division']
      json_data = []

      def sids_converter(o):
            if isinstance(o, datetime.date):
                  return str(o.year) + str("/") + str(o.month) + str("/") + str(o.day)

      for result in rv:
            json_data.append(dict(zip(row_headers , result)))
      return json.dumps(json_data, default=sids_converter)


#2
@app.route('/cultgroup',methods=['GET', 'POST'])
@cross_origin()
def cultivationgroup():
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


#3
@app.route('/pluckdaily',methods=['GET', 'POST'])
@cross_origin()

def pluckingdaily():
      cur = mysql.connection.cursor()
      d1 = "'2020-07-01'"
      d2 = "'2020-07-02'"
      #d1 = "'" + (str(request.args.get("start"))) + "'"
      #d2 = "'" + (str(request.args.get("end"))) + "'"

      con = "fieldentry.date,SECTAB.SEC_NAME,SQUTAB.SQU_NAME"
      val = "FIELDENTRY.MND_VAL, FIELDENTRY.GL_VAL, FIELDENTRY.AREA_VAL"
      fom = "ROUND((GL_VAL/MND_VAL),2), ROUND((GL_VAL/AREA_VAL),2),ROUND((MND_VAL/AREA_VAL),2)"
      con2 = "DIVTAB.DIV_NAME, SECTAB.SEC_PRUNE , SECTAB.SEC_JAT, SECTAB.SEC_AREA"
      tab = "FIELDENTRY,SQUTAB,JOBTAB,SECTAB,DIVTAB"
      joi = "FIELDENTRY.SQU_ID = SQUTAB.SQU_ID AND FIELDENTRY.JOB_ID=JOBTAB.JOB_ID AND FIELDENTRY.SEC_ID=SECTAB.SEC_ID AND DIVTAB.DIV_ID=SECTAB.DIV_ID"
      job = "(FIELDENTRY.JOB_ID = 1 )"
      cur.execute(f'''select {con} , {val} , {fom} , {con2} from {tab} where {joi} and date >={d1} and date <={d2} and {job}''')

      row_headers = ['Date', 'Section_Name', 'Squad_Name', 'Mandays', 'Greenleaf', 'AreaCovered', 'Gl/Mnd', 'Gl/Ha', 'Mnd/Ha','Division','Prune','Jat', "Sec Area"]
      rv = cur.fetchall()
      json_data = []

      def sids_converter(o):
            if isinstance(o, datetime.date):
                  return str(o.year) + str("/") + str(o.month) + str("/") + str(o.day)

      for result in rv:
            json_data.append(dict(zip(row_headers , result)))
      return json.dumps(json_data, default=sids_converter)


#4
@app.route('/pluckgroup',methods=['GET', 'POST'])
@cross_origin()

def pluckinggroup():
      cur = mysql.connection.cursor()
      #d1 = "'" + (str(request.args.get("start"))) + "'"
      #d2 = "'" + (str(request.args.get("end"))) + "'"
      #grp = "'" + (str(request.args.get("grpby"))) + "'"
      d1 = "'2020-07-01'"
      d2 = "'2020-07-02'"
      grp = "Squad"

      if grp == 'Section':
            con = "SECTAB.SEC_NAME"
            val = "sum(FIELDENTRY.MND_VAL), sum(FIELDENTRY.GL_VAL), sum(FIELDENTRY.AREA_VAL)"
            fom = "ROUND((sum(GL_VAL)/sum(MND_VAL)),2), ROUND((sum(GL_VAL)/sum(AREA_VAL)),2),ROUND((sum(MND_VAL)/sum(AREA_VAL)),2)"
            tab = "FIELDENTRY,SQUTAB,JOBTAB,SECTAB,DIVTAB"
            joi = "FIELDENTRY.SQU_ID = SQUTAB.SQU_ID AND FIELDENTRY.JOB_ID=JOBTAB.JOB_ID AND FIELDENTRY.SEC_ID=SECTAB.SEC_ID AND DIVTAB.DIV_ID=SECTAB.DIV_ID"
            job = "(FIELDENTRY.JOB_ID = 1 )"
            cur.execute(f'''select {con} , {val} , {fom} from {tab} where {joi} and date >={d1} and date <={d2} and {job} ''')
            row_headers = ['Section_Name', 'Mandays', 'Greenleaf', 'AreaCovered', 'GL/Mnd', 'GL/Area', 'Mnd/Area']
            rv = cur.fetchall()

      if grp == 'Division':
            con = "DIVTAB.DIV_NAME"
            val = "sum(FIELDENTRY.MND_VAL), sum(FIELDENTRY.GL_VAL), sum(FIELDENTRY.AREA_VAL)"
            fom = "ROUND((SUM(GL_VAL)/SUM(MND_VAL)),2), ROUND((sum(GL_VAL)/sum(AREA_VAL)),2),ROUND((SUM(MND_VAL)/SUM(AREA_VAL)),2)"
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
            fom = "ROUND((sum(GL_VAL)/sum(MND_VAL)),2), ROUND((sum(GL_VAL)/sum(AREA_VAL)),2),ROUND((sum(MND_VAL)/sum(AREA_VAL)),2)"
            tab = "FIELDENTRY,SQUTAB,JOBTAB,SECTAB,DIVTAB"
            joi = "FIELDENTRY.SQU_ID = SQUTAB.SQU_ID AND FIELDENTRY.JOB_ID=JOBTAB.JOB_ID AND FIELDENTRY.SEC_ID=SECTAB.SEC_ID AND DIVTAB.DIV_ID=SECTAB.DIV_ID"
            job = "(FIELDENTRY.JOB_ID = 1 )"
            cur.execute(f'''select {con} , {val} , {fom} from {tab} where {joi} and date >={d1} and date <={d2} and {job} group by SQUTAB.SQU_ID order by SQUTAB.SQU_NAME asc''')

            row_headers = ['Squad', 'Mandays', 'Greenleaf', 'AreaCovered', 'GL/Mnd', 'GL/Area', 'Mnd/Area']
            rv = cur.fetchall()

      json_data = []
      def sids_converter(o):
            if isinstance(o, datetime.date):
                  return str(o.year) + str("/") + str(o.month) + str("/") + str(o.day)

      for result in rv:
            json_data.append(dict(zip(row_headers, result)))
      return json.dumps(json_data, default=sids_converter)


#5
@app.route('/mnddeploy',methods=['GET', 'POST'])
@cross_origin()

def mandaydeployment():
      cur = mysql.connection.cursor()
      # d1 = "'" + (str(request.args.get("start"))) + "'"
      # d2 = "'" + (str(request.args.get("end"))) + "'"
      d1 = "'2020-07-01'"
      d2 = "'2020-07-04'"

      con = "JOBTAB.JOB_NAME"
      val = "SUM(FIELDENTRY.MND_VAL)"
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


#6
@app.route('/fuelreport',methods=['GET', 'POST'])
@cross_origin()

def fuelreport():
      cur = mysql.connection.cursor()
      # d1 = "'" + (str(request.args.get("start"))) + "'"
      # d2 = "'" + (str(request.args.get("end"))) + "'"
      d1 = "'2020-07-01'"
      d2 = "'2020-07-02'"

      con = " MACHINETAB.MACH_NAME"
      fom = " sum(FUELENTRY.FUEL_VAL), sum(TM_VAL), ROUND((SUM(TM_VAL)/sum(FUELENTRY.FUEL_VAL)),2)"
      tab = "FUELENTRY, MACHINETAB, FUELTAB, TMENTRY"
      joi = "FUELENTRY.FUEL_ID = FUELTAB.FUEL_ID AND FUELENTRY.MACH_ID = MACHINETAB.MACH_ID AND TMENTRY.TM_DATE = FUELENTRY.DATE"
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


#7
@app.route('/teastock',methods=['GET', 'POST'])
@cross_origin()

def teastock():
      cur = mysql.connection.cursor()
      # d1 = "'" + (str(request.args.get("start"))) + "'"
      d1 = "'2020-07-03'"

      con = "TEAGRADETAB.TEAGRADE_NAME, STOCKENTRY.KG_VAL"
      tab = "STOCKENTRY, TEAGRADETAB"
      joi = "(STOCKENTRY.TEAGRADE_ID = TEAGRADETAB.TEAGRADE_ID)"
      cur.execute(f'''select {con} from {tab} where {joi} and DATE = {d1}''')
      row_headers = ['Grade', 'Kg' ]
      rv = cur.fetchall()
      json_data = []

      def sids_converter(o):
            if isinstance(o, datetime.date):
                  return str(o.year) + str("/") + str(o.month) + str("/") + str(o.day)

      for result in rv:
            json_data.append(dict(zip(row_headers, result)))
      return json.dumps(json_data, default=sids_converter)


#8
@app.route('/teamade', methods=['GET', 'POST'])
@cross_origin()
def displayteamade():
    cur = mysql.connection.cursor()
    cur1 = mysql.connection.cursor()
    cur2 = mysql.connection.cursor()
    cur3 = mysql.connection.cursor()
    cur4 = mysql.connection.cursor()
    rv = []

    # d1 = "'" + (str(request.args.get("start"))) + "'"

    d0 = "'2020-03-01'"  # start date current year
    d00 = "'2019-03-01'"  # start date last year
    d1 = "'2020-07-03'"  # current date
    d11 = "'2019-07-02'"  # end date last year

    # [TM TODAY]
    val = "TMENTRY.TM_VAL "
    tab = "TMENTRY"
    cur.execute(f'''select {val} from {tab} where TM_DATE = {d1} ''')
    rv.append(cur.fetchall()[0][0])

    # [TM TODATE]
    val1 = "sum(TMENTRY.TM_VAL)"
    tab1 = "TMENTRY"
    cur1.execute(f'''select {val1} from {tab1} where TM_DATE >= {d0} AND TM_DATE <= {d1} ''')
    rv.append(cur1.fetchall()[0][0])

    # [TM TODATE LAST YEAR]
    val2 = "sum(TMENTRY.TM_VAL)"
    tab2 = "TMENTRY"
    cur2.execute(f'''select {val2} from {tab2} where TM_DATE >= {d00} AND TM_DATE <= {d11} ''')
    rv.append(cur2.fetchall()[0][0])

    # [RECOVERY % TODAY
    val3 = " ROUND(SUM(FIELDENTRY.GL_VAL)/SUM(TMENTRY.TM_VAL),4) * 100 "
    tab3 = "TMENTRY , FIELDENTRY"
    joi3 = "(TMENTRY.TM_DATE = FIELDENTRY.DATE) and (TMENTRY.TM_DATE="
    cur3.execute(f'''select {val3} from {tab3} where {joi3}{d1})''')
    rv.append(cur3.fetchall()[0][0])

    # [RECOVERY % TO DATE
    val4 = " ROUND(SUM(FIELDENTRY.GL_VAL)/SUM(TMENTRY.TM_VAL),4) * 100 "
    tab4 = 'TMENTRY , FIELDENTRY'
    joi4 = "(TMENTRY.TM_DATE = FIELDENTRY.DATE) and (TMENTRY.TM_DATE>="
    cur4.execute(f'''select {val4} from {tab4} where {joi4}{d0}) and (TMENTRY.TM_DATE<={d1})''')
    rv.append(cur4.fetchall()[0][0])

    def sids_converter(o):
        if isinstance(o, datetime.date):
            return str(o.year) + str("/") + str(o.month) + str("/") + str(o.day)

    column_headers = ['TM Today', 'TM Todate', 'TM Todate LY', 'Recovery % Today', 'Recovery% Todate']
    json_data = []
    json_data.append(dict(zip(column_headers, rv)))
    return json.dumps(json_data, default=sids_converter)


#9##
@app.route('/GL',methods=['GET', 'POST'])
@cross_origin()

def greenleaf():
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


#10##
@app.route('/gradeper',methods=['GET', 'POST'])
@cross_origin()

def gradepercent():
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

#11
@app.route('/invoicelist',methods=['GET', 'POST'])
@cross_origin()

def invoicelist():
      cur = mysql.connection.cursor()

      con = "INVOICEENTRY.INVOICE_NO, TEAGRADETAB.TEAGRADE_NAME"
      val = "INVOICEENTRY.NET_WT , INVOICEENTRY.PAPERSACKS, INVOICEENTRY.PACKDATE,INVOICEENTRY.DISPATCHDATE"
      tab = "INVOICEENTRY,TEAGRADETAB"
      joi = "INVOICEENTRY.TEAGRADE_ID=TEAGRADETAB.TEAGRADE_ID"
      cur.execute(f'''select {con} , {val} from {tab} where {joi}''')
      row_headers = ['Inv No','Grade', 'Net Wt.','Papersacks','Packdate','Dispatch Date']
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

