from django.shortcuts import redirect, render
from django.views.generic import TemplateView


from .models import Meeting
from .forms import MeetingModelForm


class HomePageView(TemplateView):
    template_name = 'meetings/home.html'

def meeting_list(request):
    meetings = Meeting.objects.all()
    context = {
        "meetings":meetings
    }
    return render(request, 'meetings/meeting_list.html', context)



def upload_document(request):
    if request.method == "POST":
        form = MeetingModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('academic_meetings:meeting-list')
    else:
        form = MeetingModelForm()
    context = {
        'form':form
    }
    return render(request, 'meetings/upload_document.html',context)