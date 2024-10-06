'''exceptionHandling
Test cases for the seasons module.
'''
import exceptionHandling as exceptionHandling

ERROR_MSG = "Verify that the program is correctly incrementing the age of each person."

def test_one(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["Lee 18","Lua 21","Mary Beth 19","Stu 33","-1"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    exceptionHandling.exceptionHandling()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert all(x in all_outputs for x in ["Lee 19","Lua 22","Mary 0","Stu 34"]), ERROR_MSG

def test_two(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["Laura 63","Vaishnavi 24", "Sarah Sims 33", "-1"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    exceptionHandling.exceptionHandling()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert all(x in all_outputs for x in ["Laura 64","Vaishnavi 25", "Sarah 0"]), ERROR_MSG

def test_three(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["Huw 29","Jaspar 49","Melina Lynn 32","Quinta 13","Mina Ny 38","Hanna 28","-1"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    exceptionHandling.exceptionHandling()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert all(x in all_outputs for x in ["Huw 30","Jaspar 50","Melina 0","Quinta 14","Mina 0","Hanna 29"]), ERROR_MSG

def test_four(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["Laura Jean 17","Christine 55","Felicia 31","Kofi Drew 39","Margaux 98","-1"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    exceptionHandling.exceptionHandling()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert all(x in all_outputs for x in ["Laura 0","Christine 56","Felicia 32","Kofi 0","Margaux 99"]), ERROR_MSG

    