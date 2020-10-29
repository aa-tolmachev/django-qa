from django.shortcuts import render
import deeppavlov

#test
path = './data/tanks/British Tanks/FV4202 105.txt'
with open(path, 'r') as file:
    context = file.read().replace('\n', '. ')

def index(request):
    question = ''
    answer = ''

    if request.method == 'POST':
        question = request.POST['question']
        answer = '374'




    context = {

        'question': question,
        'answer': answer,

    }
    return render(request, 'homepage/index.html', context)
