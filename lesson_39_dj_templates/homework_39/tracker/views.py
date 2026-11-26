from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

TRANSACTIONS = [
    {
        "id": 1,
        "amount": 30000,
        "type": "Income",
        "category": "Salary",
        "date": datetime(2026, 11, 15),
        "description": "Зарплата за листопад",
        "created_at": datetime(2026, 11, 15, 10, 30),
    },
    {
        "id": 2,
        "amount": 5000,
        "type": "Expense",
        "category": "Food",
        "date": datetime(2026, 11, 16),
        "description": "Продукти в супермаркеті",
        "created_at": datetime(2026, 11, 16, 18, 15),
    },
    {
        "id": 3,
        "amount": 3000,
        "type": "Expense",
        "category": "Transport",
        "date": datetime(2026, 11, 17),
        "description": "Пальне на АЗС",
        "created_at": datetime(2026, 11, 17, 9, 0),
    },
    {
        "id": 4,
        "amount": 15000,
        "type": "Income",
        "category": "Freelance",
        "date": datetime(2026, 11, 18),
        "description": "Розробка сайту",
        "created_at": datetime(2026, 11, 18, 14, 45),
    },
]

BUDGETS = [
    {"id": 1, "category": "Food", "limit": 10000, "spent": 5000, "remaining": 5000, "percentage": 50},
    {"id": 2, "category": "Transport", "limit": 5000, "spent": 3000, "remaining": 2000, "percentage": 60},
    {"id": 3, "category": "Entertainment", "limit": 3000, "spent": 0, "remaining": 3000, "percentage": 0},
]


def dashboard(request):
    total_income = sum(t["amount"] for t in TRANSACTIONS if t["type"] == "Income")
    total_expense = sum(t["amount"] for t in TRANSACTIONS if t["type"] == "Expense")
    context = {
        "user_name": "Михайло",
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": total_income - total_expense,
        "recent_transactions": TRANSACTIONS[:5],
    }
    return render(request, "dashboard.html", context)


def transactions(request):
    trans_type = request.GET.get("type")
    items = TRANSACTIONS
    if trans_type:
        items = [t for t in TRANSACTIONS if t["type"].lower() == trans_type.lower()]
    return render(request, "transactions.html", {"transactions": items, "filter": trans_type})


def transaction_detail(request, trans_id):
    trans = next((t for t in TRANSACTIONS if t["id"] == trans_id), None)
    if not trans:
        return HttpResponse("Транзакцію не знайдено", status=404)
    return render(request, "transaction_detail.html", {"trans": trans})


def budgets(request):
    return render(request, "budgets.html", {"budgets": BUDGETS})


def reports(request):
    total_income = sum(t["amount"] for t in TRANSACTIONS if t["type"] == "Income")
    total_expense = sum(t["amount"] for t in TRANSACTIONS if t["type"] == "Expense")
    expenses_by_category = {}
    for t in TRANSACTIONS:
        if t["type"] == "Expense":
            expenses_by_category[t["category"]] = expenses_by_category.get(t["category"], 0) + t["amount"]
    return render(request, "reports.html", {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": total_income - total_expense,
        "expenses_by_category": expenses_by_category,
    })


def about(request):
    return render(request, "about.html")


def placeholder(request, **kwargs):
    return HttpResponse("Ця функція (CRUD) буде реалізована на наступних заняттях! <a href='/'>На головну</a>")
