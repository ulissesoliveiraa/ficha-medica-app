🩺 Ficha Médica Web – Sistema de Digitalização de Evoluções em UBS

Este projeto foi criado para resolver um problema real presente na maioria das Unidades Básicas de Saúde (UBS): a ausência de digitalização das fichas de evolução, fazendo com que médicos e profissionais da enfermagem ainda registrem tudo manualmente em formulários de papel.

A aplicação permite o preenchimento digital de fichas médicas, gerando automaticamente um arquivo no formato DOCX, seguindo exatamente o modelo utilizado pelas UBS.
Isso acelera o trabalho do profissional e reduz erros, rasuras e retrabalho.

---

🌐 Acesse a versão online (Render)

🔗 [https://ficha-medica-app.onrender.com/login](https://ficha-medica-app.onrender.com/login)

⚠ IMPORTANTE:
O Render entra em modo hibernação quando o app está inativo.
A primeira abertura pode demorar entre 30–60 segundos.
Depois que o servidor “acorda”, o sistema funciona normalmente.

---

🚀 Funcionalidades Atuais

🔐 Login Seguro

* Sistema com autenticação
* Senha com botão “mostrar/ocultar”
* Interface moderna e responsiva

📝 Dados do Paciente

* Campos completos da ficha médica da UBS
* Conversão automática de datas para o formato brasileiro

🏥 Evoluções Clínicas

* Adicionar múltiplas evoluções
* Editar evoluções registradas
* Remover evoluções
* Evoluções separadas automaticamente no documento

📄 Geração Automática de Documento

* Arquivo DOCX gerado no modelo oficial da UBS
* Divisão automática de texto em linhas
* Compatível com Word, Google Docs e LibreOffice

🎨 Interface Moderna

* Tela de login com imagem personalizada da médica (Dra. Fernanda Azevedo)
* Fundo com degradê azul
* Design responsivo para celulares, tablets e PCs

---

🛠️ Tecnologias Utilizadas

* Python + Flask
* docxtpl
* HTML5 e CSS3
* JavaScript
* Ambiente virtual (venv)
* Deploy no Render

---

📦 Como Executar o Projeto Localmente (direto pelo terminal do VS Code)

Passo a passo completo para rodar o sistema utilizando apenas o terminal integrado do Visual Studio Code.

---

1. Abrir o projeto no VS Code

* Clique em “File” → “Open Folder”
* Selecione a pasta ficha-medica-app

---

2. Abrir o terminal integrado

Use o atalho:

```
CTRL + `
```

Ou:
Menu → Terminal → New Terminal

O terminal será aberto já na pasta do projeto.

---

3. Criar o ambiente virtual (venv)

Windows:

```
python -m venv venv
```

Mac / Linux:

```
python3 -m venv venv
```

---

4. Ativar o venv

Windows:

```
venv\Scripts\activate
```

Mac / Linux:

```
source venv/bin/activate
```

Quando estiver ativado, o terminal exibirá algo assim:

```
(venv) PS C:\Sistemas\ficha-medica-app>
```

---

5. Instalar dependências

```
pip install -r requirements.txt
```

Se quiser instalar manualmente:

```
pip install flask docxtpl
pip freeze > requirements.txt
```

---

6. Executar o servidor Flask

```
python app.py
```

O terminal exibirá:

```
Running on http://127.0.0.1:5000/
```

---

7. Acessar o sistema no navegador

```
http://localhost:5000
```

---

8. Fechar o servidor

Pressione:

```
CTRL + C
```

---

🔮 Atualizações Futuras (Roadmap Oficial)

A aplicação já cumpre o objetivo principal de digitalizar fichas médicas, substituindo o processo manual realizado com caneta e papel.
Isso traz:

* Maior agilidade no atendimento
* Redução de erros
* Padronização no preenchimento
* Facilidade de arquivamento
* Melhoria no fluxo interno da UBS

Abaixo está o roadmap oficial de evolução do sistema.

---

🟦 1. Múltiplos Perfis de Usuário

👤 Recepção – poderá:

* Cadastrar pacientes
* Editar e apagar perfis
* Salvar dados completos
* Anexar foto do paciente
* Pesquisar por nome, CPF ou cartão SUS
* Armazenar cadastro em pasta ou banco de dados

🩺 Enfermagem / Triagem – poderá:

* Pesquisar pacientes cadastrados
* Criar evolução de triagem (pressão, sinais vitais, queixas iniciais)
* Salvar evolução vinculada ao atendimento
* Baixar ficha ou deixar salva para o médico

👨‍⚕️ Médico – poderá:

* Acessar paciente por nome, CPF ou cartão SUS
* Visualizar evolução registrada pela enfermagem
* Editar, apagar ou adicionar novas evoluções
* Gerar ficha final em DOCX
* Baixar ficha ou salvar histórico do paciente

---

🟦 2. Histórico de Pacientes

Estrutura planejada:

```
/pacientes/
    /CPF_DO_PACIENTE/
        cadastro.json
        evolucoes/
            evolucao_2025-01-29.docx
            evolucao_2025-02-03.docx
```

---

🟦 3. Evoluções Organizadas no Documento

* Linha em branco entre evoluções
* Cabeçalho separado por data e hora
* Identificação de evolução da enfermagem e evolução médica

---

🟦 4. Banco de Dados Futuro

* Fase 1: armazenamento local baseado em arquivos (JSON + DOCX)
* Fase 2: migração para banco de dados

  * SQLite
  * MySQL
  * PostgreSQL

---

⭐ Conclusão

O sistema moderniza o fluxo das UBS ao digitalizar fichas médicas, reduzindo erros e agilizando o atendimento.
Com as atualizações planejadas, este projeto evoluirá para um mini-prontuário eletrônico, integrando recepção, triagem e atendimento médico.

---

👨‍💻 Desenvolvedor
Ulisses Oliveira

Criado para auxiliar diretamente na rotina da
Dra. Fernanda Azevedo e demais profissionais da atenção básica.

