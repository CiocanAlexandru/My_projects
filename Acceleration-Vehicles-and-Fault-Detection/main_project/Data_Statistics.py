import common_library

class Data_Statistic:
    def __init__(self,data=None):
        if(data!=None):
          self.data_frame=data.Get_DataFrame()
          self.data=data  ## Data Manipulation object
        else:
           print("For models Diagrams") 
    def Number_of_Instance(self,info):
        if (self.data!=None):
            print(f"Number of instances {info}= {self.data_frame[info].count()}")
            print("Now for every instance in particular base on classes:")
            unique_class={i:0 for i in self.data_frame[info]}
            for i in self.data_frame[info]:
               unique_class[i]+=1
            for key,value in unique_class.items():
               print(f"For key= {key} we have: {value} of instances")
        else:
            print("Operation Not working")
    def Dsitribution_Data_Base(self,info):
        if (self.data!=None):
            common_library.plt.style.use('seaborn')
            common_library.sns.displot(self.data_frame,x=info,height=4, aspect=2)
            common_library.plt.xticks(rotation=45)
            common_library.plt.subplots_adjust(bottom=0.2)
            common_library.plt.savefig("./DiagramsWav/Distribution dataset by "+info+".jpg",format='jpg')
            common_library.plt.show()
            
        else:
            print("Operation not working")

    def Diagram_FTT(self,info):
       path="./DiagramsWav/FFT_Transformation.jpg"
       common_library.plt.figure(figsize=(10, 6))
       common_library.plt.plot(common_library.np.abs(info))
       common_library.plt.title('Transformare FFT')
       common_library.plt.xlabel('Frecvență')
       common_library.plt.ylabel('Magnitudine')
       common_library.plt.savefig(path,format='jpg')
       common_library.plt.show()
       return 0
    
    def Diagram_PSD(self,info):
       path="./DiagramsWav/PSD_Transformation.jpg"
       common_library.plt.figure(figsize=(10, 6))
       common_library.plt.plot(common_library.np.abs(info))
       common_library.plt.title('Transformare PSD')
       common_library.plt.xlabel('Frecvență')
       common_library.plt.ylabel('Magnitudine')
       common_library.plt.savefig(path,format='jpg')
       common_library.plt.show()
       return 0
    
    def Diagram_MFCC(self,info):
       path="./DiagramsWav/MFCC_Transformation.jpg"
       common_library.plt.figure(figsize=(10, 6))
       common_library.plt.plot(common_library.np.mean(info,axis=0))
       common_library.plt.title('Transformare MFCC')
       common_library.plt.xlabel('Cadru Temporal')
       common_library.plt.ylabel('Magnitudine Medie a Coeficienților MFCC')
       common_library.plt.savefig(path,format='jpg')
       common_library.plt.show()
       return 0

    def Data_Frame_Diagram_WAV(self,data_frame,sample_rate,file_name,modified=None):
        if (self.data!=None):
            if (modified==None):
             common_library.librosa.display.waveshow(data_frame, sr=sample_rate)
             common_library.plt.title('Waveform for '+file_name)
             common_library.plt.xlabel('Time (s)')
             common_library.plt.ylabel('Amplitude')
             common_library.plt.show()
            else:
             common_library.librosa.display.waveshow(data_frame, sr=sample_rate)
             common_library.plt.title('Waveform for '+file_name+' modified')
             common_library.plt.xlabel('Time (s)')
             common_library.plt.ylabel('Amplitude')
             common_library.plt.show()  
        else:
            print("Operation not working")
    def Wav_Frame(self,audio_data=None,sample_rate=None,name=None):
        if (self.data!=None):
           common_library.librosa.display.waveshow(audio_data, sr=sample_rate)
           common_library.plt.title(name)
           common_library.plt.xlabel('Time (s)')
           common_library.plt.ylabel('Amplitude')
           common_library.plt.savefig('./DiagramsWav/'+name+".jpg",format='jpg')
           common_library.plt.show()
        else:
           print("Operation not working!!")
    def Train_confusion_matrix(self,content,title,test):
       path="./Diagrams_Accuracy_Loss/"
       common_library.plt.figure(figsize=(8, 6))
       common_library.sns.heatmap(content, annot=True, fmt='g', cmap='Blues',
                                       xticklabels=common_library.np.unique(test),
                                       yticklabels=common_library.np.unique(test))
       common_library.plt.xlabel('Predicted labels')
       common_library.plt.ylabel('True labels')
       common_library.plt.title(title)
       save=path+"Normal_Training_"+title+".jpg"
       common_library.plt.savefig(save,format="jpg")
       common_library.plt.show()
    def Vizualize_GridShearch1(self,data_info,title,features_name):
       path="./Diagrams_Accuracy_Loss/"
       print(data_info)
       common_library.plt.style.use('seaborn')
       common_library.plt.figure(figsize=(10, 8))
       for C, gamma_scores in data_info.items():
        gammas = list(gamma_scores.keys())
        scores = list(gamma_scores.values())
        common_library.plt.plot(gammas, scores, marker='o', markersize=5, linewidth=2, label=f"C={C}")
       common_library.plt.title("GridSearch")
       common_library.plt.xlabel("gamma")
       common_library.plt.ylabel("score")
       common_library.plt.legend()
       save=path+title+' '+features_name+".jpg"
       common_library.plt.savefig(save,format='jpg')
       common_library.plt.show()
       print(title)
       return 0
    
    def Vizualize_GridShearch(self,gamma_values,C_values,cv_results,title):
        path="./Diagrams_Accuracy_Loss/"
        contour = common_library.plt.contour(common_library.np.log10(gamma_values), common_library.np.log10(C_values), cv_results.reshape(3, -1), cmap='viridis')
        common_library.plt.figure(figsize=(10, 8))
        # Adăugare bară de culoare
        common_library.plt.colorbar(contour, label='Mean Test Score')
        
        # Etichete și titlu
        common_library.plt.xlabel('log10(gamma)')
        common_library.plt.ylabel('log10(C)')
        common_library.plt.title('Efectul parametrului gamma în căutarea pe grilă')
        save=path+title+".jpg"
        common_library.plt.savefig(save,format='jpg')
        #common_library.plt.show()
        # Afișare diagramă
    
    def NkFlold_train_SVM(self,cycles_nkfold=False,shape=None,accuracy=None,title=None):
       path="./Diagrams_Accuracy_Loss/"
       save=path+title+".jpg"
       if cycles_nkfold==False:
          if shape[0]==40:
             print("MFCC")
             common_library.plt.style.use('seaborn')
             common_library.plt.figure(figsize=(10,5))
             for i in range(0,len(accuracy)):
                label="K-fold-"+str(i)
                common_library.plt.plot(i,accuracy[i],label=label)
             common_library.plt.ylabel('accuracy')
             common_library.plt.xlabel('k-Fold')
             common_library.plt.legend(loc='upper right') 
             common_library.plt.savefig(save,format='jpg')
             common_library.plt.show()
          else :
             print("FFT,PSD")
             common_library.plt.style.use('seaborn')
             common_library.plt.figure(figsize=(10,5))
             for i in range(0,len(accuracy)):
                label="K-fold-"+str(i)
                common_library.plt.plot(i,accuracy[i],label=label)
             common_library.plt.ylabel('accuracy')
             common_library.plt.xlabel('k-Fold')
             common_library.plt.legend(loc='upper right') 
             common_library.plt.savefig(save,format='jpg')
             common_library.plt.show()
       if cycles_nkfold==True:
          if shape[0]==40:
             print("MFCC")
             common_library.plt.style.use('seaborn')
             common_library.plt.figure(figsize=(10,5))
             labels=[]
             for i in range(0,len(accuracy)):
                labels.append("cycles-"+str(i+1)+" accuracy-"+str(accuracy[i]))
             common_library.plt.plot([i*2+1 for i in range(0,7//2+1)],accuracy,label=labels)
             common_library.plt.ylabel('accuracy')
             common_library.plt.xlabel('k-Fold-cycles')
             common_library.plt.legend(loc='upper right') 
             common_library.plt.savefig(save,format='jpg')
             common_library.plt.show()
          else :
             common_library.plt.style.use('seaborn')
             common_library.plt.figure(figsize=(10,5))
             labels=[]
             for i in range(0,len(accuracy)):
                labels.append("cycles-"+str(i+1)+" accuracy-"+str(accuracy[i]))
             common_library.plt.plot([i*2+1 for i in range(0,7//2+1)],accuracy,label=labels)
             common_library.plt.ylabel('accuracy')
             common_library.plt.xlabel('k-Fold-cycles')
             common_library.plt.legend(loc='upper right')
             common_library.plt.savefig(save,format='jpg') 
             common_library.plt.show()
       print(accuracy)
       return 0
    def Accuracy_Diagrams(self,history,function,function_number=False,features_name=None,model_name=None,accuracy=None):
        path="./Diagrams_Accuracy_Loss/"
        if function_number==False:
           print(f"Accuracy diagrams for the normal_training whit one lost function")
           print(f"history={history}\nmodel={model_name}\nfunctions={function}\nfeatures={features_name}\nmodel_name={model_name}")
           common_library.plt.style.use('seaborn')
           common_library.plt.figure(figsize=(10,5))
           common_library.plt.plot(history.history['binary_accuracy'],label='train')
           common_library.plt.plot(history.history['val_binary_accuracy'],label='test')
           common_library.plt.plot([],[],' ',label='loss_function='+function)
           common_library.plt.plot([],[],' ',label='accuracy='+str(accuracy))
           common_library.plt.title(model_name+' whit '+features_name+' accuracy normal training whit one lost func')
           common_library.plt.ylabel('accuracy')
           common_library.plt.xlabel('epoch')
           common_library.plt.legend(loc='upper right') 
           full_name=path+'Accuracy_'+model_name+'_'+features_name+'_'+'normaltrainng'+'_one_lost_function'+'.jpg'
           common_library.plt.savefig(full_name,format='jpg')  
           common_library.plt.show()     
        if function_number==True:
           print(f"Accuracy diagrams for the normal_training whit multi lost function")
           print(f"history={history}\nmodel={model_name}\nfunctions={function}\nfeatures={features_name}\nmodel_name={model_name}")
           common_library.plt.style.use('seaborn')
           common_library.plt.figure(figsize=(10,5))
           k=0
           for i in history:
             common_library.plt.plot(i.history['binary_accuracy'],label='train '+function[k])
             common_library.plt.plot(i.history['val_binary_accuracy'],label='test '+function[k])
             k+=1
           k=0
           for i in function:
             common_library.plt.plot([],[],' ',label='acuracy '+i+'='+str(accuracy[i]))  
           common_library.plt.title(model_name+' whit '+features_name+' model accuracy normal training whit multy lost func ')
           common_library.plt.ylabel('accuracy')
           common_library.plt.xlabel('epoch')
           common_library.plt.legend(loc='upper right') 
           full_name=path+'Accuracy_'+model_name+'_'+features_name+'_'+'normaltrainng'+'_multi_lost_function'+'.jpg'
           common_library.plt.savefig(full_name,format='jpg')  
           common_library.plt.show()  
        return 0
    def Loss_Diagrams(self,history,function,function_number=False,features_name=None,model_name=None):
        path="./Diagrams_Accuracy_Loss/"
        if function_number==False:
           print(f"Loss diagrams for the normal_training whit one lost function")
           print(f"history={history}\nmodel={model_name}\nfunctions={function}\nfeatures={features_name}\nmodel_name={model_name}")
           common_library.plt.style.use('seaborn')
           common_library.plt.figure(figsize=(10,5))
           common_library.plt.plot(history.history['loss'],label='train')
           common_library.plt.plot(history.history['val_loss'],label='test')
           common_library.plt.plot([],[],' ',label='loss_function='+function)
           common_library.plt.title(model_name+' whit '+features_name+' model loss normal training whit one lost func')
           common_library.plt.ylabel('loss')
           common_library.plt.xlabel('epoch')
           common_library.plt.legend(loc='upper right')   
           full_name=path+'Loss_'+model_name+'_'+features_name+'_'+'normaltrainng'+'_one_lost_function'+'.jpg'
           common_library.plt.savefig(full_name,format='jpg')
           common_library.plt.show()          
        if function_number==True:
           print(f"Loss diagrams for the normal_training whit multi lost function")
           print(f"history={history}\nmodel={model_name}\nfunctions={function}\nfeatures={features_name}\nmodel_name={model_name}")
           common_library.plt.style.use('seaborn')
           common_library.plt.figure(figsize=(10,5))
           k=0
           for i in history:
             common_library.plt.plot(i.history['loss'],label='train '+function[k])
             common_library.plt.plot(i.history['val_loss'],label='test '+function[k])
             k+=1
           common_library.plt.title(model_name+' whit '+features_name+' model loss normal training whit multi lost func and')
           common_library.plt.ylabel('loss')
           common_library.plt.xlabel('epoch')
           common_library.plt.legend(loc='upper left')  
           full_name=path+'Loss_'+model_name+'_'+features_name+'_'+'normaltrainng'+'_multi_lost_function'+'.jpg'
           common_library.plt.savefig(full_name,format='jpg') 
           common_library.plt.show() 
        return 0
    def Accuracy_Diagrams_Nkfold(self,history,function,function_number=False,features_name=None,model_name=None,cycles_nkfold=False,accuracy=None,nkfold=None):
        path="./Diagrams_Accuracy_Loss/"
        if function_number==True and cycles_nkfold==False:   
           print(f"Accuracy diagrams for the nkfold training whit multi lost function and no cycles")
           print(f"Diagram for every fold")
           print(f"history={history}\nfunctions={function}\nfeatures={features_name}\nmodel={model_name}\ncycles={cycles_nkfold}")
           common_library.plt.style.use('seaborn')
           num_datasets = len(function)
           num_cols = int(common_library.np.ceil(common_library.np.sqrt(num_datasets)))
           num_rows = int(common_library.np.ceil(num_datasets / num_cols))
           common_library.plt.figure(figsize=(15, 5 * num_rows))
           k=1
           for i in history:
              p=0
              common_library.plt.subplot(num_rows, num_cols, k)
              for j in i:
                 label='K-fold='+str(p)
                 common_library.plt.plot(j.history["val_binary_accuracy"],label=label)
                 p+=1
              common_library.plt.plot([],[],' ',label='loss_function='+function[k-1])
              common_library.plt.plot([],[],' ',label='acuracy='+str(accuracy[function[k-1]]))
              common_library.plt.legend(loc='upper right')
              common_library.plt.ylabel('accuracy')
              common_library.plt.xlabel('epoch')
              common_library.plt.title(model_name+' whit '+features_name+' model accuracy '+str(len(history[0]))+'-fold whit one lost function')
              k+=1  
           full_name=path+'Accuracy_'+model_name+'_'+features_name+'_'+'kfold'+'_multi_lost_function_nocycles'+'.jpg'
           common_library.plt.savefig(full_name,format='jpg')
           common_library.plt.show() 
        if function_number==False and cycles_nkfold==False:
           print(f"Accuracy diagrams for the nkfold training whit one lost function and no cycles")
           print(f"Diagram for every fold")
           print(f"history={history}\nfunctions={function}\nfeatures={features_name}\nmodel={model_name}\ncycles={cycles_nkfold}")
           common_library.plt.style.use('seaborn')
           common_library.plt.figure(figsize=(10,5))
           k=0
           for i in history:
             label=("K-Fold="+str(k))
             common_library.plt.plot(i.history['val_binary_accuracy'],label=label)
             k+=1
           common_library.plt.plot([],[],' ',label='loss_function='+function)
           common_library.plt.plot([],[],' ',label='accuracy='+str(accuracy))
           common_library.plt.title(model_name+' whit '+features_name+' model '+'accuracy '+str(len(history))+'-fold whit one lost func')
           common_library.plt.ylabel('accuracy')
           common_library.plt.xlabel('epoch')
           common_library.plt.legend(loc='upper right') 
           full_name=path+'Accuracy_'+model_name+'_'+features_name+'_'+'kfold'+'_one_lost_function_nocycles'+'.jpg'  
           common_library.plt.savefig(full_name,format='jpg')
           common_library.plt.show() 

        if function_number==True and cycles_nkfold==True:
           print(f"Accuracy diagrams for the nkfold training whit multi lost function and cycles")
           print(f"history={history}\nfunctions={function}\nfeatures={features_name}\nmodel={model_name}\ncycles={cycles_nkfold}")
           num_datasets = len(function)
           num_cols = int(common_library.np.ceil(common_library.np.sqrt(num_datasets)))
           num_rows = int(common_library.np.ceil(num_datasets / num_cols))
           common_library.plt.style.use('seaborn')
           common_library.plt.figure(figsize=(15, 5 * num_rows))
           k=1
           for i in history:
               common_library.plt.subplot(num_rows, num_cols, k)
               p=0
               for j in i:
                label='Cycle-'+str(p*2+1)+'acc-'+str(accuracy[k-1][p])
                common_library.plt.plot(j['val_binary_accuracy'],label=label) 
                p+=1
               common_library.plt.plot([],[],' ',label='loss_function='+function[k-1])
               common_library.plt.plot([],[],' ',label='acc-'+str(common_library.np.mean(accuracy[k-1],axis=0)))
               common_library.plt.title(model_name+' whit '+features_name+'acuracy for the '+str(nkfold)+'-fold whit cycle')
               common_library.plt.ylabel('accuracy')
               common_library.plt.xlabel('epoch')
               common_library.plt.legend(loc='upper right') 
               k+=1
           full_name=path+'Accuracy_'+model_name+'_'+features_name+'_'+'kfold'+'_multi_lost_function_yescycles'+'.jpg'  
           common_library.plt.savefig(full_name,format='jpg')
           common_library.plt.show() 
        if function_number==False and cycles_nkfold==True:
           print(f"Accuracy diagrams for the nkfold training whit one lost function and cycles")
           print(f"history={history}\nfunctions={function}\nfeatures={features_name}\nmodel={model_name}\ncycles={cycles_nkfold}")
           common_library.plt.style.use('seaborn')
           common_library.plt.figure(figsize=(10,5))
           k=0
           for i in history:
              label='Cycle-'+str(k*2+1)+'acc-'+str(accuracy[k])
              common_library.plt.plot(i['val_binary_accuracy'],label=label)
              k+=1
           common_library.plt.plot([],[],' ',label='loss_function='+function)
           common_library.plt.plot([],[],' ',label='acc_mean-'+str(common_library.np.mean(accuracy,axis=0)))
           common_library.plt.title(model_name+' whit '+features_name+'acuracy for the '+str(nkfold)+'-fold whit cycle')
           common_library.plt.ylabel('accuracy')
           common_library.plt.xlabel('epoch')
           common_library.plt.legend(loc='upper right')
           full_name=path+'Accuracy_'+model_name+'_'+features_name+'_'+'kfold'+'_one_lost_function_yescycles'+'.jpg'  
           common_library.plt.savefig(full_name,format='jpg')
           common_library.plt.show()
        return 0
    def Loss_Diagrams_Nkfold(self,history,function,function_number=False,features_name=None,model_name=None,cycles_nkfold=False,nkfold=None):
        path="./Diagrams_Accuracy_Loss/"
        if function_number==True and cycles_nkfold==False:   
           print(f"Loss diagrams for the nkfold training whit multi lost function and no cycles")
           print(f"Diagram for every fold")
           print(f"history={history}\nfunctions={function}\nfeatures={features_name}\nmodel={model_name}\ncycles={cycles_nkfold}")
           common_library.plt.style.use('seaborn')
           num_datasets = len(function)
           num_cols = int(common_library.np.ceil(common_library.np.sqrt(num_datasets)))
           num_rows = int(common_library.np.ceil(num_datasets / num_cols))
           common_library.plt.figure(figsize=(15, 5 * num_rows))
           k=1
           for i in history:
              p=0
              common_library.plt.subplot(num_rows, num_cols, k)
              for j in i:
                 label='K-fold='+str(p)
                 common_library.plt.plot(j.history["val_loss"],label=label)
                 p+=1
              common_library.plt.plot([],[],' ',label='loss_function='+function[k-1])
              common_library.plt.legend(loc='upper right')
              common_library.plt.ylabel('loss')
              common_library.plt.xlabel('epoch')
              common_library.plt.title(model_name+' whit '+features_name+' model loss '+str(len(history[0]))+'-fold whit one lost function')
              k+=1  
           full_name=path+'Loss_'+model_name+'_'+features_name+'_'+'kfold'+'_multi_lost_function_nocycles'+'.jpg'  
           common_library.plt.savefig(full_name,format='jpg')
           common_library.plt.show()         
        if function_number==False and cycles_nkfold==False:
           print(f"Loss diagrams for the nkfold training whit one lost function and no cycles")
           print(f"Diagram for every fold")
           print(f"history={history}\nfunctions={function}\nfeatures={features_name}\nmodel={model_name}\ncycles={cycles_nkfold}")
           common_library.plt.style.use('seaborn')
           common_library.plt.figure(figsize=(10,5))
           k=0
           for i in history:
             label=("K-Fold="+str(k))
             common_library.plt.plot(i.history['val_loss'],label=label)
             k+=1
           common_library.plt.plot([],[],' ',label='loss_function='+function)
           common_library.plt.title(model_name+' whit '+features_name+' model '+'accuracy '+str(len(history))+'-fold whit one lost func')
           common_library.plt.ylabel('loss')
           common_library.plt.xlabel('epoch')
           common_library.plt.legend(loc='upper right')
           full_name=path+'Loss_'+model_name+'_'+features_name+'_'+'kfold'+'_one_lost_function_nocycles'+'.jpg'  
           common_library.plt.savefig(full_name,format='jpg')   
           common_library.plt.show() 
        if function_number==True and cycles_nkfold==True:
           print(f"Loss diagrams for the nkfold training whit multi lost function and cycles")
           print(f"history={history}\nfunctions={function}\nfeatures={features_name}\nmodel={model_name}\ncycles={cycles_nkfold}")
           num_datasets = len(function)
           num_cols = int(common_library.np.ceil(common_library.np.sqrt(num_datasets)))
           num_rows = int(common_library.np.ceil(num_datasets / num_cols))
           common_library.plt.style.use('seaborn')
           common_library.plt.figure(figsize=(15, 5 * num_rows))
           k=1
           for i in history:
               common_library.plt.subplot(num_rows, num_cols, k)
               p=0
               for j in i:
                label='Cycle-'+str(p*2+1)
                common_library.plt.plot(j['val_loss'],label=label) 
                p+=1
               common_library.plt.plot([],[],' ',label='loss_function='+function[k-1])
               common_library.plt.title(model_name+' whit '+features_name+'acuracy for the '+str(nkfold)+'-fold whit cycle')
               common_library.plt.ylabel('accuracy')
               common_library.plt.xlabel('epoch')
               common_library.plt.legend(loc='upper right') 
               k+=1
           full_name=path+'Loss_'+model_name+'_'+features_name+'_'+'kfold'+'_multi_lost_function_yescycles'+'.jpg'  
           common_library.plt.savefig(full_name,format='jpg')
           common_library.plt.show() 
        if function_number==False and cycles_nkfold==True:
           print(f"Loss diagrams for the nkfold training whit one lost function and cycles")
           print(f"history={history}\nfunctions={function}\nfeatures={features_name}\nmodel={model_name}\ncycles={cycles_nkfold}")
           common_library.plt.style.use('seaborn')
           common_library.plt.figure(figsize=(10,5))
           k=0
           for i in history:
              label='Cycle-'+str(k*2+1)
              common_library.plt.plot(i['val_loss'],label=label)
              k+=1
           common_library.plt.plot([],[],' ',label='loss_function='+function)
           common_library.plt.title(model_name+' whit '+features_name+'loss for the '+str(nkfold)+'-fold whit cycle')
           common_library.plt.ylabel('accuracy')
           common_library.plt.xlabel('epoch')
           common_library.plt.legend(loc='upper right')
           full_name=path+'Loss_'+model_name+'_'+features_name+'_'+'kfold'+'_one_lost_function_yescycles'+'.jpg'  
           common_library.plt.savefig(full_name,format='jpg')
           common_library.plt.show()
        return 0
    

