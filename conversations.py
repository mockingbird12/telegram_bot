#!/usr/bin/python
import random


def conv_start(options):
    hello_msg = "Здравствуйте, я - бот Василий" \
                ", представитель компании Мутант," \
                "буду стараться помочь Вам"
    services = "Наша компания предоставляет следующие услуги:\n" \
               "1. Межевание участков\n" \
               "2. Межевание участковых домов\n" \
               "3. Согласование ремонта\n" \
               "4. Согласование изменения несущей\n"
    if options == 'hello':
        return hello_msg
    if options == 'services':
        return services
    else:
        return "Unknown command"


def conv_bogdan(options):
    hello_msg = "Здравствуйте, я бот - Веселый Богданчик." \
                "Я могу рассказать Вам много веселых и смешных анекдотов. " \
                "Просто попросите меня рассказать шутку('хочу шутку', 'расскажи шутку')" \
                "и не надорвите свои животики"
    intro_msg = ["Ах ты похотливое животное, держи одну шутку",
                 "Ну хорошо, только не надорви свой животик",
                 "Вот вообще бомба, читай"]
    if options == 'hello':
        return hello_msg
    if options == 'intro':
        return intro_msg[random.randint(0,2)]