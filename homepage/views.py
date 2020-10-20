from django.shortcuts import render



def index(request):
    question = ''

    if request.method == 'POST':
        question = request.POST['question']
        




    context = {

        'question': question,

    }
    return render(request, 'homepage/index.html', context)
