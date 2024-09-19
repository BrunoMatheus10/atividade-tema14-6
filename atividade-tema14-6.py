import datetime


# Função para converter uma data no formato DD/MM/AAAA para uma string no formato "D de mêsPorExtenso de AAAA"
def data_por_extenso(data):
    try:
        # Converte a string da data para um objeto datetime
        data_formatada = datetime.datetime.strptime(data, "%d/%m/%Y")

        # Lista com os nomes dos meses em português
        meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro",
                 "novembro", "dezembro"]

        # Extrai o dia, mês e ano da data
        dia = data_formatada.day
        mes = meses[data_formatada.month - 1]
        ano = data_formatada.year

        # Retorna a data no formato desejado
        return f"{dia} de {mes} de {ano}"
    except ValueError:
        # Retorna NULL se a data for inválida
        return "NULL"


# Leitura da data do usuário
data = input("Digite uma data (DD/MM/AAAA): ")

# Exibição da data por extenso
print(data_por_extenso(data))
