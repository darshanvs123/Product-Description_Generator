# description_generator/views.py

from django.shortcuts import render
from django.http import HttpResponse
from .models import GeneratedDescription

# Import the product_desc_generator function from product_description_generator.py
from .product_description_generator import product_desc_generator

def index(request):
    return render(request, 'index.html')

from django.http import JsonResponse

def generate_description(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        keywords = request.POST['keywords']
        
        # Generate product description using the OpenAI function
        description = product_desc_generator(product_name, keywords)
        
        # Save the generated description (optional)
        GeneratedDescription.objects.create(
            product_name=product_name,
            keywords=keywords,
            description=description
        )
        
        # Return the generated description as JSON response
        response_data = {
            'description': description
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid request method'})

