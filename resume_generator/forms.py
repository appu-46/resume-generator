

from django import forms


class Header(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    mobile = forms.IntegerField()
    email = forms.EmailField(label='Email ID', max_length=20)
    description = forms.CharField(label='Description', max_length=100)
    # pub_date = forms.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name, self.mobile, self.email, self.description


class Body(forms.Form):

    # class work_experience(forms.Form):
    # no_of_companies_worked_in = forms.IntegerField()
    company_name = forms.CharField(label='Company Name', max_length=20)
    position = forms.CharField(label='Position', max_length=15)
    time_period = forms.CharField(
        label=' Time Period you worked in this company', max_length=15)
    responsibilites = forms.CharField(
        label='Responsibilites in that', max_length=200)

    # class projects(forms.Form):
    project_title = forms.CharField(label='Project name', max_length=20)
    project_description = forms.CharField(
        label="Project Description", max_length=50)

    # class achivements (forms.Form):
    achievement_title = forms.CharField(
        label='Achievement title', max_length=15)
    achievement_description = forms.CharField(
        label='Achievement description', max_length=50)

    # work_experience = forms.CharField(max_length=500)
    # projects = forms.CharField(max_length=500)
    # achievements = forms.CharField(max_length=500)

    # class skills(forms.Form):
    skills = forms.CharField(max_length=15)
    # pub_date = forms.DateTimeField('date published')

    def __str__(self):
        return self.work_experience, self.projects, self.achievements, self.skills
