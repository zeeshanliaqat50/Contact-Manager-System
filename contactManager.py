#!/usr/bin/env python
# coding: utf-8

# #Adding
# def add():
#     fname=input("Please Enter FirstName : ")
#     lname=input("Please Enter LastName : ")
#     pno=input("Please Enter Phone Number : ")
#     email=input("Please Enter Email : ")
#     
#     #opening file
#     f=open('contacts.txt','a')
#     line="Firstname: "+fname+" Lastname: "+lname+" Phone # : "+pno+" Email : "+email+"\n"
#     f.writelines(line)
#     print(" \n Contact Added Successfully \n ")
#     f.close()
# 
# #Searching
# def search():
#     query=input("Enter Query : ");
#     f=open('contacts.txt','r')
#     Lines = f.readlines() 
#     # Strips the newline character 
#     print("\nFound Contacts \n")
#     for line in Lines: 
#         line=line.strip()
#         if(query in line):
#             print(line)
#             print("\n")
# def update():
#     
#     #query=input("Enter Parameter to Update Record E.g Name,email etc  : ");
#     #Enter Record detail to update
#     print("Enter Record to Replace \n")
#     fname=input("Please Enter FirstName : ")
#     lname=input("Please Enter LastName : ")
#     pno=input("Please Enter Phone Number : ")
#     email=input("Please Enter Email : ")
#     line="Firstname: "+fname+" Lastname: "+lname+" Phone # : "+pno+" Email : "+email+"\n"
#     #Enter data to update there
#     print(" \n Enter Updated Data \n")
#     fname=input("Please Enter FirstName : ")
#     lname=input("Please Enter LastName : ")
#     pno=input("Please Enter Phone Number : ")
#     email=input("Please Enter Email : ")
#     line1="Firstname: "+fname+" Lastname: "+lname+" Phone # : "+pno+" Email : "+email+"\n"
#     #opening file to read searched data
#     fin = open("contacts.txt", "rt")
#     data = fin.read()
#     if(line not in data):
#         print("No Such Record Exists,Please try again")
#         return;
#     data = data.replace(line, line1)
#     fin.close()
#     
# 
#     fin = open("contacts.txt", "wt")
#     fin.write(data)
#     fin.close()
#     print("Updation Done \n")
# 
# def delete():
#     print("Enter Record to Delete \n")
#     fname=input("Please Enter FirstName : ")
#     lname=input("Please Enter LastName : ")
#     pno=input("Please Enter Phone Number : ")
#     email=input("Please Enter Email : ")
#     line="Firstname: "+fname+" Lastname: "+lname+" Phone # : "+pno+" Email : "+email+"\n"
#    
#     #opening file to read searched data
#     fin = open("contacts.txt", "rt")
#     data = fin.read()
#     if(line not in data):
#         print("No Such Record Exists,Please try again. . .  \n ")
#         return;
#     data = data.replace(line,'')
#     fin.close()
#     
# 
#     fin = open("contacts.txt", "wt")
#     fin.write(data)
#     fin.close()
#     print("Deletion Done \n")
# 
# choice=0;
# while(choice!=-1):
#     print("**Welcome To contact Manager \n **")
#     print("Print 1 to Add Contact")
#     print("Print 2 to Search Contact")
#     print("Print 3 to Delete Contact")
#     print("Print 4 to Update Contact")
#     print("Print -1 to Quit")
#     choice=int(input("Enter Choice : "))
#     if((choice<1 and choice!=-1) or choice>4):
#         print("Invalid Choice")
#     else:
#         if(choice==1):
#             add()
#         elif(choice==2):
#             search()
#         elif(choice==3):
#             delete()
#         elif(choice==4):
#             update()
# print("System Halts")

# In[ ]:


fin = open("tt.txt", "rt")
data = fin.read()
data = data.replace('pyton', 'python')
fin.close()

fin = open("tt.txt", "wt")
fin.write(data)
fin.close()
print("done")


# In[ ]:




