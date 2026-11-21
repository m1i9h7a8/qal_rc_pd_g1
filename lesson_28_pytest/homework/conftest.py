import pytest
from gamanec import User, Transaction, Budget, ExpenseTracker


@pytest.fixture
def sample_user():
    return User("Олександр")


@pytest.fixture
def sample_income():
    return Transaction(15000.0, "income", "Salary", "Зарплата")


@pytest.fixture
def sample_expense():
    return Transaction(500.0, "expense", "Food", "Продукти")


@pytest.fixture
def empty_budget():
    return Budget()


@pytest.fixture
def populated_tracker(sample_user, sample_income, sample_expense):
    tracker = ExpenseTracker(sample_user)
    tracker.add_transaction(sample_income)
    tracker.add_transaction(sample_expense)
    return tracker
