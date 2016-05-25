from django.shortcuts import render, HttpResponse

from .forms import SignUpForm
from .models import SignUp
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

def list(request):
	sign_ups = SignUp.objects.all()
	context = {"users":sign_ups}
	return render(request, "list.html", context)

def search(request):
	text = request.GET['query']
	sign_ups = SignUp.objects.filter(first_name=text)
	context = {"users":sign_ups}
	if sign_ups is not None:
		return render(request, "search_results.html", context)
	else :
		return HttpResponse("No results found")
def search_view(request):
	return render(request, "search.html", {})
