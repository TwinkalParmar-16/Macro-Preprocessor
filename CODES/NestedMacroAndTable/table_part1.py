#syntax of my macro
#DEFINITION:
'''MACRO->[name_of_the_macro] #starting
  number_of_argument
  ~arg1,~arg2,~arg3,~arg4..
  inst1
  inst2
  ..
  ..
  [name_of_the_macro]<-MACRO #ending
'''
#CALLING:
'''
name_of_the_macro ARG(number_of_element):arg1,arg2,arg3....
'''
#without nested calling
#python code to fill the ARG_TAB,NAME_TAB,DEF_TAB

#------------------------------------------------------------------------------------------------------------------------------

# taking the input file
f=open("input.text",'r')

#stores the input into the input_file list
input_file=f.readlines() 

# it will remove /n from the input_file list
for i in range(len(input_file)):
    input_file[i]=input_file[i].strip()

#it will remove the blank lines or extra new lines from the list
if '' in input_file:
    while '' in input_file:
        input_file.remove('')

#to remove comment
d=0
for d in range(len(input_file)):
  string=input_file[d]
  if '/c/' in string: #this line has the comment
    index=string.index('/c/')
    l_w_c_str=string[:index]
    del input_file[d] # delet the line which has comment
    input_file.insert(d,l_w_c_str) #assign new line without comment

#copy of input file for further use
copy_input_file=input_file

#declaration of list for TABLE
NAME_TAB=[] #name ,starting index and ending index
DEF_TAB=[] #all macro definition from starting line to ending line
F_ARG_TAB=[] #name,number of arg,and formal arguments
A_ARG_TAB=[]#name,number of arg,and actual arguments

#loop to scan each line of the input text file
#this will fill DEF_TAB and NAME_TAB
i=0
for i in range(len(input_file)):
    #searching of macro definition
    if "MACRO->" in input_file[i]:#if find
        print("line=",input_file[i])
        str=input_file[i]
        index1=str.index('[')
        index2=str.index(']')
        str=str[index1+1:index2]#str contains the name of the macro (temprory)
        #it will help to get the end line of the macro
        str2="["
        str2=str2+str
        str2=str2+']<-MACRO'#str2 stores the end line of the macro(temporary)
        str1="MACRO->"
        str1=str1+'['
        str1=str1+str
        str1=str1+']'#str1 stores the first line of the macro(temporary)
        
        #this loop will extract the index(address) of the start_of_macro_definition and end_of_macro_definition
        j=0
        for j in range(len(input_file)):
            if str1 in input_file[j]:
                start_index=j
            if str2 in input_file[j]:
                end_index=j
        NAME_TAB.append(str) #apped the name of the macro into the NAME_TAB
        NAME_TAB.append(start_index)#apped the starting address of the macro into the NAME_TAB
        NAME_TAB.append(end_index)#apped the ending address of the macro into the NAME_TAB
        
       #following loop will store the definition in the DEF_TAB
        l=0
        for l in range(start_index,end_index+1,1):
               DEF_TAB.append(input_file[l])
        
#following loop will fill ARG_TAB(ACTUAL ARGUMENT)
i=0
for i in range(0,len(NAME_TAB),3):#gap=3 bcz next two index contains the addresses
    str=NAME_TAB[i] #name of the macro
    j=0
    Temp_str='['
    Temp_str=Temp_str+str
    Temp_str=Temp_str+']'#stores the starting line of the macro ,whoes arguments are going
                                   #to be stored(temporary)

    #following loop will search macro calling
    for j in range(len(input_file)):
        if str in input_file[j] and Temp_str not in input_file[j]: # if temp_str will there ,than it can be macro definition
            str1=input_file[j]
            
            #number of arguments>0
            if 'ARG' in str1:
                index=len(str)+len('ARG')+1
                str2=str1[index:]
                index1=str2.index('(')
                index2=str2.index(')')
                no_of_arg=str2[index1+1:index2]#stores the number of arguments
                index3=str2.index(":")
                str3=str2[index3+1:]#str3 will contains the the arguments separatef by commas
                k=0                
                A_ARG_TAB.append(str)#append the name of the macro ,whoes arguments are goint to be stored
                A_ARG_TAB.append(no_of_arg)#append the number of arguments
                temp_str=''
                #following loop will store the arumnets
                for k in range(len(str3)):
                    if no_of_arg=='1' and "," not in str3:#str3 itselt is a complete argument
                        A_ARG_TAB.append(str3)
                        break
                    elif k==len(str3)-1:#last argument 
                         temp_str=temp_str+str3[k]
                         A_ARG_TAB.append(temp_str)
                         temp_str=''
                    elif str3[k]!=",":
                        temp_str=temp_str+str3[k]
                    elif str3[k]==",":
                        A_ARG_TAB.append(temp_str)
                        temp_str=''
                    
                        
            #if NO argument
            elif "ARG" not in str1:
                A_ARG_TAB.append(str)
                A_ARG_TAB.append("0")


#following loop will take the FORMAL ARGUMENTS(at the time of definition)
i=0
for i in range(len(DEF_TAB)):
    str=DEF_TAB[i]
    if "MACRO->" in str:
        index1=str.index('[')
        index2=str.index(']')
        name=str[index1+1:index2]#stores the name of the macro(temporary)
        F_ARG_TAB.append(name)#append name of the macro
        F_ARG_TAB.append(DEF_TAB[i+1])#append number of arguments
        #if NO arguments
        if DEF_TAB[i+1]=='0':
            continue
        # if number of arguments>0
        temp_str=''
        k=0
        str3=DEF_TAB[i+2]
        for k in range(len(str3)):
         if DEF_TAB[i+1]=='1' and "," not in str3:#only one argument is there
            F_ARG_TAB.append(str3)#str3 itselt is a complete argument
            break
         elif k==len(str3)-1:#last arhument
            temp_str=temp_str+str3[k]
            F_ARG_TAB.append(temp_str)
            temp_str=''
         elif str3[k]!=",":
            temp_str=temp_str+str3[k]
         elif str3[k]==",":
            F_ARG_TAB.append(temp_str)
            temp_str=''

#list which only contain the name of macros
i=0
only_name=[]
for i in range(0,len(NAME_TAB),3):
  only_name.append(NAME_TAB[i])
