import pytest
from datetime import datetime
from gamanec import User, Transaction, InvalidAmountError


def test_user_creation(sample_user):
    assert sample_user.username == "Олександр"


def test_transaction_creation_valid():
    t = Transaction(250.5, "expense", "Transport", "Таксі")
    assert t.amount == 250.5
    assert t.transaction_type == "expense"
    assert t.category == "Transport"
    assert t.description == "Таксі"
    assert isinstance(t.date, datetime)


def test_transaction_empty_description():
    t = Transaction(100, "income", "Gift")
    assert t.description == ""


def test_transaction_zero_amount_raises_error():
    with pytest.raises(InvalidAmountError):
        Transaction(0, "income", "Salary")


def test_transaction_negative_amount_raises_error():
    with pytest.raises(InvalidAmountError):
        Transaction(-50.0, "expense", "Food")
