from flask import Flask, render_template, request, send_file
from docxtpl import DocxTemplate
import os
from datetime import datetime
import io
import time

app = Flask(__name__)

# Certifique-se de que o arquivo de modelo exista
TEMPLATE_FILE = 'Modelo_evolução.docx'
if not os.path.exists(TEMPLATE_FILE):
    print(f"Erro: Arquivo de modelo '{TEMPLATE_FILE}' não encontrado. Certifique-se de que ele esteja na mesma pasta que app.py")
    exit()

# Função para quebrar o texto da evolução em pedaços para as linhas da tabela
def split_evolution_text(text, max_chars_per_line=90, total_lines=36): # Alterado para 90
    """Divide o texto de evolução em partes, considerando um limite de caracteres por linha."""
    lines = []
    current_index = 0
    while current_index < len(text) and len(lines) < total_lines:
        segment = text[current_index : current_index + max_chars_per_line]

        if len(text) > current_index + max_chars_per_line:
            last_space_in_segment = segment.rfind(' ')
            if last_space_in_segment != -1 and last_space_in_segment > max_chars_per_line * 0.8:
                segment = segment[:last_space_in_segment]
                current_index += len(segment) + 1
            else:
                current_index += max_chars_per_line
        else:
            current_index += max_chars_per_line

        lines.append(segment.strip())

    while len(lines) < total_lines:
        lines.append("")
    return lines


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_doc', methods=['POST'])
def generate_doc():
    if request.method == 'POST':
        context = {
            'nome': request.form.get('nome', ''),
            'numero': request.form.get('numero', ''),
            'data_nascimento': request.form.get('data_nascimento', ''),
            'idade': request.form.get('idade', ''),
            'sexo': request.form.get('sexo', ''),
            'estado_civil': request.form.get('estado_civil', ''),
            'ocupacao': request.form.get('ocupacao', ''),
            'nome_pai': request.form.get('nome_pai', ''),
            'nome_mae': request.form.get('nome_mae', ''),
            'endereco_permanente': request.form.get('endereco_permanente', ''),
            'endereco_temporario': request.form.get('endereco_temporario', ''),
            'cartao_sus': request.form.get('cartao_sus', ''),
            'data_atendimento': request.form.get('data_atendimento', ''),
            'evolucao': request.form.get('evolucao', '')
        }

        for key in ['data_nascimento', 'data_atendimento']:
            if context[key]:
                try:
                    date_obj = datetime.strptime(context[key], '%Y-%m-%d')
                    context[key] = date_obj.strftime('%d/%m/%Y')
                except ValueError:
                    context[key] = context[key]

        full_evolution_text = context['evolucao']
        evolution_parts = split_evolution_text(full_evolution_text, max_chars_per_line=90, total_lines=36)

        for i, part in enumerate(evolution_parts):
            context[f'evolucao{i+1}'] = part

        del context['evolucao']

        try:
            doc = DocxTemplate(TEMPLATE_FILE)
            doc.render(context)

            file_stream = io.BytesIO()
            doc.save(file_stream)
            file_stream.seek(0)

            download_filename = f"Ficha_Evolucao_{context['nome'].replace(' ', '_')}_{datetime.now().strftime('%Y%m%d%H%M%S')}.docx"

            response = send_file(
                file_stream,
                mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                as_attachment=True,
                download_name=download_filename
            )
            return response

        except Exception as e:
            print(f"Erro ao gerar ou enviar o documento: {e}")
            return f"Ocorreu um erro ao gerar a ficha: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)