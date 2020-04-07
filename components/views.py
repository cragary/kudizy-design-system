from django.shortcuts import render,redirect

# Create your views here.
def testingthisshit(request):
    return render(request, "components/testingthisshit.html", locals())