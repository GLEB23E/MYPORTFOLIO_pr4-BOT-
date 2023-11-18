import telebot
from telebot import types
# your token 
token="5952735744:AAHHNyzTea_-ksXGeSBmq1BIRNH-mAmnuAI"
bot=telebot.TeleBot(token)
present_simple_use = ['– for permanent situations, habits, repeated actions or routines;','\n', '– for general truth;','\n', '– for storytelling and sports commentaries;','\n', '– for timetables (transport, programmes).','\n', 'Time expressions: usually, often, sometimes, hardly ever, every day/ month/ summer/ year, on Mondays/ Tuesdays ect.']
present_simple_form = ['+ V/ Vs','- do + not + V/ does + not+ V','? Do/Does __ V?', '\n','Affirmative form:','I invest.','She/he/it invests.','We/you/they invest.', '\n', 'Negative form:','I don’t invest.','She/he/it doesn’t invest.','We/you/ they don’t invest.', '\n', 'Question form:','Do I invest?','Does he/she/ it invest?','Do you/we/they invest? ']
present_continuous_use = ['– for actions taking place right now, at the moment of speaking;','\n','– for temporary situations at the present time;','\n','– for or changing or developing situations;','\n','– for expressing irritation or anger using adverbs: always, constantly;','\n','– for actions that have been already arranged to do in the nearest future.','\n','Time expressions: now, right now, at the moment, still, tonight.']
present_continuous_form = ['+ to be(am/is/are) + Ving','- to be(am/is/are) +not + Ving','? To be (am/is/are) _ Ving?','\n','Affirmative form:','I am investing.','She/he/it is investing.','We/you/they are investing.','Negative form:','I’m not investing.','She/he/it isn’t investing.','We/you/ they aren’t investing.','\n','Question form:','Am I investing?','Is he/she/ it investing?','Are you/we/they investing?']
present_perfect_use = ['– for completed actions with a result in the present;', '\n', '– for unfinished actions with yet;','\n','– for describing life experience;','\n','– for unfinished actions that started in the past and continue to the present (usually with state verbs);','\n','– for actions that have happened recently with words: this week, this month, today.','\n','Time expressions: never, ever, already, just, yet, before, recently, lately, since, for.']
present_perfect_form = ['+ has/have+ Past Participle','- has/ have + not+ Past Participle','? Have/Has ____ Past Participle?','\n','Affirmative form:','I have invested.','She/he/it has invested.','We/you/they have invested.','\n','Negative form:','I haven’t invested.','She/he/it hasn’t invested.','We/you/ they haven’t invested.','\n','Question form:','Have I invested?','Has he/she/ it invested?','Have you/we/they invested?']
future_simple_use = ['– for predictions, often with I think, believe, hope;', '\n', '– for decisions made at the moment of speaking;','\n','– for facts about the future;','\n','– for promises and offers.','\n','Time expressions:','tomorrow, next week/ Monday/ weekend/ soon/ in a week/ month/ year.']
future_simple_form = ['+ will V','- will+not+V','? Will ____V?','\n','Affirmative form:','I will invest.','He/she/it will invest.','We/you/ they will invest.','\n','Negative form:','I won’t invest.','He/she/it won’t invest.','We/you/ they won’t invest.','\n','Question form:','Will I invest?','Will he/she/it invest?','Will we/you/ they invest?']
future_continuos_use = ['– for activities planned to a future time;','\n','– for actions that will be in progress at a stated future time.','\n','Time expressions: from 6 till 8 tomorrow, whole day tomorrow, this time tomorrow/ next week. ']
future_continuos_form = ['+will be + Ving','-will be +not+ Ving','? Will ____ be Ving?','\n','Affirmative form:','I will be investing.','He/she/it will be investing.', 'We/you/they will be investing.','\n','Negative form:','I won’t be investing.','He/she/it won’t be investing.','We/you/they won’t be investing.','\n','Question form:','Will I be investing?','Will he/she/ it be investing?','Will we/ you/ they be investing?']
past_simple_use = ['– for past habits or states which are now finished;','\n','– for past actions which happened one after the other;','\n','– for actions which happened at definite time in the past;','\n','Time expressions: ','yesterday, ago, last week/ Monday/ weekend/ year, when, in 2012/1956.']
past_simple_form = ['+ Ved / V2 (Past Form)','- did+not+V','? Did ____V?','\n','Affirmative form:','I invested.','He/she/it invested.','We/you/ they invested.','\n','Negative form:','I didn’t invest.','He/she/it didn’t invest.','We/you/ they didn’t invest.','\n','Question form:','Did I invest?','Did he/she/it invest?','Did we/you/ they invest?']
past_continuos_use = ['– for actions which was in progress at a stated time in the past;','\n','– for an action which was in progress when another action interrupted it;','\n','– for two or more simultaneous past actions;','\n','– for describing story background.','\n','Time expressions: while, when, as, all morning/ evening/ day yesterday.']
past_continuos_form = ['+ to be(was/were) + Ving.','- to be (was/were) + not + Ving.', '? To be (was /were) ____ Ving?','Affirmative form:','I was investing.','He/she/it was investing.','We/you/they were investing.','\n','Negative form:','I wasn’t investing.','He/she/it wasn’t investing.','We/you/they weren’t investing.','\n','Question form:','Was I investing?','Was he/she/it investing?','Were we/you/they investing?']
past_perfect_use = ['– for an action which happened before another past action or before a stated time in the past; ','\n','– for actions which finished in the past and their result was visible in the past. ','\n','Time expressions: before, until, by, by the time, since, already, when, after, just, for.']
past_perfect_form = ['+ had + Past Participle.  ','- had + not+ Past Participle.  ','? Had ____ Past Participle ?','\n','Affirmative form:','I had invested.','He/she/it had invested.','We/you/they had invested.','\n','Negative form:','I hadn’t invested.','He/she/it hadn’t invested.','We/you/they hadn’t invested.','\n','Question form:','Had I invested?','Had he/she/ it invested?','Had we/ you/ they invested?']
passive_all_use = ['– for actions when the person who carries out the action is unknown, unimportant or obvious;', '\n','– for situations when the action itself is more important than the person who carries it out;','\n','– for actions describing an unpleasant event and we do not want to say who or what is to blame;','\n','We can us a phrase with by to say who did the action.;', 'The present perfect continuous, the future continuous, the past perfect continuous and the future perfect continuous are not normally used in passive voice.']
present_simple_form1 = ['+ to be (am/is/are) + Past Participle','- to be (am/is/are) +not + Past Participle','? to be (am/is/are) ____ Past Participle?','\n','Affirmative form:','Money is invested. Shares are sold to investors. ','\n','Negative form:','Money isn’t invested. ','Shares aren’t sold to investors. ','\n','Question form:','Is money invested? Are shares sold to investors? ']
future_simple_form =['+ to be (will be) + Past Participle ','– to be (will be) + not+ Past Participle','? Will ____be Past Participle?','\n','Affirmative form:','Money will be invested. Shares will be sold to investors.', '\n','Negative form:','Money won’t be invested. ','Shares won’t be sold to investors.','\n','Question form:','Will money be invested?','Will shares be sold to investors?']
present_perfect_use = ['+ will have + been +Past Participle','– will have + not+ been+ Past Participle','? Will ____ have +been + Past Participle? ','\n','Affirmative form:','Money will have been invested. Shares will have been to investors. ','\n','Negative form:','Money won’t have been invested. ','Shares won’t have been sold to investors.','\n','Question form:','Will money have been invested?','Will shares have been sold to investors?']
p_c_e = ['European governments are finalizing support measures for households and businesses struggling to pay for energy.', '\n', 'The bank is assuming that the government approximately halves its support for households’ energy bills.', '\n', 'Supply and demand are constantly changing.']
p_c_E = ['We (go) to the cinema later.', 'They (work) now.', 'You (not walk).', 'They (learn) new things?', 'When he (start) work?', 'Why I (stay) at home?', 'It (get) dark?',  'We (not win).', 'They  (not bring) a cake.', 'How she (travel)?']
@bot.message_handler(commands=["start"])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Active voice")
    button2 = types.KeyboardButton(text="passive voice")
    button3 = types.KeyboardButton(text="Others")
    keyboard.add(button1, button2, button3)
    bot.send_message(message.chat.id,"Выберите раздел!", reply_markup=keyboard)


def active_voice(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Present")
    button2 = types.KeyboardButton(text="Past")
    button3 = types.KeyboardButton(text="Future")
    button4 = types.KeyboardButton(text="Back")
    keyboard.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id,"Выберите время", reply_markup=keyboard)

    
def present(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Present Simple")
    button2 = types.KeyboardButton(text="Present Continuous")
    button3 = types.KeyboardButton(text="Present Perfect")
    button5 = types.KeyboardButton(text="Present Perfect Continuous")
    button4 = types.KeyboardButton(text="Back to voices")
    keyboard.add(button1, button2, button3, button5, button4)
    bot.send_message(message.chat.id,"Выберите точное время", reply_markup=keyboard)
def past(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Past Simple")
    button2 = types.KeyboardButton(text="Past Continuous")
    button3 = types.KeyboardButton(text="Past Perfect")
    button5 = types.KeyboardButton(text="Past Perfect Continuous")
    button4 = types.KeyboardButton(text="Back to voices")
    keyboard.add(button1, button2, button3, button5, button4)
    bot.send_message(message.chat.id,"Выберите точное время", reply_markup=keyboard)
def future(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Future Simple")
    button2 = types.KeyboardButton(text="Future Continuous")
    button3 = types.KeyboardButton(text="Future Perfect")
    button5 = types.KeyboardButton(text="Future Perfect Continuous")
    button4 = types.KeyboardButton(text="Back to voices")
    keyboard.add(button1, button2, button3, button5, button4)
    bot.send_message(message.chat.id,"Выберите точное время", reply_markup=keyboard)




def examepls_of_pc(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Present Simple")
    button2 = types.KeyboardButton(text="Present Continuous")
    button3 = types.KeyboardButton(text="Present Perfect")
    button5 = types.KeyboardButton(text="Present Perfect Continuous")
    button4 = types.KeyboardButton(text="Back to voices")
    keyboard.add(button1, button2, button3, button5, button4)
    bot.send_message(message.chat.id,"\n".join(p_c_e), reply_markup=keyboard)



def examepls_of_pc(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bot.send_message(message.chat.id,"\n".join(p_c_e), reply_markup=keyboard)
def exsersises_of_pc(message):
    for i in p_c_E:
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        bot.send_message(message.chat.id,i, reply_markup=keyboard)


def tr(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bot.send_message(message.chat.id,'Right', reply_markup=keyboard)
def fl(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bot.send_message(message.chat.id,'False', reply_markup=keyboard)


def present_simple(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Rules present simple")
    button2 = types.KeyboardButton(text="Examples present simple")
    button3 = types.KeyboardButton(text="Exsersises present simple")
    button4 = types.KeyboardButton(text="Back to times")
    keyboard.add(button1, button2, button3,button4)
    bot.send_message(message.chat.id,"Выберите функцию", reply_markup=keyboard)
def past_simple(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Rules past simple")
    button2 = types.KeyboardButton(text="Examples past simple")
    button3 = types.KeyboardButton(text="Exsersises past simple")
    button4 = types.KeyboardButton(text="Back to times")
    keyboard.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id,"Выберите функцию", reply_markup=keyboard)
def future_simple(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Rules future simple")
    button2 = types.KeyboardButton(text="Examples future simple")
    button3 = types.KeyboardButton(text="Exsersises future simple")
    button4 = types.KeyboardButton(text="Back to times")
    keyboard.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id,"Выберите функцию", reply_markup=keyboard)
def present_continuous(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Rules present continuous")
    button2 = types.KeyboardButton(text="Examples present continuous")
    button3 = types.KeyboardButton(text="Exsersises present continuous")
    button4 = types.KeyboardButton(text="Back to times")
    keyboard.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id,"Выберите функцию", reply_markup=keyboard)
def past_continuous(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Rules past continuous")
    button2 = types.KeyboardButton(text="Examples past continuous")
    button3 = types.KeyboardButton(text="Exsersises past continuous")
    button4 = types.KeyboardButton(text="Back to times")
    keyboard.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id,"Выберите функцию", reply_markup=keyboard)
def future_continuous(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Rules future continuous")
    button2 = types.KeyboardButton(text="Examples future continuous")
    button3 = types.KeyboardButton(text="Exsersises future continuous")
    button4 = types.KeyboardButton(text="Back to times")
    keyboard.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id,"Выберите функцию", reply_markup=keyboard)
def present_perfect(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Rules present perfect")
    button2 = types.KeyboardButton(text="Examples present perfect")
    button3 = types.KeyboardButton(text="Exsersises present perfect")
    button4 = types.KeyboardButton(text="Back to times")
    keyboard.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id,"Выберите функцию", reply_markup=keyboard)
def past_perfect(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Rules past perfect")
    button2 = types.KeyboardButton(text="Examples past perfect")
    button3 = types.KeyboardButton(text="Exsersises past perfect")
    button4 = types.KeyboardButton(text="Back to times")
    keyboard.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id,"Выберите функцию", reply_markup=keyboard)
def future_perfect(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Rules future perfect")
    button2 = types.KeyboardButton(text="Examples future perfect")
    button3 = types.KeyboardButton(text="Exsersises future perfect")
    button4 = types.KeyboardButton(text="Back to times")
    keyboard.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id,"Выберите функцию", reply_markup=keyboard)
def present_simple_rules(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button2 = types.KeyboardButton(text="Examples present simple")
    button3 = types.KeyboardButton(text="Exsersises present simple")
    button4 = types.KeyboardButton(text="Back to times")
    keyboard.add(button2, button3,button4)
    bot.send_message(message.chat.id,"USE:", reply_markup=keyboard)
    bot.send_message(message.chat.id,"\n".join(present_simple_use), reply_markup=keyboard)
    bot.send_message(message.chat.id,"FORM:", reply_markup=keyboard)
    bot.send_message(message.chat.id,"\n".join(present_simple_form), reply_markup=keyboard)
def past_simple_rules(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button2 = types.KeyboardButton(text="Examples past simple")
    button3 = types.KeyboardButton(text="Exsersises past simple")
    button4 = types.KeyboardButton(text="Back to times")
    keyboard.add(button2, button3, button4)
    bot.send_message(message.chat.id,"USE:", reply_markup=keyboard)
    bot.send_message(message.chat.id,"\n".join(past_simple_use), reply_markup=keyboard)
    bot.send_message(message.chat.id,"FORM:", reply_markup=keyboard)
    bot.send_message(message.chat.id,"\n".join(past_simple_form), reply_markup=keyboard)
def future_simple_rules(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button2 = types.KeyboardButton(text="Examples future simple")
    button3 = types.KeyboardButton(text="Exsersises future simple")
    button4 = types.KeyboardButton(text="Back to times")
    keyboard.add(button2, button3, button4)
    bot.send_message(message.chat.id,"USE:", reply_markup=keyboard)
    bot.send_message(message.chat.id,"\n".join(future_simple_use), reply_markup=keyboard)
    bot.send_message(message.chat.id,"FORM:", reply_markup=keyboard)
    bot.send_message(message.chat.id,"\n".join(future_simple_form), reply_markup=keyboard)
def present_continuous_rules(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button2 = types.KeyboardButton(text="Examples present continuous")
    button3 = types.KeyboardButton(text="Exsersises present continuous")
    button4 = types.KeyboardButton(text="Back to times")
    keyboard.add(button2, button3, button4)
    bot.send_message(message.chat.id,"USE:", reply_markup=keyboard)
    bot.send_message(message.chat.id,"\n".join(present_continuous_use), reply_markup=keyboard)
    bot.send_message(message.chat.id,"FORM:", reply_markup=keyboard)
    bot.send_message(message.chat.id,"\n".join(present_continuous_form), reply_markup=keyboard)
def past_continuous_rules(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button2 = types.KeyboardButton(text="Examples past continuous")
    button3 = types.KeyboardButton(text="Exsersises past continuous")
    button4 = types.KeyboardButton(text="Back to times")
    keyboard.add(button2, button3, button4)
    bot.send_message(message.chat.id,"USE:", reply_markup=keyboard)
    bot.send_message(message.chat.id,"\n".join(past_continuos_use), reply_markup=keyboard)
    bot.send_message(message.chat.id,"FORM:", reply_markup=keyboard)
    bot.send_message(message.chat.id,"\n".join(past_continuos_form), reply_markup=keyboard)
def future_continuous_rules(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button2 = types.KeyboardButton(text="Examples future continuous")
    button3 = types.KeyboardButton(text="Exsersises future continuous")
    button4 = types.KeyboardButton(text="Back to times")
    keyboard.add(button2, button3, button4)
    bot.send_message(message.chat.id,"USE:", reply_markup=keyboard)
    bot.send_message(message.chat.id,"\n".join(future_continuos_use), reply_markup=keyboard)
    bot.send_message(message.chat.id,"FORM:", reply_markup=keyboard)
    bot.send_message(message.chat.id,"\n".join(future_continuos_form), reply_markup=keyboard)
def present_perfect_rules(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button2 = types.KeyboardButton(text="Examples present perfect")
    button3 = types.KeyboardButton(text="Exsersises present perfect")
    button4 = types.KeyboardButton(text="Back to times")
    keyboard.add(button2, button3, button4)
    bot.send_message(message.chat.id,"USE:", reply_markup=keyboard)
    bot.send_message(message.chat.id,"\n".join(present_perfect_use), reply_markup=keyboard)
    bot.send_message(message.chat.id,"FORM:", reply_markup=keyboard)
    bot.send_message(message.chat.id,"\n".join(present_perfect_form), reply_markup=keyboard)
def past_perfect_rules(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button2 = types.KeyboardButton(text="Examples past perfect")
    button3 = types.KeyboardButton(text="Exsersises past perfect")
    button4 = types.KeyboardButton(text="Back to times")
    keyboard.add(button2, button3, button4)
    bot.send_message(message.chat.id,"USE:", reply_markup=keyboard)
    bot.send_message(message.chat.id,"\n".join(past_perfect_use), reply_markup=keyboard)
    bot.send_message(message.chat.id,"FORM:", reply_markup=keyboard)
    bot.send_message(message.chat.id,"\n".join(past_perfect_form), reply_markup=keyboard)
def future_perfect_rules(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button2 = types.KeyboardButton(text="Examples future perfect")
    button3 = types.KeyboardButton(text="Exsersises future perfect")
    button4 = types.KeyboardButton(text="Back to times")
    keyboard.add(button2, button3, button4)
    bot.send_message(message.chat.id,"Выберите функцию", reply_markup=keyboard)



def passive_voice(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Present Passive")
    button2 = types.KeyboardButton(text="Past Passive")
    button3 = types.KeyboardButton(text="Future Passive")
    button4 = types.KeyboardButton(text="Back")
    keyboard.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id,"Выберите время", reply_markup=keyboard)
# def present(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button1 = types.KeyboardButton(text="Present Simple")
#     button2 = types.KeyboardButton(text="Present Continuous")
#     button3 = types.KeyboardButton(text="Present Perfect")
#     button4 = types.KeyboardButton(text="Back to voices")
#     keyboard.add(button1, button2, button3,button4)
# #     bot.send_message(message.chat.id,"Выберите точное время", reply_markup=keyboard)
# def past(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button1 = types.KeyboardButton(text="Past Simple")
#     button2 = types.KeyboardButton(text="Past Continuous")
#     button3 = types.KeyboardButton(text="Past Perfect")
#     button4 = types.KeyboardButton(text="Back to voices")
#     keyboard.add(button1, button2, button3,button4)
#     bot.send_message(message.chat.id,"Выберите точное время", reply_markup=keyboard)
# def future(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button1 = types.KeyboardButton(text="Future Simple")
#     button2 = types.KeyboardButton(text="Future Continuous")
#     button3 = types.KeyboardButton(text="Future Perfect")
#     button4 = types.KeyboardButton(text="Back to voices")
#     keyboard.add(button1, button2, button3, button4)
#     bot.send_message(message.chat.id,"Выберите точное время", reply_markup=keyboard)



# def present_simple_passive(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button1 = types.KeyboardButton(text="Rules present simple passive")
#     button2 = types.KeyboardButton(text="Examples present simple passive")
#     button3 = types.KeyboardButton(text="Exsersises present simple passive")
#     button4 = types.KeyboardButton(text="Back to times passive")
#     keyboard.add(button1, button2, button3,button4)
#     bot.send_message(message.chat.id,"Выберите функцию", reply_markup=keyboard)
# def past_simple_passive(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button1 = types.KeyboardButton(text="Rules past simple passive")
#     button2 = types.KeyboardButton(text="Examples past simple passive")
#     button3 = types.KeyboardButton(text="Exsersises past simple passive")
#     button4 = types.KeyboardButton(text="Back to times passive")
#     keyboard.add(button1, button2, button3, button4)
#     bot.send_message(message.chat.id,"Выберите функцию", reply_markup=keyboard)
# def future_simple_passive(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button1 = types.KeyboardButton(text="Rules future simple passive")
#     button2 = types.KeyboardButton(text="Examples future simple passive")
#     button3 = types.KeyboardButton(text="Exsersises future simple passive")
#     button4 = types.KeyboardButton(text="Back to times passive")
#     keyboard.add(button1, button2, button3, button4)
#     bot.send_message(message.chat.id,"Выберите функцию", reply_markup=keyboard)
# def present_continuous_passive(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button1 = types.KeyboardButton(text="Rules present continuous passive")
#     button2 = types.KeyboardButton(text="Examples present continuous passive")
#     button3 = types.KeyboardButton(text="Exsersises present continuous passive")
#     button4 = types.KeyboardButton(text="Back to times passive")
#     keyboard.add(button1, button2, button3, button4)
#     bot.send_message(message.chat.id,"Выберите функцию", reply_markup=keyboard)
# def past_continuous_passive(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button1 = types.KeyboardButton(text="Rules past continuous passive")
#     button2 = types.KeyboardButton(text="Examples past continuous passive")
#     button3 = types.KeyboardButton(text="Exsersises past continuous passive")
#     button4 = types.KeyboardButton(text="Back to times passive")
#     keyboard.add(button1, button2, button3, button4)
#     bot.send_message(message.chat.id,"Выберите функцию", reply_markup=keyboard)
# def future_continuous_passive(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button1 = types.KeyboardButton(text="Rules future continuous passive")
#     button2 = types.KeyboardButton(text="Examples future continuous passive")
#     button3 = types.KeyboardButton(text="Exsersises future continuous passive")
#     button4 = types.KeyboardButton(text="Back to times passive")
#     keyboard.add(button1, button2, button3, button4)
#     bot.send_message(message.chat.id,"Выберите функцию", reply_markup=keyboard)
# def present_perfect_passive(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button1 = types.KeyboardButton(text="Rules present perfect passive")
#     button2 = types.KeyboardButton(text="Examples present perfect passsive")
#     button3 = types.KeyboardButton(text="Exsersises present perfect passsive")
#     button4 = types.KeyboardButton(text="Back to times passive")
#     keyboard.add(button1, button2, button3, button4)
#     bot.send_message(message.chat.id,"Выберите функцию", reply_markup=keyboard)
# def past_perfect_passive(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button1 = types.KeyboardButton(text="Rules past perfect passive")
#     button2 = types.KeyboardButton(text="Examples past perfect passsive")
#     button3 = types.KeyboardButton(text="Exsersises past perfect passsive")
#     button4 = types.KeyboardButton(text="Back to times passive")
#     keyboard.add(button1, button2, button3, button4)
#     bot.send_message(message.chat.id,"Выберите функцию", reply_markup=keyboard)
# def future_perfect_passive(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button1 = types.KeyboardButton(text="Rules future perfect passive")
#     button2 = types.KeyboardButton(text="Examples future perfect passsive")
#     button3 = types.KeyboardButton(text="Exsersises future perfect passsive")
#     button4 = types.KeyboardButton(text="Back to times passive")
#     keyboard.add(button1, button2, button3, button4)
#     bot.send_message(message.chat.id,"Выберите функцию", reply_markup=keyboard)
# def present_simple_rules_passive(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button2 = types.KeyboardButton(text="Examples present simple passive")
#     button3 = types.KeyboardButton(text="Exsersises present simple passive")
#     button4 = types.KeyboardButton(text="Back to times passsive")
#     keyboard.add(button2, button3,button4)
#     bot.send_message(message.chat.id,"USE:", reply_markup=keyboard)
#     bot.send_message(message.chat.id,"\n".join(passive_all_use), reply_markup=keyboard)
#     bot.send_message(message.chat.id,"FORM:", reply_markup=keyboard)
#     bot.send_message(message.chat.id,"\n".join(present_simple_form), reply_markup=keyboard)
# def past_simple_rules_passive(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button2 = types.KeyboardButton(text="Examples past simple passive")
#     button3 = types.KeyboardButton(text="Exsersises past simple passive")
#     button4 = types.KeyboardButton(text="Back to times passive")
#     keyboard.add(button2, button3, button4)
#     bot.send_message(message.chat.id,"USE:", reply_markup=keyboard)
#     bot.send_message(message.chat.id,"\n".join(passive_all_use), reply_markup=keyboard)
#     bot.send_message(message.chat.id,"FORM:", reply_markup=keyboard)
#     bot.send_message(message.chat.id,"\n".join(past_simple_form), reply_markup=keyboard)
# def future_simple_rules_passive(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button2 = types.KeyboardButton(text="Examples future simple passive")
#     button3 = types.KeyboardButton(text="Exsersises future simple passive")
#     button4 = types.KeyboardButton(text="Back to times passive")
#     keyboard.add(button2, button3, button4)
#     bot.send_message(message.chat.id,"USE:", reply_markup=keyboard)
#     bot.send_message(message.chat.id,"\n".join(passive_all_use), reply_markup=keyboard)
#     bot.send_message(message.chat.id,"FORM:", reply_markup=keyboard)
#     bot.send_message(message.chat.id,"\n".join(future_simple_form), reply_markup=keyboard)
# def present_continuous_rules_passive(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button2 = types.KeyboardButton(text="Examples present continuous passive")
#     button3 = types.KeyboardButton(text="Exsersises present continuous passive")
#     button4 = types.KeyboardButton(text="Back to times passive")
#     keyboard.add(button2, button3, button4)
#     bot.send_message(message.chat.id,"USE:", reply_markup=keyboard)
#     bot.send_message(message.chat.id,"\n".join(passive_all_use), reply_markup=keyboard)
#     bot.send_message(message.chat.id,"FORM:", reply_markup=keyboard)
#     bot.send_message(message.chat.id,"\n".join(present_continuous_form), reply_markup=keyboard)
# def past_continuous_rules_passive(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button2 = types.KeyboardButton(text="Examples past continuous passive")
#     button3 = types.KeyboardButton(text="Exsersises past continuous psssive")
#     button4 = types.KeyboardButton(text="Back to times passive")
#     keyboard.add(button2, button3, button4)
#     bot.send_message(message.chat.id,"USE:", reply_markup=keyboard)
#     bot.send_message(message.chat.id,"\n".join(passive_all_use), reply_markup=keyboard)
#     bot.send_message(message.chat.id,"FORM:", reply_markup=keyboard)
#     bot.send_message(message.chat.id,"\n".join(past_continuos_form), reply_markup=keyboard)
# def future_continuous_rules_passive(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button2 = types.KeyboardButton(text="Examples future continuous passive")
#     button3 = types.KeyboardButton(text="Exsersises future continuous passive")
#     button4 = types.KeyboardButton(text="Back to times passive")
#     keyboard.add(button2, button3, button4)
#     bot.send_message(message.chat.id,"USE:", reply_markup=keyboard)
#     bot.send_message(message.chat.id,"\n".join(passive_all_use), reply_markup=keyboard)
#     bot.send_message(message.chat.id,"FORM:", reply_markup=keyboard)
#     bot.send_message(message.chat.id,"\n".join(future_continuos_form), reply_markup=keyboard)
# def present_perfect_rules_passive(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button2 = types.KeyboardButton(text="Examples present perfect passive")
#     button3 = types.KeyboardButton(text="Exsersises present perfect passive")
#     button4 = types.KeyboardButton(text="Back to times passive")
#     keyboard.add(button2, button3, button4)
#     bot.send_message(message.chat.id,"USE:", reply_markup=keyboard)
#     bot.send_message(message.chat.id,"\n".join(passive_all_use), reply_markup=keyboard)
#     bot.send_message(message.chat.id,"FORM:", reply_markup=keyboard)
#     bot.send_message(message.chat.id,"\n".join(present_perfect_form), reply_markup=keyboard)
# def past_perfect_rules_passive(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button2 = types.KeyboardButton(text="Examples past perfect passive")
#     button3 = types.KeyboardButton(text="Exsersises past perfect passive")
#     button4 = types.KeyboardButton(text="Back to times passive")
#     keyboard.add(button2, button3, button4)
#     bot.send_message(message.chat.id,"USE:", reply_markup=keyboard)
#     bot.send_message(message.chat.id,"\n".join(passive_all_use), reply_markup=keyboard)
#     bot.send_message(message.chat.id,"FORM:", reply_markup=keyboard)
#     bot.send_message(message.chat.id,"\n".join(past_perfect_form), reply_markup=keyboard)
# def future_perfect_rules_passive(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button2 = types.KeyboardButton(text="Examples future perfect passive")
#     button3 = types.KeyboardButton(text="Exsersises future perfect passive")
#     button4 = types.KeyboardButton(text="Back to times passive")
#     keyboard.add(button2, button3, button4)
#     bot.send_message(message.chat.id,"Выберите функцию", reply_markup=keyboard)




    
@bot.message_handler(content_types=["text"])
def all_message(message):
    if message.text.lower() == 'active voice':
        active_voice(message)
    elif message.text.lower() == 'past':
        past(message)
    elif message.text.lower() == 'present':
        present(message)
    elif message.text.lower() == 'future':
        future(message)
    elif message.text.lower() == 'present simple':
        present_simple(message)
    elif message.text.lower() == 'past simple':
        past_simple(message)
    elif message.text.lower() == 'future simpe':
        future_simple(message)
    elif message.text.lower() == 'present continuous':
        present_continuous(message)
    elif message.text.lower() == 'past continuous':
        past_continuous(message)
    elif message.text.lower() == 'future continuous':
        future_continuous(message)
    elif message.text.lower() == 'present perfect':
        present_perfect(message)
    elif message.text.lower() == 'past perfect':
        past_perfect(message)
    elif message.text.lower() == 'future perfect':
        future_perfect(message)
    elif message.text.lower() == 'back':
        start_message(message)
    elif message.text.lower() == 'back to voices':
        active_voice(message)
    elif message.text.lower() == 'back to times':
        active_voice(message)
    elif message.text.lower() == 'back to voices passive':
        passive_voice(message)
    elif message.text.lower() == 'back to times passive':
        passive_voice(message)
    elif message.text.lower() == 'rules present simple':
        present_simple_rules(message)
    elif message.text.lower() == 'rules present continuous':
        present_continuous_rules(message)
    elif message.text.lower() == 'rules present perfect':
        present_continuous_rules(message)
    elif message.text.lower() == 'rules past simple':
        past_simple_rules(message)
    elif message.text.lower() == 'rules future simple':
        future_simple_rules(message)
    elif message.text.lower() == 'rules past continuous':
        past_continuous_rules(message)
    elif message.text.lower() == 'rules future continuous':
        future_continuous_rules(message)
    elif message.text.lower() == 'rules past perfect':
        past_perfect_rules(message)
    elif message.text.lower() == 'rules future perfect':
        future_perfect_rules(message)
    elif message.text.lower() == 'examples present continuous':
        examepls_of_pc(message)
    elif message.text.lower() == 'exsersises present continuous':
        exsersises_of_pc(message)
    elif message.text.lower() == 'are going':
        tr(message)
    elif message.text.lower() == 'are not walking':
        tr(message)
    elif message.text.lower() == 'are they learning':
        tr(message)
    elif message.text.lower() == 'is he starting':
        tr(message)
    elif message.text.lower() == 'am i staying':
        tr(message)
    elif message.text.lower() == 'is it getting':
        tr(message)
    elif message.text.lower() == 'are not winning':
        tr(message)
    elif message.text.lower() == 'are not bringing':
        tr(message)
    elif message.text.lower() == 'is she traveling':
        tr(message)
    else:
        fl(message)
    
if __name__ == '__main__':
    bot.infinity_polling()
