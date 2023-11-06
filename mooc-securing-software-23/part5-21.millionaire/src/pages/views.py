from django.shortcuts import render, redirect

from .models import questions


def find_topic(tid):
    for q in questions:
        if q['id'] == tid:
            return q
    return None


def quizView(request, tid):
    topic = find_topic(tid)

    request.session['level'] = 0
    request.session['topic'] = tid
    return render(request, 'pages/question.html', {'topic': topic, 'question': topic['questions'][0]})


def answerView(request, tid, aid):
    if request.session['topic'] != tid:
        return redirect('/cheater/')

    topic = find_topic(tid)

    level = request.session['level']

    if topic['questions'][level]['correct'] == aid:
        level += 1
        request.session['level'] = level

        if level == len(topic['questions']):
            request.session['done'] = True
            request.session['topic'] = -1
            return redirect('/finish/')

        return render(request, 'pages/question.html', {'topic': topic, 'question': topic['questions'][level]})
    else:
        request.session['topic'] = -1
        return redirect('/incorrect/')


def incorrectView(request):
    return render(request, 'pages/incorrect.html')


def finishView(request):
    if 'done' not in request.session or not request.session['done']:
        return redirect('/cheater/')
    return render(request, 'pages/finish.html')


def cheaterView(request):
    return render(request, 'pages/cheater.html')


def thanksView(request):
    request.session['done'] = False
    # Like we were going to pay anyone
    return render(request, 'pages/thanks.html')


def topicView(request, tid):
    topic = find_topic(tid)
    return render(request, 'pages/topic.html', {'topic': topic})


def topicsView(request):
    return render(request, 'pages/topics.html', {'questions': questions})
