from django.shortcuts import render, redirect
from .models import Reviews_post
from .forms import Reviews_postForm
# Create your views here.
def films(request):
    reviews = Reviews_post.objects.all()
    return render(request, 'movie_project/reviews.html', {'reviews': reviews})
   
def create_reviews(request):
    error = ""
    if request.method == 'POST':
        form = Reviews_postForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('movie_project_films')
        else:
            error = "Данные были заполнены не корректно"      
    form = Reviews_postForm()
    return render(request, 'movie_project/add_reviews_post.html', {'form': form, 'errors': error})
    