from pyowm import OWM #импортируем
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'

place = input("Введите название города: ")
owm = OWM('26b4ba69b7ab18910b98a176c147ef4a', config_dict) #переменная с нашим API
mgr = owm.weather_manager() #менеджер погоды
observation = mgr.weather_at_place(place) #переменная с названием города
w = observation.weather

#температура
t = w.temperature("celsius")
t1 = t['temp']
t2 = t['feels_like']
t3 = t['temp_max']
t4 = t['temp_min']

#скорость ветра
wi = w.wind()['speed']

#влажность
humi = w.humidity

#облачность
cl = w.clouds

#статус (подпись описания погоды(снежность, дождь)
st = w.status

#детали
dt = w.detailed_status

#справочное время (время когда в последний раз брали данные о погоде)
ti = w.reference_time('iso')

#давление
pr = w.pressure['press']

#видимость
vd = w.visibility_distance

print("В городе " + str(place) + " температура " + str(t1) + " °C" + "\n" + 
	"Максимальная температура " + str(t3) + " °C" +"\n" + 
	"Минимальная температура " + str(t4) + " °C" + "\n" + 
	"Ощущается как " + str(t2) + " °C" + "\n" +
	"Скорость ветра " + str(wi) + " м/с" + "\n" + 
	"Давление " + str(pr) + " мм.рт.ст" + "\n" + 
	"Влажность " + str(humi) + " %" + "\n" + 
	"Видимость " + str(vd) + "  метров" + "\n" +
	"Описание " + str(st) + " - " + str(dt))
