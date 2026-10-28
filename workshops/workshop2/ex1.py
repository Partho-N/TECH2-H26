import pandas as pd
import numpy as np
titanic=pd.read_csv("data/titanic.csv")
missing_ages=titanic["Age"].isna().sum()
mean_age=titanic["Age"].mean()
ages=titanic["Age"].to_numpy()
numpy_mean=np.mean(ages)
numpy_nanmean=np.nanmean(ages)
print("Missing ages:",missing_ages)
print("Pandas mean:",mean_age)
print("Numpy mean:",numpy_mean)
print("Numpy nanmean:",numpy_nanmean)

titanic["Age"]=titanic["Age"].fillna(round(mean_age)).astype(int)
titanic["Female"]=(titanic["Sex"]=="female").astype(int)
del titanic["Sex"]
titanic.to_csv("titanic_clean.csv",sep=",", index=False)
titanic_clean=pd.read_csv("titanic_clean.csv")
print(titanic_clean)





