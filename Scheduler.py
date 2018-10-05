from telegram.ext import Updater, CommandHandler
import datetime
import urllib.request

def hoy(bot,update):
	user = update.message.from_user
	file = urllib.request.urlopen("https://raw.githubusercontent.com/Garco97/ScheduleTelegramBot/master/Horario.txt")
	day = datetime.datetime.now()
	for line in file:
		line = line.decode('utf-8')
		if day.strftime("%A") in line:
			update.message.reply_text(line)
			for line2 in file:
				line2 = line2.decode('utf-8')
				if line2  in ["Monday", "Tuesday", "Wednesday","Thursday" ,"Friday"]:
					print("No more")
					break
				horaInicio, separador,finAsignatura = line2.partition("-")
				horaFinal,separador,asignatura = finAsignatura.partition("_")
				hora, separador, minuto = horaFinal.partition(":")
				final = (int(hora) * 60) + int(minuto)
				now = datetime.datetime.now()
				actual = ((now.hour + 2) * 60) + now.minute
				if actual < final:
					update.message.reply_text(horaInicio + "-" + horaFinal + " " + asignatura)

def horario(bot,update):
	update.message.reply_text("https://web.unican.es/centros/ciencias/Documents/Horarios%201819/Grado/G-Inf%202018-19%20V6.pdf")


def trabajosPendientes(bot,update):
	file = urllib.request.urlopen("https://raw.githubusercontent.com/Garco97/ScheduleTelegramBot/master/trabajos.txt")
	for line in file:
		line = line.decode('utf-8')
		print(line)
		trabajo,separador,asignatura,separadorr,dia = line.partition("-")
		#asignatura,separador,dia = resto.partition("-")	
		update.message.reply_text("Entregar " + trabajo + " de " + asignatura + " el " + dia)



def main():
	updater = Updater('697984917:AAEPmyM3LemXq5MkEcepsrzb927Im9_wsAA')
	updater.dispatcher.add_handler(CommandHandler('Hoy', hoy))
	updater.dispatcher.add_handler(CommandHandler('Horario', horario))
	updater.dispatcher.add_handler(CommandHandler('Entregas',trabajosPendientes))
	updater.start_polling()
	updater.idle
if __name__ == '__main__':
    main()
