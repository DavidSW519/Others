import pandas as pd
import numpy as np

import locale
locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')
pd.options.display.max_rows = 100

def moneda(x):
    return locale.currency(float(x),grouping=True)

trabajo1 = 'SCotiabank'
trabajo2 = 'HDI'


sueldo1 = 37_000
deducciones1 = 0.8
aguinaldo_dias1 = 30
vacaciones_dias1 = 20
prima1 = 0.5
bono1 = 3_300 + 4000 # Vales Despensa
dias1 = 3 # DIAS EN OFICINA
transporte1 = 80
comida1 = 100
otros_gastos1 = 200 # GASTOS SEMANALES EXTRA
fondo_ahorro1 = 0.06
fondo_ahorro_tot1 = sueldo1*fondo_ahorro1*2
sueldo1 = sueldo1*(deducciones1-fondo_ahorro1)

sueldo2 = 31_000 
deducciones2 = 0.8
aguinaldo_dias2 = 30
vacaciones_dias2 = 15
prima2 = 1
bono2 = sueldo2 * 0.1 # Vales Despensa 
dias2 = 3
transporte2 = 80
comida2 = 150
otros_gastos2 = 200
fondo_ahorro2 = 0.05
fondo_ahorro_tot2 = sueldo2*fondo_ahorro2*2
sueldo2 = sueldo2*(deducciones1-fondo_ahorro2)


# Calculo de ingresos anuales
aguinaldo1 = sueldo1 / 30 * aguinaldo_dias1
vacaciones1 = sueldo1 / 30 * vacaciones_dias1 *prima1
ingresos_anuales1 = sueldo1 * 12 + aguinaldo1 + vacaciones1 + bono1*12 +fondo_ahorro_tot1 *12

aguinaldo2 = sueldo2 / 30 * aguinaldo_dias2
vacaciones2 = sueldo2 / 30 * vacaciones_dias2 * prima2
ingresos_anuales2 = sueldo2 * 12 + aguinaldo2 + vacaciones2 + bono2*12 +fondo_ahorro_tot2*12

# Cálculo de gastos anuales
gastos1 = (transporte1*dias1*52) + (comida1*dias1*52) + (otros_gastos1*52)
gastos2 = (transporte2*dias2*52) + (comida2*dias2*52) + (otros_gastos2*52)


# Crear dataframes con los resultados
import pandas as pd

data = {'Ingresos Anuales':[ingresos_anuales1, ingresos_anuales2],
        'Gastos Anuales':[gastos1, gastos2]}
df = pd.DataFrame(data, index=[f'Trabajando en {trabajo1}', f'Trabajando en {trabajo2}'])
df['Ganancias Anuales'] = df['Ingresos Anuales'] - df['Gastos Anuales']

dif_gan = df.loc[f'Trabajando en {trabajo2}','Ganancias Anuales'] - df.loc[f'Trabajando en {trabajo1}','Ganancias Anuales']
dif_ingreso = df.loc[f'Trabajando en {trabajo2}','Ingresos Anuales'] - df.loc[f'Trabajando en {trabajo1}','Ingresos Anuales']
dif_gasto = df.loc[f'Trabajando en {trabajo2}','Gastos Anuales'] - df.loc[f'Trabajando en {trabajo1}','Gastos Anuales']

for c in df.columns:
    df[c] = df[c].map(moneda)

print(df)

if dif_ingreso<0:
    print(f'\nTrabajando en {trabajo1} el ingreso es mayor que en {trabajo2} por: '+moneda(-dif_ingreso))
else:
    print(f'\nTrabajando en {trabajo2} el ingreso es mayor que en {trabajo1} por: '+moneda(dif_ingreso))

if dif_gasto<0:
    print(f'\nTrabajando en {trabajo1} el gasto es mayor que en {trabajo2} por: '+moneda(-dif_gasto))
else:
    print(f'\nTrabajando en {trabajo2} el gasto es mayor que en {trabajo1} por: '+moneda(dif_gasto))

if dif_gan<0:
    print(f'\nTrabajando en {trabajo1} la ganancia neta es más que en {trabajo2} por: '+moneda(-dif_gan))
else:
    print(f'\nTrabajando en {trabajo2} la ganancia neta es más que en {trabajo1} por: '+moneda(dif_gan))

