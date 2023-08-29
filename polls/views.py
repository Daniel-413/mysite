from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import *

class IndexView(ListView):
    model = Question
    template_name = "index.html"
    context_object_name = 'questions'
    
class QuestionView(DetailView):
    model = Question
    template_name = "question.html"

    def post(self, request, *args, **kwargs):
        question = self.get_object()
        choice_id = request.POST.get('choice')
        selected_choice = question.choice_set.get(pk=choice_id)
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('results', question.id)


class ResultsView(DetailView):
    model = Question
    template_name = "results.html"
    


'''
def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("results", args=(question.id,)))
'''