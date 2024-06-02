
from django.shortcuts import render
from django.http import HttpResponse


def load_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        # обработка загрузки файла
        return HttpResponse('File loaded successfully!')
    # в случае GET запроса или отсутствия файла
    return render(request, 'wordcount/index.html')


def word_count(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        # подсчет количества слов
        return HttpResponse(f'Word count for "{word}": 10')
    # в случае GET запроса
    return render(request, 'wordcount/index.html')

def clear_memory(request):
    if request.method == 'POST':
        # очистка данных
        return HttpResponse('Memory cleared!')
    return render(request, 'wordcount/index.html')



