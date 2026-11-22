from django.shortcuts import render

def home(request):
    return render(request, "home.html", {
        "title": "Головна сторінка",
        "project_name": "Мій перший Django-проєкт",
        "text": "Вітаю! Це головна сторінка мого навчального вебзастосунку.",
    })

def about(request):
    return render(request, "about.html", {
        "title": "Про мене",
        "author": "Міша",
        "text": "Я вивчаю веб-розробку на Python та фреймворк Django.",
    })
