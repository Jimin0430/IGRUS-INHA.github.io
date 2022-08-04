import pandas as pd
import openpyxl

dfx=pd.read_excel("C:/Users/tangb/OneDrive/바탕 화면/myproj/final.xlsx",usecols=[3,8])
print(dfx)

dfx.to_excel('C:/Users/tangb/OneDrive/바탕 화면/myproj/botreader.xlsx',sheet_name='sheet1')