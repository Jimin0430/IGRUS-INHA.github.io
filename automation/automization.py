import pandas as pd
import openpyxl

dfx=pd.read_excel("C:/Users/tangb/OneDrive/바탕 화면/myproj/deposit.xlsx",usecols=[2,6])
print(dfx)

dfx.to_excel('C:/Users/tangb/OneDrive/바탕 화면/myproj/test.xlsx',sheet_name='sheet')