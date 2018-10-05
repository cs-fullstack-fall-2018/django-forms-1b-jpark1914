from django.shortcuts import render
from basicapp import forms


# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html')


def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            # Do something
            print("VALIDATION SUCCESSFUL")
            print("Favorite Website Entered: "+form.cleaned_data['url'])

    return render(request, 'basicapp/form_page.html', {'form': form})
