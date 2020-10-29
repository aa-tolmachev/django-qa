from django.shortcuts import render
import os
import pickle

import deeppavlov
from deeppavlov import build_model, configs

model_qa = build_model(configs.squad.squad, download=True)
x = model_qa(["In meteorology, precipitation is any product of the condensation of atmospheric water vapor \
         that falls under gravity. The main forms of precipitation include drizzle, rain, sleet, snow, \
         graupel and hail. Precipitation forms as smaller droplets coalesce via collision with other rain drops \
         or ice crystals within a cloud. Short, intense periods of rain in scattered locations are called showers. \
         Tank have 20 damage."],
         ["What damage have tank?"])

print(x)

#test
path = 'homepage/data/all tanks/FV4202 105.txt'

global context
with open(path, 'r') as file:
    context = file.read().replace('\n', '. ')



def index(request):
    question = ''
    answer = ''
    global context

    if request.method == 'POST':
        question = request.POST['question']
        answer = context




    context = {

        'question': question,
        'answer': answer,

    }
    return render(request, 'homepage/index.html', context)
