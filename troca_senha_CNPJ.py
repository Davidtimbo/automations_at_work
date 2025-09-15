import requests
import psycopg2


# Função para verificar se o CPF ou CNPJ está presente no banco de dados
def verificar_cpfcnpj_valido(cpfcnpj):
    try:
        connection = psycopg2.connect(
            user="***",
            password="***",
            host="***",
            port="***",
            database="***"
        )

        cursor = connection.cursor()

        if len(cpfcnpj) == 11:  # Se for um CPF
            if not cpfcnpj.startswith('000'):
                cpfcnpj = '000' + cpfcnpj
        elif len(cpfcnpj) == 14:  # Se for um CNPJ
            # Aqui você pode adicionar lógica adicional para manipular CNPJs, se necessário
            pass
        else:
            print("CPF ou CNPJ inválido.")
            return False

        query = "SELECT COUNT(*) FROM usuarios WHERE cpfcnpj = %s"
        cursor.execute(query, (cpfcnpj,))
        resultado = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return resultado > 0

    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar ao banco de dados PostgreSQL:", error)
        return False
# Função para solicitar um novo CPF ou CNPJ do usuário
def solicitar_cpfcnpj():
    return input("\nDigite o CPF ou CNPJ do usuário (ou 'sair' para encerrar):")


# Função para enviar uma solicitação de atualização de senha para o servidor
def atualizar_senha(token, cpfcnpj):
    url_atualiza_senha = 'https://api.******'

    nova_senha = '***'

    if len(cpfcnpj) == 11:  # Se for um CPF
        cpfcnpj = '000' + cpfcnpj
    elif len(cpfcnpj) == 14:  # Se for um CNPJ
        # Lógica para manipular CNPJ, se necessário
        pass
    else:
        print("CPF ou CNPJ inválido.")
        return False

    data_atualiza_senha = {
        'token': token,
        'cpfcnpj': cpfcnpj,
        'senha': nova_senha
    }

    response_atualiza_senha = requests.post(url_atualiza_senha, json=data_atualiza_senha)

    if response_atualiza_senha.status_code == 200:
        print("\nSenha atualizada com sucesso para o CNPJ/CPF:", cpfcnpj)
        print("Nova Senha:", nova_senha)
    else:
        print("\nErro ao atualizar a senha para o CNPJ/CPF:", cpfcnpj)
        print("\nMensagem de erro:", response_atualiza_senha.text)
        
# URL do endpoint para gerar o token
url_token = 'https://api.crasesigma.com.br/api/login'

# Parâmetros para a requisição de geração de token
data_token = {
    'cpfcnpj': '***',
    'senha': '***'
}

# Loop principal
while True:
    response_token = requests.post(url_token, json=data_token)

    if response_token.status_code == 200:
        token = response_token.json()['token']

        cpfcnpj = solicitar_cpfcnpj()

        if cpfcnpj.lower() == 'sair':
            break

        if verificar_cpfcnpj_valido(cpfcnpj):
            atualizar_senha(token, cpfcnpj)
        else:
            print("\nCPF ou CNPJ não encontrado no banco de dados ou inválido.\n")

    else:
        print('Erro ao gerar o token:\n', response_token.text)

