##Input Format##
#Input is a Relational algebric expression in the form of string which contains symbols according to attached file symbols.jpg
#a single relational algebric expression should be enclosed by [ ].
#all the words are in the input string should seperated by single blank space(" ") except the condition.
#In case of condition and list of attributes, all the words should be contiguous i.e. they are written without space.
#For example: "E_SAL>10000" is correct format while "E_SAL > 10000" is incorrect.
#For example: "PROJ E_ID,E_NAME (EMP)" is correct format and "PROJ E_ID , E_NAME (EMP)" is incorrect.

#following are some examples whose output are attached in the form of screenshot picture.
#Just copy the input string and paste in the variable "inpt".

#Input1= "[ PROJ C_SAL UNION E_SAL ( CUSTOMER JOIN C_SAL<E_SAL EMPLOYEE ) ]"
#Input2= "[ [ PROJ E_AGE ( PROJ E_ID,E_AGE ( EMPLOYEE ) ) ] UNION [ SIGMA E_AGE>20 ( SIGMA E_ID<25 ( [ SIGMA E_MARKS>70 ^ E_PER>75 ( EMPLOYEE ) ] ) ) ] ]"
#Input3= "[ [ SIGMA C_ID>24 ^ C_NO>900 ( [ PROJ C_ID ( PROJ C_NAME,C_ID ( CUSTOMER ) ) ] ) ] JOIN C_ID<A_ID [ SIGMA B_NO<500 ( SIGMA A_NO>1200 ( ACCOUNT ) ) ] ]"

inpt="[ [ PROJ E_AGE ( PROJ E_ID,E_AGE ( EMPLOYEE ) ) ] UNION [ SIGMA E_AGE>20 ( SIGMA E_ID<25 ( [ SIGMA E_MARKS>70 ^ E_PER>75 ( EMPLOYEE ) ] ) ) ] ]"
represent_dict={} # for input containing expressions
dict_depend ={}  # contains list of dependent expressions
dict_equivalent ={}  # list of equivalent expressions 

inpt=inpt.split()
stack=[]
represent_dict={}
#print(inpt)
ct=0
for i in range(len(inpt)):
    if(inpt[i]==']'):
        cv=""
        c=0
        while(stack[len(stack)-1]!='['):
            cv=stack.pop()+" "+cv
        stack.pop()
        if c!=1:
            stack.append("EXP"+str(ct))
            represent_dict["EXP"+str(ct)]=cv[:-1]
            #print("EXP"+str(ct),"=",cv)
            ct+=1
        #else:
            #stack.append("( "+cv+" )")
            
    else:
        stack.append(inpt[i])
    #print(stack)
print("Following are the expressions:")
for i in represent_dict:
  print(i,"=",represent_dict[i])


for i in represent_dict:
  temp = represent_dict[i].split()
  #print(temp)
  emp_list=[]
  for j in temp:
    if 'EXP' in j:
      emp_list.append(j)

  dict_depend[i]=emp_list

  
#print(dict_depend)

  

###############################################################################################################################
#Function for Equivalance Rule-12

def f12(query):
  cond_check = query.split()
  #print(cond_check)
  out_list = [query]
  if('UNION' in cond_check):
      out_str= "PROJ "+cond_check[1]+" ( "+cond_check[3]+" ) UNION "+"PROJ "+cond_check[1]+" ( "+cond_check[5]+" )"
      out_list.append(out_str)
  return out_list

#Function for Equivalance Rule-11
def f11(query):
  cond_check = query.split()
  #print(cond_check)
  out_list = [query]
  out_str= "SIGMA "+cond_check[1]+" ( "+cond_check[3]+" ) UNION "+"SIGMA "+cond_check[1]+" ( "+cond_check[5]+" )"
  out_list.append(out_str)
  return out_list


#Function for Equivalance Rule-10
def f10(query):
  cond_check = query.split()
  #print(cond_check)
  out_list = [query]
  if('-' not in cond_check):
      if(cond_check[1]=='UNION' or cond_check[1]=='INTERSECTION'):
          out_str="( "+cond_check[0]+" "+cond_check[1]+" "+cond_check[3]+" ) "+cond_check[1]+" "+cond_check[5]
      elif(cond_check[2]=='UNION' or cond_check[2]=='INTERSECTION'):
          out_str=cond_check[1]+" "+cond_check[2]+" ( "+cond_check[3]+" "+cond_check[2]+" "+cond_check[6]+" )"
      out_list.append(out_str)
  return out_list



#Function for Equivalance Rule-9
def f9(query):
  cond_check = query.split()
  #print(cond_check)
  out_list = [query]
  if('-' not in cond_check):
      out_str= cond_check[2]+" "+cond_check[1]+" "+cond_check[0]
      out_list.append(out_str)
  return out_list



#Function for Equivalance Rule-8
def f8(query):
  cond_check = query.split()
  #print(cond_check)
  out_list = [query]
  out_str= "( PROJ "+cond_check[1]+" ( "+cond_check[5]+" ) ) JOIN "+cond_check[7]+" ( PROJ "+cond_check[3]+" ( "+cond_check[8]+" ) )"
  out_list.append(out_str)
  return out_list



#Function for Equivalance Rule-7
def f7(query):
  cond_check = query.split()
  #print(cond_check)
  out_list = [query]
  print("RULE-7")
  out_str="("+" SIGMA "+cond_check[1]+" ( "+cond_check[5]+" ) )"+" JOIN "+cond_check[7]+" ( SIGMA "+cond_check[3]+" ( "+cond_check[8]+" ) )"
  out_list.append(out_str)
  return out_list



#Function for Equivalance Rule-6
def f6(query):
  cond_check = query.split()
  #print(cond_check)
  out_list = [query]
  if('^' not in cond_check):    #Rule-6a
      print("RULE-6a")
      if(cond_check[1]=='JOIN'):
          out_str="( "+cond_check[0]+" JOIN "+cond_check[3]+" ) "+"JOIN "+cond_check[5]
      elif(cond_check[2]=='JOIN'):
          out_str=cond_check[1]+" JOIN "+"( "+cond_check[3]+" JOIN "+cond_check[6]+" )"
      
  else:                   #Rule-6b
      print("RULE-6b")
      out_str=cond_check[1]+" JOIN "+cond_check[3]+" ^ "+cond_check[9]+" ( "+cond_check[4]+" JOIN "+cond_check[7]+" "+cond_check[10]+" )"
  out_list.append(out_str)
  return out_list



#Function for Equivalance Rule-5
def f5(query):
  cond_check = query.split()
  #print(cond_check)
  out_list = [query]
  cond_check[len(cond_check)-1],cond_check[0]=cond_check[0],cond_check[len(cond_check)-1]
  out_str = ""
  for i in cond_check:
      out_str+=i+" "
  out_str=out_str[:len(out_str)-1]
  out_list.append(out_str)
  return out_list



#Function for Equivalance Rule-4
def f4(query):
  cond_check = query.split()
  #print(cond_check)
  out_list = [query]
  if('*' in cond_check):     #Rule-4a
      print("RULE-4a")
      out_str = cond_check[3]+' JOIN '+cond_check[1]+" "+cond_check[5]
  elif('JOIN' in cond_check):  #Rule-4b
      print("RULE-4b")
      out_str = cond_check[3]+' JOIN '+cond_check[1]+" ^ "+cond_check[5]+cond_check[6]
  out_list.append(out_str)
  return out_list



#Function for Equivalance Rule-3
def f3(query):
  cond_check = query.split()
  out_list = [query]
  #print(cond_check)
  for i in range(len(cond_check)-1,-1,-1):
    if(cond_check[i]!=')'):
      expression = cond_check[i]
      break
  out_str = cond_check[0]+" "+cond_check[1]+" ( "+expression+" )"
  out_list.append(out_str)
  return out_list



#Function for Equivalance Rule-2
def f2(query):
  cond_check = query.split()
  out_list = [query]
  #print(cond_check)
  out_str = cond_check[0]+" "+cond_check[4]+" ("+" SIGMA "+cond_check[1]+" ( "+cond_check[6]+" )"+" )"
  out_list.append(out_str)
  return out_list


#Function for Equivalance Rule-1
def f1(query):
  cond_check = query.split()
  #print(cond_check)
  out_list = [query]
  out_str = cond_check[0]+" "+cond_check[1]+" ( "+"SIGMA "+cond_check[3]+" ( "+cond_check[5]+" )"+" )"
  out_list.append(out_str)
  return out_list


########################################################################################################################################
print()
print("Following Rules are used:")
for i in represent_dict:
  query = represent_dict[i]
  cond_check = query.split()
  if('SIGMA' in cond_check and '^' in cond_check and 'JOIN' in cond_check):
    #print("RULE-7")
    temp_out = f7(query)
    dict_equivalent[i]=temp_out
  elif('PROJ' in cond_check and 'UNION' in cond_check and 'JOIN' in cond_check):
    print("RULE-8")
    temp_out = f8(query)
    dict_equivalent[i]=temp_out
  elif(cond_check[0]=='SIGMA' and cond_check[2]=='^'):
    print("RULE-1")
    temp_out = f1(query)
    dict_equivalent[i]=temp_out
  elif(cond_check[0]=='SIGMA' and cond_check[3]=='SIGMA'):
    print("RULE-2")
    temp_out = f2(query)
    dict_equivalent[i]=temp_out
  elif(cond_check[0]=='PROJ' and cond_check[3]=='PROJ'):
    print("RULE-3")
    temp_out = f3(query)
    dict_equivalent[i]=temp_out
  elif(cond_check[0]=='SIGMA' and (cond_check[4]=='*' or cond_check[4]=='JOIN')):
    #print("RULE-4")
    temp_out = f4(query)
    dict_equivalent[i]=temp_out
  elif(cond_check[1]=='JOIN' and cond_check.count('JOIN')==1):
    print("RULE-5")
    temp_out = f5(query)
    dict_equivalent[i]=temp_out
  elif(cond_check.count('JOIN') > 1):
    #print("RULE-6")
    temp_out = f6(query)
    dict_equivalent[i]=temp_out
  elif(('UNION' in cond_check and cond_check.count('UNION')>1) or ('INTERSECTION' in cond_check and cond_check.count('INTERSECTION')>1) or ('-' in cond_check and cond_check.count('-')>1)):
    print("RULE-10")
    temp_out = f10(query)
    dict_equivalent[i]=temp_out
  elif(cond_check[0]=='SIGMA' and ('UNION' in cond_check or 'INTERSECTION' in cond_check or '-' in cond_check)):
    print("RULE-11")
    temp_out = f11(query)
    dict_equivalent[i]=temp_out
  elif(cond_check[0]=='PROJ' and ('UNION' in cond_check or 'INTERSECTION' in cond_check or '-' in cond_check)):
    print("RULE-12")
    temp_out = f12(query)
    dict_equivalent[i]=temp_out
  elif(('UNION' in cond_check and cond_check.count('UNION')==1) or ('INTERSECTION' in cond_check and cond_check.count('INTERSECTION')==1) or ('-' in cond_check and cond_check.count('-')==1)):
    print("RULE-9")
    temp_out = f9(query)
    dict_equivalent[i]=temp_out
  
    

    
for i in dict_equivalent:
  #print(i,dict_equivalent[i] )
  pass

  
def Make_Euivalant(LHS):
  for i in dict_depend[LHS]:
    if(len(dict_depend[i])!=0):
      Make_Euivalant(i)
    lis_updated=[]
    for j in dict_equivalent[LHS]:
      for k in dict_equivalent[i]:
        lis_updated.append(j.replace(i,k))
    dict_equivalent[LHS]=lis_updated
  #return dict_equivalent
#print('EXP'+str(len(represent_dict)-1))

Make_Euivalant('EXP'+str(len(represent_dict)-1))
print()
print("TOTAL NO. OF EUIVALANT EXPRESSIONS ARE :",len(dict_equivalent['EXP'+str(len(represent_dict)-1)]))
print()
zx=0
for j in dict_equivalent['EXP'+str(len(represent_dict)-1)]:
  zx+=1
  #print(dict_equivalent[j])
  print("["+str(zx)+"].",j)
  print()
