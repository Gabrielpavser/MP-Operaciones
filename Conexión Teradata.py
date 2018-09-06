import teradata as td
import pandas as pd
from teradata import tdodbc
udaExec = td.UdaExec (appName="test", version="1.0",logConsole=False)
with udaExec.connect(method="ODBC", system="teradata.melicloud.com",username="introducirusuariotera", password="introducircontraseñatera") as session:
    query= "select * from whowner.bt_mp_pay_payments where pay_payment_id = 3349200510;"
    df = pd.read_sql(query,session)


