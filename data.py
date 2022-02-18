import random
import plotly.express as px
import plotly.figure_factory as pff
import pandas as pd
import statistics as s
import plotly.graph_objects as go

df=pd.read_csv("data.csv")
data=df["temp"].tolist()
mean=s.mean(data)
print(mean)
sd=s.stdev(data)
print(sd)
graph=pff.create_distplot([data],["temp"],show_hist=False)

#graph.show()
datalist=[]
for i in range(0,100):
    randomIndex=random.randint(0,len(data)-1)
    value=data[randomIndex]
    datalist.append(value)
mean=s.mean(datalist)
sd=s.stdev(datalist)
print(mean,sd)