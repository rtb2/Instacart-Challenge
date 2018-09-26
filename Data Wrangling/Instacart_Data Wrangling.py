#importing required libraries
import pandas as pd
import numpy as np
import glob
from scipy import stats

#Finding the list of files to uplod
pattern = '*.csv'
csv_files = glob.glob(pattern)
print(csv_files)

#uploading files
aisles = pd.read_csv("aisles.csv")
departments = pd.read_csv("departments.csv")
orders = pd.read_csv("orders.csv")
orders_products_prior = pd.read_csv("order_products__prior.csv")
orders_products_train = pd.read_csv("order_products__train.csv")
products = pd.read_csv("products.csv")

# Assigining names to the datasets
data_list = [aisles, departments, orders, 
             orders_products_prior, orders_products_train, products]
data_list_name = ['aisles', 'departments', 'orders', 
'orders_products_prior', 'orders_products_train', 'products']

j=0
for i in data_list:
    i.name = data_list_name[j]
    j += 1

#Checking of there are any null values
def null_columns(x):
    y = x.columns[x.isnull().any()]
    return y

for dataset in data_list:
    if len(null_columns(dataset)) == 0:
        print('Dataset ' + dataset.name + ' has no null values ')
    else:
        print('Dataset '+ dataset.name + ' has null values in column '+ str([i for i in null_columns(dataset)]))

#Dataset orders has null values in column ['days_since_prior_order'] 
#Finding the number of null values in orders.days_since_prior_order

sum(orders.days_since_prior_order.isnull())

#There are 206209 null values
#Lets examine the null values
orders.loc[orders.days_since_prior_order.isnull()==True,['user_id', 'order_number']]

#days_since_prior_order attribue for first order for all the users is null so it can be changed to 0

orders.days_since_prior_order = orders.days_since_prior_order.fillna(int(0))

#Datatypes
orders.dtypes
# "order_id", "user_id" should be discrete 
#should be of data type object
to_object= ["order_id", "user_id"]
orders[to_object]= orders[to_object].astype('object')

aisles.dtypes #aisle_id should be object
aisles.aisle_id = aisles.aisle_id.astype('object')

departments.dtypes#department_id should be object
departments.department_id = departments.department_id.astype('object')

orders_products_prior.dtypes#order_id and product_id should be of type object
orders_products_prior[['order_id', 'product_id']] = orders_products_prior[['order_id', 'product_id']].astype('object')

orders_products_train.dtypes
orders_products_train[['order_id', 'product_id']] = orders_products_train[['order_id', 'product_id']].astype('object')


#Finding Outliers
#Datasets aisles and departments are just categorical data, so there is no chance of outliers

for column in orders:
    if orders[column].dtype != 'object':
        percentile_range = np.percentile(orders[column], [2.5, 97.5])
        outliers=orders[column][(orders[column]<c[0])&(orders[column]>c[1])]
        print(outliers)
        
for column in orders_products_prior:
    if orders_products_prior[column].dtype != 'object':
        percentile_range = np.percentile(orders_products_prior[column], [2.5, 97.5])
        outliers=orders_products_prior[column][(orders_products_prior[column]<c[0])&(orders_products_prior[column]>c[1])]
        print(outliers)
        
for column in orders_products_train:
    if orders_products_train[column].dtype != 'object':
        percentile_range = np.percentile(orders_products_train[column], [2.5, 97.5])
        outliers=orders_products_train[column][(orders_products_train[column]<c[0])&(orders_products_train[column]>c[1])]
        print(outliers)
#there are no outliers in all the datasets
        






            
            






















    



