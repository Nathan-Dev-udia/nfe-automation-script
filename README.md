# 🤖 Nfe Automation

**Nfe Automation** é um script de automação desenvolvido em **Python com Selenium** que cadastra automaticamente **produtos e notas fiscais** no sistema **ConnectUse** (Applix Sistema).

Antes da automação, o cadastro dos produtos de cada nota fiscal levava cerca de 1 minuto e 20 segundos por item. Como as notas chegavam todas de uma vez, com dezenas ou até centenas de produtos, e ainda havia outras funções a cumprir, o processo tomava quase uma semana inteira — mesmo com ajuda. Com o script, o tempo caiu para 25 segundos por item (ou menos), permitindo concluir tudo em 1 ou 2 dias, com muito menos esforço.

---

## ⚙️ Funcionalidades

- 🔐 Login automático no sistema ConnectUse;
- 🖱️ Simulação de cliques com `pyautogui` para interação com elementos complexos;
- 📝 Criação automática de novos produtos com base nas notas recebidas;
- 📋 Preenchimento de categorias, famílias e flags de compra/venda;
- 📎 Associação automática do produto à nota fiscal no sistema.

---

## 📁 Estrutura do Projeto

- `conecct_cadastro.ipynb`: Script principal da automação;
- `imports.txt`: Coleta dos principais seletores usados;
- `connect scan.txt`: Mapeamento dos elementos no sistema;
- `token.json` e `credentials.json`: (não aplicável nesse projeto);
- Utiliza `pyautogui` para simular interações onde o Selenium não atua diretamente.

---

## 🧠 Tecnologias

- **Python 3**
- **Selenium**
- **PyAutoGUI**
- **ChromeDriver + WebDriverManager**
- **Jupyter Notebook**

---

## ▶️ Como usar

1. Instale as dependências:

```bash
pip install selenium pyautogui webdriver-manager pandas
```
### 💡 Dica: para descobrir as coordenadas da tela
Execute o seguinte código para ver onde o mouse está apontando:
```bash
import pyautogui, time
while True:
    print(pyautogui.position())
    time.sleep(1)
```
## 📌 Observações
- O script exige que o usuário não mova o mouse durante a execução;
- Algumas interações exigem que o navegador esteja maximizado;
- Certifique-se de que o Chrome está atualizado e o sistema está configurado corretamente.

---
## 🧪 Resultado
Antes: Cadastro manual levava cerca de 1 minuto e 10 segundos por produto.
Depois: Cadastro automático realiza tudo em cerca de 25 segundos por produto, com mínima intervenção humana.

> Criado por Nathan Fernandes Alves para automatizar tarefas repetitivas de cadastro no sistema ConnectUse.
