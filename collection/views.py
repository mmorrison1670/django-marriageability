from django.shortcuts import render
from collection.forms import ScoreForm
from collection.models import Score
from django.template.defaultfilters import slugify

# Create your views here.
def index(request):
# defining the variable
    scores = Score.objects.all()
    return render(request, 'index.html',{
        'scores':scores,
    })

def score_detail(request, slug):
    #grab the object...
    score = Score.objects.get(slug=slug)
    # and pass to the template
    return render(request, 'scores/score_detail.html', {
        'score': score,
    })

# add below your thing_detail view
def edit_score(request, slug):
    # grab the object...
    score = Score.objects.get(slug=slug)
    # set the form we're using...
    form_class = ScoreForm

def create_score(request):
    form_class = ScoreForm
    # if we're coming to this view from a submitted form,
    if request.method == 'POST':
        # grab the data from the submitted form
        form = form_class(request.POST)
        if form.is_valid():
            # create an instance but do not save yet
            score = form.save(commit=False)
            # set the additional details
            score.user = request.user
            score.slug = slugify(score.name)
            # save the object
            score.save()
            # redirect to our newly created score
            return redirect('score_detail', slug=score.slug)

    # otherwise just create the form
    else:
        form = form_class()

# and render the template
    return render(request, 'scores/create_score.html', {
        'form': form,
})
