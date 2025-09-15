# Automations at Work 🚀

Este repositório contém 4 scripts Python desenvolvidos para automatizar tarefas administrativas, de integração com banco de dados e terminais, utilizados internamente na empresa.

---

## 📂 Scripts

### 1. `troca_senha_CNPJ.py`
Este script:

- Faz login na API da Empresa para obter um token.
- Solicita um CPF ou CNPJ ao usuário.
- Verifica se o CPF/CNPJ existe no banco de dados PostgreSQL.
- Caso exista, envia uma requisição para atualizar a senha do usuário para `***`.
- Repete o processo em loop até o usuário digitar `sair`.

**Uso:** Automatiza o reset de senhas para usuários específicos via API.

---

### 2. `matarlogin2.py`
Este script:

- Abre um terminal (`xterm`)
- Usa `pyautogui` para digitar comandos automaticamente em um sistema via Telnet:
  - Conecta ao servidor
  - Navega até um diretório específico
  - Executa um programa chamado `sci001`

**Uso:** Automatiza o login e a execução de programas em sistemas legados via terminal.

---

### 3. `removerRevista.py`
Este script:

- Solicita o número de um prédio.
- Consulta o banco de dados `imageview` para buscar apartamentos (`uapto`) relacionados ao prédio.
- Abre um terminal e se conecta via Telnet ao sistema.
- Para cada apartamento, digita comandos simulando a navegação no sistema e a execução de funções relacionadas a "imagens".

**Uso:** Automatiza interações repetitivas em sistemas baseados em terminal, especialmente tarefas relacionadas a registros de prédios e apartamentos.

---

### 4. `cadprest.py`
Muito semelhante ao `removerRevista.py`, mas com uma sequência diferente de comandos enviados via `pyautogui`.  
Presume-se que seja uma variação da automação para outra rotina no mesmo sistema legado.

---

## ⚠️ Observações

- Os scripts utilizam bibliotecas como `pyautogui`, `psycopg2`, `subprocess`, `requests`.
- São dependentes de um ambiente Linux com `xterm`, acesso ao banco PostgreSQL e à API da Empresa.
- A execução desses scripts deve ser feita com cautela, pois interagem diretamente com sistemas em produção.

---

## ✅ Requisitos

Antes de rodar os scripts, certifique-se de que os seguintes pacotes estejam instalados:

```bash
pip install requests psycopg2 pyautogui
```
