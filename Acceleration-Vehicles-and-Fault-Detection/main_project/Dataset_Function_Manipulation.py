import common_library
class Manipulation_Data_set:
    def __init__(self,file_name): #Merge
        exel_files= ["./exel/data_set.xlsx","./exel/FTT.xlsx","./exel/PST.xlsx","./exel/MFCC.xlsx"]
        if common_library.os.path.exists(file_name):
            print(f"\n Initialize Data_set:{file_name}")
            self.ok=1
        else:
            print("Nu esixta")
            self.ok=0
        if self.ok==1:
            self.file_name=file_name
            self.info=common_library.pd.read_excel(file_name,engine="openpyxl")
        if (self.ok==1 and self.file_name=="./exel/data_set.xlsx"):
            print(f"\n File is empty :{file_name}")
            print(common_library.os.path.getsize(self.file_name))
            print(common_library.os.stat(self.file_name).st_size)
            if  len(self.info)==0:
                 print(f"\n Header added :{file_name}")  
                 self.info ["Root"]=None
                 self.info ["Tip"]=None
                 self.info ["Brand"]=None
                 self.info ["State"]=None
                 self.info.to_excel(file_name,index=False,header=True)
        if (self.ok==1 and self.file_name=="./exel/MFCC.xlsx"):
            print(f"\n File is empty :{file_name}")
            print(common_library.os.path.getsize(self.file_name))
            print(common_library.os.stat(self.file_name).st_size)
            if  len(self.info)==0: 
                 print(f"\n Header added :{file_name}")
                 for i in range(100):
                      self.info["Row"+str(i)]=None    
                 self.info ["Tip/Brand/State"]=None
                 self.info.to_excel(file_name,index=False,header=True)
        if (self.ok==1 and len([ i  for i in exel_files[1:3] if self.file_name==i  ]))==1:
            print(f"\n Header added :{file_name}") ## Adauga coloane pentru nr si future
            print(common_library.os.path.getsize(self.file_name))
            print(common_library.os.stat(self.file_name).st_size)
            if len(self.info)==0:
                    for i in range(10):
                      self.info["Row"+str(i)]=None    
                    self.info ["Tip/Brand/State"]=None
                    self.info.to_excel(file_name,index=False,header=True)
        if len([ i  for i in exel_files[0:4] if self.file_name==i  ])==0:
           self.ok=0
                
    def Delete_All(self,header=0):  
        if (self.ok==1):
          if (header==0):
            self.info=self.info.iloc[0:0,:]
            self.info.to_excel(self.file_name,index=False,header=True)
          else:
            self.info=self.info.iloc[0:0,0:0]
            self.info.to_excel(self.file_name,index=False,header=True)
        else:
            print("Operation not working")
    def Delete_Instance(self,number): 
        if(self.ok==1):
          self.info=self.info.drop(number)
          self.info.to_excel(self.file_name,index=False,header=True)
        else:
            print("Operation not working")
    def Add_Instance (self,Info): 
        if(self.ok==1):
         new_Info=[]
         max_number_of_caracters=32767
         if (type(Info[0]) is str)==True:
                 print("Data set!!")
                 self.info.loc[len(self.info)] = Info
                 self.info.to_excel(self.file_name, index=False, engine="openpyxl", header=True)
         elif Info[0].shape[0]!=40:
                 print("FFT sau PSD")
                 new_form=''
                 for i in Info[0]:
                     new_form+=str(i)
                     new_form+=','
                 if (len(new_form)-1)%max_number_of_caracters==0:
                     k=(len(new_form)-1)//max_number_of_caracters
                 else :
                     k=(len(new_form)-1)//max_number_of_caracters+1
                 for i in range(k):
                     new_Info.append(new_form[(max_number_of_caracters*i):(max_number_of_caracters*(i+1)+1)])
                 if (len(new_Info)-1)<11:
                     for i in range(len(new_Info)-1,9):
                         new_Info.append(['-'])
                 new_Info.append(Info[1])
                 print(new_Info)
                 print(len(new_Info))
                 self.info.loc[len(self.info)] = new_Info
                 self.info.to_excel(self.file_name, index=False, engine="openpyxl", header=True)
         elif Info[0].shape[0]==40:
                 print("MFCC")
                 new_form=''
                 for i in Info[0]:
                     for j in i :
                         new_form+=str(j)
                         new_form+=','
                     new_form+='|'      
                 if (len(new_form)-1)%max_number_of_caracters==0:
                     k=(len(new_form)-1)//max_number_of_caracters
                 else :
                     k=(len(new_form)-1)//max_number_of_caracters+1
                 for i in range(k):
                     new_Info.append(new_form[(max_number_of_caracters*i):(max_number_of_caracters*(i+1)+1)])
                 if len(new_Info)-1<101:
                     for i in range(len(new_Info)-1,99):
                         new_Info.append(['-'])
                 new_Info.append(Info[1])
                 self.info.loc[len(self.info)] = new_Info
                 self.info.to_excel(self.file_name, index=False, engine="openpyxl", header=True)
        else:
            print("Operation not working")
    def Show_Content (self): 
        if(self.ok==1):
         print (self.info)
        else:
          print("Operation not working")
    def Get_Instances(self): 
        if(self.ok==1):
          return [self.info.iloc[i].to_list() for i in range (0,len(self.info))]
        return "Operation not working"
    def Get_One_Instance(self,number): 
         if(self.ok==1):
           return self.info.iloc[number].to_list()
         return "Operation not working"
    def Get_number_of_instance(self): 
        return len(self.info)-2 
    
    def Get_DataFrame(self):
        return self.info
