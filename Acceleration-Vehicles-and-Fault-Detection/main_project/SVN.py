import common_library 
common_library.warnings.filterwarnings("ignore")
'''
Seemse to be a a problemm for kfold  whit data set the data is to complex 
 or the problem 

'''
class SVN:
    def __init__(self,class_index,encoded_data=None,diagrams=None,features_name=None):
        self.encoded_data=encoded_data
        self.diagrams=diagrams
        self.class_index=class_index
        self.features=common_library.np.array([i[0] for i in  self.encoded_data])
        self.transformed_labels=common_library.np.array([i[1] for i in  self.encoded_data])
        print(self.transformed_labels[0])
        print(class_index)
        print("SVN model initialiezed ")
        self.features_name=features_name
        self.model_name="SVN"
        self.C=None
        self.Gamma=None
        self.Kernel='rbf'
        self.normal_label=[]
        for i in self.transformed_labels:
            self.normal_label.append(common_library.np.array([j for j in range(0,i.shape[0]) if i[j]!=0]))
        print(common_library.np.array(self.normal_label))
        print('-----------------------------------------------')
        self.normal_label=common_library.np.array(self.normal_label)
        mlb=common_library.MultiLabelBinarizer()
        self.normal_label=mlb.fit_transform(self.normal_label)
        print(self.normal_label)
        print("---------------------------------")
        print(self.class_index)
        self.GridShearch()
    def custom_binary_accuracy(self,y_true, y_pred):
      # Conversia probabilităților în etichete binare
      y_pred_binary = (y_pred > 0.5).astype(int)
      # Calculăm acuratețea binară
      return common_library.accuracy_score(y_true, y_pred_binary)
    def GridShearch(self):
        print("Grid Shearche")
        if self.features[0].shape[0]==40:
          print("Shape features: ",self.features.shape)
          flattened_features = common_library.np.array(self.features)

          num_samples, num_features, num_values = flattened_features.shape

          flattened_features = flattened_features.reshape((num_samples * num_features, num_values))

          adjusted_transformed_labels = common_library.np.repeat(self.transformed_labels, num_features, axis=0)

          X_train, X_test, y_train, y_test = common_library.train_test_split(flattened_features, adjusted_transformed_labels, test_size=0.3)
          svc = common_library.SVC(kernel='linear')
           
          multi_target_svc =common_library.OneVsRestClassifier(svc)
  
          param_grid = {'estimator__C': [0.1,0.5,1,10,100,150,200,250,500,1000],
              'estimator__gamma': [0.001,0.1,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09]}
          
          grid_search = common_library.GridSearchCV(multi_target_svc, param_grid, cv=5,n_jobs=-1,scoring='accuracy',error_score='raise')
          grid_search.fit(X_train, y_train)
          data_info={}
          for i in param_grid['estimator__C']:
                  data_info[i]={}
                  for j in param_grid['estimator__gamma']:
                      data_info[i][j]=None
          print(data_info)
          print(grid_search.cv_results_.keys())
          gamma_values = grid_search.cv_results_['param_estimator__gamma']
          C_values = grid_search.cv_results_['param_estimator__C']
          scores = grid_search.cv_results_['mean_test_score']
          
          self.C= grid_search.best_params_['estimator__C']
          self.Gamma = grid_search.best_params_['estimator__gamma']
  
          print("Combinatiile de parametri si scorurile lor:")
          for gamma, C, score in zip(gamma_values, C_values, scores):
              print("Gamma:", gamma, "C:", C, "Score:", score)
              data_info[C][gamma]=score
          title="GridShearch"+"SVM whit kerne="+str(self.Kernel)+' gamma='+str(self.Gamma)+' C='+str(self.C)
          self.diagrams.Vizualize_GridShearch1(data_info,title,self.features_name)
          print(self.features_name)
        else:
            svc=common_library.SVC(kernel='rbf')
            multi_target_svc =common_library.OneVsRestClassifier(svc)
  
            param_grid = {'estimator__C': [0.1,0.5,1,10,100,150,200,250,500,1000],
                'estimator__gamma': [0.001,0.1,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09]}
            
            grid_search = common_library.GridSearchCV(multi_target_svc, param_grid, cv=2,n_jobs=-1,scoring='accuracy',error_score='raise')
            grid_search.fit(self.features,self.normal_label)
            data_info={}
            for i in param_grid['estimator__C']:
                    data_info[i]={}
                    for j in param_grid['estimator__gamma']:
                        data_info[i][j]=None
            print(data_info)
            print(grid_search.cv_results_.keys())
            gamma_values = grid_search.cv_results_['param_estimator__gamma']
            C_values = grid_search.cv_results_['param_estimator__C']
            scores = grid_search.cv_results_['mean_test_score']
            
            self.C= grid_search.best_params_['estimator__C']
            self.Gamma = grid_search.best_params_['estimator__gamma']
    
            print("Combinatiile de parametri si scorurile lor:")
            for gamma, C, score in zip(gamma_values, C_values, scores):
                print("Gamma:", gamma, "C:", C, "Score:", score)
                data_info[C][gamma]=score
            title="GridShearch"+"SVM whit kerne="+str(self.Kernel)+' gamma='+str(self.Gamma)+' C='+str(self.C)
            self.diagrams.Vizualize_GridShearch1(data_info,title,self.features_name)
            print(self.features_name)
            '''
           
            data_info={}
            for i in param_grid['estimator__C']:
                 data_info[i]={}   
                 for j in param_grid['estimator__gamma']:
                       data_info[i][j]=None
            print(data_info)
           

            max_accuracy=0
            best_gamma=None
            best_C=None

            for i in param_grid['estimator__C']:  
                 for j in param_grid['estimator__gamma']:
                     X_train, X_test, y_train, y_test = common_library.train_test_split(self.features,self.normal_label, test_size=0.2
                                                                               ,shuffle=True,stratify=self.normal_label)
                     print(f"Modelul se antreneaza cu C={i} si Gamma={j}  ")
                     svc = common_library.SVC(kernel='rbf',probability=True,C=i,gamma=j)
                     multi_target_svc =common_library.OneVsRestClassifier(svc)
                     multi_target_svc.fit(X_train,y_train)
                     predictions=multi_target_svc.predict(X_test)
                     binary_predictions = (predictions > 0.5).astype(int)
                     precision = common_library.precision_score(y_test, predictions, average='samples')
                     jaccard_score_value = common_library.jaccard_score(y_test, binary_predictions, average='samples')
                     hamming_loss_value = common_library.hamming_loss(y_test,binary_predictions)
                     data_info[i][j]=precision
                     if max_accuracy<precision:
                         max_accuracy=precision
                         best_C=i
                         best_gamma=j
                     print(f"Modelul sa antrenat cu C={i} si Gamma={j} si are scorul  {precision} si jaccard {jaccard_score_value} si hammming {hamming_loss_value} ")
            
            print(data_info)

            self.C=best_C
            self.Gamma=best_gamma

            title="GridShearch"+"SVM whit kerne="+str(self.Kernel)+' gamma='+str(self.Gamma)+' C='+str(self.C)
            self.diagrams.Vizualize_GridShearch1(data_info,title,self.features_name)
            print(self.features_name)
            '''
            
            '''
            multi_target_svc.fit(X_train,y_train)

            predictions=multi_target_svc.predict(X_test)
            
            accuracy = common_library.accuracy_score(y_test, predictions)
            precision = common_library.precision_score(y_test, predictions, average='weighted')
            recall = common_library.recall_score(y_test, predictions, average='weighted')
            f1 = common_library.f1_score(y_test, predictions, average='weighted')
            
            # Afișarea rezultatelor
            print("Acuratețe:", accuracy)
            print("Precizie:", precision)
            print("Revocare:", recall)
            print("Scor F1:", f1)
            '''
    
            #param_grid ={'estimator__C': common_library.loguniform(1e0, 1e3).rvs(size=15),
            #  'estimator__gamma': common_library.loguniform(1e-4, 1e-3).rvs(size=15)}
            '''
            param_grid = {'estimator__C': [100],
              'estimator__gamma': [0.1]}
            
            #custom_binary_scorer = common_library.make_scorer(self.custom_binary_accuracy)
            grid_search = common_library.GridSearchCV(multi_target_svc, param_grid, cv=2,n_jobs=-1 ,scoring='precision',error_score='raise')
            grid_search.fit(self.features, self.normal_label)
            data_info={}
            for i in param_grid['estimator__C']:
                 data_info[i]={}   
                 for j in param_grid['estimator__gamma']:
                       data_info[i][j]=None
            print(data_info)
            print(grid_search.cv_results_.keys())
            gamma_values = grid_search.cv_results_['param_estimator__gamma']
            C_values = grid_search.cv_results_['param_estimator__C']
            scores = grid_search.cv_results_['mean_test_score']
            
            self.C= grid_search.best_params_['estimator__C']
            self.Gamma = grid_search.best_params_['estimator__gamma']

            print("Combinatiile de parametri si scorurile lor:")
            for gamma, C, score in zip(gamma_values, C_values, scores):
                print("Gamma:", gamma, "C:", C, "Score:", score)
                data_info[C][gamma]=score
            print(data_info)
            
            
            title="GridShearch"+"SVM whit kerne="+str(self.Kernel)+' gamma='+str(self.Gamma)+' C='+str(self.C)
            self.diagrams.Vizualize_GridShearch1(data_info,title,self.features_name)
            print(self.features_name)
            '''
            
    def Model(self):
        model=common_library.MultiOutputClassifier(common_library.SVC(C=self.C, kernel=self.Kernel, gamma=self.Gamma,probability=True))
        return model
    def Training(self,features_extraction_method):
        title='Average_Confusion_Matrix_SVM_whit_'+features_extraction_method
        path="./Models/model_"
        if self.features[0].shape[0]==40:
            #Train_confusion_matrix(content,title,test)
            flattened_features = common_library.np.array(self.features)
            
            num_samples, num_features, num_values = flattened_features.shape

            flattened_features = flattened_features.reshape((num_samples * num_features, num_values))

            adjusted_transformed_labels = common_library.np.repeat(self.transformed_labels, num_features, axis=0)

            X_train, X_test, y_train, y_test = common_library.train_test_split(flattened_features, adjusted_transformed_labels, test_size=0.3)
            model=self.Model()
            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)

            self.accuracy = common_library.accuracy_score(y_test, y_pred)
            
            conf_matrix = common_library.multilabel_confusion_matrix(y_test, y_pred)
    
           
            average_conf_matrix=common_library.np.mean(conf_matrix,axis=0)
                
            
            self.diagrams.Train_confusion_matrix(average_conf_matrix,title,y_test)
        else:
            
            X_train, X_test, y_train, y_test = common_library.train_test_split(self.features,self.normal_label, test_size=0.3)
            model=self.Model()
            model.fit(X_train, y_train)
            
            y_pred = model.predict(X_test)

            self.accuracy = common_library.accuracy_score(y_test, y_pred)
            
            conf_matrix = common_library.multilabel_confusion_matrix(y_test, y_pred)
    
            
            average_conf_matrix=common_library.np.mean(conf_matrix,axis=0)

            
            self.diagrams.Train_confusion_matrix(average_conf_matrix,title,y_test)
        path+=self.model_name+"_"+self.features_name+"_"+"normaltraining"+".pkl"
        print(path)
        with open(path,"wb") as f:
            common_library.pickle.dump(model,f)       
        return 0
        
    def Nk_Fold_Traning(self,features_extraction_method,cycles_nkfold=False):
        #def NkFlold_train_SVM(cycles_nkfold=False,shape=None,accuracy=None):
        path="./Models/model_"
        if cycles_nkfold==False:
            best_model=None 
            max_accuracy=0
            if self.features[0].shape[0]==40:
                n_splits=5
                skf = common_library.KFold(n_splits=n_splits, shuffle=True)
                list_accuracy=[]
                flattened_features = common_library.np.array(self.features)
                num_samples, num_features, num_values = flattened_features.shape
                flattened_features = flattened_features.reshape((num_samples * num_features, num_values))
                adjusted_transformed_labels = common_library.np.repeat(self.transformed_labels, num_features, axis=0)
                k=0
                for train_index, val_index in skf.split(flattened_features[:20], adjusted_transformed_labels[:20]):
                     print(f"Kfold pas {k}")
                     X_train, X_test = flattened_features[train_index], flattened_features[val_index]
                     y_train, y_test = adjusted_transformed_labels[train_index], adjusted_transformed_labels[val_index]
                     model=self.Model()
                     model.fit(X_train, y_train)
                     y_pred = model.predict(X_test)
                     accuracy = common_library.accuracy_score(y_test, y_pred)
                     if accuracy>=max_accuracy:
                         best_model=model
                         max_accuracy=accuracy
                     list_accuracy.append(accuracy)
                     k+=1
                print("My acyraces:",list_accuracy)
                self.accuracy=common_library.np.mean(list_accuracy,axis=0)
                title='SVM_whit_kfold_no_cycles_'+features_extraction_method
                self.diagrams.NkFlold_train_SVM(False,self.features.shape,list_accuracy,title)
            else:
                n_splits=5
                skf = common_library.KFold(n_splits=n_splits, shuffle=True)
                list_accuracy=[]
                k=0
                for train_index, val_index in skf.split(self.features[:20], self.transformed_labels[:20]):
                     X_train, X_test = self.features[train_index], self.features[val_index]
                     y_train, y_test = self.transformed_labels[train_index], self.transformed_labels[val_index]
                     model=self.Model()
                     model.fit(X_train, y_train)
                     y_pred = model.predict(X_test)
                     accuracy = common_library.accuracy_score(y_test, y_pred)
                     if accuracy>=max_accuracy:
                         best_model=model
                         max_accuracy=accuracy
                     list_accuracy.append(accuracy)
                     k+=1
                print("My acyraces:",list_accuracy)
                self.accuracy=common_library.np.mean(list_accuracy,axis=0)
                title='SVM_whit_kfold_no_cycles_'+features_extraction_method
                self.diagrams.NkFlold_train_SVM(False,self.features.shape,list_accuracy,title)
            path+=self.model_name+"_"+self.features_name+"_"+"kfold_nocycles"+".pkl"
            common_library.pickle.dump(best_model,path) 
        if cycles_nkfold==True:
            print("Cycles NKfold")
            best_model=None 
            max_accuracy=0
            if self.features[0].shape[0]==40:
                cycles=[1,3,5,7]
                n_splits=5
                skf = common_library.KFold(n_splits=n_splits, shuffle=True)
                flattened_features = common_library.np.array(self.features)
                num_samples, num_features, num_values = flattened_features.shape
                flattened_features = flattened_features.reshape((num_samples * num_features, num_values))
                adjusted_transformed_labels = common_library.np.repeat(self.transformed_labels, num_features, axis=0)
                accuracy_mean=[]
                for cycle in cycles:
                    print("yes")
                    print("----------------------------")
                    print(f"Number of the cycle {cycle}")
                    print("-----------------------------")
                    accuracy_list=[]
                    for i in range(cycle):
                     print("----------------------------")
                     print(f"Number kfold {i} for cycle {cycle}")
                     print("-----------------------------")
                     for train_index, val_index in skf.split(flattened_features[:20], adjusted_transformed_labels[:20]):
                      X_train, X_test = flattened_features[train_index], flattened_features[val_index]
                      y_train, y_test = adjusted_transformed_labels[train_index], adjusted_transformed_labels[val_index]
                      model = self.Model()
                      model.fit(X_train, y_train)
                      y_pred = model.predict(X_test)
                      accuracy = common_library.accuracy_score(y_test, y_pred)
                      print("yes")
                      if accuracy>=max_accuracy:
                         best_model=model
                         max_accuracy=accuracy
                      accuracy_list.append(accuracy)
                    accuracy_mean.append(common_library.np.mean(accuracy_list,axis=0))
                self.accuracy=common_library.np.mean(accuracy_mean,axis=0)
                print("My acyraces:",accuracy_mean)
                title='SVM_whit_kfold_yes_cycles_'+features_extraction_method
                self.diagrams.NkFlold_train_SVM(True,self.features.shape,accuracy_mean,title)
            else:
                cycles=[1,3,5,7]
                n_splits=5
                skf = common_library.KFold(n_splits=n_splits, shuffle=True)
                accuracy_mean=[]
                for cycle in cycles:
                    print("yes")
                    print("----------------------------")
                    print(f"Number of the cycle {cycle}")
                    print("-----------------------------")
                    accuracy_list=[]
                    for i in range(cycle):
                     print("----------------------------")
                     print(f"Number kfold {i} for cycle {cycle}")
                     print("-----------------------------")
                     for train_index, val_index in skf.split(self.features[:20], self.transformed_labels[:20]):
                      X_train, X_test = self.features[train_index], self.features[val_index]
                      y_train, y_test = self.transformed_labels[train_index], self.transformed_labels[val_index]
                      model = self.Model()
                      model.fit(X_train, y_train)
                      y_pred = model.predict(X_test)
                      accuracy = common_library.accuracy_score(y_test, y_pred)
                      if accuracy>=max_accuracy:
                         best_model=model
                         max_accuracy=accuracy
                      accuracy_list.append(accuracy)
                    accuracy_mean.append(common_library.np.mean(accuracy_list,axis=0))
                    print("yes")
                self.accuracy=common_library.np.mean(accuracy_mean,axis=0)
                print("My acyraces:",accuracy_mean)
                title='SVM_whit_kfold_yes_cycles_'+features_extraction_method
                self.diagrams.NkFlold_train_SVM(True,self.features.shape,accuracy_mean,title)
            path+=self.model_name+"_"+self.features_name+"_"+"kfold_yescycles"+".pkl"
            with open(path,"wb") as f:
             common_library.pickle.dump(model,f)
        return 0
    def Test(self):
         print(f"Suport Vector Machine acuracy is :{self.accuracy}")
         return 0
    
 

'''
  #FFT or PSD
           X,y=common_library.make_multilabel_classification(n_samples=1000, n_features=20, n_classes=3, n_labels=32)
           X_train, X_test, y_train, y_test=common_library.train_test_split(X,y,test_size=0.3)#common_library.train_test_split(self.features,self.transformed_labels,test_size=0.3)
           svm_=common_library.SVC(kernel=self.Kernel)
           print(self.Kernel)
           svm_model = common_library.MultiOutputClassifier(svm_,n_jobs=-1)
           param_grid = {
           'estimator__C': [0.1, 1, 10, 100,0.01],            
           'estimator__gamma': [1, 0.1, 0.01, 0.001] 
           }
           
           grid_search = common_library.GridSearchCV(svm_model, param_grid, cv=3, scoring='accuracy', n_jobs=-1)
           print(X_train[0])
           print(y_train[0])
           print(y_train[1])
           print(y_train[2])
           print(X_train.shape)
           print(y_train.shape)
           print(type(X_train))
           print(type(y_train))
           grid_search.fit(X_train[0:10], y_train[0:10])

           best_params = grid_search.best_params_

           print("Best Hyperparameters:", best_params)
           self.C= grid_search.best_params_['estimator__C']
           self.Gamma = grid_search.best_params_['estimator__gamma']
           print("Finalized GreadSherach")
           self.Vizualize_GridShearch(X_train,y_train)
 '''