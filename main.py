#___________________________установка библиотеки для работы четными числами

# from isOdd import isOdd



# print(isOdd(0)) 
# print(isOdd(4)) 

#___________________________установка библиотеки для создания программы для чтения данных________________

# from progress.bar import Bar
# import time
# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)
#     bar.next()
# bar.finish()

#_________________________________установка библиотеки для создания смайликов_______________________________________

# import emoji

# print(emoji.emojize('Python is :thumbs_up:'))


#______________________установка библиотеки для создания графиков ______________________________


# import numpy as np
# import matplotlib.pyplot as plt

# # Fixing random state for reproducibility
# np.random.seed(19680801)

# dt = 0.01
# t = np.arange(0, 30, dt)
# nse1 = np.random.randn(len(t))                 # white noise 1
# nse2 = np.random.randn(len(t))                 # white noise 2

# # Two signals with a coherent part at 10Hz and a random part
# s1 = np.sin(2 * np.pi * 10 * t) + nse1
# s2 = np.sin(2 * np.pi * 10 * t) + nse2

# fig, axs = plt.subplots(2, 1)
# axs[0].plot(t, s1, t, s2)
# axs[0].set_xlim(0, 2)
# axs[0].set_xlabel('time')
# axs[0].set_ylabel('s1 and s2')
# axs[0].grid(True)

# cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
# axs[1].set_ylabel('coherence')

# fig.tight_layout()
# plt.show()

#______________________создание простой визуализации_________________________

# import numpy as np
# import matplotlib.pyplot as plt

# list=[1,2,3,2,7]
# plt.plot(list)


# plt.show()


#_____________________бот_________________________________________________

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *



updater = Updater('5147196968:AAFr2QNPKpwzhnMCnIzTsWj7ULacVwoqZ00')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))

print('server start')

updater.start_polling()
updater.idle()