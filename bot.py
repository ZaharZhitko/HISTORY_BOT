import config
import telebot
from telebot import types
import time
import random
bot = telebot.TeleBot(config.token)
test = 0
@bot.message_handler(commands=["start"])
def start_message(message): # Клавиатура главного меню
    bot.send_message(message.chat.id, 'Привет 🤟')
    bot.send_message(message.chat.id, 'Этот бот поможет подтянуть твои знания по истории Беларуси 🇧🇾 и успешно сдать экзамен по ней 😁. HISTORY BOT постарается донести информацию простым и понятным языком. Также мы используем иллюстрации для большего понимания материала, но если вам этого окажется мало, то бот с радостью предоставит вам ссылку на более подробный источник (однако там информация может быть изложена не так понятно). Удачи !🙂')
    markup = types.InlineKeyboardMarkup()
    item1e = types.InlineKeyboardButton('Белорусские земли в VII-XII вв.', callback_data = 'era_1')
    item2e = types.InlineKeyboardButton('Белорусские земли в составе ВКЛ и Речи Посполитой (вторая половина XIII-конец XVIII в.)', callback_data = 'era_2')
    item3e = types.InlineKeyboardButton('Белорусские земли в составе Российской империи (конец XVIII-начало XX в.)', callback_data = 'era_3')
    item4e = types.InlineKeyboardButton('Беларусь в составе ССРБ, БССР и СССР (1917г. - 1991г.)', callback_data = 'era_4')
    item5e = types.InlineKeyboardButton('Республика Беларусь как суверенное государство', callback_data = 'era_5')
    markup.row(item1e)
    markup.row(item2e)
    markup.row(item3e)
    markup.row(item4e)
    markup.row(item5e)
    bot.send_message(message.chat.id, text='Выберите нужную вам эпоху для изучения:', reply_markup=markup)






@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global test
    try:
        if call:
            if call.data == "era_1":
                markup = types.InlineKeyboardMarkup()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Теперь выберите тему:')
                item1p_1 = types.InlineKeyboardButton('1. Древние люди на территории беларуси (VII-IX вв.)', callback_data='per_1_era_1')
                item2p_1 = types.InlineKeyboardButton('2. Полоцкое и Туровское княжество в X-XIII вв.', callback_data='per_2_era_1')
                item3p_1 = types.InlineKeyboardButton('3. Христианизация белорусских земель в X-XIII вв.', callback_data='per_3_era_1')
                item_back = types.InlineKeyboardButton('Назад 🔙', callback_data='back')
                markup.row(item1p_1)
                markup.row(item2p_1)
                markup.row(item3p_1)
                markup.row(item_back)
                bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=markup)
            if call.data == 'back':
                markup1 = types.InlineKeyboardMarkup()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите нужную вам эпоху для изучения:')
                item1e = types.InlineKeyboardButton('Белорусские земли в VII-XIII вв.', callback_data='era_1')
                item2e = types.InlineKeyboardButton('Белорусские земли в составе ВКЛ и Речи Посполитой (вторая половина XIII-конец XVIII в.)', callback_data='era_2')
                item3e = types.InlineKeyboardButton('Белорусские земли в составе Российской империи (конец XVIII-начало XX в.)', callback_data='era_3')
                item4e = types.InlineKeyboardButton('Беларусь в составе ССРБ, БССР и СССР (1917г. - 1991г.)', callback_data='era_4')
                item5e = types.InlineKeyboardButton('Республика Беларусь как суверенное государство', callback_data='era_5')
                markup1.row(item1e)
                markup1.row(item2e)
                markup1.row(item3e)
                markup1.row(item4e)
                markup1.row(item5e)
                bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.id,
                                              reply_markup=markup1)

            if call.data == "era_2":
                markup = types.InlineKeyboardMarkup()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Теперь выберите тему:')
                item1p_1 = types.InlineKeyboardButton('4. Образование Великого Княжества Литовского', callback_data='per_1_era_2')
                item2p_1 = types.InlineKeyboardButton('5. Борьба с агрессией крестоносцев в XIII-XV вв.', callback_data='per_2_era_2')
                item3p_1 = types.InlineKeyboardButton('6. Франциск Скорина - белорусский первопечатник, гуманист, просветитель', callback_data='per_3_era_2')
                item4p_1 = types.InlineKeyboardButton('8. Люблинская уния. Борьба ВКЛ за сохранение самостоятельности', callback_data='per_3_era_2')
                item5p_1 = types.InlineKeyboardButton('9. Формирование белорусской народности в XIV-XVIII вв.', callback_data='per_4_era_2')
                item_back = types.InlineKeyboardButton('Назад 🔙', callback_data='back')
                markup.row(item1p_1)
                markup.row(item2p_1)
                markup.row(item3p_1)
                markup.row(item4p_1)
                markup.row(item5p_1)
                markup.row(item_back)
                bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.id,
                                              reply_markup=markup)
            if call.data == "era_3":
                markup = types.InlineKeyboardMarkup()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Теперь выберите тему:')
                item1p_1 = types.InlineKeyboardButton('7. Беларусь в период Отечественной войны 1812г.', callback_data='per_1_era_3')
                item2p_1 = types.InlineKeyboardButton('10. Аграрная реформа 1861 г. и Столыпинская реформа на белорусских землях', callback_data='per_2_era_3')
                item3p_1 = types.InlineKeyboardButton('11. Революция 1905-1907 гг. и Февральская революция 1917 г.', callback_data='per_3_era_3')
                item4p_1 = types.InlineKeyboardButton('12. Беларусь в годы Первой мировой войны', callback_data='per_4_era_3')
                item_back = types.InlineKeyboardButton('Назад 🔙', casllback_data='back')
                markup.row(item1p_1)
                markup.row(item2p_1)
                markup.row(item3p_1)
                markup.row(item4p_1)
                markup.row(item_back)
                bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.id,
                                              reply_markup=markup)
            if call.data == "era_4":
                markup = types.InlineKeyboardMarkup()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Теперь выберите тему:')
                item1p_1 = types.InlineKeyboardButton('13. Беларусь во время Октябрьской революции 1917 г.', callback_data='per_1_era_4')
                item2p_1 = types.InlineKeyboardButton('14. Создание ССРБ: причины, основные события', callback_data='per_2_era_4')
                item3p_1 = types.InlineKeyboardButton('15. Беларусь в годы польско-советской войны 1919-1921 гг.', callback_data='per_3_era_4')
                item4p_1 = types.InlineKeyboardButton('16. Политика белоруссизации. Культура и образование в 1920-1930-е гг.', callback_data='per_4_era_4')
                item5p_1 = types.InlineKeyboardButton('17. Индустриализация и коллективизация сельского хозяйства в БССР', callback_data='per_5_era_4')
                item6p_1 = types.InlineKeyboardButton('18. Западная Беларусь в составе Польши (1921-1939 гг.)', callback_data='per_6_era_4')
                item7p_1 = types.InlineKeyboardButton('19. Подвиг белорусского народа в годы Великой Отечественной войны', callback_data='per_7_era_4')
                item8p_1 = types.InlineKeyboardButton('20. Геноцид населения Беларуси в годы ВОВ: план "Ост" германский "новый порядок"', callback_data='per_8_era_4')
                item9p_1 = types.InlineKeyboardButton('21. Социально-экономическое развитие БССР в 1940-х - 1980-е гг.', callback_data='per_9_era_4')
                item10p_1 = types.InlineKeyboardButton('22. Культура БССР во второй половине 1940-х - 1980-е гг.', callback_data='per_10_era_4')
                item_back = types.InlineKeyboardButton('Назад 🔙', callback_data='back')
                markup.row(item1p_1)
                markup.row(item2p_1)
                markup.row(item3p_1)
                markup.row(item4p_1)
                markup.row(item5p_1)
                markup.row(item6p_1)
                markup.row(item7p_1)
                markup.row(item8p_1)
                markup.row(item9p_1)
                markup.row(item10p_1)
                markup.row(item_back)
                bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.id,
                                              reply_markup=markup)
            if call.data == "era_5":
                markup = types.InlineKeyboardMarkup()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Теперь выберите тему:')
                item1p_1 = types.InlineKeyboardButton('Становление государственного суверенитета Республики Беларусь', callback_data='per_1_era_5')
                item2p_1 = types.InlineKeyboardButton('Внешняя политика Республики Беларусь', callback_data='per_2_era_5')
                item3p_1 = types.InlineKeyboardButton('Социально-экономисческое развитие Республики Беларусь', callback_data='per_3_era_5')
                item_back = types.InlineKeyboardButton('Назад 🔙', callback_data='back')
                markup.row(item1p_1)
                markup.row(item2p_1)
                markup.row(item3p_1)
                markup.row(item_back)
                bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.id,
                                              reply_markup=markup)

            if call.data == 'per_2_era_1':

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'''Полоцкое и Туровское княжества в X—XII вв.: территория, действия князей по укреплению и возвышению княжеств, раздробленность Полоцкой и Туровской земель
                Полоцкое княжество было первым государством на территории Беларуси. Впервые Полоцк упоминается в летописи в 862г., однако первый известный историкам его князь - Рогволод - упоминается только в 960-е гг. При нём Полоцкое княжество было достаточно сильным и соперничало даже с Новгородом и Киевом. Князья обоих городов хотели получить себе в жёны дочь Рогволода Рагнеду. Рогволод выбрал для своей дочери киевского князя, в ответ на это Новгородский князь - Владимир - двинул свои войска к Полоцку. Город был взят и сожжён, Рогволод и его сыновья убиты, а Рагнеда увезена в Новгород. После неудачного покушения Рогнеды на Владимира, её должны были казнить, но благодаря смелому поступку её сына - Изяслава - Владимир выслал её с сыном в только что построенный город - Изяславль (сейчас Заславль). Изчслав стал править в этом городе, Полоцкое вече пригласило его княжить в Полоцке, и династия полоцких князей была восстановлена.
            Изяслав и его мать были первыми христианами на территории Беларуси, сам Изяслав известен тем, что за всё правление ни разу не воевал, а Рогнеда, постригшаяся в монахини, стала одной из первых монашек на территории современной Беларуси. Усиление Полоцкого княжества произошло в XI в. при сыне Изяслава, полоцком князе Брячиславе (1001-1044). Он со своим войском захватил волоки, соединявшие Западную Двину и Днепр на пути «из варяг в греки» и принадлежавшие Новгороду. Волоки - учатки пути, на которых корабли тащили на суше (по брёвнам).
            Далее Полоцком стал править сын Брячислава - Всеслав(1044-1101). Стремясь укрепить свою власть и завоевать новые территории, он захватил и разграбил Новгород. В ответ сыновья Ярослава мудрого напали на Менск, город был разрушен, а его жители пленены. Вскоре князя постигла та же участь. Всеслав был заточён в тюрьму, однако, благодаря поднявшим восстание киевлянам, он не только освободился, но и стал киевским князем. Проправив 7 месяце, он вернулся в Полоцк. После смерти Всеслава Полоцкое княжество раздробилось на удельные княжества.
            Нельзя не выделить княжеско-вечевой строй. При таком строе шлавой княжества и главой войска - дружины и народного ополчения - был князь, но в период его отсутствия в городе правило вече. Также вече имело право заменить князя на другого или, если князь был убит, выбрать нового. Вече состояло из взрослых мужчин.
            Туровское княжество (Туров) впервые упоминается в летописи в 980 г. и тогда же упоминается его первый князь - Тур. Через некоторое время Туров стал зависим от Киевского княжества, однако в 1157 г. туровский князь Юрий Ярославич вернул Турову независимость, обовонив от войск великого князя. Юрий правил в Турове до 1162г.''', parse_mode="html")
                item_test = types.InlineKeyboardButton('   Тест по билетам 😈😈😈    ', callback_data='test')
                markup = types.InlineKeyboardMarkup()
                item_back = types.InlineKeyboardButton('Назад 🔙', callback_data='era_1')
                item_info = types.InlineKeyboardButton('Дополнительная информация 📚🔍')
                markup.row(item_info)
                markup.row(item_back)
                markup.row(item_test)
                bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=markup)

            if call.data == 'test':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Введите номера билетов через пробел, по которым хотите пройти тест (минимум 2):')

            if call.data == 'start_test_2':
                bot.send_message(call.message.chat.id, '1-й вопрос. Кто отвоевал у Новгородского княжества волоки, соединяющие Западную Двину С Днепром? (Введите имя и отчество)')
                test = 21



    except Exception as e:
        print(repr(e))

@bot.message_handler(content_types=["text"])
def test_message(message):
    str = message.text
    global test
    if test == 21 and 'брячислав' in str.lower():
        bot.send_message(message.chat.id, 'Верно! :)')
        test = 22
    elif test == 21:
        test = 22
        bot.send_message(message.chat.id, 'Неправильно, это Брячислав')
    elif any(['1 ' in message.text, '2 ' in message.text, '3 ' in message.text, '4 ' in message.text, '5 ' in message.text,
        '6 ' in message.text, '7 ' in message.text, '8 ' in message.text, '9 ' in message.text]):
        msg = message.text
        print(msg)

        list = msg.split()
        str = ''
        for i in range(len(list)):
            str = str + list[i] + ', '
        print(list)
        bot.send_message(message.chat.id, f'Вы выбрали билеты {str[:len(str) - 2]}')
        bot.send_message(message.chat.id, f'Бот начал выбирать случайный билет для вас 😈')
        time.sleep(3)
        bot.send_message(message.chat.id, f'Итак, ваш билет...')
        time.sleep(2)
        num = random.randrange(len(list))
        num_bil = 'start_test_' + list[num]
        for i in range(len(list)):
            list[i] = int(list[i])
        print(list)

        bot.send_message(message.chat.id, f'Номер {list[num]}')
        markup = types.InlineKeyboardMarkup()
        bil = list[num]
        item_bilet = types.InlineKeyboardButton(f'Начать тест по {bil}-му билету', callback_data=num_bil)
        markup.row(item_bilet)
        bot.send_message(message.chat.id, text='Нажмите на кнопку и тест начнётся', reply_markup=markup)

if __name__ == '__main__':
     bot.infinity_polling()