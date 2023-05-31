from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect

monthlyGoals = {
    "january": "Hello January!",
    "february": "Hello February!",
    "march": "Hello March!",
    "april": "Hello April!",
    "may": "Hello May!",
    "june": "Hello June!",
    "july": "Hello July!",
    "august": "Hello August!"
}

def index(request):
    # dataToReturn = "<ul style='padding: 0;'>"

    months = list(monthlyGoals.keys())
    # for month in months:
    #    monthPath = f"/challenges/{month}"
    #    dataToReturn += f"<li style='font-size: 30px; list-style-type: none; display: inline; padding-right: 20px;'><a style='color: orchid;' href='{monthPath}'>{month.upper()}</a></li>"
    # dataToReturn += "</ul>"
    # return HttpResponse(dataToReturn)
    return render(request, 'challenges/index.html', {
        "months_key": months
    })



def monthly_goal_by_num(request, month):
    # return HttpResponse(f"<h1>numeric month entered: {month}</h1>")
    # use dictionary to help with our redirect
    months = list(monthlyGoals.keys())
    if month > len(months) or month < 1:
        return HttpResponseNotFound("You entered an invalid numeric month")
    forward_month = months[month-1]
    return HttpResponseRedirect(f"/challenges/{forward_month}")

def monthly_goal(request, month):
    strToReturn = ""

    try:
        strToReturn = monthlyGoals[month]
        # return HttpResponse(strToReturn)
        return render(request, "challenges/challenge.html", {
            "text": strToReturn,
            "month_name": month.capitalize()
        })
    except:
        return HttpResponseNotFound("<strong>ERROR:</strong> month not found")