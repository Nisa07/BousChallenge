from itertools import count
import statistics as stat
from time import time
import pandas as pd
import numpy as np
import seaborn as sns
import datetime


df=pd.read_csv('C:/Users/escal/Documents/ChallengeBous/BousChallenge/cartera.txt', sep="|")
print(df.groupby("Region").nunique())
#De aqui obtenemos que no es reelevante la región porque todos los clientes se concentran en Quintana Roo, CDMX y Nuevo León
df['FECHA INICIO']=pd.to_datetime(df['FECHA INICIO'],format="%Y-%m-%d %H:%M:%S")
df['FECHA_DE_TERMINACION']=pd.to_datetime(df['FECHA INICIO'],format="%Y-%m-%d")
df['ANIO_INICIO']=df['FECHA INICIO'].dt.year
df['MES_INICIO']=df['FECHA INICIO'].dt.month
yearResume=df.groupby("ANIO_INICIO").nunique()
monthResume=df.groupby("MES_INICIO").nunique()
# Se ha obtenido un crecimiento de numero de clientes en función del pasar de los años. 
#Siendo los años más fructiferos 2020,2018 y 2021 por la cantidad de contratos y clientes adquiridos
print(yearResume['PLAZO'].mean())
#Los clientes se deciden en promedio por un plazo de 48.7 meses para terminar de rentar su auto a largo plazo

tdCliente=pd.pivot_table(df,'ID_CLIENTE','MES_INICIO','ANIO_INICIO',aggfunc='nunique')

#La seguda mitad del año es la preferida por los clientes adquirir el producto, esto sin contar el año 2020 que presento una caida de clientes a partir de marzo, solo recuperadose hasta diciembre.
tdContratos=pd.pivot_table(df,'CONTRATO','MES_INICIO','ANIO_INICIO',aggfunc='nunique')
#este comportamiento se vuelve a ver en los contratos
ContratosCliente=pd.pivot_table(df,'CONTRATO','ID_CLIENTE',aggfunc='nunique')
print(ContratosCliente['CONTRATO'].mean())
print(ContratosCliente['CONTRATO'].mode())

#Observamos que la media de contratos por cliente es de 12.7, lo que quiere decir que en promedio los clientes deciden renovar su contato en varias ocasiones.

productoCliente=pd.pivot_table(df,['ID_CLIENTE','CONTRATO'],'PRODUCTO',aggfunc='nunique')
print(productoCliente)
#El porcentaje de contratos que eligen arrendamiento y arrendamiento puro son practicamente el 50%, sin embargo solo el 20% de los clientes totales eligen un arrendamiento puro




