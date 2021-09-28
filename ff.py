from numpy import result_type
import pandas as pd

#Data - https://www.fantasypros.com/2021/09/week-3-fantasy-football-trade-value-chart-2021/

#WR
df = pd.read_csv(r'WRdata.csv')
#create a new dataframe with only the name and value column
new = df[['X.1', 'STANDARD']].copy()
#remove top row
new = new.iloc[1: , :]
#rename X.1 to name
new = new.rename(columns={'X.1': 'Name', 'STANDARD': 'Value'})

#RB
df_RB = pd.read_csv(r'RBdata.csv')
#create a new dataframe with only the name and value column
new_RB = df_RB[['X.1', 'STANDARD']].copy()
#remove top row
new_RB = new_RB.iloc[1: , :]
#rename X.1 to name
new_RB = new_RB.rename(columns={'X.1': 'Name', 'STANDARD': 'Value'})
#remove name and value
#new_RB = new_RB.iloc[1: , :]

#combine the two dataframes and sort by Value
frames = [new, new_RB]
result = pd.concat(frames)

#Sort by Value
#result.sort_values(by=['Name'], na_position='first')
#sort = 
result.sort_values(by=['Value'])

print(result)

result.to_excel("outputnew.xlsx")  

