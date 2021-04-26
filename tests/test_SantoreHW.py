
def test_happy_simple(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Massachusetts")
    state = input("Please enter a state to do business in.\n"
                  "You may pick between Massachusetts, New Hampshire, or Maine\n")

    assert state == "Massachusetts"


def test_happy_extended(monkeypatch):
    state_tax_maine = .0550
    price = 0
    total = 0
    wic_prices = [2.99, 1.49, 3.29, 4.05, 0.89, 8.69, 0.49, 2.00, 1.99, 3.50]
    monkeypatch.setattr('builtins.input', lambda _: "Juice")
    items = input("Please enter items you would like to buy from above\n"
                  "Enter item twice if you have two of same thing and so forth\n"
                  "Enter 'done' when finished ")
    if items.lower() == "juice":
        price += wic_prices[2]
    monkeypatch.setattr('builtins.input', lambda _: "Maine")
    state = input("Please enter a state to do business in.\n"
                  "You may pick between Massachusetts, New Hampshire, or Maine\n")
    if state.lower() == "maine":
        total = price + (price * state_tax_maine)
    assert total == 3.47095


def test_bad_data_cases(monkeypatch):
    state_tax_new_hampshire = 0
    price = 0
    total = 0
    wic_prices = [2.99, 1.49, 3.29, 4.05, 0.89, 8.69, 0.49, 2.00, 1.99, 3.50]
    monkeypatch.setattr('builtins.input', lambda _: "bREad")
    items = input("Please enter items you would like to buy from above\n"
                  "Enter item twice if you have two of same thing and so forth\n"
                  "Enter 'done' when finished ")
    if items.lower() == "bread":
        price += wic_prices[2]
    monkeypatch.setattr('builtins.input', lambda _: "NEw haMPSHirE")
    state = input("Please enter a state to do business in.\n"
                  "You may pick between Massachusetts, New Hampshire, or Maine\n")
    if state.lower() == "new hampshire":
        total = price + (price * state_tax_new_hampshire)
    assert total == 3.29
