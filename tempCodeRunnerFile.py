with open('test2.inp', 'w') as FileInp:

    ten = FileInp.rstrip('\n')
    tuoiHienTai = int(FileInp.readline())

with open('test2.out','r') as FileOut:
    FileOut.write(u'Vao 20 nam nua, tuoi cua {} se la {}'.format(ten, tuoiHienTai + 20))