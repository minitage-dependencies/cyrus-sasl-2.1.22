import os
import sys
def getsaslenv(options=None,buildout=None):
    # patch Makefile
    os.chdir(options['compile-directory'])
    for dir in ['.','include','lib','saslauthd','man','sasldb','plugins','pwcheck','utils' ]:
        oldpwd=os.getcwd()
        os.chdir(dir)
        pwd=os.getcwd()
        file=open('/'.join((pwd,'Makefile')))
        #file=open('/home/kiorky/Makefile')
        lines=file.readlines()
        for i,line in enumerate(lines):
            if line[:8] == 'framedir':
                lines[i]='framedir = %s/include\n' % options['location']
        file=open('/'.join((os.getcwd(),'Makefile')),'w+')
        file.writelines(lines)
        file.close()
        os.chdir(oldpwd)

def reconfigure(options=None,buildout=None):
    if sys.platform.startswith('cygwin'):
        c = os.getcwd()
        os.chdir(options['compile-directory'])
        os.system("automake -fcav")
        os.chdir('saslauthd')
        os.system('../config/missing  '
                  '--run aclocal-1.7  '
                  '-I ../cmulocal/    '
                  '-I ../config/      ')
        os.system("automake -fcav")
        os.chdir(options['compile-directory'])
        os.environ['LDFLAGS'] = '%s %s' %( os.environ.get('LDFLAGS', '') , '-no-undefined')
        os.chdir(c)
    os.system(
        'sed -e "s/\$ac_cache_corrupted/ [[ "a" == "b" ]] /g" -i %s' % (
            os.path.join(options['compile-directory'],'saslauthd','configure')
        )
    )
    os.system(
        'sed -e "s/\$ac_cache_corrupted/ [[ "a" == "b" ]] /g" -i %s' % (
            os.path.join(options['compile-directory'],'configure')
        )
    )


# vim:set ts=4 sts=4 et  :
