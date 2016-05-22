from django.shortcuts import render

from .forms import SignUpForm
# Create your views here.
def home(request):
	title = "Welcome"
	form = SignUpForm(request.POST or None)

	context = {
	"title": title,
	"form": form
	}

	if form.is_valid():
		instance = form.save(commit = False)


		roll_no = form.cleaned_data.get("roll_no")
		first_name = form.cleaned_data.get("first_name")
		last_name = form.cleaned_data.get("last_name")
		instance.save()


		context = {
		"title": "Success!",
		}



	return render(request,"home.html", context)