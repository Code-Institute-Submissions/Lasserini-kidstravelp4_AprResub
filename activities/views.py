from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Experience, Review
from .filters import ExperienceFilter


# The Index page view
class HomeView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


# The Experience Filter View
def search(request):
    experience_list = Experience().objects.all()
    experience_filter = ExperienceFilter(request.GET, queryset=experience_list)
    return render(request, 'search/index.html', {'filter': experience_filter})


# class ExperienceView(generic.ListView):
#	model = Experience
#	queryset = Experience.objects.all().order_by('category')
#	template_name = 'results.html'
