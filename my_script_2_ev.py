from traceback import print_list


class evClass():

    def calHPev(dstat, lvl, iv, bstat, ev):

        modif = 1.0

        d = (2 * bstat + iv + (ev / 4)) * (lvl / 100)

        evs = (((((dstat / modif) - d) * 400) / lvl) / 4) * 4

        return evs

    def calATKev(dstat, lvl, iv, bstat, ev, ntr):
        if ntr == 1 or ntr == 2 or ntr == 3 or ntr == 4:
            modif = 1.1
        elif ntr == 5 or ntr == 10 or ntr == 15 or ntr == 20:
            modif = 0.9
        else:
            modif = 1.0

        d = (2 * bstat + iv + (ev / 4)) * (lvl / 100)

        evs = (((((dstat / modif) - d) * 400) / lvl) / 4) * 4

        return evs

    def calDEFev(dstat, lvl, iv, bstat, ev, ntr):
        if ntr == 5 or ntr == 7 or ntr == 8 or ntr == 9:
            modif = 1.1
        elif ntr == 1 or ntr == 11 or ntr == 16 or ntr == 21:
            modif = 0.9
        else:
            modif = 1.0

        d = (2 * bstat + iv + (ev / 4)) * (lvl / 100)

        evs = (((((dstat / modif) - d) * 400) / lvl) / 4) * 4

        return evs

    def calSPATKev(dstat, lvl, iv, bstat, ev, ntr):
        if ntr == 15 or ntr == 16 or ntr == 17 or ntr == 19:
            modif = 1.1
        elif ntr == 3 or ntr == 8 or ntr == 13 or ntr == 23:
            modif = 0.9
        else:
            modif = 1.0

        d = (2 * bstat + iv + (ev / 4)) * (lvl / 100)

        evs = (((((dstat / modif) - d) * 400) / lvl) / 4) * 4

        return evs

    def calSPDEFev(dstat, lvl, iv, bstat, ev, ntr):
        if ntr == 20 or ntr == 21 or ntr == 22 or ntr == 23:
            modif = 1.1
        elif ntr == 4 or ntr == 9 or ntr == 14 or ntr == 19:
            modif = 0.9
        else:
            modif = 1.0

        d = (2 * bstat + iv + (ev / 4)) * (lvl / 100)

        evs = (((((dstat / modif) - d) * 400) / lvl) / 4) * 4

        return evs

    def calSPEEDev(dstat, lvl, iv, bstat, ev, ntr):
        if ntr == 10 or ntr == 11 or ntr == 13 or ntr == 14:
            modif = 1.1
        elif ntr == 2 or ntr == 7 or ntr == 17 or ntr == 22:
            modif = 0.9
        else:
            modif = 1.0

        d = (2 * bstat + iv + (ev / 4)) * (lvl / 100)

        evs = (((((dstat / modif) - d) * 400) / lvl) / 4) * 4

        return evs

    def trobolshut(dstat, lvl, iv, bstat, ev, ntr):
        modif = 1.0

        d = (2 * bstat + iv + (ev / 4)) * (lvl / 100)

        evs = (((((dstat / modif) - d) * 400) / lvl) / 4) * 4

        print("Desired Stat: " + str(dstat))
        print("Modifiers: " + str(modif))
        print("D: " + str(d))
        print("Base: " + str(bstat))
        print("IV: " + str(iv))
        print("EV: " + str(ev))
        print("Level: " + str(lvl))