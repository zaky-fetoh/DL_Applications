from glob import glob
import os


def getnew_name(old):
    s, e = [old.find(x) for x in ['(',')']]
    conf = ' '.join(old[s+1:e].split()[::-1]+[''])
    return conf + old[:s-1]+'.pdf'
    
files = glob('*.pdf')
for file in files:
    os.rename(file, getnew_name(file ) ) 
    
