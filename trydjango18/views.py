from django.shortcuts import render
from newsletter.models import SignUp
from newsletter.forms import SignUpForm


def list(request):
	context = {}
	form = SignUpForm(request.GET or None)
	query_results = SignUp.objects.all()
	roll_no = form.cleaned_data.get("roll_no")
	first_name = form.cleaned_data.get("first_name")
	last_name = form.cleaned_data.get("last_name")

	

	

	context = {
	"roll_no":roll_no,
	"first_name":first_name,
	"last_name":last_name
	}
	return render(request, "list.html", context)