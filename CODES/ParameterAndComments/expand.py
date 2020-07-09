import table

from table import NAME_TAB
from table import DEF_TAB
from table import A_ARG_TAB
from table import F_ARG_TAB
from table import input_file
print("INPUT_FILE")
print(input_file)
print("NAME_TAB")
print(NAME_TAB)
print("F_ARG_TAB")
print(F_ARG_TAB)      
print("DEF_TAB")
print(DEF_TAB)      
print("A_ARG_TAB")
print(A_ARG_TAB)

#list which only contain the name of macros
i=0
only_name=[]
for i in range(0,len(NAME_TAB),3):
  only_name.append(NAME_TAB[i])
  
#remove the definition part
#find the index of the last line of last macro definition
input_file.reverse()
i=0
for i in range(len(input_file)):
  if "]<-MACRO" in input_file[i]:
    index=i
    #print(index)
    #print(input_file[i])
    break

del input_file[46:] # it will remove definition part from input_file
input_file.reverse()

#creating output_file to write expanded code
print(NAME_TAB)

i=0
for i in range(len(input_file)):
  str=input_file[i]
  j=0
  for j in range(0,len(NAME_TAB),3):
    count=j
    if NAME_TAB[j] in str:
      #print("str=",str)
      str1=NAME_TAB[count+1]
      #print("str1=",str1)
      str2=NAME_TAB[count+2]
      #print("str2=",str2)
      index1=int(str1)
      index2=int(str2)
      #print("index1=",index1,"index2=",index2)
      temp_list=DEF_TAB[index1+1:index2]#stores the definition of the macro
      #print(temp_list)
      # now go to the arg table and search the name of the macro in arg tab and then find thr number of
      #argument if==0 then only copy the definition
      if temp_list[0]=='0':
        #print("in zero case")
        #print(temp_list[1:])
        del input_file[i]
        s=0
        chk=i
        for s in range(1,len(temp_list),1):
         input_file.insert(chk,temp_list[s])
         chk=chk+1
        #print(input_file)
      else:
        #print("in other case")
        arg_number=int(temp_list[0])
        #print("arg_number=",arg_number)
        arg_name=NAME_TAB[j]
        #print("arg_name=",arg_name)
        #print("F_ARG_TAB=",F_ARG_TAB)
        o=0
        #loop for formal argument
        for o in range(len(F_ARG_TAB)):
          if arg_name==F_ARG_TAB[o]:
            f_list1=[]
            z=0           
            for z in range(arg_number):
              #print("o=",o)
              #print("z=",z)
              f_list1.append(F_ARG_TAB[o+z+2])#fetching the formal arguments +2 to left name and atg_number
        #print("f_list1=",f_list1)
        
        #loop for actual argument
        #print("only_name=",only_name)
        #print("A_ARG_TAB=",A_ARG_TAB)
        o=0
        for o in range(len(A_ARG_TAB)):
          if arg_name==A_ARG_TAB[o]:
            a_list1=[]
            z=0           
            for z in range(arg_number):
             if o+z+2<len(A_ARG_TAB):  
                if A_ARG_TAB[o+z+2] not in only_name:
                 #print("o=",o)
                 #print("z=",z)
                 a_list1.append(A_ARG_TAB[o+z+2])#fetching the formal arguments +2 to left name and atg_number
                elif A_ARG_TAB[o+z+2] in only_name:
                  break
                #print("o=",o)
        #print("a_list1=",a_list1)
        
        if len(a_list1)<len(f_list1):
          q=0
          length=len(f_list1)-len(a_list1)
          for q in range(length):
            a_list1.append('NULL')
            if len(a_list1)==len(f_list1):
             break
        print("f_list=",f_list1)#f list stores the fomal argument of that macro
        print("a_list=",a_list1)#a_list stored the actual argument of that macro
        print("temp_list=",temp_list)
        expand_data_list=temp_list[2:]
        print("BEFORE:",expand_data_list)
        e=0
        #this loop will replace the formal argument with actual argument
        for e in range(len(expand_data_list)):
          str6=expand_data_list[e]
          d=0
          for d in range(len(f_list1)):
            if f_list1[d] in str6:
              print("str6=",str6)
              pre=f_list1[d]
              post=a_list1[d]
              print("pre=",pre,"post=",post)
              str6=str6.replace(pre,post)
              print("replace=",str6)
          del expand_data_list[e]
          expand_data_list.insert(e,str6)
        print("AFTER:",expand_data_list)
        del input_file[i]
        temp_index=i
        h=0
        for h in range(len(expand_data_list)):
            print("i=",i,"h=",h,expand_data_list[h])
            input_file.insert(i+h,expand_data_list[h])


print(input_file)


#ceating output expanded file
f1=open("output.text","w")
i=o
for i in range(len(input_file)):
  f1.write(input_file[i])
  f1.write('\n')

f1.close()
