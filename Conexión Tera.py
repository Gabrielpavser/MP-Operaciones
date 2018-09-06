#import teradata
#host,username,password = '10.32.207.128','carogonzalez', 'Caro!1993'
#udaExec = teradata.UdaExec (appName="test", version="1.0", logConsole=False)
#udaExec.connect(method="odbc",system=host, username=username,password=password, driver="Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb)")

import teradata as td
import pandas as pd
from teradata import tdodbc
udaExec = td.UdaExec (appName="test", version="1.0",logConsole=False)
with udaExec.connect(method="ODBC", system="teradata.melicloud.com",username="carogonzalez", password="Caro$$1993") as session:
    query= "select * from whowner.bt_mp_pay_payments where pay_payment_id = 3349200510;"
    df = pd.read_sql(query,session)


