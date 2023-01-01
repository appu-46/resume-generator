

from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# from django.urls import is_valid_path
# from django.views import generic

from .forms import *
from .models import *

# Create your views here.


# class IndexView(generic.FormView):
#     template_name = 'resume_generator/index.html'

def index(request):
    # header_models = get_object_or_404(Header_models, pk=header_id)

    return render(request, 'resume_generator/index.html')


def user_creation(request):

    # header_models = get_object_or_404(Header_models, pk=header_id)

    if request.method == 'POST':
        form = Header(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            mobile = form.cleaned_data['mobile']
            email = form.cleaned_data['email']
            description = form.cleaned_data['description']
            print(name, description, mobile, email)

            form = Header_models(name=name, mobile=mobile,
                                 email=email, description=description,
                                 pub_date=timezone.now())
            form.save()

            # return HttpResponseRedirect(reverse('resume_generator:details'))
            return render(request, 'resume_generator/details.html',)
    else:
        form = Header()
    return HttpResponse("Your data didnt get save in db.")


def details(request, header_id):

    header_models = get_object_or_404(Header_models, pk=header_id)
    print(header_models)
    print("Details is running dont worry. If you didnt see this message, need to look code.")

    if request.method == 'POST':
        form = Body(request.POST)

        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            position = form.cleaned_data['position']
            time_period = form.cleaned_data['time_period']
            responsibilites = form.cleaned_data['responsibilites']

            project_title = form.cleaned_data['project_title']
            project_description = form.cleaned_data['project_description']

            achievement_title = form.cleaned_data['achievement_title']
            achievement_description = form.cleaned_data['achievement_description']

            skills = form.cleaned_data['skills']

            print(company_name, position, time_period, responsibilites,
                  project_title, project_description, achievement_title, achievement_description,
                  skills)

            form = Body_models(header_models_id=header_models.id, company_name=company_name, position=position,
                               time_period=time_period, responsibilites=responsibilites,
                               project_title=project_title, project_description=project_description,
                               achievement_title=achievement_title, achievement_description=achievement_description,
                               skills=skills,
                               pub_date=timezone.now())
            form.save()

            return HttpResponseRedirect(reverse('resume_generator:preview', args=(header_models,)))
    # return render(request, 'resume_generator/preview.html')

    else:
        form = Body()
        return HttpResponse("Your data didnt get save in db.")
    # return render(request, 'resume_generator/details.html')


def preview(request):
    return render(request, 'resume_generator/preview.html')
# --------------------------------------
# def create_user(request):
#     if request.method == 'POST':
#         form = Header(request.POST)

#         if form.is_valid():
#             form.cleaned_data['contact']

#             print form.cleaned_data['contact']

#             form.save()

#             return HttpResponseRedirect('resume_generator/thanks.html')
#     else:
#         form = Header()

#     return render(request, 'resume_generator/index.html')
