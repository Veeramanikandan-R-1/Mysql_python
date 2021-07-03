import xlwt,os,subprocess
from pathlib import Path
# to check if file exist or create a new file
file_to_write=Path("F:/mani/GURUKUL/db/db_py/college_in_db_common.xls")
file_to_write1=Path("F:/mani/GURUKUL/db/db_py")
subprocess.run("chmod 777 college_in_db_common.xls",shell=True)
if file_to_write.is_file():
    os.chmod("college_in_db_common.xls", 0o777) #to give user all rights for the file
    book=open("college_in_db_common.xls","w")
else:
    book = xlwt.Workbook(encoding="utf-8")