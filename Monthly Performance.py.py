import pandas as pd
import matplotlib.pyplot as plt
import time
#pd.set_option('display.max_columns',None)

l="INFORMATICS PRACTICES PROJECT\nTOPIC-LIST OF EMPLOYEES\nTHIS PROJECT IS DONE BY:- Kris"
for i in l:
   print(i,end='')
   time.sleep(0.05)

print()
print("----------------------------------------------------------------------------")
print()
print("PLEASE ENTER THE PASSWORD")
print()

k="~THE PASSWORD IS 'ADMIN'~"
for i in k:
   print(i,end='')
   time.sleep(0.05)

print()

print()
a=input(':-')
print()

for z in a:
    if a=='ADMIN':
       print('                                               ~MENU~                                               ')
       print()
       print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
       print('*  1) LIST OF ALL THE EMPLOYEES(CSV FILE)                                  *')
       print('*  2) LIST OF ALL THE EMPLOYEES(CSV FILE WITHOUT INDEX)       *')
       print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
       print('*  3) THE NUMBER OF PEOPLE IN EACH BRANCH (BAR GRAPH)       *')
       print('*  4) THE PERFORMANCE OF AN EMPLOYEE (LINE GRAPH)             *') 
       print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  ')
       print('*  5) SORTING THE DATA AS PER YOUR CHOICE                              *')
       print('*  6) VIEWING DATA FROM TOP AND BOTTOM OF THE FILE            *')
       print('*  7) VIEWING SPECIFIC COLUMN(s) FROM THE FILE                       *')
       print('*  8) ADDING DATA TO THE FILE                                                        *')
       print('*  9) EXIT                                                                                            *')
       print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
       print()
    else:
       print('INCORRECT PASSWORD PLEASE TRY AGAIN')
       exit()
    b=int(input('ENTER THE NUMBER AS PER THE MENU:-'))
    print()




    if b==1:
        print('LIST OF ALL THE EMPLOYEES')
        print()
        df=pd.read_csv("D:\LIST OF ALL EMPLOYEES.CSV")
        print(df)

    

    
    
    if b==2:
        print('LIST OF ALL THE EMPLOYEES WITHOUT THE INDEX')
        print()
        df=pd.read_csv("D:\LIST OF ALL EMPLOYEES.CSV",index_col=0)
        print(df)
    
    
    if b==3:
        print('THE NUMBER OF EMPLOYEES IN EACH BRANCH')
        print()
        df=pd.read_csv("D:\LIST OF ALL EMPLOYEES.CSV")
        y=[1,2,3,4]
        br=[7,6,5,6]
        plt.xlabel("BRANCH")
        plt.ylabel("NUMBER OF EMPLOYEES")
        plt.bar(y,br)
        plt.show()
    
    def line_plot():
       df=pd.read_csv("D:\LIST OF ALL EMPLOYEES.CSV")
       name=df['EMP_NAME']
       per1=df['PERFORMANCE(MONTH 1)']
       per2=df['PERFORMANCE(MONTH 2)']
       per3=df['PERFORMANCE(MONTH 3)']
       plt.xlabel('NAMES')
       plt.xticks(rotation='vertical')

       print('SELECT THE SPECIFIC MONTH')
       print('PRESS 1 FOR MONTH 1')
       print('PRESS 2 FOR MONTH 2')
       print('PRESS 3 FOR MONTH 3')
       print()

       op=int(input('ENTER YOUR CHOICE:-'))
       print()

       if op==1:
          plt.ylabel('PERFORMANCE')
          plt.title('PERFORMANCE IN MONTH 1')
          plt.plot(name,per1)
          plt.show()

       if op==2:
          plt.ylabel('PERFORMANCE')
          plt.title('PERFORMANCE IN MONTH 2')
          plt.plot(name,per2)
          plt.show()

       if op==3:
          plt.ylabel('PERFORMANCE')
          plt.title('PERFORMANCE IN MONTH 3')
          plt.plot(name,per3)
          plt.show()

    if b==4:
        print('THE PERFORMANCE OF AN EMPLOYEE')
        print()
        line_plot()

    
    def data_sorting():
        df=pd.read_csv("D:\LIST OF ALL EMPLOYEES.CSV")
        print('PRESS 1 TO ARRANGE THE RECORD AS PER THE EMP_CODE')
        print('PRESS 2 TO ARRANGE THE RECORD AS PER THE EMP_NAME')
        print('PRESS 3 TO ARRANGE THE RECORD AS PER THE BRANCH')
        print('PRESS 4 TO ARRANGE THE RECORD AS PER THE SALARY')
        print()
        op=int(input('ENTER YOUR SELECTED NUMBER:-'))
        if op==1:
            df.sort_values(['EMP_CODE'],inplace=True)
            print(df)
        if op==2:
            df.sort_values(['EMP_NAME'],inplace=True)
            print(df)
        if op==3:
            df.sort_values(['BRANCH'],inplace=True)
            print(df)
        if op==4:
            df.sort_values(['SALARY'],inplace=True)
            print(df)
    
    if b==5:
        print()
        data_sorting()
    
    def top_bottom():
        df=pd.read_csv("D:\LIST OF ALL EMPLOYEES.CSV")
        top=int(input('HOW MANY RECORDS TO DISPLAY FROM TOP:-'))
        print('FIRST',top,'RECORDS')
        print(df.head(top))
        bottom=int(input('HOW MANY RECORDS TO DISPLAY FROM BOTTOM:-'))
        print('LAST',bottom,'RECORDS')
        print(df.tail(bottom))

    if b==6:
        print()
        top_bottom()
    
    def specific_col():
        print("COLUMNNAMES=EMP_CODE,EMP_NAME,BRANCH,SALARY,PERFORMANCE (MONTH 1),PERFORMANCE (MONTH 2),PERFORMANCE (MONTH 3)")
        col=(input('ENTER THE COLUMN YOU WANT TO VIEW (CAPITAL LETTERS):='))
        df=pd.read_csv("D:\LIST OF ALL EMPLOYEES.CSV",usecols=[col])
        print(df)
    
    if b==7:
        print()
        specific_col()
    
    if b==8:
        print()
        df=pd.read_csv("D:\LIST OF ALL EMPLOYEES.CSV")
        print('ENTER THE FOLLOWING IN CAPITAL LETTERS WHERE NECESSARY')
        r=input('ENTER THE EMPLOYEE CODE:-')
        t=input('ENTER THE EMPLOYEE NAME:-')
        y=input('ENTER THE BRANCH OF THE EMPLOYEE:-')
        u=input('ENTER THE SALARY OF THE EMPLOYEE:-')
        p1=input('ENTER THE PERFORMANCE OF EMPLOYEE IN THE FIRST MONTH:-')
        p2=input('ENTER THE PERFORMANCE OF EMPLOYEE IN THE SECOND MONTH:-')
        p3=input('ENTER THE PERFORMANCE OF EMPLOYEE IN THE THIRD MONTH:-')
        df1=df.append({'EMP_CODE':r,'EMP_NAME':t,'BRANCH':y,'SALARY':u,'PERFORMANCE(MONTH 1)':p1,'PERFORMANCE(MONTH 2)':p2,'PERFORMANCE(MONTH 3)':p3},ignore_index=True)
        df1.to_csv("D:\LIST OF ALL EMPLOYEES.CSV",index=False, header=True)
        print(df1)

    if b==9:
        print()
        print('PRESS THE ENTER KEY TO EXIT THE SYSTEM')
        exit()

