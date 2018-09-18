from telegram.ext import Updater, CommandHandler
import datetime
import urllib.request



def horario(bot,update):

	file = urllib.request.urlopen("https://raw.githubusercontent.com/Garco97/ScheduleTelegramBot/master/Horario.txt")	
	day = datetime.datetime.now()
	for line in file:
		line = line.decode('utf-8')
		print(line)
		if day.strftime("%A") in line:
			update.message.reply_text(line )
			for line2 in file:
				if line2  in ["Monday", "Tuesday", "Wednesday","Thursday" ,"Friday"]:
					print("No more classes")
					break
				horaInicio, separador,finAsignatura = line2.partition("-")
				horaFinal,separador,asignatura = finAsignatura.partition("_")
				hora, separador, minuto = horaFinal.partition(":")			
				final = (int(hora)*60) + int(minuto)
				now = datetime.datetime.now()			
				actual = (now.hour*60) + now.minute		
				if actual < final:
					update.message.reply_text(horaInicio + "-" + horaFinal + " " + asignatura)
			pass
	pass

	
def main():
	updater = Updater('697984917:AAEPmyM3LemXq5MkEcepsrzb927Im9_wsAA')

	updater.dispatcher.add_handler(CommandHandler('horario', horario))
	updater.start_polling()
	updater.idle

	print("Ejecutando")
if __name__ == '__main__':
    main()