import ctypes, sys

class Admin:

    def __init__(self):
        pass

    def is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def run_as_admin(self):
        if self.is_admin():
            print("Run as Admin !!!")
            return True
        else:
            # Re-run the program with admin rights
            print(sys.argv)
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)