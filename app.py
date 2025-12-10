from flask import (
    Flask,
    render_template,
    request,
    send_file,
    redirect,
    url_for,
    session,
    flash
)
from docxtpl import DocxTemplate
import os
from datetime import datetime
import io
from functools import wraps

app = Flask(__name__)

# CHAVE SECRETA
app.secret_key = "chave_super_secreta_ficha_medica"

# LOGIN PADRÃO (não aparece na interface)
MEDICO_USERNAME = "medico(a)"
MEDICO_PASSWORD = "@Medico(a)0123"

# TEMPLATE DOCX
TEMPLATE_FILE = "Modelo_evolução.docx"
if not os.path.exists(TEMPLATE_FILE):
    print(f"Erro: Arquivo '{TEMPLATE_FILE}' não encontrado!")
    exit()


# LOGIN REQUIRED
def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "usuario" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return wrapper


# DIVISÃO DO TEXTO DE EVOLUÇÃO
def split_evolution_text(text, max_chars_per_line=90, total_lines=36):
    lines = []
    current_index = 0

    while current_index < len(text) and len(lines) < total_lines:
        segment = text[current_index: current_index + max_chars_per_line]

        if len(text) > current_index + max_chars_per_line:
            last_space = segment.rfind(" ")
            if last_space != -1 and last_space > max_chars_per_line * 0.8:
                segment = segment[:last_space]
                current_index += len(segment) + 1
            else:
                current_index += max_chars_per_line
        else:
            current_index += max_chars_per_line

        lines.append(segment.strip())

    while len(lines) < total_lines:
        lines.append("")

    return lines


# ROTAS
@app.route("/")
def home():
    if "usuario" in session:
        return redirect(url_for("ficha"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("username", "")
        pw = request.form.get("password", "")

        if user == MEDICO_USERNAME and pw == MEDICO_PASSWORD:
            session["usuario"] = user
            return redirect(url_for("ficha"))
        else:
            flash("Usuário ou senha incorretos.")

    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login"))


@app.route("/ficha")
@login_required
def ficha():
    return render_template("index.html")


@app.route("/generate_doc", methods=["POST"])
@login_required
def generate_doc():
    context = {
        "nome": request.form.get("nome", ""),
        "numero": request.form.get("numero", ""),
        "data_nascimento": request.form.get("data_nascimento", ""),
        "idade": request.form.get("idade", ""),
        "sexo": request.form.get("sexo", ""),
        "estado_civil": request.form.get("estado_civil", ""),
        "ocupacao": request.form.get("ocupacao", ""),
        "nome_pai": request.form.get("nome_pai", ""),
        "nome_mae": request.form.get("nome_mae", ""),
        "endereco_permanente": request.form.get("endereco_permanente", ""),
        "endereco_temporario": request.form.get("endereco_temporario", ""),
        "cartao_sus": request.form.get("cartao_sus", ""),
        "data_atendimento": request.form.get("data_atendimento", ""),
        "evolucao": request.form.get("evolucao", ""),
    }

    for key in ["data_nascimento", "data_atendimento"]:
        if context[key]:
            try:
                date_obj = datetime.strptime(context[key], "%Y-%m-%d")
                context[key] = date_obj.strftime("%d/%m/%Y")
            except:
                pass

    evolution_segments = split_evolution_text(context["evolucao"])
    for i, part in enumerate(evolution_segments):
        context[f"evolucao{i+1}"] = part

    del context["evolucao"]

    try:
        doc = DocxTemplate(TEMPLATE_FILE)
        doc.render(context)

        buffer = io.BytesIO()
        doc.save(buffer)
        buffer.seek(0)

        filename = f"Ficha_{context['nome'].replace(' ', '_')}_{datetime.now().strftime('%Y%m%d%H%M%S')}.docx"

        return send_file(
            buffer,
            mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            as_attachment=True,
            download_name=filename
        )
    except Exception as e:
        return f"Erro: {e}", 500


if __name__ == "__main__":
    app.run(debug=True)
