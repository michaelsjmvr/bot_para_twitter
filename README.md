### Hi, I'm Michael D.🤙

[![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/michael-douglas-640a11180/)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/michael.douglaspdl/)
[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://web.facebook.com/MikeeD.Cloud9/)

# Twitter Bot com PySide6

Este é um projeto de bot para o Twitter que permite postar automaticamente tweets em intervalos programados e responder a tweets com palavras-chave específicas. O bot foi desenvolvido em Python e utiliza as bibliotecas Tweepy para interagir com a API do Twitter e PySide6 para criar uma interface gráfica.

## Configuração

Antes de usar o bot, é necessário configurar suas credenciais de API do Twitter. Siga as etapas abaixo:

1. Crie uma conta de desenvolvedor no [Twitter Developer Platform](https://developer.twitter.com/en/apps).
2. Crie um aplicativo no Twitter Developer Platform para obter as chaves de API (Consumer Key, Consumer Secret, Access Token e Access Token Secret).
3. Substitua as chaves de API no arquivo `main.py` pelas suas próprias credenciais:

   ```python
   CONSUMER_KEY = 'SUA_CONSUMER_KEY'
   CONSUMER_SECRET = 'SUA_CONSUMER_SECRET'
   ACCESS_TOKEN = 'SEU_ACCESS_TOKEN'
   ACCESS_TOKEN_SECRET = 'SEU_ACCESS_TOKEN_SECRET'

Como Usar
Certifique-se de ter as bibliotecas Tweepy e PySide6 instaladas em seu ambiente Python:

pip install tweepy

Execute o aplicativo:

python main.py

A interface gráfica será exibida, permitindo que você configure o bot da seguinte maneira:

Especifique uma palavra-chave para monitorar.
Digite o texto do tweet que será postado como resposta.
Defina o intervalo de tempo entre as verificações de tweets.
Clique no botão "Iniciar Bot" para iniciar o bot.

O bot começará a procurar tweets com a palavra-chave especificada e responderá a eles com o texto do tweet configurado.

Você pode parar o bot a qualquer momento clicando no botão "Parar Bot".

Observações
Lembre-se de usar este bot de acordo com as políticas e regras de uso da API do Twitter. O uso indevido pode resultar na suspensão de sua conta.

Este é um exemplo básico de um bot de Twitter. Você pode estender e personalizar este bot conforme suas necessidades e adicionar recursos adicionais, como tratamento de erros e autenticação segura de chaves de API.

Certifique-se de manter suas chaves de API confidenciais e não compartilhá-las publicamente no seu repositório.
