from docxtpl import DocxTemplate
from datetime import datetime

# 1. Carrega o modelo Word corrigido
doc = DocxTemplate("Orçamento Base Coffee Break Padrão.docx")

# 2. Preenche os dados simulados (você vai substituir depois pelo que o agente digitar)
dados = {
    "Nome_do_Evento": "Coffee Break – Diretoria Regional",
    "Cliente": "Construtora XPTO",
    "data": "10 de Agosto de 2025",
    "horário": "08h às 10h",
    "endereço": "Av. Brasil, 123 – Rio de Janeiro",
    "quantidade": "40",
    "Valor_total": "R$ 2.800,00",
    "data_emissao": datetime.today().strftime("%d de %B de %Y")
}

# 3. Preenche e salva como novo arquivo
doc.render(dados)
doc.save("Proposta_ConstrutoraXPTO.docx")
