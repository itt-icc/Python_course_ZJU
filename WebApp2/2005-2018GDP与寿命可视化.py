import pandas as pd
from plotly.offline import  plot
import plotly.express as px

startyear=2005

#整理人均寿命
dataset=pd.read_excel("life_expectancy_years.xlsx")
a=pd.DataFrame(columns=("country","life-exp","year"))
for i in range(startyear,2019):
    b=dataset[['country',i]].copy()
    b['year']=i                               #新创建一列
    b.columns=['country','life-exp','year']   #更换列索引
    c=a.append(b)                             #按照行拼接
    a=c
print(a)

#整理人均收入
dataset=pd.read_excel("income_per_person_gdppercapita_ppp_inflation_adjusted.xlsx")
x=pd.DataFrame(columns=("country",'income',"year"))
for i in range(startyear,2019):
    y=dataset[['country',i]].copy()
    y['year']=i
    y.columns=['country','income','year']
    z=x.append(y)
    x=z

#整理人口数量
dataset=pd.read_excel("population_total.xlsx")
m=pd.DataFrame(columns=("country",'pop',"year"))
for i in range(startyear,2019):
    n=dataset[['country',i]].copy()
    n['year']=i
    n.columns=['country','pop','year']
    w=m.append(n)
    m=w
print(m)

data=pd.merge(a,x,sort=True)
data=pd.merge(data,m,sort=True)
print(data)


#为国家添加洲名
dt=px.data.gapminder()
dt=dt[["country","continent"]]
dt=dt.drop_duplicates(subset=["country","continent"],keep="first")#相同行只保留第一行
data=pd.merge(data,dt,left_on="country",right_on="country",how="left")
data=data.dropna()

print(data)
data.to_excel(f"2005到2018人均GDP和人均寿命.xlsx")

dataset=pd.read_excel("2005到2018人均GDP和人均寿命.xlsx")
figure = px.scatter(dataset, x="income", y="life-exp", 
                 animation_frame="year",
                 animation_group="country",
                 size="income", color="country",#按照国家进行展示
                 hover_name="country",log_x=True, size_max=45,
                 range_x=[500,200000], range_y=[25,90],
                 labels=dict(income="人均GDP",lifeExp="人均期望寿命"))
                 
plot(figure)