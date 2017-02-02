# -*- coding: utf-8 -*-

input_file = open("C:/Users/Public/Documents/p30.csv", "rt", encoding="cp1251")
first_l = input_file.readline()
d = first_l.split(";")
print(len(d))
print(first_l)
m_f = {}
for line in input_file.readlines():
    print(line)
    d = line.rstrip().split(";")
    if d[1] in m_f:
        if d[0] in m_f[d[1]]:
            m_f[d[1]][d[0]].extend(d[2:])
        else:
            m_f[d[1]][d[0]] = d[2:]
    else:
        m_f[d[1]] = {}
        m_f[d[1]][d[0]] = []
        m_f[d[1]][d[0]].extend(d[2:])
print("**************************************")

outf = open("C:/Users/Public/Documents/p30.txt", "w", encoding="utf-8")
for key, value in m_f.items():
    print(key)
    outf.write(key + "\n")
    outf.write("=".ljust(len(key), "="))
    outf.write("\n")
    outf.write("\n")
    for lk, lv in value.items():
        outf.write(lk + "\n")
        outf.write("-".ljust(len(lk), "-"))
        outf.write("\n \n")
        offset = 0
        outf.write(".. csv-table:: \n")
        outf.write('   :header: "Код","Возможность","Риск", "Версия" \n')
        outf.write('   :widths: 10 70 10 10 \n \n')
        offset = 0
        while offset < len(lv) - 1:
            outf.write(" ".ljust(3, " "))
            outf.write('"' + lv[offset] + '"')
            outf.write("," + '"' +  lv[offset + 1] + '"')
            outf.write("," + '"' +  lv[offset + 2] + '"')
            outf.write("," + '"' +  lv[offset + 3] + '"')
            outf.write("\n")
            offset = offset + 4
        outf.write("\n")    
input_file.close()
outf.close()
print("Все OK")
