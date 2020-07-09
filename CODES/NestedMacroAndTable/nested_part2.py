#code to expand the nested macro definition
import nested_part1
import table_part1
from nested_part1 import NEW_NAME_TAB
from nested_part1 import NEW_DEF_TAB
from table_part1 import A_ARG_TAB
from table_part1 import F_ARG_TAB
from table_part1 import input_file
from table_part1 import only_name

#remove the definition part
#find the index of the last line of last macro definition
input_file.reverse()
i=0
for i in range(len(input_file)):
  if "]<-MACRO" in input_file[i]:
    index=i
    break
del input_file[i:] # it will remove definition part from input_file
input_file.reverse()

input_file.append("$")#to get the end of the input file
i=0
while(input_file[i]!="$"):#scan input file
  print(i)
  str1=input_file[i]
  j=0
  print(input_file[i])
  for j in range(len(only_name)):
    if only_name[j] in str1: #means macro calling

      #find out the name of the macro
      name=only_name[j]

      #find out the stat and end address of the definition
      k=0
      for k in range(len(NEW_NAME_TAB)):
        if name==NEW_NAME_TAB[k]: #means now we will find the start and end address of definition
          s_index=int(NEW_NAME_TAB[k+1])
          e_index=int(NEW_NAME_TAB[k+2])

      #to get the starting
      start_line='MACRO->['
      start_line=start_line+name
      start_line=start_line+']'
      #get end line
      end_line='['
      end_line=end_line+name
      end_line=end_line+']<-MACRO'
      l=0
      #fetch the definition from DEF_TAB
      for l in range(len(NEW_DEF_TAB)):
        def_list=NEW_DEF_TAB[s_index+1:e_index]

     #def_list[0] will define the number of argument in the macro
      number_of_arg=int(def_list[0])

      if number_of_arg==0:
        del input_file[i]
        assign_list=def_list[1:]
        a=0
        for a in range(len(assign_list)):
          input_file.insert(i+a,assign_list[a])

      else:
        #when number_of_arg>0
        #to get the formal argument in the f_list
        m=0
        for m in range(len(F_ARG_TAB)):
          if name==F_ARG_TAB[m]:#yes,then get the arg list
            f_list=F_ARG_TAB[m+2:m+2+number_of_arg]
            break

        #get the actual argument in the a_list
        
        colon_index=str1.index(':')
        arg_str=str1[colon_index+1:]#arg_str will contains the the arguments separatef by commas                
        temp_str=''
        #following loop will store the arumnets
        a_list=[]
        n=0
        a_list=list(arg_str.split(","))

        #if number of actual parameter is less than number of arg than assign default value
        if(len(a_list)<number_of_arg):
          times=number_of_arg-len(a_list)
          o=0
          for o in range(time):
            a_list.append("NULL")

        
        expand_list=def_list[2:]
        #replacing formal with actual parameter
        p=0
        for p in range(len(expand_list)):
          #if line contains the formal parameter
          q=0
          for q in range(len(f_list)):
            if f_list[q] in expand_list[p]:#means the line contains the formal argument
              pre=f_list[q]
              post=a_list[q]
              new_line=expand_list[p].replace(pre,post)
              del expand_list[p]
              expand_list.insert(p,new_line)

        #expand list contains the actual definition with actual paramerter
        #delet the macro callinf and expand with expand_list

        del input_file[i]
        r=0
        for r in range(len(expand_list)):
              input_file.insert(r+i,expand_list[r])
   
  i=i+1

f1=open("output.text",'w')
c=0
for c in range(len(input_file)-1):
  f1.write(input_file[c])
  f1.write("\n")
f1.close()
