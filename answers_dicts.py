import messages as msg


rus_answers = {'привет': msg.ru_hello,
               'пока': msg.ru_bye,
               'сколько тебе лет?': msg.ru_age}

eng_answers = {'hello': msg.eng_hello,
               'bye': msg.eng_bye}

global_answers = {'rus': rus_answers,
                  'eng': eng_answers}

