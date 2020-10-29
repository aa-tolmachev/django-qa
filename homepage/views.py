from django.shortcuts import render
import os

#import deeppavlov
print(os.listdir())


def index(request):
    question = ''
    answer = ''

    if request.method == 'POST':
        #test
        path = 'homepage/data/tanks/British Tanks/FV4202 105.txt'

        with open(path, 'r') as file:
            context = file.read().replace('\n', '. ')

        
        question = request.POST['question']
        answer = context




    context = {

        'question': question,
        'answer': answer,

    }
    return render(request, 'homepage/index.html', context)
