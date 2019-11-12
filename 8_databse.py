import sqlite3
import sys
def establish_connection(filename) :
  conn=None
  try :
    conn=sqlite3.connect(filename)
    print("Datbase",filename,"succesfully created .!!!!")
  except Exception as e :
    print("unable to create database")
  return conn

def create_table(conn,tablename) :
  try :
    c=conn.cursor()
    c.execute("create table if not exists "+tablename+" (name text,usn text primary key,sem integer,cgpa text)")
    print("Table",tablename,"succesfully created .!!!!")
  except Exception as e :
    print("unable to create table")

def insert(conn,tablename,name,usn,sem,cgpa):
  try :
    c=conn.cursor()
    c.execute("insert into "+tablename+" values (?,?,?,?)",(name,usn,sem,cgpa))
    print("Record succesfully inserted .!!!!")
  except Exception as e :
    print("unable to insert")

def display(conn,tablename,usn,All=False) :
  if All==False :
    try :
      c=conn.cursor()
      for i in range(len(usn)):
        c.execute("select * from "+tablename+" where usn="+usn[i])
        record=c.fetchone()
        print(record)
    except Exception as e :
      print(e)
  if All==True :
    try :
      c=conn.cursor()
      for i in range(len(usn)):
        c.execute("select * from "+tablename)
        record=c.fetchall()
        print(record)
    except Exception as e :
      print(e)


def update(conn,tablename,usn,name,sem,cgpa):
  try:
    sql = ''' UPDATE student
                SET name = ? ,
                    sem = ? ,
                    cgpa = ?
                WHERE usn = ?'''
    task=(name,sem,cgpa,usn)
      
    cur = conn.cursor()
    cur.execute(sql, task)
    print("updated successfully ...!!!")
  except Exception as e:
    print("unable to update")

def delete(conn,tablename,usn) :
  try :
    c=conn.cursor()
    s1="delete from "+tablename+" where usn="+usn
    c.execute(s1)
    print("succesfully deleted ...!!!")
  except Exception as e :
    print(e)

		



connection=establish_connection('student.db')
create_table(connection,'student')
choice=1
while choice :
  print("selct your choice :- \n1) insert record 2)display_specific 3)display all 4)update 5)delete 0)exit ")
  choice=int(input("choice : "))
  if choice ==1: 
    n=int(input("enter Number of students : "))
    for i in range(n) :
      insert(connection,"student",input("enter name : "),input("enter usn : "),int(input("enter sem : ")),input("enter cgpa : "))
  if choice ==2: 
    display(connection,"student",list(input("enter usn : ")))
  if choice ==3 :
    display(connection,"student",[1],True)
  if choice ==4 :
    update(connection,"student",input("enter usn : "),input("enter name : "),int(input("enter sem : ")),input("enter cgpa : "))
  if choice==5 :
    delete(connection,"student",input("enter usn : "))
  if choice==0:
    exit()
