#-*- coding:utf-8 -*-

import survey
import thinkstats as ts

def CreateTables():
    table = survey.Pregnancies()
    table.ReadRecords()

    first = survey.Pregnancies()
    other = survey.Pregnancies()

    for rec in table.records:
        if rec.outcome != 1:
            continue

        if rec.birthord == 1:
            first.AddRecord(rec)
        else:
            other.AddRecord(rec)

    return first, other

def SetDev(table):
    plist = map(lambda pl: pl.prglength, table.records)
    
    table.dev_plen = ts.Var(plist)

def SetTotalAndMean(table):
    plist = map(lambda pl: pl.prglength, table.records)

    table.num_of_birth = len(plist)
    table.mean_plen = ts.Mean(plist)

def main():
    first, other = CreateTables()

    SetTotalAndMean(first)
    SetTotalAndMean(other)

    print u'第一子総数            : %d 人' % first.num_of_birth
    print u'第二子以降総数        : %d 人\n' % other.num_of_birth

    print u'第一子平均妊娠期間    : %f 週間' % first.mean_plen
    print u'第二子以降平均妊娠期間: %f 週間' % other.mean_plen
    print u'妊娠期間の差          : %f 時間\n' % (float(first.mean_plen - other.mean_plen) * 7.0 * 24.0)

    SetDev(first)
    SetDev(other)

    print u'第一子標準偏差        : %f' % first.dev_plen
    print u'第二子以降標準偏差    : %f' % other.dev_plen
    print u'標準偏差の差          : %f' % (first.dev_plen - other.dev_plen)

if  __name__ == '__main__':
    main()
