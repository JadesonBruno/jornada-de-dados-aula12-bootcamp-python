# Import libs terceiros
import pandas as pd

df = pd.read_csv("exemplo.csv")
print(df, end="\n\n")
df_filtrado = df[df["estado"] == "SP"]
df_filtrado = df[df["preco"] == "10,50"]
print(df_filtrado, end="\n\n")

df2 = pd.read_csv("exemplo_2.csv")
print(df2, end="\n\n")
df_filtrado_2 = df2[df2["estado"] == "PE"]
df_filtrado_2 = df2[df2["preco"] == "10,50"]
print(df_filtrado_2)
