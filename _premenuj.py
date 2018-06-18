import os, sys

def najdiRiesenie(jehoDir):
    files = os.listdir(os.path.join(os.getcwd(), jehoDir))
    for file in files:
        if file.endswith('.pdf') and file != 'output.pdf':
          return file
    sys.error('Nenasiel som .pdf subor!')


dirs = [d for d in os.listdir(os.getcwd()) if not d.startswith('_')]
for d in dirs:
  output = 'output.pdf'
  print('mv "%s" "%s"' % (os.path.join(d, output), os.path.join(d, najdiRiesenie(d))))
  os.system('mv "%s" "%s"' % (os.path.join(d, output), os.path.join(d, najdiRiesenie(d))))
  print('Komentar k rieseniu najdes v povodnom pdfku', file = open(os.path.join(d, 'komentar.txt'), 'w'))
