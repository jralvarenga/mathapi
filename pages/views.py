from django.shortcuts import render

def landing_page(req):
  return render(req, 'pages/index.html')