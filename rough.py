import mysql.connector
import xlwt
mydb = mysql.connector.connect(
  host="34.93.223.114",
  user="root",
  password="admin",
  database="gurukul_db"
)
mycursor = mydb.cursor()
sql="SELECT college_id FROM college_courses_tb;"
mycursor.execute(sql)
myresult = mycursor.fetchall()
# print(myresult)
new_list=[]
for i in myresult:
  new_list.append(i[0])
new_list_1=set(new_list)
# print(new_list_1)
new_list_2=[]
for i in new_list_1:
  new_list_2.append(i)
new_list_2.sort()
# print(len(new_list_2))
def finding_loaded_clgs():
  college_name=[]
  f=open("colleges.txt","w")
  for i in new_list_2:
    len=1
    sql1="SELECT college_name FROM colleges_tb WHERE college_id=%s"
    variable=(i,)
    mycursor.execute(sql1,variable)
    college_name_1=mycursor.fetchall()
    college_name.append((college_name_1[0]))
    f.write(str(college_name_1[0]))
    f.write("\n")
    len+=1
  f.close()
  for i in college_name:
    print(i)

# finding_loaded_clgs()

sql2="SELECT college_id FROM colleges_tb;"
mycursor.execute(sql2)
myresult=(mycursor.fetchall())
print(myresult)
college_id_in_college_tb=[]
for i in myresult:
  college_id_in_college_tb.append(i[0])
print(len(college_id_in_college_tb))
print(len(new_list_1))
print(new_list_1)
print(college_id_in_college_tb)
college_not_loaded_with_courses=(set(college_id_in_college_tb)).difference(set(new_list_1))
print(len(college_not_loaded_with_courses))

# Writing to an excel
# sheet using Python
import xlwt
from xlwt import Workbook

# Workbook is created
# wb = Workbook()

# add_sheet is used to create sheet.
# sheet1 = wb.add_sheet('Sheet 1')
# sheet2 = wb.add_sheet('Sheet 2')
college_not_loaded_with_courses=list(college_not_loaded_with_courses)
print(college_not_loaded_with_courses)
f=open("colleges_not_loaded.txt","w")
f1=open("colleges_not_loaded_code.txt","w")
f2=open("colleges_not_loaded_university.txt","w")
for i in range(len(college_not_loaded_with_courses)):
  # print(i)
  sql3="SELECT college_name FROM colleges_tb WHERE college_id=%s"
  print(college_not_loaded_with_courses[i])
  variable = (college_not_loaded_with_courses[i],)
  mycursor.execute(sql3, variable)
  college_name = mycursor.fetchall()
  print((college_name[0])[0])
  f.write((college_name[0])[0])
  f.write('\n')
  f1.write(str(college_not_loaded_with_courses[i]))
  f1.write('\n')

  # sheet1.write(0,0,"courses_uploaded_college")
  # sheet1.write(i+1,0,college_not_loaded_with_courses[i])
  # sheet2.write(i+1,0,college_name)

# wb.save('colleges_not_uploaed.xls')
f.close()
f1.close()

