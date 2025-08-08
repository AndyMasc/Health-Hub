from django.http import HttpResponse
from django.shortcuts import render
from google import genai
from django.conf import settings

# Create your views here.
def symptom_diagnoser(request):
    if request.method == 'POST':
        symptoms = request.POST.get('symptoms')
        prompt = f"Diagnose the following symptoms: {symptoms}. Provide a explanation of the possible conditions and any recommended actions or treatments. Only show the most likely conditions and do not list all possible conditions. If the symptoms are too broad or silly, respond sensibly and shortly and/or not applicable. Make it concise, clear, informative and readable. If the symptoms are serious, recommend seeing a doctor immediately, however still give advice. Do not refer to yourself as as a person but rather as a Health Hub medical assistant."
        response = load_gemini_response(prompt)
        return render(request, 'symptom_diagnoser/symptom_diagnoser.html', {'response': response})
    return render(request, 'symptom_diagnoser/symptom_diagnoser.html')

def load_gemini_response(prompt):
    client = genai.Client(api_key=settings.GEMINI_API_KEY)
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = f"{prompt}. Do not use code blocks or markdown formatting. Use linebreaks where and if appropriate. If the idea is too broad or silly, respond sensibly and shortly and/or not applicable. Make it concise, clear, informative and readable.",
    )
    return response.text