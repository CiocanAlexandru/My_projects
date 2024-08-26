import header 
Extractor=header.Extract_Features_Augmentation.Features_Augmentation()
features=header.common_library.sys.argv[1]
model=header.common_library.sys.argv[2]
file=header.common_library.sys.argv[3]
model_type=header.common_library.sys.argv[4]
path_file="../UploadFile/"+file
sample_rate,audio=Extractor.read_data(path_file)
index_class = {v: k for k, v in Extractor.index_class_from_file("../../exel/index.txt").items()}
if features.lower()=="fft":
    features_extraction=Extractor.FFT_Futures(audio,sample_rate)
    features_extraction=features_extraction[:-1]
    features_extraction=features_extraction.reshape(1,624)
if features.lower()=="mfcc":
    features_extraction=Extractor.MFFC_Features(audio,sample_rate)
    dimensiune_dorita = 3035
    padding_zero = max(0, dimensiune_dorita - features_extraction.shape[1])
    features_extraction= header.common_library.np.pad(features_extraction, ((0, 0), (0, padding_zero)), 'constant', constant_values=(0, 0))
    features_extraction=features_extraction.reshape((1,40,3035))
    ##print(features_extraction.shape)
if features.lower()=="psd":
   features_extraction=Extractor.PSD_Features(audio,sample_rate)
   padding_zero = max(0, 3034 - features_extraction.shape[0])
   features_extraction= header.common_library.np.pad(features_extraction, (0, padding_zero), 'constant', constant_values=(0, 0))
   print(features_extraction.shape)
   features_extraction=features_extraction.reshape(1,3034)
result=""
if model_type.lower()!="svm":
   model_extraction=header.common_library.load_model(model)
   prediction=model_extraction.predict(features_extraction)
   top_3_indices = header.common_library.np.argsort(prediction[0])[-3:]
   for i in top_3_indices:
       result+=index_class[i]+","
   print(result)
else:
   print("Something else")

