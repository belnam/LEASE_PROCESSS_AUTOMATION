import pandas as pd

df = pd.read_excel('AGENCY CHEAT SHEET.xlsx')

df['LOCATION'] = df['LOCATION'].str.split(',')
df = df.explode('LOCATION')
df['LOCATION'] = df['LOCATION'].str.strip()
df = df[df['LOCATION'] != '']
df.to_excel('REFINED AGENCY CHEAT SHEET.xlsx', index=False)