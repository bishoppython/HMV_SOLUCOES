import re
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/submit', methods=['POST'])
def enviar():
    # Obtenha os dados do formulário
    plantonista = request.form['platonista']
    horario = request.form.getlist('horario')
    datahoraini = request.form['datahoraini']
    datahorafin = request.form['datahorafin']
    intercorrencias = request.form.getlist('intercorrencias')
    ocorrencias = request.form['ocorrencias']
    chamados = request.form.getlist('chamados')
    pendencias = request.form['pendencias']
    equipamento = request.form.getlist('equipamento')
    motivo = request.form['motivo']
    setor = request.form['setor']
    modelo = request.form['modelo']
    serie = request.form['serie']
    recolhimento = request.form['recolhido/substituido']
    organizacao = request.form.getlist('organizacao')
    desc_org = request.form['organizacao_desc']
    fora_comum = request.form.getlist('intercorrencias_a')
    comum = request.form['lista_ocorrencias']
    consideracoes = request.form.getlist('consideracoes')
    considera = request.form['consideracoes_f']


    # Verificando se o endereço de e-mail é válido
    email_destino = 'senar20514@in2reach.com'
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email_destino):
        return 'O endereço de e-mail de destino é inválido'

    # Envie o e-mail com os dados do formulário
    from Google import Create_Service
    import base64
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    CLIENT_SECRET_FILE = 'credentials.json'
    API_NAME = 'gmail'
    API_VERSION = 'v1'
    SCOPES = ['https://mail.google.com/']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    # Obtenha os dados do formulário
    plantonista = request.form['platonista']
    horario = request.form.getlist('horario')
    datahoraini = request.form['datahoraini']
    datahorafin = request.form['datahorafin']
    # Converter a string em um objeto datetime
    datahora_ini = datetime.strptime(datahoraini, '%Y-%m-%dT%H:%M')
    datahora_fin = datetime.strptime(datahorafin, '%Y-%m-%dT%H:%M')

    # Formatar a data e hora no formato desejado
    datahora_ini_f = datahora_ini.strftime('%d-%m-%Y %H:%M:%S')
    datahora_fin_f = datahora_fin.strftime('%d-%m-%Y %H:%M:%S')

    intercorrencias = request.form.getlist('intercorrencias')
    ocorrencias = request.form['ocorrencias']
    chamados = request.form.getlist('chamados')
    pendencias = request.form['pendencias']
    equipamento = request.form.getlist('equipamento')
    img_equipamento = request.files['imagens-equipamento']
    motivo = request.form['motivo']
    setor = request.form['setor']
    modelo = request.form['modelo']
    serie = request.form['serie']
    recolhimento = request.form['recolhido/substituido']
    organizacao = request.form.getlist('organizacao')
    desc_org = request.form['organizacao_desc']
    img_organizacao = request.files['organizacao_imagens']
    fora_comum = request.form.getlist('intercorrencias_a')
    comum = request.form['lista_ocorrencias']
    consideracoes = request.form.getlist('consideracoes')
    considera = request.form['consideracoes_f']
    try:
        # Crie o corpo do e-mail com os dados do formulário
        emailMsg = f''' :: RESUMO DO PLANTÃO ::
        ====================================================
           Plantonista: {plantonista}
           Turno do Plantão: {horario}
           Horário do Inicio Ronda: {datahora_ini_f}
           Horário do Final Ronda: {datahora_fin_f}
           Houve Intercorrências na Ronda: {intercorrencias}
           Lista de ocorrências: {"Sem dados Disponíveis" if len(ocorrencias) <= 0 else ocorrencias}
           Existe Chamados Pendentes: {chamados}
           Quais pendências: {"Sem dados Disponíveis" if len(pendencias) <= 0 else pendencias}
           Houve substituição de Equipamentos: {equipamento}
           Motivo: {"Sem dados Disponíveis" if len(motivo) <= 0 else motivo}
           Setor: {"Sem dados Disponíveis" if len(setor) <= 0 else setor}
           Modelo: {"Sem dados Disponíveis" if len(modelo) <= 0 else modelo}
           Serie: {"Sem dados Disponíveis" if len(serie) <= 0 else serie}
           Recolhido/Substituido: {"Sem dados Disponíveis" if len(recolhimento) <= 0 else recolhimento}
           Houve Organização do Setor: {organizacao}
           Descreva o que foi realizado: {"Sem dados Disponíveis" if len(desc_org) <= 0 else desc_org}
           Houve Ocorrências Fora do Comum: {fora_comum}
           Lista de Ocorrencias Insolitas: {"Sem dados Disponíveis" if len(comum) <= 0 else comum}
           Considerações Finais? {consideracoes}
           Considerações: {"Sem dados Disponíveis" if len(considera) <= 0 else considera}'''

        # Crie o objeto MIMEMultipart e anexe o corpo do e-mail
        mimeMessage = MIMEMultipart()
        mimeMessage['to'] = 'senar20514@in2reach.com'
        mimeMessage['subject'] = ':: RESUMO DO PLANTÃO ::'
        mimeMessage.attach(MIMEText(emailMsg, 'plain'))

        # adicione o arquivo de imagem
        if img_equipamento:
            img_data = img_equipamento.read()
            img_mime = MIMEImage(img_data, name=img_equipamento.filename)
            mimeMessage.attach(img_mime)

        if img_organizacao:
            img_data = img_organizacao.read()
            img_mime = MIMEImage(img_data, name=img_organizacao.filename)
            mimeMessage.attach(img_mime)

        # Codifique o objeto MIMEMultipart para o formato raw e envie o e-mail
        raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
        message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
        print(message)

        # Aqui você precisa escrever o código para enviar o e-mail

        return 'E-mail enviado com sucesso!'
        return redirect(url_for('formulario'))
    except Exception as e:
        return 'Erro ao enviar e-mail: ' + str(e)

if __name__ == '__main__':
    app.run(debug=True)
