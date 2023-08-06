import subprocess
import sys   
class LOADER():
    def __init__(self,modules) -> None:
        for i in modules:
            self.package = i
            #print(self.package)
            import_or_install(self.package)
def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])  
if __name__ == "__main__":
   subprocess.check_call([sys.executable, "-m", "pip", "install", "tk-tools"])
   subprocess.check_call([sys.executable, "-m", "pip", "install", "customtkinter"])
   subprocess.check_call([sys.executable, "-m", "pip", "install", "mysql-connector-python"])