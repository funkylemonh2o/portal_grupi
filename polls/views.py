from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Poll, Question, Vote, Choice
from .forms import VoteForm

def poll_list(request):
    polls = Poll.objects.all()
    return render(request, 'polls/poll_list.html', {'polls': polls})

@login_required
def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    questions = poll.questions.all()
    return render(request, 'polls/poll_details.html', {'poll': poll, 'questions': questions})

@login_required
def poll_vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    questions = poll.questions.all()

    if request.method == 'POST':
        for question in questions:
            choice_id = request.POST.get(f'question_{question.id}')
            if choice_id:
                Vote.objects.update_or_create(
                    user=request.user,
                    choice_id=choice_id,
                    defaults={'choice_id': choice_id}
                )
        return redirect('poll_results', poll_id=poll.id)

    return render(request, 'polls/poll_detail.html', {'poll': poll, 'questions': questions})

def poll_results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/poll_results.html', {'poll': poll})