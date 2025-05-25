from django.shortcuts import HttpResponse

def task_create(request):
    html = """
    <style>
    h1{
         colour: red
         background-color:green:
         }
         </style>
    <h1>Blog site</h1>
    
    """
    return HttpResponse(html)