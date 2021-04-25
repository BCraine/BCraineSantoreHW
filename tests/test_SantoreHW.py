# import main


def test_happy(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Massachusetts")
    state = input("Please enter a state to do business in.\n"
                  "You may pick between Massachusetts, New Hampshire, or Maine\n")

    assert state == "Massachusetts"
