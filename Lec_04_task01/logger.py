from datetime import datetime as dt   # Метод логирования если есть какие_ либо сведения мы должны их записать
from time import time                  # если неоходимо что-то логировать то надо использовать datatime  time

def temperature_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};temperature;{}\n'
                    .format(time, data))

def pressure_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};pressure;{}\n'
                    .format(time, data))


def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};wind_speed;{}\n'
                    .format(time, data))
