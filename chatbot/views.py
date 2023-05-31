from django.shortcuts import render
import openai
from .models import PastQ

def chat(question):
    GPT_Response = openai.Completion.create(
            model="text-davinci-003",
            prompt=question,
            temperature=0.1,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
    return GPT_Response["choices"][0]["text"].strip()

def draw(question, imageSize):
    GPT_Response = openai.Image.create(prompt=question, n=1, size=imageSize+"x"+imageSize)
    return GPT_Response["data"][0]["url"].strip()
# Create your views here.
def home(request):
    if request.method == "POST":
        userQuestion = request.POST['question']
        model = request.POST['model']
        size = request.POST['size']

        openai.api_key="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"
        openai.Model.list()

        if model == "draw":
            GPT_Response = draw(userQuestion, size)
        else:
            GPT_Response = chat(userQuestion)
        GPT_Response = "hi"

        saveQ = PastQ(question=userQuestion, answer=GPT_Response)
        saveQ.save()

        return render(request, "chatbot/home.html", {"userQuestion":userQuestion, "GPT_Response":GPT_Response})
    
    return render(request, "chatbot/home.html", {
    })