## Aici voi creea mai multe instante cu retele neuronale si futures pe care le voi folosi la main 
import header
## Instance  pentru exel-uri
data_set=None
FFT_exel=None
MFCC_exel=None
Extractor=None
PSD_exel=None
def Delete_All_Content(header=0,data=True,FFT=False,MFCC=False,PSD=False):
    print("Delete All Content")
    global data_set,FFT_exel,MFCC_exel,PSD_exel 
    if data==True:
      data_set.Delete_All(header)
    if FFT==True:  
      FFT_exel.Delete_All(header)
    if MFCC==True:
      MFCC_exel.Delete_All(header)
    if PSD==True:
      PSD_exel.Delete_All(header)

def Initialize():
    global data_set,FFT_exel,MFCC_exel,PSD_exel,Extractor
    print("Initialize variabels")
    data_set=header.Dataset_Function_Manipulation.Manipulation_Data_set("./exel/data_set.xlsx")
    FFT_exel=header.Dataset_Function_Manipulation.Manipulation_Data_set("./exel/FTT.xlsx")
    PSD_exel=header.Dataset_Function_Manipulation.Manipulation_Data_set("./exel/PST.xlsx") 
    MFCC_exel=header.Dataset_Function_Manipulation.Manipulation_Data_set("./exel/MFCC.xlsx")
    Extractor=header.Extract_Features_Augmentation.Features_Augmentation()
    return 0
def Load_data_set_exel():
     global data_set,FFT_exel,MFCC_exel,PSD_exel,Extractor  
     wav_root="./wav_"
     for root,dir,files in header.common_library.os.walk(wav_root):
        for  file in files :
         file_name_split=file.split(",")
         if len(file_name_split)==4:
            ## Inregistrari de la masini 
            content=[wav_root+'/'+file,file_name_split[0],file_name_split[1],file_name_split[2]]
            data_set.Add_Instance(content)
            print(file)
         else:
            content=[wav_root+'/'+file,file_name_split[0],'-',file_name_split[1]]
            data_set.Add_Instance(content)
     data_set.Show_Content()
def Load_FFT_exel():
     global data_set,FFT_exel,MFCC_exel,PSD_exel,Extractor
     FFT_data_augmanted=[]
     data=data_set.Get_Instances()
     data_only_good_instance=[data[i][1:4] for i in range (0,data_set.Get_number_of_instance()) if data[i][3]=='good']
     for i in data:
         if i[3]=='good':
             sample_rate,vehicle_audio=Extractor.read_data(i[0])
             Feature=Extractor.FFT_Futures(vehicle_audio,sample_rate)
             content=[Feature,i[1:4]]
             FFT_data_augmanted.append(content)
             k=0
             print(Feature.shape)
             for j in range(0,15):
                 k+=0.1
                 vehicle_audio_aug=Extractor.addNoise(vehicle_audio,k)
                 Feature=Extractor.FFT_Futures(vehicle_audio_aug,sample_rate)
                 content=[Feature,i[1:4]]
                 FFT_data_augmanted.append(content)
                 vehicle_audio_aug=Extractor.changePitch(vehicle_audio,sample_rate,k)
                 Feature=Extractor.FFT_Futures(vehicle_audio_aug,sample_rate)
                 content=[Feature,i[1:4]]
                 FFT_data_augmanted.append(content)
         if i[3]=='bad':
             sample_rate,vehicle_audio=Extractor.read_data(i[0])
             Feature=Extractor.FFT_Futures(vehicle_audio,sample_rate)
             
             ok=1
             k=0.02
             for j in data_only_good_instance[0:20]:
                 k+=0.01
                 state=j[0:2]
                 state.append("bad")
                 if ok==1:
                     content=[Feature,state]
                     FFT_data_augmanted.append(content)
                     ok==0
                 else:
                      vehicle_audio_aug=Extractor.addNoise(vehicle_audio,k)
                      Feature=Extractor.FFT_Futures(vehicle_audio_aug,sample_rate)
                      content=[Feature,state]
                      FFT_data_augmanted.append(content)
     FFT_data_augmanted=header.common_library.np.array(FFT_data_augmanted)   
     k=1
     Extractor.Set_Colum_Row(625,0)
     for i in FFT_data_augmanted:
         FFT_exel.Add_Instance(i)
         print(f"Pas k={k}")
         #if k==1001:
         #    break
         k+=1
     print("Finish adding element")
     return 0
def Load_MFCC_exel():
     global data_set,FFT_exel,MFCC_exel,PSD_exel,Extractor
     MFCC_data_augmanted=[]
     data=data_set.Get_Instances()
     data_only_good_instance=[data[i][1:4] for i in range (0,data_set.Get_number_of_instance()) if data[i][3]=='good']
     row=40
     colum=0
     for i in data:
         if i[3]=='good':
             sample_rate,vehicle_audio=Extractor.read_data(i[0])
             Feature=Extractor.MFFC_Features(vehicle_audio,sample_rate)
             content=[Feature,i[1:4]]
             MFCC_data_augmanted.append(content)
             k=0
             if colum<Feature.shape[1]:
                 colum=Feature.shape[1]
             for j in range(0,15):
                 k+=0.1
                 vehicle_audio_aug=Extractor.addNoise(vehicle_audio,k)
                 Feature=Extractor.MFFC_Features(vehicle_audio_aug,sample_rate)
                 content=[Feature,i[1:4]]
                 MFCC_data_augmanted.append(content)
                 vehicle_audio_aug=Extractor.changePitch(vehicle_audio,sample_rate,k)
                 Feature=Extractor.MFFC_Features(vehicle_audio_aug,sample_rate)
                 content=[Feature,i[1:4]]
                 MFCC_data_augmanted.append(content)
         if i[3]=='bad':
             sample_rate,vehicle_audio=Extractor.read_data(i[0])
             Feature=Extractor.MFFC_Features(vehicle_audio,sample_rate)
             if colum<Feature.shape[1]:
                 colum=Feature.shape[1]
             ok=1
             k=0.02
             for j in data_only_good_instance[0:20]:
                 k+=0.01
                 state=j[0:2]
                 state.append("bad")
                 if ok==1:
                     content=[Feature,state]
                     MFCC_data_augmanted.append(content)
                     ok==0
                 else:
                      vehicle_audio_aug=Extractor.addNoise(vehicle_audio,k)
                      Feature=Extractor.MFFC_Features(vehicle_audio_aug,sample_rate)
                      content=[Feature,state]
                      MFCC_data_augmanted.append(content)
     MFCC_data_augmanted=header.common_library.np.array(MFCC_data_augmanted)
     print(len(MFCC_data_augmanted))
     print(f"row={row} and colum={colum}")
     Extractor.Set_Colum_Row(row,colum)
     k=1 
     for i in MFCC_data_augmanted:
         i[0]=Extractor.padding_data(i[0])
         print(f"Pass k={k} shape={i[0].shape}")
         k+=1
         MFCC_exel.Add_Instance(i)
     print("Finish adding element")
     return 0
def Load_PSD_exel():
     global data_set,FFT_exel,MFCC_exel,PSD_exel,Extractor
     PSD_data_augmanted=[]
     data=data_set.Get_Instances()
     data_only_good_instance=[data[i][1:4] for i in range (0,data_set.Get_number_of_instance()) if data[i][3]=='good']
     row=0
     colum=0
     for i in data:
         if i[3]=='good':
             sample_rate,vehicle_audio=Extractor.read_data(i[0])
             Feature=Extractor.PSD_Features(vehicle_audio,sample_rate)
             content=[Feature,i[1:4]]
             PSD_data_augmanted.append(content)
             k=0
             if row<Feature.shape[0]:
                 row=Feature.shape[0]
             for j in range(0,15):
                 k+=0.1
                 vehicle_audio_aug=Extractor.addNoise(vehicle_audio,k)
                 Feature=Extractor.PSD_Features(vehicle_audio_aug,sample_rate)
                 content=[Feature,i[1:4]]
                 PSD_data_augmanted.append(content)
                 vehicle_audio_aug=Extractor.changePitch(vehicle_audio,sample_rate,k)
                 Feature=Extractor.PSD_Features(vehicle_audio_aug,sample_rate)
                 content=[Feature,i[1:4]]
                 PSD_data_augmanted.append(content)
         if i[3]=='bad':
             sample_rate,vehicle_audio=Extractor.read_data(i[0])
             Feature=Extractor.PSD_Features(vehicle_audio,sample_rate)
             if row<Feature.shape[0]:
                 row=Feature.shape[0]
             ok=1
             k=0.02
             for j in data_only_good_instance[0:20]:
                 k+=0.01
                 state=j[0:2]
                 state.append("bad")
                 if ok==1:
                     content=[Feature,state]
                     PSD_data_augmanted.append(content)
                     ok==0
                 else:
                      vehicle_audio_aug=Extractor.addNoise(vehicle_audio,k)
                      Feature=Extractor.PSD_Features(vehicle_audio_aug,sample_rate)
                      content=[Feature,state]
                      PSD_data_augmanted.append(content)
     PSD_data_augmanted=header.common_library.np.array(PSD_data_augmanted)
     print(len(PSD_data_augmanted))
     print(f"row={row} and colum={colum}")   
     Extractor.Set_Colum_Row(row,colum)
     k=1 
     for i in PSD_data_augmanted:
         i[0]=Extractor.padding_data(i[0])
         print(f"Pass k={k}")
         k+=1
         PSD_exel.Add_Instance(i)
  
     print("Finish adding element")
     return 0
     


ok_model=input("Do you want to train the model and test ?(Yes/No)")
if ok_model.lower()=="yes":
    print("Train and test models")

if ok_model.lower()=="no":
    ok_exel=input("Do you want to work whit exel ?(Yes/No)")
    if ok_exel.lower()=="yes":
       ok_delete_header=input("Do you want do delete whit header da data? (Yes/No)")
       ok_FFT=input("Do you want to refil de FFT exel again ?(Yes/No)")
       ok_MFCC=input("Do you want to refil de MFCC exel again ?(Yes/No)")
       ok_PSD=input("Do you want to refil de PSD exel again ?(Yes/No)")
       if ok_delete_header.lower()=="yes" :
         if ok_FFT.lower()=="yes":
               Initialize()
               Delete_All_Content(1,True,True,False,False)
               Initialize()
               Load_data_set_exel()
               Load_FFT_exel() 
         if ok_MFCC.lower()=="yes":
               Initialize()
               Delete_All_Content(1,True,False,True,False)
               Initialize()
               Load_data_set_exel()
               Load_MFCC_exel()
         if ok_PSD.lower()=="yes":
               Initialize()
               Delete_All_Content(1,True,False,False,True)
               Initialize()
               Load_data_set_exel()
               Load_PSD_exel()
       else:
          if ok_FFT.lower()=="yes":
               Initialize()
               Delete_All_Content(0,True,True,False,False)
               Load_data_set_exel()
               Load_FFT_exel() 
          if ok_MFCC.lower()=="yes":
               Initialize()
               Delete_All_Content(0,True,False,True,False)
               Load_data_set_exel()
               Load_MFCC_exel()
          if ok_PSD.lower()=="yes":
               Initialize()
               Delete_All_Content(0,True,False,False,True)
               Load_data_set_exel()
               Load_PSD_exel()
    else:
        print("No i do somethig diffrente")