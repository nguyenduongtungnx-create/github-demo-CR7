import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score,recall_score,f1_score,classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from sklearn.model_selection import GridSearchCV
from ydata_profiling import ProfileReport
"""
data = pd.read_csv("diabetes.csv")

# Tạo báo cáo
#profile = ProfileReport(data, title="Diabetes Profiling Report")
#profile.to_file("report.html")  # Xuất ra file HTML để xem
target = "Outcome"
x = data.drop(target,axis =1)
y = data[target]
# library : scikit-learn
# train set or test set
x_train, x_test, y_train ,y_test = train_test_split(
    x,y,
    test_size = 0.2,
    random_state = 1009  # de nhung lan tiếp theo han che dung nhung bo test khac nhau=> luôn giu nguyen
)
# data processing => use the min and  max scaler(normalization) , standardScaler (standardzation)=> sẽ được uu chuong hon cái truocs
# it bị ảnh hưởng bởi outlier

scaler = StandardScaler()
# method function
scaler.fit(x_train) # use to measure
output  = scaler.transform(x_train) # based on the measurement number to do something
#scaler.fit_transform() # to be back the past to do the similar ones without the new requirement if don't need

#model = RandomForestClassifier(random_state = 100)
model = LogisticRegression()
model.fit(x_train,y_train)

y_predict = model.predict(x_test)
print(y_predict)
#for i,j in zip(y_predict, y_test):
    #print("Prediction : {}.Actual value :{}".format(i,j))
print("ACC :{}".format(accuracy_score(y_test, y_predict)))
print("Pre :{}".format(precision_score(y_test, y_predict)))
print("Re :{}".format(recall_score(y_test, y_predict)))
print("F1 :{}".format(f1_score(y_test, y_predict)))
"""
# homework
df =  pd.read_csv('your_data.csv')
#drop two columns
df = df.drop(columns=['team_a_rounds','team_b_round'])
profile = ProfileReport(df,title ="CS Match Data Report",exploration = True)
profile.to_file("report.html")
