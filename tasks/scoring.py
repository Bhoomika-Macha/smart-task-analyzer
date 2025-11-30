from datetime import date, datetime

def calculate_task_score(task):
    score = 0
    today = date.today()

    due = task.get("due_date")
    if isinstance(due, str):
        try:
            due = datetime.strptime(due, "%Y-%m-%d").date()
        except:
            return -999

    if not due:
        return -500

    days_left = (due - today).days

    if days_left < 0:
        score += 100
    elif days_left <= 3:
        score += 50
    elif days_left <= 7:
        score += 20

    score += task.get("importance", 5) * 5

    hours = task.get("estimated_hours", 1)
    if hours < 2:
        score += 10
    elif hours > 8:
        score -= 5

    deps = task.get("dependencies", [])
    score -= len(deps) * 2

    return score
