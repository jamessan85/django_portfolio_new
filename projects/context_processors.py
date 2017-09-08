from models import Project_Info

#context processor added so items can be viewed in all views
def projects(request):
    return {'projects': Project_Info.objects.all()}