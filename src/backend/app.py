from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message

app = Flask(__name__)
CORS(app)

# Configurações do servidor de e-mail (exemplo Gmail)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'josiane15santos24@gmail.com'       # coloque seu e-mail aqui
app.config['MAIL_PASSWORD'] = 'gkpk nprl cmmw mnxg'          # senha de app do Gmail

mail = Mail(app)

@app.route('/enviar-email', methods=['POST'])
def enviar_email():
    data = request.json
    nome = data.get('nome')
    email = data.get('email')
    mensagem = data.get('mensagem')

    try:
        msg = Message(
            subject=f'Nova mensagem de {nome}',
            sender=email,
            recipients=[app.config['MAIL_USERNAME']],
            body=mensagem
        )
        mail.send(msg)
        return jsonify({'message': 'E-mail enviado com sucesso!'}), 200
    except Exception as e:
        return jsonify({'message': 'Erro ao enviar e-mail.', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
