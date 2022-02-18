import random
import plotly.express as px
import plotly.figure_factory as pff
import pandas as pd
import statistics as s
import plotly.graph_objects as go

df=pd.read_csv("data.csv")
data=df["temp"].tolist()

def randomsetofmean(number):
    datalist=[]
    for i in range(0,number):

        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        datalist.append(value)
    mean=s.mean(datalist)
    sd=s.stdev(datalist)
    return mean

def showgraph(meanlist):
    df=meanlist
    mean=s.mean(df)
    graph=pff.create_distplot([df],["temp"],show_hist=False)
    graph.show()

def randommean():
    meanlist=[]
    for i in range(0,1000):
        setofmeans=randomsetofmean(100)
        meanlist.append(setofmeans)
    sd=s.stdev(meanlist)
    print(sd)
    sd=s.mean(meanlist)
    print(sd)
    showgraph(meanlist)
   
randommean()



