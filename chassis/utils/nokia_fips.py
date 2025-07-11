#!/usr/bin/env python3

import time,os

if __name__ == "__main__":
    time.sleep(180)
    cmd = 'sudo mkdir /var/run/sswsyncd'
    os.system(cmd)
    cmd = 'sudo /usr/bin/dsserve /usr/bin/fips_macsec.exe'
    os.system(cmd)
