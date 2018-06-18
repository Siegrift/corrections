import os, sys


def najdiRiesenie(jehoDir):
    files = os.listdir(os.path.join(os.getcwd(), jehoDir))
    for file in files:
        if file.endswith('.pdf') and file != 'output.pdf':
            return file
    sys.error('Nenasiel som .pdf subor!')


dirs = sorted([d for d in os.listdir(os.getcwd()) if not d.startswith('_')])
index = 0
if not os.path.exists(os.path.join(os.getcwd(), '_poslednyRiesitel')):
    print(
        dirs[0],
        file=open(os.path.join(os.getcwd(), '_poslednyRiesitel'), 'w'))
else:
    file = open('_poslednyRiesitel', 'r')
    index = dirs.index(file.readline().strip()) + 1
    if index < len(dirs):
        print(
            dirs[index],
            file=open(os.path.join(os.getcwd(), '_poslednyRiesitel'), 'w'))

if index >= len(dirs):
    print('Huraaaa, mas vsetkych! :)')
else:
    print('xournal "%s"' % os.path.join(os.getcwd(), dirs[index],
                                        najdiRiesenie(dirs[index])))
    os.system('xournal "%s"' % os.path.join(os.getcwd(), dirs[index],
                                            najdiRiesenie(dirs[index])))
    print('code %s' % os.path.join(os.getcwd(), dirs[index], 'body.txt'))
    os.system('code %s' % os.path.join(os.getcwd(), dirs[index], 'body.txt'))
