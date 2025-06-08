from django.shortcuts import render

def some_response(request):
    """
    Generate a HTTP response
    :param obj request: The Django request object
    :return object HttpResponse: The Django HttpResponse
    """
    return render(request, 'vibe_app/some_model.html')
