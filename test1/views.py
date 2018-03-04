from django.shortcuts import render
def post_list(request):
    return render(request, 'test1/post_list.html', {})
