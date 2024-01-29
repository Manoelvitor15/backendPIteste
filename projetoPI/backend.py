from flask import Flask, render_template, request, redirect
import psycopg2
import os

sistema = Flask(__name__)

def conecta_db():
    conecta = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password='123')
    return conecta

@sistema.route('/cadastro')
def homepage():
    return render_template('index.html')

@sistema.route("/cadastro", methods=['POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        identidade = request.form['identidade']
        orgao_expedidor = request.form['orgao_expedidor']
        sexo = request.form['sexo']
        nome_pai = request.form['nome_pai']
        nome_mae = request.form['nome_mae']
        naturalidade = request.form['naturalidade']
        uf_identidade = request.form['uf_identidade']
        pais = request.form['pais']
        logradouro = request.form['logradouro']
        complemento = request.form['complemento']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        uf_endereco = request.form['uf_endereco']
        cep = request.form['cep']
        telefone = request.form['telefone']
        data_nasc = request.form['data_nasc']
        estado_civil = request.form['estado_civil']
        nome_conjuge = request.form['nome_conjuge']
        profissao = request.form['profissao']
        escolaridade = request.form['escolaridade']
        data_batismo = request.form['data_batismo']
        batizado_esp_santo = request.form['batizado_esp_santo']
        entrada_rol_membros = request.form['entrada_rol_membros']
        congregacao = request.form['congregacao']
        funcao = request.form['funcao']
        origem = request.form['origem']
        situacao = request.form['situacao']
        igreja_cidade = request.form['igreja_cidade']
        data_consagracao = request.form['data_consagracao']
        local = request.form['local']
        igreja_serve = request.form['igreja_serve']
        data_reconhecimento = request.form['data_reconhecimento']
        cargos = request.form['cargos']
        historico = request.form['historico']


        conexao = conecta_db()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO cadastro_membros (nome, cpf, identidade, orgao_expedidor, sexo, nome_pai, nome_mae, naturalidade, uf_identidade, pais, logradouro, complemento, bairro, cidade, uf_endereco, cep, telefone, data_nasc, estado_civil, nome_conjuge, profissao, escolaridade, data_batismo, batizado_esp_santo, entrada_rol_membros, congregacao, funcao, origem,situacao, igreja_cidade, data_consagracao, local, igreja_serve, data_reconhecimento, cargos, historico) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (nome, cpf, identidade, orgao_expedidor, sexo, nome_pai, nome_mae, naturalidade, uf_identidade, pais, logradouro, complemento, bairro, cidade, uf_endereco, cep, telefone, data_nasc, estado_civil, nome_conjuge, profissao, escolaridade, data_batismo, batizado_esp_santo, entrada_rol_membros, congregacao, funcao, origem,situacao, igreja_cidade, data_consagracao, local, igreja_serve, data_reconhecimento, cargos, historico))
        conexao.commit()
        cursor.close()
        conexao.close()

        return render_template('cad.sucesso.html')    

if __name__ == "__main__":
    sistema.run(debug=True, port=8085, host='127.0.0.3')
