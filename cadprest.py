import time
import pyautogui
import subprocess
import psycopg2  # Importa o módulo psycopg2 para conexão com PostgreSQL

# Função para conectar ao banco de dados PostgreSQL
def connect_to_db():
    conn = None
    try:
        conn = psycopg2.connect(
            dbname="***",
            user="***",
            host="***",
            port="***"
        )
        print("Conexão com o banco de dados estabelecida.")
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    return conn

# Função para executar a consulta SQL e retornar os resultados
def execute_query(conn, query):
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except Exception as e:
        print(f"Erro ao executar a consulta: {e}")
    finally:
        cursor.close()

# Solicita ao usuário para inserir o nome do prédio
predio = input('Qual é o número do prédio? ')

time.sleep(3)

subprocess.Popen(['/usr/bin/xterm'])

# Aguarda a abertura do qterminal
time.sleep(3)

# Consulta no banco de dados para obter os "uapto"
conn = connect_to_db()
if conn:
    query = f"SELECT uapto FROM c_email01global WHERE ccod = '{predio}';"
    resultados = execute_query(conn, query)
    conn.close()
    
    if not resultados:
        print(f"Nenhum resultado encontrado para o prédio: {predio}")
    else:
        print(f"Resultados obtidos para o prédio {predio}: {resultados}")

        # Lista de comandos para enviar
        pyautogui.write('telnet 1.0.0.1')
        time.sleep(1)        
        pyautogui.press('enter')
        time.sleep(1)

        pyautogui.write('jairus')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)

        pyautogui.write('123456')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)

        pyautogui.write('24')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)

        pyautogui.write('1')
        pyautogui.press('enter')
        time.sleep(1)

        pyautogui.write('imagem')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)

        for row in resultados:
            uapto = row[0]
            
            pyautogui.write(predio)
            pyautogui.press('enter')
            time.sleep(1)
            
            pyautogui.write(str(uapto))
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)

            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)

            pyautogui.press('1')
            pyautogui.press('enter')
            time.sleep(1)

            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)

            pyautogui.write('S')
            pyautogui.press('enter')
            time.sleep(1)

        pyautogui.press('enter')
        time.sleep(1)
        
        pyautogui.press('2')
        pyautogui.press('enter')
        time.sleep(1)
        
        pyautogui.write(predio)
        pyautogui.press('enter')
        time.sleep(1)

