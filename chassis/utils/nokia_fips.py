#!/usr/bin/env python3

import time,os

if __name__ == "__main__":
    time.sleep(180)
    cmd = 'sudo mkdir /var/run/sswsyncd'
    os.system(cmd)
    asic = 1
    if asic == 0:
        pci_id = '06:00.0'
    else:
        pci_id = '07:00.0'
    config_file = f'/usr/share/sonic/device/x86_64-nokia_ixr7250e_36x400g-r0/Nokia-IXR7250E-36x400G/{asic}/jr2cp-nokia-18x400g-config.bcm'
    cmd="sed -i '10i { \"key\": \"sfp_init_tx_en\", \"stringval\": \"yes\" },' /etc/opt/srlinux/startup_debug.json"
    os.system(cmd)
    cmd = f"sudo /usr/bin/dsserve /usr/bin/fips_macsec.exe --cfg-file {config_file} --pci-id {pci_id} --asic {asic}"
    os.system(cmd)
