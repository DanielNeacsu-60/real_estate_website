from django.shortcuts import render, get_object_or_404
from .models import Property


def home(request):
    properties = Property.objects.all().order_by('-created_at')

    location_query = request.GET.get('location')
    if location_query:
        properties = properties.filter(location__icontains=location_query)

    max_price_query = request.GET.get('max_price')
    if max_price_query:
        properties = properties.filter(price__lte=max_price_query)

    return render(request, 'real_estate/home.html', {'properties': properties})


def property_detail(request, pk):
    property_item = get_object_or_404(Property, pk=pk)

    return render(request, 'real_estate/property_detail.html', {
        'property': property_item
    })


