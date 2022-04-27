import my_script_1_stat as mystat
import my_script_2_ev as myev
from time import sleep
from os import system


def pokemain():  # Choice if the user want to calculate the STATS or the EV
    try:
        system('cls')
        print("1. Calculate Stat\n2. Calculate EV")
        choice = int(input("Option: "))
        if choice == 1:
            statinps()  # call function for inputing stats
        elif choice == 2:
            evinps()  # call function for inputing EV
        else:
            print("Select what only on the choices!\nRestarting in 3 seconds...")
            sleep(2)
            pokemain()
    except ValueError:
        print("Invalid Input!\nRestarting in 3 seconds...")
        sleep(2)
        pokemain()


def statinps():  # function for inputing stats
    try:  # error catching
        system('cls')
        print("Enter Base Stats: ")
        bhp = int(input("HP: "))
        batk = int(input("Attack: "))
        bdef = int(input("Defense: "))
        bspatk = int(input("Special Attack: "))
        bspdef = int(input("Special Defense: "))
        bspd = int(input("Speed: "))
        system('cls')
        iv = int(input("Individual Value (0-31): "))
        if iv > 31 or iv < 0:
            print("0 - 31 only!\nRestarting in 3 seconds...")
            sleep(2)
            statinps()
        ev = int(input("Effort Value (0-255): "))
        if ev > 255 or ev < 0:
            print("0 - 255 only!\nRestarting in 3 seconds...")
            sleep(2)
            statinps()
        lvl = int(input("Target Level: "))
        nopt = natural()
    except ValueError:
        print("Invalid Input!\nRestarting in 3 seconds...")
        sleep(2)
        statinps()

    hp = mystat.statClass.calHP(bhp, iv, ev, lvl)  # calculate stats
    oatk = mystat.statClass.calATK(batk, iv, ev, lvl, nopt)
    odef = mystat.statClass.calDEF(bdef, iv, ev, lvl, nopt)
    ospatk = mystat.statClass.calSPATK(bspatk, iv, ev, lvl, nopt)
    ospdef = mystat.statClass.calSPDEF(bspdef, iv, ev, lvl, nopt)
    ospd = mystat.statClass.calSPD(bspd, iv, ev, lvl, nopt)

    system('cls')  # print stats
    print("Calculated Stats:")
    print("HP:              ", round(hp))
    print("Attack:          ", round(oatk))
    print("Defense:         ", round(odef))
    print("Special Attack:  ", round(ospatk))
    print("Special Defense: ", round(ospdef))
    print("Speed:           ", round(ospd))

    sleep(5)
    clsornot()


def naturea():
    system('cls')
    print("""Pokemon Nature:
0 - Hardy       5 - Bold        10 - Timid      15 - Modest     20 - Calm
1 - Lonely      6 - Docile      11 - Hasty      16 - Mild       21 - Gentle
2 - Brave       7 - Relaxed     12 - Serious    17 - Quiet      22 - Sassy
3 - Adamant     8 - Impish      13 - Jolly      18 - Bashful    23 - Careful
4 - Naughty     9 - Lax         14 - Naive      19 - Rash       24 - Quirky""")
    nopt = int(input("Nature: "))
    if nopt > 24 or nopt < 0:
        print("0 - 24 only!\nRestarting in 3 seconds...")
        sleep(2)
        naturea()

    return nopt


def evCheck(ev):
    if ev > 255 or ev < 0:
        print("0 - 255 only!\nRestarting in 3 seconds...")
        sleep(2)
        evinps()
    return ev


def threeval():
    basee = int(input("Base Value: "))
    desired = int(input("Desired Stat: "))
    ev = int(input("Current EV (0-255): "))
    if ev == 255:
        print("Max EV for this stat reached!")
        sleep(3)
        clsornot()

    ev = evCheck(ev)

    return basee, desired, ev


def evinps():  # function for inputing EV
    system('cls')
    print("Calculate Needed EVs to reach desired stat")
    lvl = int(input("Target Level: "))
    iv = int(input("Individual Value (0-31): "))
    if iv > 31 or iv < 0:
        print("0 - 31 only!\nRestarting in 3 seconds...")
        sleep(2)
        evinps()

    ntr = naturea()

    print("Calculate for:\n1. Single\n2. All stats")
    sas = int(input("Option: "))
    if sas > 2 or sas < 1:
        print("1 or 2 only!\nRestarting in 3 seconds...")
        sleep(2)
        evinps()

    elif sas == 1:
        print("""Select Base Stat:
1. HP
2. Attack
3. Defense
4. Special Attack
5. Special Defense
6. Speed""")
        ses = int(input("Stat: "))
        if ses > 6 or ses < 1:
            print("1 - 6 only!\nRestarting in 3 seconds...")
            sleep(2)
            evinps()
        baseval, stat, ev = threeval()

        if ses == 1:
            HPev = myev.evClass.calHPev(stat, lvl, iv, baseval, ev)
        elif ses == 2:
            ATKev = myev.evClass.calATKev(stat, lvl, iv, baseval, ev, ntr)
        elif ses == 3:
            DEFev = myev.evClass.calDEFev(stat, lvl, iv, baseval, ev, ntr)
        elif ses == 4:
            SPATKev = myev.evClass.calSPATKev(stat, lvl, iv, baseval, ev, ntr)
        elif ses == 5:
            SPDEFev = myev.evClass.calSPDEFev(stat, lvl, iv, baseval, ev, ntr)
        elif ses == 6:
            SPDev = myev.evClass.calSPEEDev(stat, lvl, iv, baseval, ev, ntr)

    elif sas == 2:
        maxEV = 510
        print("Enter Values for HP")
        baseval, stat, ev = threeval()
        HPev = myev.evClass.calHPev(stat, lvl, iv, baseval, ev)
        print("Enter Values for Attack")
        baseval, stat, ev = threeval()
        ATKev = myev.evClass.calATKev(stat, lvl, iv, baseval, ev, ntr)
        print("Enter Values for Defense")
        baseval, stat, ev = threeval()
        DEFev = myev.evClass.calDEFev(stat, lvl, iv, baseval, ev, ntr)
        print("Enter Values for Special Attack")
        baseval, stat, ev = threeval()
        SPATKev = myev.evClass.calSPATKev(stat, lvl, iv, baseval, ev, ntr)
        print("Enter Values for Special Defense")
        baseval, stat, ev = threeval()
        SPDEFev = myev.evClass.calSPDEFev(stat, lvl, iv, baseval, ev, ntr)
        print("Enter Values for Speed")
        baseval, stat, ev = threeval()
        SPDev = myev.evClass.calSPEEDev(stat, lvl, iv, baseval, ev, ntr)

    system('cls')
    if sas == 1:
        if ses == 1:
            print("Required EV to reach desired HP stats: ", HPev)
        elif ses == 2:
            print("Required EV to reach desired Attack stats: ", ATKev)
        elif ses == 3:
            print("Required EV to reach desired Defense stats: ", DEFev)
        elif ses == 4:
            print("Required EV to reach desired Special Attack stats: ", SPATKev)
        elif ses == 5:
            print("Required EV to reach desired Special Defense stats: ", SPDEFev)
        elif ses == 6:
            print("Required EV to reach desired Speed stats: ", SPDev)

    elif sas == 2:
        print("Required EV to reach desired HP stats: ", HPev)
        print("Required EV to reach desired Attack stats: ", ATKev)
        print("Required EV to reach desired Defense stats: ", DEFev)
        print("Required EV to reach desired Special Attack stats: ", SPATKev)
        print("Required EV to reach desired Special Defense stats: ", SPDEFev)
        print("Required EV to reach desired Speed stats: ", SPDev)

    sleep(5)
    clsornot()


def clsornot():
    try:
        con = int(input("""\n\nWhat to do next?
1. Calculate Another
2. Close
Option: """))
        if con == 1:
            pokemain()
        elif con == 2:
            print("Closing...")
            sleep(2)
            exit()
        elif con == 3:
            system('cls')
            myev.evClass.trobolshut()
        else:
            print("\n\n1 or 2 only!\nRestarting in 3 seconds...")
            sleep(2)
            clsornot()
    except ValueError:
        print("\n\n1 or 2 only!\nRestarting in 3 seconds...")
        sleep(2)
        clsornot()


pokemain()
