tugas = float(input("masukkan nilai tugas: "))
uts = float(input("masukkan nilai UTS: "))
uas = float(input("masukkan nilai UAS: "))

nilai = (0.15 * tugas) + (0.35 * uts) + (0.50 * uas)

if nilai > 80:
    grade = 'A'
elif nilai > 70:
    grade = 'B'
elif nilai > 60:
    grade = 'C'
elif nilai > 50:
    grade = 'D'
else:
    grade = 'E'

if nilai > 69:
    status = 'lulus'
else:
    status = 'tidak lulus'

print('nilai akhir : %0.2f' % nilai)
print('grade: {}'.format(grade))
print('status: {}'.format(status))
