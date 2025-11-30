from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .scoring import calculate_task_score

@csrf_exempt
def analyze_tasks(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    try:
        tasks = json.loads(request.body)
    except:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    result = []
    for t in tasks:
        t["score"] = calculate_task_score(t)
        result.append(t)

    result.sort(key=lambda x: x["score"], reverse=True)

    return JsonResponse(result, safe=False)

@csrf_exempt
def suggest_tasks(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    try:
        tasks = json.loads(request.body)
    except:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    result = []
    for t in tasks:
        t["score"] = calculate_task_score(t)
        result.append(t)

    result.sort(key=lambda x: x["score"], reverse=True)

    return JsonResponse({"suggested_tasks": result[:3]})
