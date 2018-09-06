import pandas as pd
import os
cc=0
vv=0
#definir las columnas para los dataframes
columns_ventas = ['Estabelecimento' , 'Categoria do Estabelecimento' , 'Adquirente' , 'Data da Venda' , 'Data do Pagamento' , 'Forma Pagamento' , 'Tipo' , 'Bandeira' , 'Período Contábil' , 'Meio de Captura' , 'Valor Total' , 'Vendas Adquirente' , 'Quantidade Adquirente' , 'Valor Total' , 'Vendas ERP' , 'Quantidade ERP' , 'Valor Vendas Conciliadas' , 'Quantidade de Vendas Conciliadas' , 'Valor Vendas Conciliadas Manualmente' , 'Quantidade de Vendas Conciliadas Manualmente' , 'Valor Vendas Divergentes' , 'Quantidade de Vendas Divergentes' , 'Valor Vendas Justificadas' , 'Quantidade de Vendas Justificadas' , 'Valor Em Aberto Adquirente' , 'Quantidade de Em Aberto Adquirente' , 'Valor Em Aberto ERP' , 'Quantidade Em Aberto ERP' , 'Vlr. Anulado ERP' , 'Qtde. Anulado ERP	Valor Desfeita ERP' , 'Quantidade Desfeita ERP' , 'Conciliação']
columns_canc = ['Estabelecimento' , 'Adquirente	Bandeira' , 'Período Contábil' , 'Dt. Venda' , 'Dt. Cancelamento' , 'Tipo Cancelamento' , 'Qtd. Cancelamentos na Adq.' , 'Vl. Bruto Cancelamento na Adq.' , 'Vl. Líquido Cancelamento na Adq.' , 'Qtd. Cancelamentos ERP' , 'Vl. Cancelamento ERP' , 'Vl. Bruto Venda' , 'Vl. Comissão Venda' , 'Vl. Líquido Venda	Conciliação' , 'Resultado']
archivos = os.listdir('C:\\Users\\carogonzalez\\Desktop\\Equals')  
cant=len(archivos)
#crear data frame con archivo CSV (según su nombre) y luego ir agregando info a cada dataframe
for i in range (0,cant):
    if archivos[i].find('cancelamentos') > 0 :
        cc=cc+1
        if cc==1:
            frame_canc = pd.read_csv('C:\\Users\\carogonzalez\\Desktop\\Equals\\' + archivos[i], sep=';', skiprows=1, names=columns_canc, encoding='latin-1')
        else:
            c = pd.read_csv('C:\\Users\\carogonzalez\\Desktop\\Equals\\' + archivos[i], sep=';', skiprows=1, names=columns_canc, encoding='latin-1')
            frame_canc = frame_canc.append(c) 
    else:
        vv = vv+1
        if vv==1:
           frame_ventas = pd.read_csv('C:\\Users\\carogonzalez\\Desktop\\Equals\\' + archivos[i], sep=';', skiprows=1, names=columns_ventas, encoding='latin-1') 
        else:
            v = pd.read_csv('C:\\Users\\carogonzalez\\Desktop\\Equals\\' + archivos[i], sep=';', skiprows=1, names=columns_ventas, encoding='latin-1')
            frame_ventas = frame_ventas.append(v)
            

