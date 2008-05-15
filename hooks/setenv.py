import os

os_ldflags=''
uname=os.uname()[0]
if uname == 'Darwin':
    os_ldflags=' -mmacosx-version-min=10.5.0'

def getsaslenv(options=None,buildout=None):
    # patch Makefile
    for dir in ['.','include','lib','saslauthd','man','sasldb','plugins','pwcheck','utils' ]:
        oldpwd=os.getcwd()
        os.chdir(dir)
        pwd=os.getcwd()
        file=open('/'.join((pwd,'Makefile')))
        #file=open('/home/kiorky/Makefile')
        lines=file.readlines()
        for i,line in enumerate(lines):
            if line[:8] == 'framedir':
                lines[i]='framedir = %s/include\n' %options['location']
        file=open('/'.join((os.getcwd(),'Makefile')),'w+')
        file.writelines(lines)
        file.close()
        os.chdir(oldpwd)

# vim:set ts=4 sts=4 et  :
