from django.shortcuts import render, redirect
from .models import TripEntry, EntryDetail
from .forms import TripForm, EntryDetailForm

#---- Trip Views ----
# view all trips
def trip_list(request): 
    trips = TripEntry.objects.all()
    return render(request, 'travel-app/trip_list.html', {'trips': trips})

# view trip details
def trip_detail(request, pk):
    trip = TripEntry.objects.get(id = pk)
    return render(request, 'travel-app/trip_detail.html', {'trip': trip})

# create a new trip
def trip_create(request):
  if request.method == "POST":
    form = TripForm(request.POST)
    if form.is_valid():
      trip = form.save()
      return redirect('trip_detail', pk=trip.pk)
  else:
    form = TripForm()
  return render(request, 'travel-app/trip_form.html', {'form': form}) 

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
  return render(request, 'travel-app/trip_form.html', {'form': form}) 
