import common_library
class Features_Augmentation:

    def __init__(self):
       self.new_data=None
       self.max_colum=None
       self.max_row=None

    def read_data(self,vehicle_audio):
        sample_rate , audio_data=common_library.read(vehicle_audio)
        audio_data=self.normelized_data(audio_data)
        return sample_rate,audio_data 
    
    def normelized_data(self,data): 
      if data.shape==(data.shape[0],):
        max=common_library.np.max(data)
        data=data/max 
        return common_library.np.array(data)
      if data.shape[1]==2:
        first_channel=[i[0] for i in  data]
        second_channel=[i[1] for i in  data]
        first_channel_norm=first_channel/common_library.np.max(common_library.np.abs(first_channel))
        second_channel_norm=second_channel/common_library.np.max(common_library.np.abs(second_channel))
        data=(first_channel_norm+second_channel_norm)/2
        return common_library.np.array(data)
    def hot_encoding(self,data):
       only_class={data[i][1][j] for i in range(0,len(data)) for j in range(0,len(data[i][1]))}
       only_class=list(only_class)
       only_class_index=[(only_class[i-1],i) for i in range(1,len(only_class)+1)]
       m=len(only_class_index)
       only_class_index={ only_class_index[i][0]:only_class_index[i][1] for i in range(0,len(only_class_index))}
       print(f"Set of classes :{only_class} \n")  
       print(f"Set of clases whit indexes {only_class_index}\n")
       new_data=data
       n=len(data)
       for i in range(0,n):
          new_content=[0 for i in range(0,m+1)]
          for  j  in data[i][1]:
             new_content[only_class_index[j]]=1
          new_data[i][1]=new_content
       try:
          open("./exel/index.txt","w").close()
          f=open("./exel/index.txt","w")
          f.write(str(only_class_index))       
       except ValueError:
          print("File dosen't exist")
       return new_data,only_class_index
    
    def random_SVM(self,data=None,only_class_index=None,number=2):
     good_data=[i for i in data  if i[1][only_class_index['good']]==1]
     common_library.random.shuffle(good_data)
     bad_data=[i for i in data  if i[1][only_class_index['bad']]==1]
     common_library.random.shuffle(bad_data)
     random_data=good_data[0:number//2]
     for i in bad_data[0:number//2]:
        random_data.append(i)
     common_library.random.shuffle(random_data)
     return common_library.np.array(random_data)
    
    def index_class_from_file(self,file_path):
       #file_path="./exel/index.txt"
       file=open(file_path,"r")
       only_class_index= common_library.ast.literal_eval(file.read())
       return only_class_index
    
    def DR_MaxInt_Var(self,vehicle_audio):
      vehicle_audio = common_library.np.abs(vehicle_audio)
      vehicle_audio = sorted(vehicle_audio)
      background = common_library.np.mean(vehicle_audio[1:1000])
      max_intensity = common_library.np.mean(vehicle_audio[-20000:-1])
      dynamic_range = max_intensity - background
      variance = common_library.np.var(vehicle_audio)
      return dynamic_range, max_intensity * 10, variance * 100
    def FFT_Matrix(self,freq, spectrum):
        spectrum = common_library.np.abs(spectrum)
        chunk_spectrum = common_library.np.zeros(25)
        chunk_matrix = common_library.np.zeros([25, 25])
        i = 0
        while i < len(chunk_spectrum):
            begin_value = i / 50
            end_value = (i + 1) / 50
            begin_index = min(range(len(freq)), key=lambda i: abs(freq[i] - begin_value))
            end_index = min(range(len(freq)), key=lambda i: abs(freq[i] - end_value))
            sorted_chunk = sorted(spectrum[begin_index:end_index])
            sorted_chunk = common_library.np.asarray(sorted_chunk)
            chunk_value = common_library.np.mean(sorted_chunk[-200:-1])
            chunk_spectrum[i] = chunk_value
            i += 1
        for i in range(len(chunk_spectrum)):
            for j in range(len(chunk_spectrum)):
                chunk_matrix[i, j] = chunk_spectrum[i] / chunk_spectrum[j]
        chunk_matrix = chunk_matrix.reshape(25 * 25)
        return chunk_matrix
    
    def Set_Colum_Row(self,max_row,max_colum):
       self.max_colum=max_colum
       self.max_row=max_row

    def padding_data(self,data):
        if data.shape==(data.shape[0],):
           print("Vector")
           self.new_data=[0 for i in range(0,self.max_row)]
           for i in range(0,len(data)):
               self.new_data[i]=data[i]   
        else:
            print(f"Shape[0]= {data.shape[0]} and row={self.max_row} Shape[1]={data.shape[1]} and colum={self.max_colum}")
            if data.shape[0]==self.max_row and data.shape[1]==self.max_colum :
               return data
            self.new_data=common_library.np.zeros((self.max_row,self.max_colum))
            self.new_data[:data.shape[0],:data.shape[1]]=data
            print(self.new_data)
        return common_library.np.array(self.new_data)
    
    def addNoise(self,vehicle_audio, noise_factor):
        noise = common_library.np.random.randn(len(vehicle_audio))
        print(noise)
        augmented_data = vehicle_audio + noise_factor * noise
        augmented_data = augmented_data.astype(type(vehicle_audio[0]))
        return augmented_data


    def changePitch(self,vehicle_audio,sample_rate,pitch_factor):
       return common_library.librosa.effects.pitch_shift(vehicle_audio.astype('float'), sr=sample_rate, n_steps=pitch_factor)
     
    def MFFC_Features(self,vehicle_audio,sample_rate):
        mffc=common_library.librosa.feature.mfcc(y=vehicle_audio,sr=sample_rate,n_mfcc=40)
        mffc=common_library.librosa.util.normalize(mffc,axis=None)
        return common_library.np.array(mffc)
    
    def PSD_Features(self,vehicle_audio,sample_rate):
        spectrogram=common_library.librosa.feature.melspectrogram(y=vehicle_audio,sr=sample_rate)
        PSD1=common_library.np.sum(spectrogram,axis=0)
        PSD1=self.normelized_data(PSD1)
        return common_library.np.array(PSD1)
    
    def FFT_Futures(self,vehicle_audio,sample_rate):     
        spect=common_library.np.fft.fft(vehicle_audio, n=sample_rate)
        freq = common_library.np.abs(common_library.np.fft.fftfreq(len(spect)))
        data=self.FFT_Matrix(freq,spect)
        return common_library.np.array(data)
    



 
    

     
