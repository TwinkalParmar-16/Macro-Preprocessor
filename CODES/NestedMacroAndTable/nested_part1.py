#code for nested macro definition
import table_part1
from table_part1 import only_name
from table_part1 import DEF_TAB
from table_part1 import input_file
from table_part1 import NAME_TAB
from table_part1 import copy_input_file

#----------------------------------------------function definition part------------------------------------------------------
#start definition
def definition(str):
  MACRO_NAME=str
  j=0
  for j in range(0,len(NAME_TAB),3):# name_tab has the index also
    if MACRO_NAME==NAME_TAB[j]:
      count=j
      first_line_index=int(NAME_TAB[count+1])
      end_line_index=int(NAME_TAB[count+2])
      List=copy_input_file[first_line_index:end_line_index+1]
      return(List)
#end_definition
    
#start_check_nestef
def check_nested(list,str):
  defi=list
  name_of_macro=str
  j=0
  for j in range(1,len(defi)-1,1):
    if 'MACRO' in defi[j]:
      return 1#means nested definition
    else:
      continue
  return 0#means no nestef definition 
#end_check_nested

#start find_nested_macro_def_name
def find_nested_macro_def_name(list,str):
  name_of_the_macro=str
  defi=list
  j=0
  nested_name_list=[]
  x=len(defi)-1
  without_s_t=defi[1:x]
  for j in range(len(only_name)):
    start_line='MACRO->['+only_name[j]+']'
    if start_line in without_s_t:#menas 
      nested_name_list.append(only_name[j])
  return nested_name_list
#end find_nested_macro_def_name

#start proper_definition
def proper_definition(list1,list2,str):
  name_of_macro=str
  defi=list1
  name_of_nested_macro=list2
  j=0
  for j in range(len(list2)):
    start_line='MACRO->['
    start_line=start_line+list2[j]
    start_line=start_line+']'
    end_line='['+list2[j]+']<-'+'MACRO'
    k=0
    remove_index_list=[]
    for k in range(1,len(defi)-1,1):
      if start_line==defi[k]:
        start_line_index=k
        remove_index_list.append(start_line_index)
        if defi[k+1]=='0':
          print("no arg")
        elif defi[k+1]!='0':
          arg_number_index=k+1
          remove_index_list.append(arg_number_index)
          arg_list_index=k+2
          remove_index_list.append(arg_list_index)
      elif end_line==defi[k]:
        end_line_index=k
        remove_index_list.append(end_line_index)

    l=0
    for l in range(len(remove_index_list)):
        index=remove_index_list[l]
        temp=defi[index]
        del defi[index]
        defi.insert(index,'@')
    return defi
#end_proper definition    
#--------------------------------------------end of function definition part-----------------------------------------------
#------------------------------------------------main code-------------------------------------------------------------------  

NEW_DEF_TAB=[]
NEW_NAME_TAB=[]
i=0
for i in range(len(only_name)):
  macro_name=only_name[i]
  temp_def_list=definition(macro_name) #this function will return the definition of macro
  chk=check_nested(temp_def_list,macro_name)#this function will check nested macro definition
  if chk==0:#no nested_definiton
    NEW_DEF_TAB=NEW_DEF_TAB+temp_def_list
    continue
  elif chk==1:#nested definition
    nested_macro_defi_name_list=find_nested_macro_def_name(temp_def_list,macro_name)
                                                                                   #this will find out the name of the macro
                                                                                  #which is inside the main macro definition
    proper_def=proper_definition(temp_def_list,nested_macro_defi_name_list,macro_name)
                                                                          #this function will get the proper definition whcih we will
                                                                           # get in the expended code

    if '@' in proper_def:#this will remove @
     while '@' in proper_def:
        proper_def.remove('@')
    NEW_DEF_TAB=NEW_DEF_TAB+proper_def

#to make the new_name_tab
n=0
for n in range(len(only_name)):
  NaMe=only_name[n]
  NEW_NAME_TAB.append(NaMe)
  line1='MACRO->['+NaMe+']'
  line2='['+NaMe+']<-MACRO'
  m=0
  for m in range(len(NEW_DEF_TAB)):
    if line1==NEW_DEF_TAB[m]:
      NEW_NAME_TAB.append(m)
    elif line2==NEW_DEF_TAB[m]:
      NEW_NAME_TAB.append(m)
