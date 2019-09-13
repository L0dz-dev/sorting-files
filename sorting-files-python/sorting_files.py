import os
import time
PROJECT_PATH = os.getcwd()
if (os.path.exists(os.environ['USERPROFILE'] + '\\Desktop\\sorted')):
    SORTING_PATH=os.path.join(os.environ['USERPROFILE'] + '\\Desktop\\', 'sorted')
else:
    os.chdir(os.path.join(os.environ['USERPROFILE'])+ '\\Desktop\\')
    os.mkdir('sorted')
    SORTING_PATH=os.path.join(os.environ['USERPROFILE'] + '\\Desktop\\' , 'sorted')

    os.chdir(PROJECT_PATH)
class Sorter:
    #INITIALIZE SORTER
    def __init__(self):
        self.original_files = []
        self.files = []
        self.ext_list = []

        #READ EXTENSIONS FROM FILE
        try:
            self.ext_read = open('ext_list.txt', 'r').read()
        except:
            open('ext_list.txt', 'wb').close()
            self.ext_read = open('ext_list.txt', 'r')


    #ALWAYS SCAN IF ANY CHANGE IS APPLIED TO DESKTOP
    def scan(self):
        self.files = os.listdir()
        for file in self.files:
            for ext, name in self.ext_list:
                filename, extension = os.path.splitext(file)
                if extension == '.' + ext:
                    return 1
        return 0

    #SORT FILES IN FOLDERS
    def sort(self):
        for file in self.files:
            filename, extension = os.path.splitext(file)
            #print(filename + '  -  ' + extension)
            if(not('Nuovo' in filename or 'nuovo' in filename)):
                for ext, name in self.ext_list:
                    #print('.' + ext)
                    if extension == '.' + ext:
                        try:
                            os.rename(filename + extension, SORTING_PATH + '\\' + name.upper() + '\\' + filename + extension)
                            print(filename + extension + ' sorted.')
                        except:
                            print('Errore. Probabilmente un file col nome {} {} esiste già'.format(filename, extension))

    #SETUP OF THE PROGRAM
    def setup(self):
        os.chdir(SORTING_PATH)
        #print(self.ext_read)
        letter = ''
        ext_clean = ''
        name = ''
        noname = 0
        for ext in self.ext_read:
            noname += noname
            if ext == ':':
                ext_clean = letter
                letter = ''
                noname += 1
            elif ext == '-':
                name = letter
                if ext_clean == '':
                    ext_clean = name
                letter = ''
                if noname == 2:
                    name = ext_clean
                else:
                    noname = 0
            elif ext != '.' and ext != ' ' and ext != '\n' and ext != '\r':
                letter += ext

            if name != '':
                try:
                    self.ext_list.append((ext_clean, name))
                    os.mkdir(name.upper())
                    print('Created directory {}'.format(name.upper()))
                except:
                    print('Directory {} already exists'.format(name.upper()))

                ext_clean = ''
                name = ''

        if not str(os.getcwd).endswith('Desktop'):
            os.chdir(os.path.join(os.environ['USERPROFILE'], 'Desktop'))
            print('Current directory changed to desktop')
        else:
            print('Already in Desktop.')
        self.original_files = os.listdir()





Sorter.__init__(Sorter)
Sorter.setup(Sorter)
Sorter.sort(Sorter)
print(Sorter.ext_list)
#CONTINUOUS PROGRAM LOOP
run = True
while run:
    if Sorter.scan(Sorter) == 1:
        Sorter.sort(Sorter)
    time.sleep(30)