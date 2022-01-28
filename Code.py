import pandas as pd
import numpy as np
import datetime


df=pd.read_csv('C:/Users/escal/Documents/ChallengeBous/cartera.txt', sep="|")
print(df.groupby("Region").nunique())
#De aqui obtenemos que no es reelevante la región porque todos los clientes se concentran en Quintana Roo, CDMX y Nuevo León
df['FECHA INICIO']=pd.to_datetime(df['FECHA INICIO'],format="%Y-%m-%d %H:%M:%S")
df['FECHA_DE_TERMINACION']=pd.to_datetime(df['FECHA INICIO'],format="%Y-%m-%d")
df['ANIO_INICIO']=df['FECHA INICIO'].dt.year
print(df.groupby("ANIO_INICIO").nunique())




