import telebot
from estrellas import estrellas, constelacion

bot = telebot.TeleBot("6141107908:AAEfYAug7bei9kW80EWyvSxlb8jFc9E7kQ4")

@bot.message_handler(commands=["start"])
def start(message):
    audio = open('bot_telegram/media/bienvenido.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)
    audio.close()
    photo = open("bot_telegram\media\gato-baile.gif", 'rb')
    bot.send_animation(message.chat.id, photo)
    photo.close()
    bot.send_message(message.chat.id, "Miaw!👋😺, ¿cómo estás? Estos son los comandos disponibles:")
    comandos(message)

@bot.message_handler(commands=["help"])
def ayuda(message):
    print("entra 2")
    bot.reply_to(message, "Estas son las ayudas ... ") # HACER LAS AYUDASSSSSS

@bot.message_handler(commands=["commands"])
def comandos(message):
    commands_list = ""
    with open("bot_telegram\comandos.txt", "r", encoding="utf-8") as f:
        for line in f:
            commands_list += line
    bot.reply_to(message, commands_list)

@bot.message_handler(commands=["estrella"])
def estrella(message):
    grafico_estrellas(message.chat.id)

@bot.message_handler(commands=["constelaciones"])
def constelaciones(message):
    constelaciones_list = "/boyero\n/casiopea\n/cazo\n/cygnet\n/geminis\n/hydra\n/osa_mayor\n/osa_menor"
    bot.reply_to(message, f"Elige una constelación 🌌: \n {constelaciones_list}")

@bot.message_handler(commands=["boyero"])
def boyero(message):
    print("entra 1")
    grafico_constelacion("Boyero", message.chat.id)

@bot.message_handler(commands=["casiopea"])
def casiopea(message):
    grafico_constelacion("Casiopea", message.chat.id)

@bot.message_handler(commands=["cazo"])
def cazo(message):
    grafico_constelacion("Cazo", message.chat.id)

@bot.message_handler(commands=["cygnet"])
def cygnet(message):
    grafico_constelacion("Cygnet", message.chat.id)

@bot.message_handler(commands=["geminis"])
def geminis(message):
    grafico_constelacion("Geminis", message.chat.id)

@bot.message_handler(commands=["hydra"])
def hydra(message):
    grafico_constelacion("Hydra", message.chat.id)

@bot.message_handler(commands=["osa_mayor"])
def osa_mayor(message):
    grafico_constelacion("Osa mayor", message.chat.id)

@bot.message_handler(commands=["osa_menor"])
def osa_menor(message):
    grafico_constelacion("Osa menor", message.chat.id)


@bot.message_handler(func=lambda message:True)


def mensaje(message):
    comandos(message)

def enviar_archivos(id, src_pic):
    photo = open(src_pic, 'rb')
    bot.send_photo(id, photo)
    photo.close()
    bot.send_message(id, "Para ver con más detalle, abre este archivo en tu navegador favorito. 🤫Tranquilo, es 100% confiable.")
    document = open('grafico.html', 'rb')
    bot.send_document(id, document)
    document.close()
    
def grafico_estrellas(id):
    estrellas()
    bot.send_message(id, "Aquí tienes un gráfico con todas las estrellas")
    enviar_archivos(id, "Coordenadas estrellas.png")

def grafico_constelacion(conste, id):
    constelacion(conste)
    bot.send_message(id, f"Aquí tienes la constelación {conste}")
    enviar_archivos(id, "Constelacion.png")


bot.polling()