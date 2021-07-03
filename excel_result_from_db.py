import stat

import mysql.connector
import xlwt,os
import pathlib
from pathlib import Path
mydb = mysql.connector.connect(
  host="34.93.223.114",
  user="root",
  password="admin",
  database="gurukul_db"
)
mycursor = mydb.cursor()
# finding all colleges id from college tb
sql="SELECT college_id FROM colleges_tb;"
mycursor.execute(sql)
myresult = mycursor.fetchall()
college_id_in_college_tb=[]
for i in myresult:
  college_id_in_college_tb.append(i[0])
college_id_in_college_tb=list(set(college_id_in_college_tb))
# print(college_list_in_college_tb)
print("colleges in colleges_tb:",len(college_id_in_college_tb))

# finding colleges names
college_name_for_colleges_in_college_tb=[]
for id in college_id_in_college_tb:
    sql="SELECT college_name FROM colleges_tb WHERE college_id=%s"
    college_id=(id,)
    mycursor.execute(sql,college_id)
    college_name=mycursor.fetchall()
    college_name_for_colleges_in_college_tb.append(college_name)

for i in range(len(college_id_in_college_tb)):
    print(college_id_in_college_tb[i],(college_name_for_colleges_in_college_tb[i])[0])

# to check if file exist or create a new file
file_to_write=Path("F:/mani/GURUKUL/db/db_py/college_in_db_common.xls")
if file_to_write.is_file():
    os.chmod("college_in_db_common.xls", 0o777) #to give user all rights for the file
    book=open("college_in_db_common.xls","w")
else:
    book = xlwt.Workbook(encoding="utf-8")

sheet1=book.add_sheet("loaded_colleges")
sheet1.write(0,0,"all_colleges_loaded_in_colleges_tb")
# writing loaded colleges in first sheet
for i in range(len(college_id_in_college_tb)):
    sheet1.write(i+1,0,college_id_in_college_tb[i])
    sheet1.write(i+1,1,(college_name_for_colleges_in_college_tb[i])[0])

sql="SELECT college_id FROM college_courses_tb"
mycursor.execute(sql)
college_id_in_college_courses_tb=list(set((mycursor.fetchall())))
print(len(college_id_in_college_courses_tb))

book.save("college_in_db_common.xls")

