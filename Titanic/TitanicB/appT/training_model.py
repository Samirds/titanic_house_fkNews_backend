
# #------------------------------------ Import Libraries ---------------------
# import pandas as pd
# import numpy as np
# from sklearn.base import BaseEstimator, TransformerMixin
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.impute import KNNImputer
# from sklearn.model_selection import train_test_split
# import pickle

# # ------------------------------------- Import Dataset-------------------------
# data = pd.read_csv("train.csv")

# #----------------------------------------  class for Pipe Lines----------------------------

# #_-------------------- Lower the column names---------------------------
# class LowerHeader:
#   def __init__(self, dataset, isLower= True):
#     self.isLower= isLower
#     self.dataset = dataset

#   def lower(self):
#     if (self.isLower):
#       self.dataset.columns= [str(i).lower() for i in self.dataset.columns]
#     else:
#       pass

#     return self.dataset
  
# #------------------------ Split dataset ----------------------------------
# class Split_Xy:
#     def __init__(self):
#         pass

#     def deleteCol(self, dataset, *cols):
#         self.dataset= dataset
#         self.cols = list(cols)
#         return self.dataset.drop(self.cols, axis=1)

#     def splitData(self, dataset):
#         self.dataset = dataset
#         drp_dataset = self.deleteCol(self.dataset, "passengerid", "name", "ticket")
#         # Splitting into X, y
#         X = drp_dataset[['age', 'fare', 'pclass', 'sex',
#             'sibsp', 'parch', 'cabin', 'embarked']]
#         y = data['survived']
#         dataset_lst = [X, y]
#         return dataset_lst
        
# #--------------------------------- Prefill the nan values--------------

# class PreFill:
#   def __init__(self, need_preCabin= True, need_preEmbarked= True, fillWith_e= "C"):
#     self.need_preCabin = need_preCabin
#     self.need_preEmbarked = need_preEmbarked
#     self.fillWith_e = fillWith_e

#   def prefill_C_e(self, dataset)-> "its assign 1st word of cabin and remove na in embark column with C":
#     self.dataset = dataset
#     if(self.need_preCabin):
#       self.dataset["cabin"] = self.dataset["cabin"].fillna("other")
#       for i in range (len(self.dataset['cabin'])):
#         self.dataset['cabin'][i] = str(self.dataset['cabin'][i])[0]

#       if(self.need_preEmbarked):
#         self.dataset["embarked"] = self.dataset['embarked'].fillna(self.fillWith_e)
#       else:
#         pass

#     else:
#       self.dataset.drop(["cabin"], axis=1)


#     return self.dataset

# #------------------------------------ Capping the Outliers----------------------
# class Capping_Outliers:
#   def __init__(self, quantile= 5, need_age= True, need_fare= True):
#     self.need_age = need_age
#     self.need_fare = need_fare
#     self.quantile = quantile



#   def cap_age(self, low_range= 0.05, high_range= 0.95):
#     self.low_range= low_range
#     self.high_range= high_range

#     for i in range(len(self.dataset['sex'])):
#       if (self.dataset['sex'][i]== 'male'):
#         if(self.dataset["age"][i]) > self.dataset[self.dataset['sex']=='male']['age'].quantile(high_range):
#           self.dataset['age'][i] = self.dataset[self.dataset['sex']=='male']['age'].quantile(high_range)
#         elif (self.dataset["age"][i]<self.dataset[self.dataset['sex']=='male']['age'].quantile(low_range)):
#           self.dataset['age'][i] = self.dataset[self.dataset['sex']=='male']['age'].quantile(low_range)

#       else:
#         if(self.dataset["age"][i]) > self.dataset[self.dataset['sex']=='female']['age'].quantile(high_range):
#           self.dataset['age'][i] = self.dataset[self.dataset['sex']=='female']['age'].quantile(high_range)
#         elif (self.dataset["age"][i]<self.dataset[self.dataset['sex']=='female']['age'].quantile(low_range)):
#           self.dataset['age'][i] = self.dataset[self.dataset['sex']=='female']['age'].quantile(low_range)


#     return self.dataset



#   def cap_fare(self, low_range= 0.05, high_range= 0.95):
#     self.low_range= low_range
#     self.high_range= high_range
#     np.where(self.dataset['fare']==0, np.nan, self.dataset['fare'])

#     for i in range(len(self.dataset['fare'])):
#       if(np.isnan(self.dataset['fare'][i])):
#         pass
#       else:
#         if (self.dataset['pclass'][i]== 1):
#           if(self.dataset["fare"][i]) > self.dataset[self.dataset['pclass']==1]['fare'].quantile(high_range):
#             self.dataset['fare'][i] = self.dataset[self.dataset['pclass']==1]['fare'].quantile(high_range)
#           elif (self.dataset["fare"][i]<self.dataset[self.dataset['pclass']==1]['fare'].quantile(low_range)):
#             self.dataset['fare'][i] = self.dataset[self.dataset['pclass']==1]['fare'].quantile(low_range)

#         elif (self.dataset['pclass'][i]== 2):
#           if(self.dataset["fare"][i]) > self.dataset[self.dataset['pclass']==2]['fare'].quantile(high_range):
#             self.dataset['fare'][i] = self.dataset[self.dataset['pclass']==2]['fare'].quantile(high_range)
#           elif (self.dataset["fare"][i]<self.dataset[self.dataset['pclass']==2]['fare'].quantile(0.05)):
#             self.dataset['fare'][i] = self.dataset[self.dataset['pclass']==2]['fare'].quantile(low_range)

#         else :
#           if(self.dataset["fare"][i]) > self.dataset[self.dataset['pclass']==3]['fare'].quantile(high_range):
#             self.dataset['fare'][i] = self.dataset[self.dataset['pclass']==3]['fare'].quantile(high_range)
#           elif (self.dataset["fare"][i]<self.dataset[self.dataset['pclass']==3]['fare'].quantile(low_range)):
#             self.dataset['fare'][i] = self.dataset[self.dataset['pclass']==3]['fare'].quantile(low_range)

#     return self.dataset



#   def AgeFareExe(self, dataset):
#     self.dataset = dataset
#     if(self.need_age):
#       self.dataset = self.cap_age()

#       if(self.need_fare):
#         self.dataset = self.cap_fare()
#       else:
#         pass

#     else:
#       if(self.need_fare):
#         self.dataset = self.cap_fare()
#       else:
#         pass

#     return self.dataset


# #----------------------------------------- Custome Imputer------------------------
# class CustomeImputer:
#   def __init__(self):

#     # mapping items
#     pclass_enc = {1: 0.468, 2: 0.352, 3: 0.180}
#     sex_enc = {"female": 0.797, "male": 0.203} # here we are encoding with survival rate
#     sibsp_enc = {0: 0.196, 1: 0.304, 2: 0.263, 3: 0.142, 4: 0.095, 5: 0.00001, 6: 0.00001, 7: 0.00001, 8: 0.00001,}
#     parch_enc = {0: 0.157, 1: 0.251, 2: 0.228, 3: 0.273, 4: 0.00001, 5: 0.091, 6: 0.0001}
#     cabin_enc = {'o': 0.063, 'C': 0.125, "E": 0.159, "G": 0.106, "D": 0.160, "A": 0.099, "B": 0.156, "F": 0.130, "T": 0.0001, }
#     embarked_enc = {"S": 0.262, "C": 0.435, "Q": 0.303}

#     self.lst_enc = [pclass_enc, sex_enc, sibsp_enc, parch_enc, cabin_enc, embarked_enc]


#   def Imputer(self, dataset):
#     self.dataset = dataset

#     for i in range(len(self.dataset.columns)):
#       if (i<=1):
#         continue
#       else:
#         self.dataset[dataset.columns[i]] = self.dataset[self.dataset.columns[i]].map(self.lst_enc[i-2])

#     return self.dataset



# # ----------------------------------- Primary Clean-----------------------------

# class primary_clean(BaseEstimator, TransformerMixin):
#   def __init__(self, need_to_lower= True,):
#     self.need_to_lower = need_to_lower


#   def fit(self, X= None, y= None):
#     self.primary_obj_= LowerHeader(isLower=self.need_to_lower, dataset=X)
#     self.split_Xy_obj_ = Split_Xy()
#     self.prefill_obj_ = PreFill()
#     self.capping_outliers_obj_ = Capping_Outliers()
#     self.customeimputer_obj_ = CustomeImputer()
#     self.knn_imputer_obj_ = KNNImputer(n_neighbors=5)
#     return self

#   def transform(self, X, y=None):
#     low_dataset_ = self.primary_obj_.lower()
#     split_data_ = self.split_Xy_obj_.splitData(low_dataset_)
#     split_data_X_ = split_data_[0] #it gives X & y in a list form so here we are taking only X
#     split_data_y_ = split_data_[1]
#     prefill_dataset_ = self.prefill_obj_.prefill_C_e(split_data_X_)
#     age_fare_dataset_ = self.capping_outliers_obj_.AgeFareExe(prefill_dataset_)
#     cutome_imputer_dataset_ = self.customeimputer_obj_.Imputer(age_fare_dataset_)
#     knn_imputer_array_ = self.knn_imputer_obj_.fit_transform(cutome_imputer_dataset_)
#     knn_imputer_dataset_ = pd.DataFrame(knn_imputer_array_, columns = cutome_imputer_dataset_.columns)
#     X_train, X_test, y_train, y_test = train_test_split(knn_imputer_dataset_, split_data_y_, random_state=1, stratify=split_data_y_)
#     trn_test_list = [X_train, X_test, y_train, y_test]

#     return trn_test_list



# #----------------------------------- Fit the Mode-----------------------------
# obj = primary_clean()
# trn_tst_list = obj.fit_transform(data)
# X_train, X_test, y_train, y_test = trn_tst_list[0], trn_tst_list[1], trn_tst_list[2], trn_tst_list[3],


# clf = RandomForestClassifier()
# clf.fit(X_train, y_train)

# #-------------------------------------- Pickle Model
# pickle.dump(clf,open('pklModel.pkl', 'wb'))
