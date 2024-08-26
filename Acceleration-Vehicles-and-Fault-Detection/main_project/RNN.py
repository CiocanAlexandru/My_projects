import common_library
'''

This one need some adaptation whit categorial entropy lost function 

model seems to overffit or be a deep diffirenc beetwen instamcee

'''
class RNN:  
    def __init__(self,class_index,encoded_data=None,diagrams=None,features_name=None):
        self.encoded_data=encoded_data
        self.diagrams=diagrams
        self.class_index=class_index
        self.features=common_library.np.array([i[0] for i in  self.encoded_data])
        self.transformed_labels=common_library.np.array([i[1] for i in  self.encoded_data])
        print(self.transformed_labels[0])
        print(class_index)
        print("RNN model initialiezed ")
        self.features_name=features_name
        self.model_name="RNN"
    def Model(self,loss_function):
        print(self.features[0].shape)
        activation_function=''
        other_function=''
        if loss_function=='categorical_crossentropy':
            activation_function='softmax'
            other_function='tanh'
        else:
            activation_function='sigmoid'   
            other_function='relu' 
        if self.features[0].shape==(self.features[0].shape[0],):
            model=common_library.tf.keras.Sequential([
            common_library.tf.keras.layers.Reshape((1, self.features[0].shape[0])),
            common_library.tf.keras.layers.LSTM(units=128),
            common_library.tf.keras.layers.Dense(units=64, activation=other_function),
            common_library.tf.keras.layers.Dense(units=128, activation='linear'),
            common_library.tf.keras.layers.Dense(units=64, activation=other_function),
            common_library.tf.keras.layers.Dense(len(self.class_index) + 1, activation=activation_function)
        ])
        else:
           model=common_library.tf.keras.Sequential([
            common_library.tf.keras.layers.LSTM(units=32,input_shape=self.features[0].shape),
            common_library.tf.keras.layers.Dense(units=64, activation=other_function),
            common_library.tf.keras.layers.Dense(units=128, activation='linear'),
            common_library.tf.keras.layers.Dense(units=64, activation=other_function),
            common_library.tf.keras.layers.Dense(len(self.class_index) + 1, activation=activation_function)
        ])        
        return model
    def Training(self,number_loss=False):
        # def Accuracy_Diagrams(self,history,function,function_number=False,features_name=None,model_name=None):
        # def Loss_Diagrams(self,history,function,function_number=False,features_name=None,model_name=None):
        loss_functions=['categorical_crossentropy','binary_crossentropy']
        loss_function='binary_crossentropy'
        path="./Models/model_"
        if number_loss==True:
           print("Normal training whit multi loss function")
           history_list=[]
           accuracy_list=[]
           for iloss_function in loss_functions:
                X_train, X_test, y_train, y_test = common_library.train_test_split(self.features, self.transformed_labels, test_size=0.3)
                model=self.Model(iloss_function)
                model.compile(optimizer='adam', loss=iloss_function, metrics=['binary_accuracy'])
                history=model.fit(X_train,y_train, epochs=100, batch_size=10, validation_split=0.3)
                history_list.append(history)
                accuracy_list.append(model.evaluate(X_test,y_test)[1])
                path+=self.model_name+"_"+self.features_name+"_"+"normaltraining_multi_lost_function_"+iloss_function+".h5"
                model.save(path)
           self.accuracy={loss_functions[i]:accuracy_list[i] for i in range(0,len(loss_functions))}
           print(self.accuracy)
           #self.accuracy=common_library.np.mean(accuracy_list,axis=0)
           self.diagrams.Accuracy_Diagrams(history_list,loss_functions,True,self.features_name,self.model_name,self.accuracy)
           self.diagrams.Loss_Diagrams(history_list,loss_functions,True,self.features_name,self.model_name)
        if number_loss==False:
           print("Normal Traing whit one loss function ")
           X_train, X_test, y_train, y_test = common_library.train_test_split(self.features, self.transformed_labels, test_size=0.3)
           model=self.Model(loss_function)
           model.compile(optimizer='adam', loss=loss_function, metrics=['binary_accuracy'])
           history=model.fit(X_train,y_train, epochs=100, batch_size=10, validation_split=0.3)
           self.accuracy=model.evaluate(X_test,y_test)[1]
           self.diagrams.Accuracy_Diagrams(history,loss_function,False,self.features_name,self.model_name,self.accuracy)
           self.diagrams.Loss_Diagrams(history,loss_function,False,self.features_name,self.model_name)
           path+=self.model_name+"_"+self.features_name+"_"+"normaltraining_one_lost_function.h5"
           model.save(path)
        return 0
    def Nk_Fold_Traning(self,number_loss=False,cycles_nkfold=False):
        #def Accuracy_Diagrams_Nkfold(self,history,function,function_number=False,features_name=None,model_name=None,cycles_nkfold=False,accuracy=None):
        #def Loss_Diagrams_Nkfold(self,history,function,function_number=False,features_name=None,model_name=None,cycles_nkfold=False,accuracy=None):
        loss_functions=['categorical_crossentropy','binary_crossentropy']
        loss_function='binary_crossentropy'
        path="./Models/model_"
        if number_loss==False and cycles_nkfold==False:     ## Diagrams for every fold  each 
            print("Nkfold whit one lost function and no cycles")
            n_splits=5
            skf = common_library.KFold(n_splits=n_splits, shuffle=True)
            history_list=[]
            accuracy_list=[]
            best_model=None
            max_accuracy=0
            for train_index, val_index in skf.split(self.features, self.transformed_labels):
              X_train, X_val = self.features[train_index], self.features[val_index]
              y_train, y_val = self.transformed_labels[train_index], self.transformed_labels[val_index]
              model = self.Model(loss_function)
              model.compile(optimizer='adam', loss=loss_function, metrics=['binary_accuracy'])
              history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_val, y_val))
              accuracy = model.evaluate(X_val, y_val, verbose=0)[1]
              if accuracy>max_accuracy:
                 max_accuracy=accuracy
                 best_model=model
              history_list.append(history)
              accuracy_list.append(accuracy)
            self.accuracy=common_library.np.mean(accuracy_list,axis=0)
            self.diagrams.Accuracy_Diagrams_Nkfold(history_list,loss_function,False,self.features_name,self.model_name,False,self.accuracy)
            self.diagrams.Loss_Diagrams_Nkfold(history_list,loss_function,False,self.features_name,self.model_name,False)
            path+=self.model_name+"_"+self.features_name+"_"+"kfold_one_lost_function_nocycles.h5"
            best_model.save(path)
        if number_loss==True and cycles_nkfold==False:      ## Diagram for every fold  each
            print("Nkfold whit multi lost function and no cycles")
            n_splits=5
            skf = common_library.KFold(n_splits=n_splits, shuffle=True)
            history_list=[]
            accuracy_list=[]
            for iloss_function in loss_functions:
                fold_accuracies_for_loss = []
                historys_for_loss = []
                best_model=None
                max_accuracy=0
                for train_index, val_index in skf.split(self.features, self.transformed_labels):
                 X_train, X_val = self.features[train_index], self.features[val_index]
                 y_train, y_val = self.transformed_labels[train_index], self.transformed_labels[val_index]
                 model = self.Model(iloss_function)
                 model.compile(optimizer='adam', loss=iloss_function, metrics=['binary_accuracy'])
                 history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_val, y_val))
                 accuracy = model.evaluate(X_val, y_val, verbose=0)[1]
                 if accuracy>max_accuracy:
                    best_model=model
                    max_accuracy=accuracy
                 fold_accuracies_for_loss.append(accuracy)
                 historys_for_loss.append(history) 
                accuracy_list.append(fold_accuracies_for_loss)
                history_list.append(historys_for_loss)
                path+=self.model_name+"_"+self.features_name+"_"+"kfold_multi_lost_function_"+iloss_function+"_"+"nocycles"+".h5"
                best_model.save(path)
            self.accuracy={loss_functions[i]:common_library.np.mean(accuracy_list[i]) for i in range(0,len(accuracy_list))}
            self.diagrams.Accuracy_Diagrams_Nkfold(history_list,loss_functions,True,self.features_name,self.model_name,False,self.accuracy)
            self.diagrams.Loss_Diagrams_Nkfold(history_list,loss_functions,True,self.features_name,self.model_name,False)
        if number_loss==False and cycles_nkfold==True:      ## Diagrams for more cycles each [1,3,5,7]
            print("Nkfold whit one lost function and cycles")
            cycles=[1,3,5,7]
            n_splits=5
            skf = common_library.KFold(n_splits=n_splits, shuffle=True)
            history_mean=[]
            accuracy_mean=[]
            best_model=None
            max_accuracy=0
            for cycle in cycles:
                print("----------------------------")
                print(f"Number of the cycle {cycle}")
                print("-----------------------------")
                history_list=[]
                accuracy_list=[]
                for i in range(cycle):
                 print("----------------------------")
                 print(f"Number kfold {i} for cycle {cycle}")
                 print("-----------------------------")
                 for train_index, val_index in skf.split(self.features, self.transformed_labels):
                  X_train, X_val = self.features[train_index], self.features[val_index]
                  y_train, y_val = self.transformed_labels[train_index], self.transformed_labels[val_index]
                  model = self.Model(loss_function)
                  model.compile(optimizer='adam', loss=loss_function, metrics=['binary_accuracy'])
                  history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_val, y_val))
                  accuracy = model.evaluate(X_val, y_val, verbose=0)[1]
                  if accuracy>max_accuracy:
                     max_accuracy=accuracy
                     best_model=model
                  history_list.append(history)
                  accuracy_list.append(accuracy)
                history_mean.append({
                 'loss': common_library.np.mean([h.history['loss'] for h in history_list], axis=0),
                 'val_loss': common_library.np.mean([h.history['val_loss'] for h in history_list], axis=0),
                 'binary_accuracy': common_library.np.mean([h.history['binary_accuracy'] for h in history_list], axis=0),
                 'val_binary_accuracy': common_library.np.mean([h.history['val_binary_accuracy'] for h in history_list], axis=0)
                 })
                accuracy_mean.append(common_library.np.mean(accuracy_list,axis=0))
            self.accuracy=accuracy_mean    
            self.diagrams.Accuracy_Diagrams_Nkfold(history_mean,loss_function,False,self.features_name,self.model_name,True,accuracy_mean,n_splits)
            self.diagrams.Loss_Diagrams_Nkfold(history_mean,loss_function,False,self.features_name,self.model_name,True,n_splits)
            path+=self.model_name+"_"+self.features_name+"_"+"kfold_one_lost_function_"+iloss_function+"_"+"yescycles"+".h5"
            best_model.save(path)
        if number_loss==True and cycles_nkfold==True:       ## Diagram for more cycles each [1,3,5,7]
            print("Nkfold whit multi lost function and cycles") 
            cycles=[1,3,5,7]
            n_splits=5
            skf = common_library.KFold(n_splits=n_splits, shuffle=True)
            history_all=[]
            accuracy_all=[]
            for iloss_function in loss_functions:
             print("-----------------------------")
             print(f"Function is {iloss_function}")
             print("-----------------------------")
             history_mean=[]
             accuracy_mean=[]
             best_model=None
             max_accuracy=0
             for cycle in cycles:
                 print("----------------------------")
                 print(f"Number of the cycle {cycle}")
                 print("-----------------------------")
                 history_list=[]
                 accuracy_list=[]
                 for i in range(cycle):
                  print("----------------------------")
                  print(f"Number kfold {i} for cycle {cycle}")
                  print("-----------------------------")
                  for train_index, val_index in skf.split(self.features, self.transformed_labels):
                   X_train, X_val = self.features[train_index], self.features[val_index]
                   y_train, y_val = self.transformed_labels[train_index], self.transformed_labels[val_index]
                   model = self.Model(iloss_function)
                   model.compile(optimizer='adam', loss=iloss_function, metrics=['binary_accuracy'])
                   history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_val, y_val))
                   accuracy = model.evaluate(X_val, y_val, verbose=0)[1]
                   if accuracy>max_accuracy:
                      max_accuracy=accuracy
                      best_model=model
                   history_list.append(history)
                   accuracy_list.append(accuracy)
                 history_mean.append({
                  'loss': common_library.np.mean([h.history['loss'] for h in history_list], axis=0),
                  'val_loss': common_library.np.mean([h.history['val_loss'] for h in history_list], axis=0),
                  'binary_accuracy': common_library.np.mean([h.history['binary_accuracy'] for h in history_list], axis=0),
                  'val_binary_accuracy': common_library.np.mean([h.history['val_binary_accuracy'] for h in history_list], axis=0)
                  })
                 accuracy_mean.append(common_library.np.mean(accuracy_list,axis=0))
             
             history_all.append(history_mean)
             accuracy_all.append(accuracy_mean)
             path+=self.model_name+"_"+self.features_name+"_"+"kfold_multi_lost_function_"+iloss_function+"_"+"yescycles"+".h5"
             best_model.save(path)
            self.accuracy=accuracy_all
            self.diagrams.Accuracy_Diagrams_Nkfold(history_all,loss_functions,True,self.features_name,self.model_name,True,accuracy_all,n_splits)
            self.diagrams.Loss_Diagrams_Nkfold(history_all,loss_functions,True,self.features_name,self.model_name,True,n_splits)
        return 0
    def Test(self):
         print(f"Neuronal model acuracy is :{self.accuracy}")
         return 0