import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

def scatter_plot_example(case):
    np.random.seed(950718)
    iris=pd.read_csv('Iris.csv')
    slc_mean=iris['SepalLengthCm'].mean()
    swc_mean=iris['SepalWidthCm'].mean()
    if case == 1:
        print("scatter plot을 그려보자")
        fig, ax = plt.subplots(1,1,figsize=(16,9))
        x=np.random.rand(20)
        y=np.random.rand(20)
        ax.scatter(x,y)
        plt.show()
    elif case==2:
        print("scatter의 다양한 요소를 활용해 그려보자")
        fig, ax = plt.subplots(1,1,figsize=(16,9))
        x=np.random.rand(20)
        y=np.random.randn(20)+1
        z=np.random.randn(20)+2
        ax.scatter(x,y,s=150,c='#00FF00',marker='^',linewidth=1,edgecolor='#000000')
        ax.scatter(x,z,s=200,c='#FF0000',marker='o',linewidth=1,edgecolor='#000000')
        plt.show()
    elif case==3:
        print("실제 데이터를 활용해보자")
        print(iris.describe(include='all'))
        fig, ax = plt.subplots(1,2,figsize=(16,9))
        ax[0].scatter(iris['SepalLengthCm'],iris['SepalWidthCm'],
        c=['#FF0000' if xx <= swc_mean else "#0000FF" for xx in iris['SepalWidthCm']]) # list comprehension 과 연계하여 조건에 맞는 색을 입히기도 가능!
        ax[0].set_title('SepalLengthCm vs SepalWidthCm')
        ax[1].scatter(iris['SepalLengthCm'],iris['PetalLengthCm'], c=['#FF0000' if xx <= slc_mean else "#0000FF" for xx in iris['SepalLengthCm']])
        ax[1].set_title('SepalLengthCm vs PetalLengthCm')
        plt.show()
        #이거가지곤 감이 잘 안오긴 함. 색을 입히지않으면 더 몰랐을듯!
    elif case==4:
        print("color에서 다 조정하는게 아니라, 어떤 조건마다 scatter를 그리는 것도 방법임.")
        print("legend를 그래프마다 결정해줄 수 있기 때문임.")
        fig, ax = plt.subplots(1,2,figsize=(16,9))
        for species in iris['Species'].unique(): 
            iris_sub = iris[iris['Species']==species]#종에 맞는 데이터만을 뽑음
            ax[0].scatter(x=iris_sub['SepalLengthCm'], y=iris_sub['SepalWidthCm'], label=species)
            ax[1].scatter(x=iris_sub['SepalLengthCm'], y=iris_sub['PetalLengthCm'], label=species)
        ax[0].legend()
        ax[1].legend()
        plt.show()
        #이렇게까지 해주니 드디어 양의 상관관계가 조금 보이기 시작함.
        #petal(꽃잎)만 가지고 한다면 더 clustering이 잘 된다는 것을 볼 수 있음.
    elif case==5:
        print("보조선도 놓고 해볼까?")
        fig, ax = plt.subplots(1,2,figsize=(16,9))
        for species in iris['Species'].unique(): 
            iris_sub = iris[iris['Species']==species]#종에 맞는 데이터만을 뽑음
            ax[0].scatter(x=iris_sub['PetalLengthCm'], y=iris_sub['PetalWidthCm'], label=species)
            ax[1].scatter(x=iris_sub['SepalLengthCm'], y=iris_sub['PetalLengthCm'], label=species)
        ax[0].axvline(2.5, color='gray', linestyle=":")
        ax[0].axhline(0.8, color='gray', linestyle=":")
        ax[1].axhline(4.9, color='#AAAAAA', linestyle=":")
        ax[1].axhline(2.1, color='#AAAAAA', linestyle=":")
        ax[0].legend()
        ax[1].legend()
        plt.show()
    elif case==6:
        print("한번에 여러 개의 데이터의 상관관계를 나타낸 그래프를 이중 반복문을 통해 구현해 볼까?")
        #step 1 : feature 이름들에 대한 list를 만들기
        feature_list = ['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']
        # 또는
        feature_list = [i for i in list(iris.columns.unique())]
        feature_list.pop(feature_list.index('Id'))
        feature_list.pop(feature_list.index('Species'))
        #step 2 : feature 갯수만큼 정방 figure 만들기
        fig, axes = plt.subplots(len(feature_list),len(feature_list),figsize=(14,14))
        #step 3 : enumerate를 활용하여 이중반복문을 구현해 ax 채우기.
        for i, f1 in enumerate(feature_list):
            for j, f2 in enumerate(feature_list):
                if i <= j : #한쪽만 하면 됨. 주대각요소부터 밑에 있는 요소들은 날릴 것임.
                    axes[i][j].set_visible(False)
                    continue
                for species in iris['Species'].unique():
                    iris_sub = iris[iris['Species']==species]
                    axes[i][j].scatter(x=iris_sub[f2],y=iris_sub[f1],label=species,alpha=0.7)
                if i==3: axes[i][j].set_xlabel(f2)
                if j==0: axes[i][j].set_ylabel(f1)
        #step 4: 출력해주면 됨.
        plt.tight_layout()
        plt.show()
        #이건 seaborn의 pairplot으로 볼 수 있는 기능.

if __name__ == "__main__":
    case=6
    scatter_plot_example(case)