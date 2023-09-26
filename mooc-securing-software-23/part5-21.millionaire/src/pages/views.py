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
	return render(request, 'pages/question.html', {'topic' : topic, 'question' : topic['questions'][0]})



def answerView(request, tid, aid):
		
	topic = find_topic(tid)

	level = request.session['level']

	if topic['questions'][level]['correct'] == aid:
		level += 1
		request.session['level'] = level

		if level == len(topic['questions']):
			return redirect('/finish/')

		return render(request, 'pages/question.html', {'topic' : topic, 'question' : topic['questions'][level]})
	else:
		return redirect('/incorrect/')


def incorrectView(request):
	return render(request, 'pages/incorrect.html')


def finishView(request):
	return render(request, 'pages/finish.html')


def cheaterView(request):
	return render(request, 'pages/cheater.html')


def thanksView(request):
	# Like we were going to pay anyone
	return render(request, 'pages/thanks.html')



def topicView(request, tid):
	topic = find_topic(tid)
	return render(request, 'pages/topic.html', {'topic' : topic})


def topicsView(request):
	return render(request, 'pages/topics.html', {'questions' : questions})
