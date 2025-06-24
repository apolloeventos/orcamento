from flask import Flask, request, send_file
from docxtpl import DocxTemplate
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/gerar-proposta", methods=["POST"])
def gerar_proposta():
    dados = request.json

    # Define a data de emissão
    dados["data_emissao"] = datetime.today().strftime("%d de %B de %Y")

    # Carrega o modelo
    doc = DocxTemplate("orcamento_base.docx")

    # Preenche os dados no modelo
    doc.render(dados)

    # Garante a pasta de saída
    os.makedirs("propostas", exist_ok=True)

    # Gera o nome do arquivo com base no cliente
    nome_arquivo = f"propostas/Proposta_{dados['Cliente'].replace(' ', '_')}.docx"
    doc.save(nome_arquivo)

    # Envia o arquivo gerado de volta
    return send_file(nome_arquivo, as_attachment=True)

@app.route('/')
def home():
    return 'API do orçamento está no ar! 😎'

if __name__ == "__main__":
    app.run(debug=True)

