from sys import displayhook
from tkinter.tix import COLUMN
import pandas as pd
import matplotlib.pyplot as plt
#from IPython.core.display_functions import display

# s1 = pd.Series([1,2,3,4,5,6,7], index=[1,2,3,4,5,6,7])

# print(s1)
# print(s1.tolist())
# print(s1.values)

# df = pd.DataFrame([('a','b','c'),('10','20',30)], index=['row1','row2'], columns=['col1','col2','col3'], copy=True)
# print(df)
path = r"C:\Users\LEGION\csvfiles" + "\\"
filename1 = "sample_2_1000.csv"
df = pd.read_csv(
    path + filename1, delimiter=";", quotechar='"', encoding="utf-8", header=0
)

# df['Платеж'] = df['Платеж'].str.replace(',','.').astype(float)
df['Платеж'] = df['Платеж'].apply(func = lambda x: float(str(x).replace(',','.')))
# res = df.groupby(['Компания','Область'])['Платеж'].sum()
# #res = df.groupby(['Компания'])['Платеж'].count()
# for row, val in res.items():
#     print(f'{row}: {val}')

результат = df.pivot_table(values=["Платеж"], index="Компания", columns=["Статус"], aggfunc="sum")

результат = df.pivot_table(values=["Платеж"], index="Компания", columns=["Статус"], aggfunc={'Платеж': ['sum','mean']})

print(результат)

# plt.scatter(x=[1,2,3,4,5,6],y=[0.1,0.5,2.0,1.0,-0.6,0.4], s=50, marker='*', c='red')
# plt.show()

df.groupby(['Компания','Область'])['Платеж'].sum().plot.bar()
plt.show()