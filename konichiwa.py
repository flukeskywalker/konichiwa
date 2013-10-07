#!/usr/bin/env python

##############################################################
TITLE = 'Konichiwa'
INSTALLCMD = 'apt-get install'

PACKAGEDATA = '''

clang -- clang llvm compiler
guake -- drop down terminal
vim -- God's own editor
exuberant-ctags -- for tag navigation in Vim
build-essential -- compilers etc.
ubuntu-restricted-extras -- For media stuff
cmake -- to make stuff
cmake-gui -- The GUI for cmake
texlive-full -- LaTeX stuff
gnuplot -- Make awesome plots
xfig -- Edit fig files
dia-common -- Make Diagrams
gimp -- Edit images
vlc -- Must install
cython -- For C and Python interfaces
libopenblas-dev -- For optimized BLAS
libfreetype6-dev -- to get matplotlib from pip
libpng-dev -- to get matplotlib from pip
python-scipy -- SciPy for Python
python-matplotlib -- Plotting in Python
python-setuptools -- To install more Python stuff
python-mdp -- Modular digital processing toolkit
python-pip -- Python package installation
ipython -- Interactive python interpreter
ipython-notebook -- for notebook
ipython-qtconsole -- for console
screenlets -- Unity screenlets
default-jdk -- Java Dev tools
gfortran -- Fortran compiler
git -- Dist. Version control
git-core -- git core package
subversion -- For SVN version control
ttf-larabie-deco -- Decorative fonts
ttf-larabie-straight -- Straight fonts
ttf-larabie-uncommon -- Uncommon fonts
nautilus-open-terminal -- Open in Terminal option
openssh-server -- for SSH/SFTP connections
cmake-curses-gui -- for using ccmake
xdotool -- for torcs stuff
gdevilspie -- for torcs stuff
libalut-dev -- for torcs stuff
libplib-dev -- for torcs stuff
libapr1-dev -- for py-lstm
libaprutil1-dev -- for py-lstm
libboost-dev -- BOOST, especially for py-lstm
lyx -- LaTeX document processor
'''

PACKAGES = []
##############################################################

import subprocess
import os

def capture_err(args):
    p = subprocess.Popen(args, stderr=subprocess.PIPE)
    return p.communicate()[1]

def get_which(q):
    p = subprocess.Popen(['which', q], stdout=subprocess.PIPE)
    return p.communicate()[0]

def find_dialog_program():
    found_dialog = get_which('dialog').strip()
    found_whiptail = get_which('whiptail').strip()
    if found_dialog != '':
        return found_dialog
    elif found_whiptail != '':
        return found_whiptail
    else:
        raise Exception('Please install \'dialog\' or \'whiptail\'.')

def show_checklist(items):
    global TITLE, INSTALLCMD, PACKAGES
    #--checklist text height width list-height [ tag item status ] ...
    cmd = [find_dialog_program(),
           '--checklist',
           TITLE,
           '22',
           '70',
           '15']
    for a, b, c in items:
        cmd.append(a)
        cmd.append(b)
        if c:
            cmd.append('on')
        else:
            cmd.append('off')
    return capture_err(cmd)

def setup():
    global PACKAGEDATA, PACKAGES
    lines = PACKAGEDATA.split('\n')
    for line in lines:
        line = line.strip()
        if line != '':
            if line[0:1] == '*':
                f = True
                line = line[1:]
            else:
                f = False
            pname, pdesc = line.split(' -- ')
            PACKAGES.append((pname, pdesc, f))
    
def main():
    q = show_checklist(PACKAGES).strip()
    if q != '':
        #print INSTALLCMD + ' ' + q
        os.system(INSTALLCMD + ' ' + q)

if __name__ == '__main__':
    setup()
    main()

#print show_checklist(PACKAGES).split()


