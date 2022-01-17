from django.shortcuts import render, redirect
from .models import TripEntry, EntryDetail
from .forms import TripForm, EntryDetailForm

#---- Trip Views ----#
# view all trips
def trip_list(request): 
    trips = TripEntry.objects.all()
    return render(request, 'travel_app/trip_list.html', {'trips': trips})

# view trip details
def trip_detail(request, pk):
    trip = TripEntry.objects.get(id = pk)
    return render(request, 'travel_app/trip_detail.html', {'trip': trip})

# create a new trip
def trip_create(request):
  if request.method == "POST":
    form = TripForm(request.POST)
    if form.is_valid():
      trip = form.save()
      return redirect('trip_detail', pk=trip.pk)
  else:
    form = TripForm()
  return render(request, 'travel_app/trip_form.html', {'form': form}) 

# edit a trip
def trip_edit(request, pk):
  post = TripEntry.objects.get(id=pk)
  if request.method == "POST":
    form = TripForm(request.POST, instance=post)
    if form.is_valid():
      post = form.save()
      return redirect('trip_detail',pk=post.pk)
  else:
    form = TripForm(instance=post)
  return render(request, 'travel_app/trip_form.html', {'form': form}) 



  #---- Detail Views ----#
# view all entries
def entry_list(request): 
    entries = EntryDetail.objects.all()
    return render(request, 'travel_app/entry.html', {'entries': entries})

# view entry details
def entry_detail(request, pk):
    entries = EntryDetail.objects.get(id=pk)
    return render(request, 'travel_app/entry_detail.html', {'entries':entries})

# create entry
def entry_create(request):
    if request.method == "POST":
        form = EntryDetailForm(request.POST)
        if form.is_valid():
            entry = form.save()
            return redirect('entry_detail', pk=entry.pk)
    else:
        form = EntryDetailForm()
    return render(request, 'travel_app/entry_form.html', {'form': form})

# edit entry
def entry_edit(request, pk):
    entry = EntryDetail.objects.get(id = pk)
    if request.method == "POST":
        form = EntryDetailForm(request.POST, instance = entry)
        if form.is_valid():
            FloatField = form.save()
            return redirect('img_detail', pk=entry.pk)
    else:
        form = EntryDetailForm(instance = entry)
    return render(request, 'travel_app/entry_form.html', {'form': form})

# delete entry
def entry_delete(request, pk):
    EntryDetail.objects.get(id=pk).delete()
    return redirect('entries')

