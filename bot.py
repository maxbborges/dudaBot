# Esse é um script de bot com conversa guiada, a duda guiara todo os passos da conversa até a postagem da aula!

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from spliteString import split_string
from funDownload import download
from time import time
materia = assunto = ''


# ranges da conversa 
MATERIA, ASSUNTO, AUDIO = range(3)

# funções de interações da duda
# duas funções para iniciar uma conversa com a duda, através de comandos ou palavras
def start(update, context):
    user = update.message.from_user
    update.message.reply_text('Olá, eu sou a Duda! Tudo bem com você? Estou aqui para disponibilizar suas aulas com conteúdos programáticos para o enem aos seus alunos, tudo pelo telefone e gratuito 🤗')
    update.message.reply_text('Você pode cancelar o processo a qualquer momento escrevendo cancelar')
    update.message.reply_text('Vamos lá!')
    update.message.reply_text('Digame qual é a matéria da sua aula?')

def start_2(update, context):
    words =['start','help','inicio','ajuda','oi','olá','ola','começar','hi','hello']
    for word in words:
        if word == update.message.text:
            update.message.reply_text('Olá, eu sou a Duda! Tudo bem com você? Estou aqui para disponibilizar suas aulas com conteúdos programáticos para o enem aos seus alunos, tudo pelo telefone e gratuito 🤗')
            update.message.reply_text('Você pode cancelar o processo a qualquer momento escrevendo cancelar')
            update.message.reply_text('Vamos lá!')
            update.message.reply_text('Digame qual é a matéria da sua aula?')
            return MATERIA
        elif word == words[-1]:
            update.message.reply_text('Me desculpa eu não sei o que fazer com esse comando, vamos tentar de novo, digite start ou /start para começarmos. 😉')

#função que resgata a materia e passa os próximos comandos
def get_materia(update, context):
    if not update.message.text == 'cancelar':
        global materia
        materia = update.message.text
        update.message.reply_text('Legal ja sei que sua aula é de {}'.format(materia.lower()))
        update.message.reply_text('Agora me diga qual o assunto da sua aula?')
        return ASSUNTO
    else:
        update.message.reply_text('Ok')
        update.message.reply_text('não quer mais postar a aula tudo bem.')
        update.message.reply_text('assim que mudar de idéia volte a falar comgio estarei te esperando\n 😉')
        return ConversationHandler.END

#função que resgata o assunto e passa os próximos comandos
def get_assunto(update, context):
    if not update.message.text == 'cancelar':
        global assunto
        assunto = update.message.text
        update.message.reply_text('Muito legal sua aula é sobre {}'.format(assunto.lower()))
        update.message.reply_text('Estamos quase no fim!')
        update.message.reply_text('Agora eu só preciso do arquivo de audio da aula e logo a aula ja será postada!')
        update.message.reply_text('O arquivo precisa ser em formato MP3 ou OGG')
        update.message.reply_text('Me envie o audio da aula:')
        return AUDIO
    else:
        update.message.reply_text('Ok')
        update.message.reply_text('não quer mais postar a aula tudo bem.')
        update.message.reply_text('assim que mudar de idéia volte a falar comgio estarei te esperando\n 😉')
        return ConversationHandler.END

#função que pega o audio e trabalha com esse audio
def get_audio(update, context):
    update.message.reply_text('Só um minutinho estou processando tudo...')
    audio = update.message.audio.get_file()
    currente_date = time()
    name_audio = f'{currente_date}-{audio.file_unique_id}-{update.message.from_user.id}-{materia.lower()}-{split_string(assunto)}'
    download(url=f'{audio.file_path}',fileName=f'{name_audio}-audio-file.mp3')
    print(name_audio)
    update.message.reply_text(f'Seu audio {name_audio}')
    
    

#funções para tratamento de erros no processo
#Mandou uma palavra en vez de um audio.
def not_audio(update, context):
    if not update.message.text == 'cancelar':
        update.message.reply_text('Me desculpe eu estava esperando um audio')
        update.message.reply_text('Vamos tentar de novo!')
        update.message.reply_text('O arquivo precisa ser em formato MP3 ou OGG')
        update.message.reply_text('Me envie o audio da aula:')
        return AUDIO
    else:
        update.message.reply_text('Ok')
        update.message.reply_text('não quer mais postar a aula tudo bem.')
        update.message.reply_text('assim que mudar de idéia volte a falar comgio estarei te esperando\n 😉')
        return ConversationHandler.END

#função de cancelamento da conversa com a duda
def cancel(update, context):
    update.message.reply_text('Cancelado!')
    return ConversationHandler.END


# área de execução da duda
def main():
    duda = Updater('TOKEN_DUDA', use_context=True)
    dp = duda.dispatcher
    # add conversa guiada
    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler('start',start),
            CommandHandler('help', start),
            CommandHandler('ajuda', start),
            CommandHandler('inicio', start),
            MessageHandler(Filters.text & ~Filters.command, start_2)
        ],
        states={
            MATERIA:[MessageHandler(Filters.text & ~Filters.command, get_materia)],
            ASSUNTO:[MessageHandler(Filters.text & ~Filters.command, get_assunto)],
            AUDIO:[
                MessageHandler(Filters.audio, get_audio), 
                MessageHandler(Filters.text & ~Filters.command, not_audio)
            ]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    dp.add_handler(conv_handler)
    duda.start_polling()
    duda.idle()

if __name__ == "__main__":
    main()