from time import time
from telepot.namedtuple import KeyboardButton,ReplyKeyboardMarkup
import telepot as t
from csv import reader
import random

k=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Begin test')]])
k1=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Try again')]])
start=0
l=0
no=0
co=0
i = random.randint(1,6)
question=[]
choise1=[]
choise2=[]
choise3=[]
choise4=[]
answer=[]
r = random.randint(1,5)
with open(f'{r}.csv', 'r',encoding='utf8',newline='') as df:
    data_frame = reader(df)
    for i in data_frame:
        question.append(i[1])
        choise1.append(i[2])
        choise2.append(i[3])
        choise3.append(i[4])
        choise4.append(i[5])
        answer.append(i[6])
    print(str(question))
    print(str(choise1))
    print(str(choise2))
    print(str(choise3))
    print(str(choise4))
    print(str(answer))
    
# about choises : strings are choices(to answer)
start_time=None

def main(ms):
    global no
    global co
    global start
    global start_time
    global l
    i=ms['chat']['id']
    c=ms['text']
    print(ms['from']['username'],' : ')
    print(c)
    if c=='/start':
        bot.sendMessage(i,'Welcome',reply_markup=k)#name of test
    if c=='Begim test' or c=='Try again':
        start=1
        start_time=time()
    if l != len(answer):
        cquestion=question[l]
        choises=['',ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=f'{choise1[l]}'),
                                            KeyboardButton(text=f'{choise2[l]}')],
                                            [KeyboardButton(text=f'{choise3[l]}'),
                                            KeyboardButton(text=f'{choise4[l]}')]]),
        ]
        canswer=answer[l]
    if l == len(answer):
        end_time=time()
        final_score=0
        timer=int(end_time-start_time)
        start=0
        bot.sendMessage(ms['chat']['id'],'Time : '+str(int(timer))+
                        ' seconds \n Number of write answers : '+str(no)+f'/{l} \n Final score : '
                        +str(int(final_score))+f'/100',reply_markup=k1)
        co=0
        no=0
        l=0
    if c==canswer:
        no=no+1
        co=co+1
    else:
        pass
    if start and start<len(question)+1:#number of questions+1
        if start<len(question)+1:
            bot.sendMessage(i,cquestion,reply_markup=choises[1])
            c=ms['text']
        if start!=0:
            start=start+1
            l+=1
bot=t.Bot()
bot.message_loop(main)

while True:
    s=1
