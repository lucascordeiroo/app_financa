from flask import Flask, render_template, request, redirect, url_for
from models import criar_tabelas, adicionar_transacao, listar_transacoes, calcular_saldo

import os
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Garante que as tabelas estão criadas
criar_tabelas()

@app.route('/')
def index():
    mes = request.args.get('mes')
    ano = request.args.get('ano')

    transacoes = listar_transacoes(mes, ano)
    saldo = calcular_saldo(transacoes)

    return render_template(
        'index.html',
        transacoes=transacoes,
        saldo=saldo,
        mes=mes,
        ano=ano
    )


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        descricao = request.form['descricao']
        valor = float(request.form['valor'])
        tipo = request.form['tipo']  # "entrada" ou "saida"
        data = request.form['data']
        adicionar_transacao(descricao, valor, tipo, data)
        return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
