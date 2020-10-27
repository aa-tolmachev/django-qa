from django.shortcuts import render
import deeppavlov


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
