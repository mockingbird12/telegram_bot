#!/usr/bin/python


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
                "Просто наберите команду /joke и не надорвите свои животики"
    if options == 'hello':
        return hello_msg