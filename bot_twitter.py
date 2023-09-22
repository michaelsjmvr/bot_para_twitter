# Importando as bibliotecas necessárias
import tweepy  # Para interagir com a API do Twitter
import sys
import time
from PySide6 import QtWidgets  # Para criar a interface gráfica

# Chaves de API do Twitter (substitua com suas próprias chaves)
CONSUMER_KEY = 'SUA_CONSUMER_KEY'
CONSUMER_SECRET = 'SUA_CONSUMER_SECRET'
ACCESS_TOKEN = 'SEU_ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'SEU_ACCESS_TOKEN_SECRET'

# Configurando a autenticação do Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)  # Criando um objeto API para interagir com o Twitter

# Definindo a classe principal da aplicação
class TwitterBotApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Configurando a interface gráfica
        self.setWindowTitle('Twitter Bot')
        self.setGeometry(100, 100, 400, 200)

        # Criando botões e elementos de entrada de texto
        self.start_button = QtWidgets.QPushButton('Iniciar Bot', self)
        self.start_button.clicked.connect(self.start_bot)  # Conectando o botão a uma função

        self.stop_button = QtWidgets.QPushButton('Parar Bot', self)
        self.stop_button.clicked.connect(self.stop_bot)  # Conectando o botão a uma função

        self.keyword_label = QtWidgets.QLabel('Palavra-chave:', self)
        self.keyword_edit = QtWidgets.QLineEdit(self)

        self.tweet_text_label = QtWidgets.QLabel('Tweet a ser postado:', self)
        self.tweet_text_edit = QtWidgets.QLineEdit(self)

        self.interval_label = QtWidgets.QLabel('Intervalo (segundos):', self)
        self.interval_spin = QtWidgets.QSpinBox(self)
        self.interval_spin.setValue(3600)  # Intervalo padrão de 1 hora

        # Configurando o layout da interface
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.keyword_label)
        layout.addWidget(self.keyword_edit)
        layout.addWidget(self.tweet_text_label)
        layout.addWidget(self.tweet_text_edit)
        layout.addWidget(self.interval_label)
        layout.addWidget(self.interval_spin)
        self.setLayout(layout)

        self.bot_running = False  # Variável para rastrear o estado do bot

    def start_bot(self):
        if not self.bot_running:  # Verifica se o bot já está em execução
            self.bot_running = True
            self.start_button.setEnabled(False)  # Desabilita o botão "Iniciar"
            self.stop_button.setEnabled(True)    # Habilita o botão "Parar"

            keyword = self.keyword_edit.text()    # Obtém a palavra-chave da entrada de texto
            tweet_text = self.tweet_text_edit.text()  # Obtém o texto do tweet a ser postado
            interval = self.interval_spin.value()  # Obtém o intervalo de tempo em segundos

            while self.bot_running:  # Enquanto o bot estiver em execução
                try:
                    # Pesquisa por tweets com a palavra-chave
                    tweets = api.search(q=keyword)
                    for tweet in tweets:
                        # Responde ao tweet encontrado mencionando o usuário e enviando o tweet
                        api.update_status(f"@{tweet.user.screen_name} {tweet_text}", in_reply_to_status_id=tweet.id)
                        print(f"Resposta enviada para @{tweet.user.screen_name}: {tweet_text}")

                    # Aguarda o intervalo antes de procurar novamente
                    time.sleep(interval)
                except Exception as e:
                    print(f"Erro: {str(e)}")
                    self.stop_bot()

    def stop_bot(self):
        self.bot_running = False  # Para o bot
        self.start_button.setEnabled(True)  # Habilita o botão "Iniciar"
        self.stop_button.setEnabled(False)  # Desabilita o botão "Parar"

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = TwitterBotApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
