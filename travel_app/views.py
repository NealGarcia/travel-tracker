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
# view all imgs
def img_list(request): 
    imgs = EntryDetail.objects.all()
    return render(request, 'travel_app/img.html', {'imgs': imgs})

# view img details
def img_detail(request, pk):
    imgs = EntryDetail.objects.get(id=pk)
    return render(request, 'travel_app/img_detail.html', {'imgs':imgs})

# create img
def img_create(request):
    if request.method == "POST":
        form = EntryDetailForm(request.POST)
        if form.is_valid():
            fad = form.save()
            return redirect('img_detail', pk=fad.pk)
    else:
        form = EntryDetailForm()
    return render(request, 'travel_app/img_form.html', {'form': form})

# edit img
def img_edit(request, pk):
    img = EntryDetail.objects.get(id = pk)
    if request.method == "POST":
        form = EntryDetailForm(request.POST, instance = img)
        if form.is_valid():
            FloatField = form.save()
            return redirect('img_detail', pk=img.pk)
    else:
        form = EntryDetailForm(instance = img)
    return render(request, 'travel_app/img_form.html', {'form': form})

# delete img
def img_delete(request, pk):
    EntryDetail.objects.get(id=pk).delete()
    return redirect('imgs')

