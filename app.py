from flask import Flask, request, jsonify
from docxtpl import DocxTemplate
from datetime import datetime
import os

app = Flask(__name__, static_url_path='/static')

@app.route("/gerar-proposta", methods=["POST"])
def gerar_proposta():
    try:
        dados = request.json
        dados["data_emissao"] = datetime.today().strftime("%d de %B de %Y")

        doc = DocxTemplate("orcamento_base.docx")
        doc.render(dados)

        os.makedirs("static/propostas", exist_ok=True)

        nome_arquivo = f"Proposta_{dados['Cliente'].replace(' ', '_')}.docx"
        caminho_arquivo = os.path.join("static", "propostas", nome_arquivo)
        doc.save(caminho_arquivo)

        # Gera URL pública
        url = f"https://orcamento-us11.onrender.com/static/propostas/{nome_arquivo}"
        return jsonify({"url": url}), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500



