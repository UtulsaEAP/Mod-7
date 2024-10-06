'''exceptionHandling
Test cases for the seasons module.
'''
import courseGrade as courseGrade

ERROR_MSG = "Verify that the program is correctly incrementing the age of each person."

def test_one(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["./Problem 3/StudentInfo.tsv"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    courseGrade.courseGrade()
    captured = capsys.readouterr()
    all_outputs = captured.out
    with open("./Problem 3/report.txt") as f:
        lines = f.read()
        assert all(x in lines for x in ["Barrett	Edan	70	45	59	F",
            "Bradshaw	Reagan	96	97	88	A",
            "Charlton	Caius	73	94	80	B",
            "Mayo	Tyrese	88	61	36	D",
            "Stern	Brenda	90	86	45	C",

            "Averages: midterm1 83.40, midterm2 76.60, final 61.60"]), ERROR_MSG
        
def test_two(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["./Problem 3/StudentInfo1.tsv"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    courseGrade.courseGrade()
    captured = capsys.readouterr()
    all_outputs = captured.out
    with open("./Problem 3/report1.txt") as f:
        lines = f.read()
        assert all(x in lines for x in ["Barber	Ryley	97	65	55	C",
        "Barrett	Edan	98	63	53	C",
        "Bradshaw	Reagan	89	55	38	D",
        "Cabot	Henry	94	97	85	A",
        "Charlton	Caius	41	73	75	D",
        "Flynn	Jane	99	95	70	B",
        "Holder	Guto	59	71	61	D",
        "King	Sonya	85	43	56	D",
        "Mayo	Tyrese	76	57	96	C",
        "Min	Johnny	46	43	67	F",
        "Preston	Mcauley	89	98	94	A",
        "Robison	Lynda	96	90	55	B",
        "Stern	Brenda	68	84	52	D",
        "Stott	Peyton	80	57	59	D",
        "Warner	Gwion	65	36	47	F",
        "Averages: midterm1 78.80, midterm2 68.47, final 64.20"]), ERROR_MSG

def test_three(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["./Problem 3/StudentInfo2.tsv"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    courseGrade.courseGrade()
    captured = capsys.readouterr()
    all_outputs = captured.out
    with open("./Problem 3/report2.txt") as f:
        lines = f.read()
        assert all(x in lines for x in ["Stott	Peyton	80	57	75	C",
        "Averages: midterm1 80.00, midterm2 57.00, final 75.00"]), ERROR_MSG
    