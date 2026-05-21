#!/usr/bin/env python3

import numpy as np
import pandas as pd


S = pd.Series([11, 28, 72])
print(S)
print()

S2 = S**2 -3*S + 2
print(S2)
print()

S1 = pd.Series([1, 2, 3, 4, 5])
print(S1)
print()
print(S+S1)
print()
print(sum(S))
print(min(S))
print(max(S))
print(np.mean(S))
print(np.std(S))
print()

S2 = S + S1
S3 = S2.apply(lambda x: 0 if pd.isna(x) else x)
print(S3)
print()

fruits = ['apples', 'oranges', 'cherries', 'pears']
F1 = pd.Series([20, 33, 52, 10], index=fruits)
F2 =pd.Series([17, 13, 31, 32], index=['apples', 'pears', 'coconuts', 'cashew'])
print(F1, "\n")
print("F1+F2:\n", F1+F2)
print()
print("Summe aus F1+F2: ", sum(F1))

print(F1['apples'])
print()
print(F1['apples' : 'cherries'])
print()
print(S3[1:5:2])
print()
S3[3]=999
print(S3[3])
print(S3.drop(labels=3, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise'))
print(S3)
F1.name = 'Früchte'
print(F1)
print()


'''
pd.DataFrame: Erstellen einer Tabelle
'''

data1 = {'Name':['Bob', 'Alice', 'Cindy'], 
         'Alter':[23, 45, 21], 
         'Gehalt':[60, 85, 57]}
angestellte = pd.DataFrame(data1)
print(angestellte)
print()
np._core.arrayprint._line_width = 60
pd.set_option('display.max_colwidth', 65)
pd.set_option('display.max_columns', 5)

i = list(range(1, 5))
s1 = pd.Series([1, 2, 3, 4], index=i)
s2 = pd.Series([5, 6, 7, 8], index=i)
s3 = pd.Series([-1, -2,-3,-4], index=i)
d1 = pd.concat([s1,s2,s3], axis=1)
d2 = pd.concat([s1,s2,s3], axis=0)
print(d1)
print()
print(d2)
print(d1.index)
print(d1.columns)
print()
d1.columns = ['Januar', 'Februar', 'März']
d1.index = range(2022,2026)
print(d1)
print()

cities = {"name": ["London", "Berlin", "Madrid", "Rome", 
                   "Paris", "Vienna", "Bucharest", "Hamburg", 
                   "Budapest", "Warsaw", "Barcelona", 
                   "Munich", "Milan"],
          "population": [8615246, 3562166, 3165235, 2874038,
                         2273305, 1805681, 1803425, 1760433,
                         1754000, 1740119, 1602386, 1493900,
                         1350680],
          "country": ["England", "Germany", "Spain", "Italy",
                      "France", "Austria", "Romania", 
                      "Germany", "Hungary", "Poland", "Spain",
                      "Germany", "Italy"]}
city_frame = pd.DataFrame(cities)
print(city_frame)
print()


'''
pd.DataFrame: Ändern des Tabellenformats
'''

city_frame2 = pd.DataFrame(city_frame, columns=['country', 'name', 'population'])
print(city_frame2)
print()
f3 = city_frame.set_index('name')
print(f3)
print()
f3 = pd.DataFrame(f3, columns=['country', 'population'])
print(f3, "\n")
f3.rename(columns={'country':'Land', 'population':'Einwohner'}, inplace=True)
print(f3)
print()


'''
pd.DataFrame: Zugriff auf Zeilen, Spalten, Elemente
'''

sel1 = f3['Barcelona':'Berlin':-2]
print(sel1, "\n")
sel2 = f3[f3.Einwohner >= 2000000]
print(sel2, "\n")
sel3 = f3.loc['Munich']
print(sel1, "\n")
sel4 = f3.loc[['Munich', 'Hamburg', 'Berlin']]
print(sel3, "\n")
print(sel4, "\n")
sel5 = city_frame.iloc[2]
print(s1,'\n')
sel5 = city_frame.iloc[4:12:3]
sel7 = city_frame.iloc[(slice(2,6), [0,1])] # Slice für Zeilen, Liste für Spalten
print(sel5, "\n")
print(sel7, "\n")
sel8 = f3.at['Hamburg','Land']
print(sel8,'\n')

sel9 = f3.iat[5,1]
print(sel9,'\n')

sel10 = f3.at['Hamburg','Einwohner']
print(sel10,'\n')

f3.at['Hamburg','Einwohner'] += 1000
sel11 = f3.at['Hamburg','Einwohner']

print(sel8,'\n')
print(sel9,'\n')
print(sel10,'\n')
print("sel11")
print(sel11,'\n')


'''
pd.DataFrame: Hinzufügen von Daten
'''

print("\npd.DataFrame: Hinzufügen von Daten\n")

f3['Stadt'] = f3.index
print(f3.head(3), "\n")
print(f3.tail(5), "\n")

df1 = pd.DataFrame([['a', 1], ['b', 2]], columns=['letter', 'number'])
df2 = pd.DataFrame([['c', 3], ['d', 4]], columns=['letter', 'number'])
df3 = pd.concat([df1, df2])
print(df1, "\n")
print(df2, "\n")
print(df3, "\n")


'''
pd.DataFrame: Anwendung von Funktionen
'''

print("\npd.DataFrame: Anwendung von Funktionen\n")

print(f"city_frame \'population\' summe:\n{city_frame['population'].sum()}", "\n")
city_frame['cum_pop_sum']=city_frame['population'].cumsum()
print(city_frame, "\n")

people = pd.DataFrame({
    "Name": ['Alice', 'Bob', None, 'David', None, 'Fiona', 'George'],
    "Age": [25, None, 23, 35, None, 31, 28],
    "Gender": ['F', 'M', 'M', None, 'F', 'F', 'M'],
    "Years": [3, None, None, None, 7, None, 2]
})
p2 = people.copy()
print(p2)
# Verwende das Durchschnittsalter, um Lücken in der Spalte age zu füllen:
p2['Age'] = p2['Age'].fillna(p2['Age'].mean())
print(p2)
# Verwende ein dict, um Lücken unterschiedlichen Spalten unterschiedlich zu
# behandeln:
p3 = people.fillna({
    'Name': 'Missing',
    'Age': people['Age'].mean(),
    'Years': 0
})
print(p3)
































