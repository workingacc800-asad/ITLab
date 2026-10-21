#Pandas Practice
import pandas as pd

#creating a data frame from a dictionary
data = {
    "Agent_ID": ["A101", "A102", "A103", "A104"],
    "Framework": ["LangGraph", "CrewAI", "AutoGen", "LangChain"],
    "Success_Rate": [0.95, 0.88, 0.91, 0.82],
    "Active": [True, True, False, True]
}
# print(info)
df = pd.DataFrame(data)
# print(df)

# print(df.head(2))
# print(df.tail(2))
# df.info()
print(df.describe())
# print(df.iloc[2])
# print(df.loc[0,"Success_Rate"])