class statClass():

    def calHP(mbhp, miv, mev, mlvl):
        hp = (((2 * mbhp + miv + (mev / 4)) * mlvl) / 100) + mlvl + 10
        return hp

    def calATK(matk, miv, mev, mlvl, mopt):
        if mopt == 1 or mopt == 2 or mopt == 3 or mopt == 4:
            ntr = 1.1
        elif mopt == 5 or mopt == 10 or mopt == 15 or mopt == 20:
            ntr = 0.9
        else:
            ntr = 1.0

        ostat = (((2 * matk + miv + (mev / 4) * mlvl) / 10) + 5) * ntr

        return ostat

    def calDEF(mdef, miv, mev, mlvl, mopt):
        if mopt == 5 or mopt == 7 or mopt == 8 or mopt == 9:
            ntr = 1.1
        elif mopt == 1 or mopt == 11 or mopt == 16 or mopt == 21:
            ntr = 0.9
        else:
            ntr = 1.0

        ostat = (((2 * mdef + miv + (mev / 4) * mlvl) / 10) + 5) * ntr

        return ostat

    def calSPATK(mspatk, miv, mev, mlvl, mopt):
        if mopt == 15 or mopt == 16 or mopt == 17 or mopt == 19:
            ntr = 1.1
        elif mopt == 3 or mopt == 8 or mopt == 13 or mopt == 23:
            ntr = 0.9
        else:
            ntr = 1.0

        ostat = (((2 * mspatk + miv + (mev / 4) * mlvl) / 10) + 5) * ntr

        return ostat

    def calSPDEF(mspdef, miv, mev, mlvl, mopt):
        if mopt == 20 or mopt == 21 or mopt == 22 or mopt == 23:
            ntr = 1.1
        elif mopt == 4 or mopt == 9 or mopt == 14 or mopt == 19:
            ntr = 0.9
        else:
            ntr = 1.0

        ostat = (((2 * mspdef + miv + (mev / 4) * mlvl) / 10) + 5) * ntr

        return ostat

    def calSPD(mspd, miv, mev, mlvl, mopt):
        if mopt == 10 or mopt == 11 or mopt == 13 or mopt == 14:
            ntr = 1.1
        elif mopt == 2 or mopt == 7 or mopt == 17 or mopt == 22:
            ntr = 0.9
        else:
            ntr = 1.0

        ostat = (((2 * mspd + miv + (mev / 4) * mlvl) / 10) + 5) * ntr

        return ostat
