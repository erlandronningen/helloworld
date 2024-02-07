import datetime
#@Erland Rønningen


def logg(mld):
    print(datetime.datetime.now(), mld)

def fil_logg(mld):
    f = open("mal_py.log", "a")
    f.write(datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + " --> " + mld + "\n")
    f.close()
    

if __name__ == '__main__':
    logg('Program starter...')
    fil_logg('Program starter...')
    logg('Program stopper...')
    fil_logg('Program stopper...')