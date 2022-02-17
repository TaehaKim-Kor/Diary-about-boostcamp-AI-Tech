import numpy as np
from sklearn.linear_model import LinearRegression
import mlflow
import mlflow.sklearn
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
if __name__=="__main__":
    np.random.seed(950718)
    x_train = np.arange(101)
    y_train = np.arange(101)
    noise_train = np.random.randn(101)
    np.random.seed(950718)
    x_test = np.random.rand(50) * 100
    y_test = np.random.rand(50) * 100
    noise_test = np.random.randn(50)
    z_train = 2*x_train+3*y_train+noise_train
    z_test = 2*x_test+3*y_test+noise_test
    train_data = np.transpose(np.array([x_train,y_train]), (1,0))
    test_data = np.transpose(np.array([x_test,y_test]), (1,0))
    reg = LinearRegression().fit(train_data,z_train)
    trainscore = reg.score(train_data,z_train)
    testscore = reg.score(test_data,z_test)
    print('train score is',trainscore)
    print('test score is',testscore)
    mlflow.log_metric('train_score',trainscore)
    mlflow.log_metric('test_score',testscore)
    mlflow.sklearn.log_model(reg,"model")
    #fig = plt.figure(figsize=(16,9))
    #ax = fig.add_subplot(1,2,1 ,projection='3d')
    #ax.set_title('train data')
    #ax.scatter(train_data[:,0],train_data[:,1],z_train,c='red')
    #ax.set_xlabel('x')
    #ax.set_ylabel('y')
    #ax.set_zlabel('z')
    #ax = fig.add_subplot(1,2,2 ,projection='3d')
    #ax.set_title('test data')
    #ax.scatter(test_data[:,0],test_data[:,1],z_test,c='red')
    #ax.set_xlabel('x')
    #ax.set_ylabel('y')
    #ax.set_zlabel('z')
    #plt.show()

