@bot.callback_query_handler(func=lambda call: call.data == 'per_1')
def per_1_era_1(call: types.CallbackQuery):
    markup = types.InlineKeyboardMarkup()
    item_link = types.InlineKeyboardButton('Дополнительная информация 📚', url = 'https://sites.google.com/view/history38/%D1%8D%D0%BA%D0%B7%D0%B0%D0%BC%D0%B5%D0%BD%D1%8B')
    item_back = types.InlineKeyboardButton('Назад 🔙', callback_data='era_1')
    markup.row(item_link)
    markup.row(item_back)
    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'era_1')
def era_1(call: types.CallbackQuery):
    markup = types.InlineKeyboardMarkup()
    item1p = types.InlineKeyboardButton('Древние люди на территории беларуси (VII-IX вв.)', callback_data='per_1')
    item2p = types.InlineKeyboardButton('Полоцкое и Туровское княжество в X-XIII вв.', callback_data='per_2')
    item3p = types.InlineKeyboardButton('Христианизация белорусских земель в X-XIII вв.', callback_data='per_3')
    item_back = types.InlineKeyboardButton('Назад 🔙', callback_data='back')
    markup.row(item1p)
    markup.row(item2p)
    markup.row(item3p)
    markup.row(item_back)
    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=markup)

https://sites.google.com/view/history38/%D1%8D%D0%BA%D0%B7%D0%B0%D0%BC%D0%B5%D0%BD%D1%8B

if any(['1' in message.text, '2' in message.text, '3' in message.text, '4' in message.text, '5' in message.text,
        '6' in message.text, '7' in message.text, '8' in message.text, '9' in message.text]):
    msg = message.text
    list = msg.split()
    str = ''
    for i in range(len(list)):
        str = str + list[i] + ', '
    bot.send_message(message.chat.id, f'Вы выбрали билеты {str[:len(str) - 1]}')
