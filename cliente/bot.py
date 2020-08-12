#Bibliotecas
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from time import time
import json
import requests
from base64 import b64decode, b64encode

#Arquivos
from cliente.spliteString import split_string
from cliente.conversation import conversation
from cliente.ibmWatson import Audio_To_Text
from cliente.config import credenciais,configuracoes

materia = assunto = name_audio = ''
numeros = ''

# ranges da conversa
MATERIA, ASSUNTO, SMS, AUDIO = range(4)

# funções de interações da duda
# duas funções para iniciar uma conversa com a duda, através de comandos ou palavras
# def start(update, context):
#     user = update.message.from_user
#     update.message.reply_text(conversation['inicio'])
#     update.message.reply_text(conversation['inicio_2'])
#     update.message.reply_text(conversation['materia'])
#     return MATERIA

def start(update, context):
    print ('Comando digitado: '+update.message.text)
    print (update)
    iniciar = ['/start','start', 'inicio', 'oi', 'olá', 'ola', 'começar', 'hi', 'hello']
    ajudar = ['/help','help','ajuda']

    update.message.reply_text('Olá '+update.message.chat.first_name+', seu código de usuário é: '+str(update.message.chat.id))

    for inicio in iniciar:
        if inicio == update.message.text:
            update.message.reply_text(conversation['inicio'])
            update.message.reply_text(conversation['materia'])
            return MATERIA

    for ajuda in ajudar:
        if ajuda == update.message.text:
            update.message.reply_text(conversation['ajuda'])
            return ConversationHandler.END

    update.message.reply_text('Me desculpa eu não sei o que fazer com esse comando, vamos tentar de novo, digite start ou /start para começarmos. 😉')



#função que resgata a materia e passa os próximos comandos
def get_materia(update, context):
    if not update.message.text == 'cancelar':
        global materia
        materia = update.message.text
        update.message.reply_text(f'Legal ja sei que sua Disciplina é de {materia.lower()}')
        update.message.reply_text(conversation['conteudo'])
        return ASSUNTO
    else:
        update.message.reply_text(conversation['cancelar'])
        update.message.reply_text(conversation['cancelar_2'])
        return ConversationHandler.END

#função que resgata o assunto e passa os próximos comandos
def get_assunto(update, context):
    if not update.message.text == 'cancelar':
        global assunto
        assunto = update.message.text
        update.message.reply_text(f'Muito legal o conteúdo da sua aula é sobre {assunto.lower()}')
        update.message.reply_text(conversation['numeros'])
        return SMS
    else:
        update.message.reply_text(conversation['cancelar'])
        update.message.reply_text(conversation['cancelar_2'])
        return ConversationHandler.END

def enviar_sms(update,context):
    global numeros
    numeros = '+55'+update.message.text
    update.message.reply_text(conversation['audio'])
    update.message.reply_text(conversation['audio_2'])
    return AUDIO

#função que pega o audio e trabalha com esse audio
def get_audio(update, context):
    update.message.reply_text('Só um minutinho estou processando tudo...')
    audio = update.message.audio.get_file()
    currente_date = time()

    dados = {'file_id':audio.file_unique_id,'file_path':audio.file_path,'materia':materia,'assunto':assunto,'horario':currente_date,'numeros':numeros}
    update.message.reply_text(f'Acesse: {configuracoes["URL_SERVER"]}audio?id={currente_date}-{audio.file_unique_id} para ouvir!')
    update.message.reply_text(f'O numero: {numeros} já vai receber o sms com as devidas informações da aula!')
    r = requests.post(configuracoes["URL_SERVER"]+'tratarAudio',data=json.dumps(dados))

    if r.status_code == 200:
        print ('ok')
    else:
        print ('erro')

    # return ConversationHandler.END

#função de tratamento de voice
def get_voice(update, context):
    update.message.reply_text('Só um minutinho estou processando tudo...')
    audio = update.message.voice.get_file()
    currente_date = time()

    dados = {'file_id':audio.file_unique_id,'file_path':audio.file_path,'materia':materia,'assunto':assunto,'horario':currente_date,'numeros':numeros}
    update.message.reply_text(f'Acesse: {configuracoes["URL_SERVER"]}audio?id={currente_date}-{audio.file_unique_id} para ouvir ou ligue para: +18566663241!')
    update.message.reply_text(f'O numero: {numeros} já recebeu o sms com as devidas informações da aula, se precisar é só me chamar novamente')
    r = requests.post(configuracoes["URL_SERVER"]+'tratarAudio',data=json.dumps(dados)) # requisição http post para o server passando os dados

    if r.status_code == 200:
        print ('ok')
        return ConversationHandler.END
    else:
        print ('erro')
        return ConversationHandler.END

    # return ConversationHandler.END

#funções para tratamento de erros no processo
#Mandou uma palavra en vez de um audio.
def not_audio(update, context):
    if not update.message.text == 'cancelar':
        update.message.reply_text('Me desculpe eu estava esperando um arquivo de audio')
        update.message.reply_text('Vamos tentar de novo!')
        update.message.reply_text('O arquivo precisa ser em formato MP3.')
        update.message.reply_text('Me envie o audio da aula:')
        return AUDIO
    else:
        update.message.reply_text(conversation['cancelar'])
        update.message.reply_text(conversation['cancelar_2'])
        return ConversationHandler.END

#função de cancelamento da conversa com a duda
def cancel(update, context):
    update.message.reply_text(conversation['cancelar'])
    update.message.reply_text(conversation['cancelar_2'])
    return ConversationHandler.END

# área de execução da duda
def main():
    token = b64decode(credenciais['TOKEN_BOT']).decode('utf-8')
    duda = Updater(token, use_context=True)
    dp = duda.dispatcher

    # Inicia o sistema e aguarda algum comando
    conv_handler = ConversationHandler(
        entry_points=[
            # CommandHandler = Comandos com /
            CommandHandler('start', start),
            CommandHandler('help', start),

            # Comandos sem /
            MessageHandler(Filters.text & ~Filters.command, start)
        ],
        states={
            MATERIA: [MessageHandler(Filters.text & ~Filters.command, get_materia)],
            ASSUNTO: [MessageHandler(Filters.text & ~Filters.command, get_assunto)],
            SMS: [MessageHandler(Filters.text & ~Filters.command, enviar_sms)],
            AUDIO: [
                MessageHandler(Filters.audio, get_audio),
                MessageHandler(Filters.voice, get_voice),
                MessageHandler(Filters.text & ~Filters.command, not_audio)
            ]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    print ('Bot Iniciado!')
    print ('Aguardando comando...')

    dp.add_handler(conv_handler)
    duda.start_polling()
    duda.idle()

if __name__ == "__main__":
    main()
