import os
import zc.buildout

os_ldflags=''
uname=os.uname()[0]
if uname == 'Darwin':
    os_ldflags=' -mmacosx-version-min=10.5.0'


def appendEnvVar(env,var,sep=":",before=True):
    """ append text to a environnement variable
    @param env String variable to set
    @param before append before or after the variable"""
    for path in var:
    	if before:os.environ[env] = "%s%s%s" % (path,sep,os.environ.get(env,''))
	else:os.environ[env] = "%s%s%s" % (os.environ.get(env,''),sep,path)


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
    return None

# vim:set ts=4 sts=4 et  :
