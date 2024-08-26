import header
header.common_library.warnings.filterwarnings("ignore")
data_set=None
FFT_exel=None
MFCC_exel=None
Extractor=None
PSD_exel=None
Diagrams_analisys=None
def Initialize():
    global data_set,FFT_exel,MFCC_exel,PSD_exel,Extractor,Diagrams_analisys
    print("Initialize variabels")
    data_set=header.Dataset_Function_Manipulation.Manipulation_Data_set("./exel/data_set.xlsx")
    FFT_exel=header.Dataset_Function_Manipulation.Manipulation_Data_set("./exel/FTT.xlsx")
    PSD_exel=header.Dataset_Function_Manipulation.Manipulation_Data_set("./exel/PST.xlsx") 
    MFCC_exel=header.Dataset_Function_Manipulation.Manipulation_Data_set("./exel/MFCC.xlsx")
    Extractor=header.Extract_Features_Augmentation.Features_Augmentation()
    Diagrams_analisys=header.Data_Statistics.Data_Statistic()
    return 0
def FFT_PSD_string_convertor(data):
   data_features=[]
   k=1
   for i in range(0,len(data)):
     print(f"Pas i={i}")
     converted_data=[[i] for i in data[i] if i!="['-']"]
     etichet=converted_data[len(converted_data)-1][0][1:len(converted_data[len(converted_data)-1][0])-1]
     instance=eval(etichet)
     all_data=""
     for j in range(0 ,len(converted_data)-1):
          for l in converted_data[j]:
             if l != '[' and l != ']' and l != "'" and l != '"' and l!=' ':
               all_data+=l
     converted_data=all_data[2:len(all_data)-2].split(",")
     vector=[]
     for j in range(0,len(converted_data)-1):
       try:
        vector.append(float(converted_data[j]))
       except ValueError:
          print("Exceptie")
          print(converted_data[j])
          k+=1
     vector=header.common_library.np.array(vector)
     data_features.append([vector,instance])
   print(data_features[1][0])
   print(len(data))
   print(f"Number of exceptions k={k}")
   data_features=header.common_library.np.array(data_features,dtype=object)
   return data_features
         
def MFCC_string_convertor(data):
   data_features=[]
   k=1
   for i in range(0,len(data)):
     print(f"Pas i={i}")
     converted_data=[[i] for i in data[i] if i!="['-']"]
     etichet=converted_data[len(converted_data)-1][0][1:len(converted_data[len(converted_data)-1][0])-1]
     instance=eval(etichet)
     print(instance)
     all_data=""
     for j in range(0 ,len(converted_data)-1):
          for l in converted_data[j]:
             if l != '[' and l != ']' and l != "'" and l != '"' and l!=' ':
               all_data+=l
     converted_data=all_data[2:len(all_data)-2].split("|")
     matrix=[]
     for j in range (0,len(converted_data)):
          one_line=converted_data[j].split(",")
          new_line=[]
          for l in one_line[0:len(one_line)-1]:
              try:
               new_line.append(float(l))
              except ValueError:
                 k+=1
                 print("Exception")
          if (j==len(converted_data)-1):
            new_line.append(0)
            new_line=header.common_library.np.array(new_line)
          else:
            new_line=header.common_library.np.array(new_line)  
          matrix.append(new_line)
     matrix=header.common_library.np.array(matrix) 
     print(matrix.shape)
     data_features.append([matrix,instance])
   print(len(data_features))
   print(f"Number of exeception k={k}")
   data_features=header.common_library.np.array(data_features,dtype=object)
   return data_features

Initialize()
FFT_ok=input("Use FFT features?(Yes/No)")
MFFC_ok=input("Use MFFC features?(Yes/No)")
PSD_ok=input("USE PSD features?(Yes/No)")

features_extraction_method=''
if FFT_ok.lower()=="yes":
    data1=FFT_exel.Get_Instances()
    data=FFT_PSD_string_convertor(data1)
    features_extraction_method="FFT"
elif MFFC_ok.lower()=="yes":
    data1=MFCC_exel.Get_Instances()
    data=MFCC_string_convertor(data1)
    features_extraction_method="MFCC"
elif PSD_ok.lower()=="yes":
     data1=PSD_exel.Get_Instances()
     data=FFT_PSD_string_convertor(data1)
     features_extraction_method="PSD"

Model_CNN_ok=input("Use CNN model?(Yes/No)") 
Model_SVN_ok=input("Use SVM model?(Yes/No)")
Model_FCNN_ok=input("Use FCNN model?(Yes/No)")
Model_RNN_ok=input("Use RNN model?(Yes/No)")
encoded_data,class_index=Extractor.hot_encoding(data)

normal_traing=input("Do you want normal training or nk-fold training?(Yes normal traing /No kfold traning)")
cycles_nkfold=""
ok_normal_traing=False
ok_cycles_nkfold=False
ok_number_of_function=False
timer_start=header.common_library.time.time()
if normal_traing.lower()=="yes":
   ok_normal_traing=True
if normal_traing.lower()=="no":
   ok_normal_traing=False
   cycles_nkfold=input("Do you want cycles in nkfold?(Yes whit more cycles/No no cycles) ")
   if cycles_nkfold.lower()=="yes":
      ok_cycles_nkfold=True
   if cycles_nkfold.lower()=="no":
      ok_cycles_nkfold=False
number_of_function=input("Do you want one lost function or more?(Yes whit multi function/No one function)")
if number_of_function.lower()=="yes":
   ok_number_of_function=True
if number_of_function.lower()=="no":
   ok_number_of_function=False
if Model_CNN_ok.lower()=="yes":
   Exemplu=header.CNN.CNN(class_index,encoded_data,Diagrams_analisys,features_extraction_method)
   if ok_normal_traing==True : 
      Exemplu.Training(ok_number_of_function) 
   if ok_normal_traing==False:
      Exemplu.Nk_Fold_Traning(ok_number_of_function,ok_cycles_nkfold)
   Exemplu.Test()
   print(f"Model_CNN whit {features_extraction_method} features extraction method")
elif Model_SVN_ok.lower()=="yes":
   #encoded_data=Extractor.random_SVM(encoded_data,class_index,encoded_data.shape[0])
   Exemplu=header.SVN.SVN(class_index,encoded_data,Diagrams_analisys,features_extraction_method)
   if ok_normal_traing==True : 
      Exemplu.Training(features_extraction_method) 
   else: 
      Exemplu.Nk_Fold_Traning(features_extraction_method,ok_cycles_nkfold)
   Exemplu.Test()
   print(f"Model_SVN whit {features_extraction_method} features extraction method")
elif Model_FCNN_ok.lower()=="yes":
   Exemplu=header.FCNN.FCNN(class_index,encoded_data,Diagrams_analisys,features_extraction_method)
   if ok_normal_traing==True : 
      Exemplu.Training(ok_number_of_function) 
   else: 
      Exemplu.Nk_Fold_Traning(ok_number_of_function,ok_cycles_nkfold)
   Exemplu.Test()
   print(f"Model_FCNN whit {features_extraction_method}")
elif Model_RNN_ok.lower()=="yes":
   Exemplu=header.RNN.RNN(class_index,encoded_data,Diagrams_analisys,features_extraction_method)
   if ok_normal_traing==True : 
      Exemplu.Training(ok_number_of_function) 
   else: 
      Exemplu.Nk_Fold_Traning(ok_number_of_function,ok_cycles_nkfold)
   Exemplu.Test()
   print(f"Model_RNN whit {features_extraction_method}")
timer_end=header.common_library.time.time()

print(f"Time of execution is :{timer_end-timer_start}")









