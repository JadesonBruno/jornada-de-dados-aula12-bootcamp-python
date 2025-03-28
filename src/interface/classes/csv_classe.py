# Import libs nativas
from typing import List

# Import libs terceiros
import pandas as pd

# 1) Momento

""" class CsvProcessar():
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None


    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)
        return None


    def filtrar_coluna(self, coluna, atributo):
        df_filtrado = self.df[self.df[coluna] == atributo]
        return df_filtrado


caminho = 'exemplo.csv'
filtro = 'estado'
limite = 'SP'

arquivo_csv = CsvProcessar(file_path=caminho)
arquivo_csv.carregar_csv()
print(arquivo_csv.filtrar_coluna(coluna=filtro, atributo=limite), end='\n\n')
print(arquivo_csv.df)

caminho_2 = 'exemplo_2.csv'
filtro_2 = 'estado'
limite_2 = 'PE'

arquivo_csv_2 = CsvProcessar(file_path=caminho_2)
arquivo_csv_2.carregar_csv()
print(arquivo_csv_2.filtrar_coluna(coluna=filtro, atributo=limite_2)) """

# 2) Momento

""" class CsvProcessar():
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        self.df_filtrado = None


    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)
        return None


    def filtrar_coluna(self, coluna, atributo):
        self.df_filtrado = self.df[self.df[coluna] == atributo]
        return self.df_filtrado


    def sub_filtro(self, coluna, atributo):
        return self.df_filtrado[self.df_filtrado[coluna] == atributo] """


# 3) Momento


class CsvProcessar:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        self.df_filtrado = None

    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)
        return None

    def filtrar_coluna(self, colunas: List, atributos: List):
        if len(colunas) != len(atributos):
            raise ValueError("Não tem o mesmo número de colunas e atributos")
        elif len(colunas) == 0 or len(atributos) == 0:
            return self.df
        else:
            coluna_atual = colunas[0]
            atributos_atual = atributos[0]
            df_filtrado = self.df[self.df[coluna_atual] == atributos_atual]

            if len(colunas) == 1:
                return df_filtrado
            else:
                return self.filtrar_coluna(colunas[1:], atributos[1:])
