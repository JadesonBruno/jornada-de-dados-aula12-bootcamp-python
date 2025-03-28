# Importando módulos próprios
from src import CsvProcessar

# 1) Momento

""" caminho = 'exemplo.csv'
filtro = 'estado'
limite = 'SP'

arquivo_csv = CsvProcessar(file_path=caminho)
arquivo_csv.carregar_csv()
print(arquivo_csv.filtrar_coluna(coluna=filtro, atributo=limite), end='\n\n')
print(arquivo_csv.sub_filtro(coluna='preco', atributo='10,50'))
print('##############---##############')

caminho_2 = 'exemplo_2.csv'
filtro_2 = 'estado'
limite_2 = 'PE'

arquivo_csv_2 = CsvProcessar(file_path=caminho_2)
arquivo_csv_2.carregar_csv()
print(arquivo_csv_2.filtrar_coluna(coluna=filtro_2, atributo=limite_2), end='\n\n')
print(arquivo_csv_2.sub_filtro(coluna='preco', atributo='10,50')) """

# 2) Momento

caminho = "exemplo.csv"
filtro = ["estado", "preco"]
limite = ["SP", "10,50"]

arquivo_csv = CsvProcessar(file_path=caminho)
arquivo_csv.carregar_csv()
print(arquivo_csv.filtrar_coluna(colunas=filtro, atributos=limite), end="\n\n")
