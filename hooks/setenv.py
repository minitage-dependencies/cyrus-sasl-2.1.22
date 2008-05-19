import os
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

def getsaslenvb(options=None,buildout=None):
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
    import pdb;pdb.set_trace()  ## Breakpoint ##

# vim:set ts=4 sts=4 et  :
