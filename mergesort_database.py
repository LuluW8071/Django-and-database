

import psycopg2

mydb = psycopg2.connect(
    database="Student",
    user="postgres",
    password="8071",
    host="localhost",
    port=5432,
)
cursor = mydb.cursor()
print(cursor)
query = 'Select * from "Student"'
cursor.execute(query)
array=cursor.fetchall()
print(array)
print("Given data is:")
for x in array:
    print(x)

def merge(array,age):
    if len(array)>1:
        mid=len(array)//2
        L=array[:mid]
        R=array[mid:]
        merge(L,age)
        merge(R,age)
        i=j=k=0
    
        while i<len(L) and j<len(R):
            if L[i][2] <= R[j][2]:
                array[k]=L[i]
                i+=1

            else:
                array[k]=R[j]
                j+=1
            k+=1

        while i<len(L):
            array[k]=L[i]
            i+=1
            k+=1

        while j<len(R):
            array[k]=R[j]
            j+=1
            k+=1

merge(array,2)
print("The sorted age is :")
for x in array:
    print(x)
