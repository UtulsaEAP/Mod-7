'''exceptionHandling
Test cases for the seasons module.
'''
import fileNameChange as fileNameChange

ERROR_MSG = "Verify that the program is correctly incrementing the age of each person."

def test_one(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["./Problem 4/ParkPhotos.txt"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    fileNameChange.fileNameChange()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert all(x in all_outputs for x in ["Acadia2003_info.txt",
        "AmericanSamoa1989_info.txt",
        "BlackCanyonoftheGunnison1983_info.txt",
        "CarlsbadCaverns2010_info.txt",
        "CraterLake1996_info.txt",
        "GrandCanyon1996_info.txt",
        "IndianaDunes1987_info.txt",
        "LakeClark2009_info.txt",
        "Redwood1980_info.txt",
        "VirginIslands2007_info.txt",
        "Voyageurs2006_info.txt",
        "WrangellStElias1987_info.txt"]), ERROR_MSG

def test_two(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["./Problem 4/ParkPhotos1.txt"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    fileNameChange.fileNameChange()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert all(x in all_outputs for x in ["Acadia2003_info.txt",
        "AmericanSamoa1989_info.txt",
        "Arches1997_info.txt",
        "Badlands2000_info.txt",
        "BigBend2008_info.txt",
        "Biscayne2019_info.txt",
        "BlackCanyonoftheGunnison1983_info.txt",
        "BryceCanyon1985_info.txt",
        "Canyonlands1996_info.txt",
        "CapitolReef1991_info.txt",
        "CarlsbadCaverns2010_info.txt",
        "ChannelIslands1999_info.txt",
        "Congaree2006_info.txt",
        "CraterLake1996_info.txt",
        "CuyahogaValley1995_info.txt",
        "DeathValley1996_info.txt",
        "Denali2001_info.txt",
        "DryTortugas1982_info.txt",
        "Everglades1984_info.txt",
        "GatesoftheArctic1989_info.txt",
        "GatewayArch1986_info.txt",
        "GlacierBay1982_info.txt",
        "Glacier1980_info.txt",
        "GrandCanyon1996_info.txt",
        "GrandTeton1997_info.txt",
        "GreatBasin2018_info.txt",
        "GreatSandDunes2006_info.txt",
        "GreatSmokyMountains1992_info.txt",
        "GuadalupeMountains2020_info.txt",
        "Haleakala2010_info.txt",
        "HawaiiVolcanoes1981_info.txt",
        "HotSprings1984_info.txt",
        "IndianaDunes1987_info.txt",
        "IsleRoyale1987_info.txt",
        "JoshuaTree1984_info.txt",
        "Katmai1997_info.txt",
        "KenaiFjords2020_info.txt",
        "KingsCanyon2002_info.txt",
        "KobukValley2014_info.txt",
        "LakeClark2009_info.txt",
        "LassenVolcanic1991_info.txt",
        "MammothCave1983_info.txt",
        "MesaVerde2012_info.txt",
        "MountRainier1999_info.txt",
        "NorthCascades1993_info.txt",
        "Olympic1986_info.txt",
        "PetrifiedForest1994_info.txt",
        "Pinnacles1998_info.txt",
        "Redwood1980_info.txt",
        "RockyMountain1986_info.txt",
        "Saguaro1980_info.txt",
        "Sequoia2009_info.txt",
        "Shenandoah1983_info.txt",
        "TheodoreRoosevelt2006_info.txt",
        "VirginIslands2007_info.txt",
        "Voyageurs2006_info.txt",
        "WhiteSands2002_info.txt",
        "WindCave1986_info.txt",
        "WrangellStElias1987_info.txt",
        "Yellowstone2017_info.txt",
        "Yosemite1992_info.txt",
        "Zion2009_info.txt"]), ERROR_MSG

def test_three(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["./Problem 4/ParkPhotos2.txt"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    fileNameChange.fileNameChange()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert all(x in all_outputs for x in ["GreatSmokyMountains1992_info.txt"]), ERROR_MSG
