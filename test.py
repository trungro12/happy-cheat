import pymem
import time
# import pymem.process
# from functions.admin import Admin

# admin = Admin()
# admin.run_as_admin()

module_name = "Tutorial-x86_64.exe"
try:
    pm = pymem.Pymem(process_name=module_name)
except Exception as e:
    print(e)
    exit()

def get_pointer_address(base_address, offsets = []):
    addr = pm.read_int(base_address)
    for offset in offsets:
        if(offset != offsets[-1]):
            pm.read_int(offset)
    addr = addr + offsets[-1]
    return addr

while True:
    pm.write_int(get_pointer_address(pm.base_address + 0x00325A70, offsets=[0x7B8, 0x418, 0x70, 0x50, 0x50, 0x1A8, 0x7F8]), 10)