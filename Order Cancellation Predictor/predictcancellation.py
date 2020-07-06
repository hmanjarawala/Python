# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 19:32:48 2020

@author: Himanshu.Manjarawala
"""
import pandas as pd
import pickle

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, mean_squared_error
from sklearn.model_selection import train_test_split, GridSearchCV

def meal_parser(x):
    if x != 'Undefined':
        return x.split(' ')[0]
    else:
        return 'Undefined'

def clean_company(x):
    try:
        return 'company_'+x.split()[0]
    except:
        return 'company_unknown'

def clean_RSD(x, dt='d'):
    try:
        if dt=='d':
            dt_no = 2
        elif dt=='m':
            dt_no = 1
        elif dt=='y':
            dt_no = 0
        return list(x)[0].split('-')[dt_no]
    except:
        return x.split('-')[dt_no]
    
def LogisticRegressionImpl(X_train, X_test, y_train, y_test):
    lr = LogisticRegression(solver="lbfgs")
    # training a linear model
    lr.fit(X_train, y_train)
    
    # predicting values
    pred = lr.predict(X_test)
    
    accuracy = accuracy_score(y_test, pred)
    
    if accuracy > 0.85:
        pickle.dump(rfc, open("./models/LRmodel.pkl", "wb"))
    
    # plotting results
    print(confusion_matrix(y_test, pred))
    
    print(classification_report(y_test, pred))
    
    print(accuracy)
    
    print(mean_squared_error(y_test, pred))

def RandomForestClassifierImpl(X_train, X_test, y_train, y_test):
    rfc = RandomForestClassifier(n_estimators=10)
    rfc.fit(X_train, y_train)
    
    # predicting values
    pred = rfc.predict(X_test)
    
    accuracy = accuracy_score(y_test, pred)
    
    if accuracy > 0.85:
        pickle.dump(rfc, open("./models/RFCmodel.pkl", "wb"))
    # plotting results
    print(confusion_matrix(y_test, pred))
    
    print(classification_report(y_test, pred))
    
    print(accuracy)
    
    print(mean_squared_error(y_test, pred))
    
def RandomForestClassifierGridSearchImpl(X_train, X_test, y_train, y_test):
    rfc = RandomForestClassifier(n_estimators=10)
    rfc.fit(X_train, y_train)
    feature_importances = pd.DataFrame(rfc.feature_importances_,
                                   index = X_train.columns,
                                    columns=['importance']).sort_values('importance', 
                                                                        ascending=False)
    print(feature_importances[:9])
    
    param_grid = { 
    'n_estimators': [200, 500],
    'max_features': ['auto', 'sqrt', 'log2'],
    'criterion' :['gini', 'entropy']
    }
    
    # init model
    rfc_final=RandomForestClassifier()
    
    # init grid searching
    CV_rfc = GridSearchCV(estimator=rfc_final, param_grid=param_grid,
                          cv=2, verbose=5, n_jobs=-1)
    
    # begin grid search
    CV_rfc.fit(X_train, y_train)
    
    print(CV_rfc.best_params_)
    
    # predicting values
    pred = CV_rfc.predict(X_test)
    
    accuracy = accuracy_score(y_test, pred)
    
    # plotting results
    print(confusion_matrix(y_test, pred))
    
    print(classification_report(y_test, pred))
    
    print(accuracy)
    
    print(mean_squared_error(y_test, pred))
    
def cleananomalies(filepath='./data/hotel_bookings.csv'):
    df = pd.read_csv(filepath, sep=',')
    
    print(df["company"].unique()[:20])
    
    df["company"] = df["company"].apply(clean_company)
    
    print(df["company"].unique()[:20])
    
    # df = pd.concat([df, pd.get_dummies(df["company"])], axis=1)
    
    df.drop("company", axis=1, inplace=True)
    
    # Cleaning reservation_status_date
    
    RSD = pd.DataFrame(pd.to_datetime(df["reservation_status_date"]).astype("str"))
    
    RSD["ReservationStatusDate_year"] = RSD["reservation_status_date"].apply(clean_RSD, args=("y")).astype(int)
    RSD["ReservationStatusDate_month"] = RSD["reservation_status_date"].apply(clean_RSD, args=("m")).astype(int)
    RSD["ReservationStatusDate_day"] = RSD["reservation_status_date"].apply(clean_RSD, args=("d")).astype(int)
    
    df = pd.concat([df, RSD.iloc[:, 1:]], axis=1)
    df.drop("reservation_status_date", axis=1, inplace=True)
    
    # Cleaning arrival_date_month
    
    print(df["arrival_date_month"].unique())
    
    month_to_num = {
        'January': '01',
        'February': '02',
        'March': '03',
        'April': '04',
        'May': '05',
        'June': '06',
        'July': '07',
        'August': '08',
        'September':'09',
        'October': '10',
        'November': '11',
        'December': '12'
    }
    
    df["arrival_date_month"] = df["arrival_date_month"].map(month_to_num).astype(int)
    
    # Cleaning meal
    
    meal_data = df["meal"].apply(meal_parser)
    meal_data = pd.get_dummies(meal_data)
    
    # df = pd.concat([df, meal_data], axis=1)
    df.drop("meal", axis=1, inplace=True)
    
    # Cleaning reservation_status
    
    df = pd.concat([df, pd.get_dummies(df["reservation_status"])], axis=1)
    df.drop("reservation_status", axis=1, inplace=True)
    
    # Cleaning country
    
    country_col = pd.get_dummies(df["country"])
    country_col_names = ['Country_' + str(con) for con in list(country_col.columns)]
    country_col.columns = country_col_names
    
    # df = pd.concat([df, country_col], axis=1)
    
    # Cleaning customer_type
    
    # df = pd.concat([df, pd.get_dummies(df["customer_type"])], axis=1)
    df.drop("customer_type", axis=1, inplace=True)
    
    # Cleaning distribution_channel
    
    # df = pd.concat([df, pd.get_dummies(df["distribution_channel"])], axis=1)
    df.drop("distribution_channel", axis=1, inplace=True)
    
    # Cleaning market_segment
    
    # df = pd.concat([df, pd.get_dummies(df["market_segment"])], axis=1)
    df.drop("market_segment", axis=1, inplace=True)
    
    drop_object_cols = ['country',
                    'reserved_room_type',
                    'assigned_room_type',
                    'deposit_type','agent', 'children']
    df.drop(drop_object_cols, axis=1, inplace=True)
    
    return(df)

def main():
    
    df = cleananomalies()
    
    # Label
    y = df["Canceled"]
    # Features

    X = df.drop(['is_canceled', 'Canceled', 'Check-Out'], axis=1)
    # X.drop(['is_canceled', 'Check-Out'], axis=1, inplace=True)
    
    print(len(X.columns))
            
    
    
    # Diving the dataset into Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    
    # LogisticRegressionImpl(X_train, X_test, y_train, y_test)
    
    RandomForestClassifierImpl(X_train, X_test, y_train, y_test)
    
    # RandomForestClassifierGridSearchImpl(X_train, X_test, y_train, y_test)

if __name__ == "__main__":
    main()