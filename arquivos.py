import csv

caminho: str = "exemplo.csv"

arquivo_csv: list = []

#usar gerenciador de contexto para abrir o arquivo,
#  abre e fecha o arquivo


with open(caminho, mode="r",encoding="utf-8") as arquivo:
    leitor_csv = csv.DictReader(arquivo)
    for linha in leitor_csv:
        arquivo_csv.append(linha)

        \

print(arquivo_csv)
