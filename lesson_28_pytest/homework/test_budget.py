import pytest
from datetime import datetime
from gamanec import Transaction, ExpenseTracker, TransactionNotFoundError


def test_empty_budget_initial_state(empty_budget):
    assert empty_budget.list_transactions() == []
    assert empty_budget.calculate_balance() == 0.0


def test_add_transaction_changes_state(empty_budget, sample_income):
    empty_budget.add_transaction(sample_income)
    transactions = empty_budget.list_transactions()
    assert len(transactions) == 1
    assert transactions[0] == sample_income

def test_calculate_balance_positive(populated_tracker):
    # 15000 - 500 = 14500
    assert populated_tracker.calculate_balance() == 14500.0


def test_calculate_balance_negative(empty_budget):
    empty_budget.add_transaction(Transaction(100.0, "income", "Bonus"))
    empty_budget.add_transaction(Transaction(350.0, "expense", "Bills"))
    assert empty_budget.calculate_balance() == -250.0


def test_delete_transaction_valid_index(populated_tracker, sample_income):
    deleted = populated_tracker.delete_transaction(0)
    assert deleted == sample_income
    assert len(populated_tracker.list_transactions()) == 1
    assert populated_tracker.calculate_balance() == -500.0


def test_delete_transaction_negative_index_raises_error(populated_tracker):
    with pytest.raises(TransactionNotFoundError):
        populated_tracker.delete_transaction(-1)


def test_delete_transaction_out_of_bounds_raises_error(populated_tracker):
    with pytest.raises(TransactionNotFoundError):
        populated_tracker.delete_transaction(10)


def test_delete_from_empty_budget_raises_error(empty_budget):
    with pytest.raises(TransactionNotFoundError):
        empty_budget.delete_transaction(0)


def test_monthly_report_current_month(populated_tracker):
    income, expense = populated_tracker.monthly_report()
    assert income == 15000.0
    assert expense == 500.0


def test_monthly_report_ignores_previous_months(empty_budget):
    old_t = Transaction(5000.0, "income", "Old Salary")
    old_t.date = datetime(2020, 1, 15)
    empty_budget.add_transaction(old_t)

    income, expense = empty_budget.monthly_report()
    assert income == 0.0
    assert expense == 0.0


def test_expense_tracker_cli_add_and_exit(sample_user, monkeypatch, capsys):
    tracker = ExpenseTracker(sample_user)
    # Імітуємо дії користувача: "2" (додати дохід), сума "1000", категорія "Freelance", опис "Сайт", "7" (вихід)
    inputs = iter(["2", "1000", "Freelance", "Сайт", "7"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    tracker.run()
    captured = capsys.readouterr()

    assert len(tracker.list_transactions()) == 1
    assert tracker.calculate_balance() == 1000.0
    assert "Успішно додано!" in captured.out
    assert "До побачення!" in captured.out


def test_expense_tracker_cli_invalid_choice(sample_user, monkeypatch, capsys):
    tracker = ExpenseTracker(sample_user)
    # Імітуємо невірний вибір "99", потім "7" для виходу
    inputs = iter(["99", "7"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    tracker.run()
    captured = capsys.readouterr()

    assert "Невірний вибір! Введіть число від 1 до 7." in captured.out
