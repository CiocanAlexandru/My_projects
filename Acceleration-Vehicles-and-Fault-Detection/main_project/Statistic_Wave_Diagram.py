## Python script for diagrams wave modified wave data set distribution 
import header
data_set_exel=header.Dataset_Function_Manipulation.Manipulation_Data_set("./exel/data_set.xlsx")
data_statistics=header.Data_Statistics.Data_Statistic(data_set_exel)
colums_name=["Tip","Brand","State"]
extractor=header.Extract_Features_Augmentation.Features_Augmentation()
def Distribution_Graf():
  global data_set_exel,data_statistics,colums_name
  for i in colums_name:
   data_statistics.Dsitribution_Data_Base(i)
def Number_of_Instances():
   global data_set_exel,data_statistics,colums_name
   for i in colums_name:
    data_statistics.Number_of_Instance(i)
def Print_Waw_And_Augmanted():
    global data_set_exel,data_statistics,colums_name,extractor
    random_number=header.common_library.np.random.randint(1,data_set_exel.Get_number_of_instance()-1)
    one_row=data_set_exel.Get_One_Instance(random_number)
    name=""
    for i in range(1,len(one_row)):
      if one_row[i]!="-":
       name+=one_row[i]
       name+=' '
    sample_rate,audio_data=extractor.read_data(one_row[0])
    data_statistics.Wav_Frame(audio_data,sample_rate,name)
    name1=name+"modified addnoise"
    audio_data_modified=extractor.addNoise(audio_data,0.05)
    data_statistics.Wav_Frame(audio_data_modified,sample_rate,name1)
    name2=name+"modified changePitch"
    audio_data_modified=extractor.changePitch(audio_data,sample_rate,0.05)
    data_statistics.Wav_Frame(audio_data_modified,sample_rate,name2)
    print(f"Instance whit number={random_number}and row content is {one_row}")

def Print_FFT_Tranformation():
   global data_set_exel,data_statistics,colums_name,extractor
   random_number=header.common_library.np.random.randint(1,data_set_exel.Get_number_of_instance()-1)
   one_row=data_set_exel.Get_One_Instance(random_number)
   name=""
   for i in range(1,len(one_row)):
      if one_row[i]!="-":
       name+=one_row[i]
       name+=' '
   sample_rate,audio_data=extractor.read_data(one_row[0])
   features=extractor.FFT_Futures(audio_data,sample_rate)
   data_statistics.Diagram_FTT(features)
   return 0

def Print_MFCC_Tranformation():
   global data_set_exel,data_statistics,colums_name,extractor
   random_number=header.common_library.np.random.randint(1,data_set_exel.Get_number_of_instance()-1)
   one_row=data_set_exel.Get_One_Instance(random_number)
   name=""
   for i in range(1,len(one_row)):
      if one_row[i]!="-":
       name+=one_row[i]
       name+=' '
   sample_rate,audio_data=extractor.read_data(one_row[0])
   features=extractor.MFFC_Features(audio_data,sample_rate)
   data_statistics.Diagram_MFCC(features)
   return 0

def Print_PSD_Tranformation():
   global data_set_exel,data_statistics,colums_name,extractor
   random_number=header.common_library.np.random.randint(1,data_set_exel.Get_number_of_instance()-1)
   one_row=data_set_exel.Get_One_Instance(random_number)
   name=""
   for i in range(1,len(one_row)):
      if one_row[i]!="-":
       name+=one_row[i]
       name+=' '
   sample_rate,audio_data=extractor.read_data(one_row[0])
   features=extractor.PSD_Features(audio_data,sample_rate)
   data_statistics.Diagram_PSD(features)
   return 0

ok_number_of_instance=input("Do you want who many instance are for every class?(Yes/No)")
ok_wav_frame=input("Do you want to show you some audio wave diagrams ?(Yes/No)")
ok_distribution_graf=input("Doy you want some distribution ghaps?(Yes/No)")
ok_transformation=input("Do you want diagram whit all transformation?(Yes/No)")
if ok_number_of_instance.lower()=="yes":
   Number_of_Instances()
   ok_wav_frame="no"
   ok_distribution_graf="no"
if ok_wav_frame.lower()=="yes":
   Print_Waw_And_Augmanted()
   ok_distribution_graf="no"
if ok_distribution_graf.lower()=="yes":
   Distribution_Graf()
if ok_transformation.lower()=="yes":
   Print_FFT_Tranformation()
   Print_PSD_Tranformation()
   Print_MFCC_Tranformation()