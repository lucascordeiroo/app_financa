# # 💰 Sistema de Controle Financeiro com Flask

Aplicação web simples e funcional para controle de receitas e despesas. Desenvolvida com Python e Flask, com banco de dados SQLite, interface responsiva com Bootstrap e suporte a filtros por data.

---

## ✅ Funcionalidades

- Cadastro de transações (entrada e saída)
- Exibição da lista com data, descrição, tipo e valor
- Cálculo automático do saldo atual
- Filtro por mês e ano
- Interface limpa e responsiva com Bootstrap

---

## 🛠 Tecnologias utilizadas

- Python 3
- Flask
- SQLite
- Bootstrap 5

---

## ▶️ Como executar

### 1. Clone o repositório

git clone https://github.com/seu-usuario/finance-app.git
cd finance-app
2. (Opcional) Crie um ambiente virtual
python -m venv venv
venv\Scripts\activate      # Windows
# ou
source venv/bin/activate   # Linux/macOS

3. Instale as dependências
pip install flask

4. Rode o projeto
python app.py

5. Acesse no navegador
http://localhost:5000

📂 Estrutura do projeto
finance-app/
├── app.py
├── models.py
├── financeiro.db          
├── templates/
│   ├── layout.html
│   ├── index.html
│   └── add.html
├── static/
│   └── style.css          # (opcional, para estilos personalizados)
└── README.md

✨ Recursos extras implementados
✅ Filtro por mês e ano usando strftime() no SQLite

✅ Saldo com cores verde/vermelho conforme valor

📈 Gráficos de despesas por categoria (em desenvolvimento)

👨‍💻 Autor
Desenvolvido por Lucas Cordeiro
📧 Contato: lucascordeirooliveira50@gmail.com

