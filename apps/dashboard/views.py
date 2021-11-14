from apps.dashboard.forms import AddEventForm
from apps.dashboard.models import Application, Event
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect


from django.contrib.auth.decorators import login_required
from .forms import AddEventForm, ApplicationForm
from django.http import HttpResponse
from apps.notification.utilities import create_notification
import csv

# Import PDF Stuff
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

#Import Calendar Stuff


from .models import *


# Generate a PDF File Venue List
@login_required
def event_pdf(request):
	# Create Bytestream buffer
	buf = io.BytesIO()
	# Create a canvas
	c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
	# Create a text object
	textob = c.beginText()
	textob.setTextOrigin(inch, inch)
	textob.setFont("Helvetica", 14)
	
	# Designate The Model
	events = Event.objects.all()

	# Create blank list
	lines = []

	for event in events:
            lines.append(event.title)
            lines.append(event.short_description)
            lines.append(event.long_description)
            #lines.append(event.start_time)
            #lines.append(event.end_time)
            lines.append(event.volunteer_area)

            lines.append("=================================================================")
    # Loop
	for line in lines:
            textob.textLine(line)

	# Finish Up
	c.drawText(textob)
	c.showPage()
	c.save()
	buf.seek(0)

	# Return something
	return FileResponse(buf, as_attachment=True, filename='event.pdf')

#Generate Csv File event list
@login_required
def event_csv(request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=event.csv'
	
        # Create a csv writer
        writer = csv.writer(response)

        # Designate The Model
        events = Event.objects.all()

        # Add column headings to the csv file
        writer.writerow(['Event Title', 'Short Description', 'Long Description','Start Time', 'End Time', 'Volunteer Area'])

        # Loop Thu and output
        for event in events:
                writer.writerow([event.title, event.short_description, event.long_description, event.start_time, event.end_time, event.volunteer_area])

        return response




@login_required
def search(request):
    return render(request, 'dashboard/search.html')



@login_required
def dashboard(request):
    events = Event.objects.filter(status=Event.ACTIVE).order_by('-created_at')[0:9]

    return render(request, 'dashboard/dashboard.html' , {'events': events})


def event_detail(request, event_id):
    event = Event.objects.get(pk=event_id)

    return render(request, 'dashboard/event_detail.html', {'event': event})

@login_required
def apply_for_event(request, event_id):
    event = Event.objects.get(pk=event_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.event = event
            application.created_by = request.user
            application.save()

            create_notification(request, event.created_by, 'application', extra_id=application.id)

            

            return redirect('admindashboard')
    else:
        form = ApplicationForm()

    return render(request, 'dashboard/apply_for_event.html',{'form': form, 'event': event})

@login_required
def add_event(request):
    if request.method == 'POST':
        form = AddEventForm(request.POST)

        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()

            return redirect('admindashboard')
    else:
        form = AddEventForm()

    return render(request, 'dashboard/add_event.html',{'form': form})


@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id, created_by=request.user)

    if request.method == 'POST':
        form = AddEventForm(request.POST, instance=event)

        if form.is_valid():
            event = form.save(commit=False)
            event.status = request.POST.get('status')
            event.save()

            return redirect('admindashboard')
    else:
        form = AddEventForm(instance=event)

    return render(request, 'dashboard/edit_event.html', {'form': form, 'event': event})

