import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

def color_example(case):
    student_data = pd.read_csv('StudentsPerformance.csv')
    groups = sorted(student_data['race/ethnicity'].unique())
    gton = dict(zip(groups, range(5))) #group을 숫자로 매칭
    student_data['color'] = student_data['race/ethnicity'].map(gton) #거기에 색상을 숫자로 매칭    
    if case==0:
        print("Toy problem으로 색상 매핑을 확인해보자.")
        fig, ax = plt.subplots(1,1,figsize=(16,9))
        ax.bar(np.arange(1,6,1), [3,6,9,12,15])
        ax.bar(np.arange(1,6,1), [2,4,6,8,10])
        ax.bar(np.arange(1,6,1), [1,2,3,4,5])
        plt.show()
    elif case==1:
        print("Color API에서, RGB보다 HSL 색공간이 조금 더 색을 이해하긴 편해!")
        # HSL이란
        # Hue(색조) : 빨강~초록~파랑~보라까지 있는 색상 스펙트럼을 360도로 돌려놓은 것
        # Saturate(채도) : 무채색과 채색과의 차이로, 선명도라고 볼 수 있음.(선명함 vs 탁함)
        # Lightness(광도) : 색상의 밝기(연함 vs 진함)
        # 이런 color pallete는 다양한 것을 사용할 수 있다. matplotlib에서
        # 예시 코드에 링크가 있으니 선택해서 사용할 수도 있음. R colormap도 괜찮음.
        print("범주형 색상, qualitative color pallete의 종류를 알아보자")
        print("Matplotlib에 있는 cm(colormap)모듈내 tab10(tabular10)의 색상 숫자를 가져오면")
        print(plt.cm.get_cmap('tab10').colors)
        from matplotlib.colors import ListedColormap #list로 전해주면 list내 원소로 색상으로 바꿔주는 함수
        qualitative_cm_list = ['Pastel1','Pastel2','Accent','Dark2','Set1','Set2','Set3','tab10']
        fig, ax = plt.subplots(2,4,figsize=(20,8))
        ax=ax.flatten()
        student_sub = student_data.sample(100)
        for idx,cm in enumerate(qualitative_cm_list):
            pcm = ax[idx].scatter(student_sub['math score'],student_sub['reading score'],
            c=student_sub['color'], #color는 안됨
            cmap = ListedColormap(plt.cm.get_cmap(cm).colors[:5])) #cmap의 위에서 5번째까지의 색상만을 사용함.)
            cbar = fig.colorbar(pcm, ax=ax[idx],ticks=range(5)) #색상 바를 subplot으로 만들기(색상정보,해당subplot,순서 순으로 넣어줌)
            cbar.ax.set_yticklabels(groups)#subplot인 색상바를 yticklabel로 ax에 넣어 주기
            ax[idx].set_title(cm)
        plt.show() #너무 많으면 잘 안보이니 5개~8개까지만
    elif case==2:
        print("연속형 색상에 대해서 알아보자")
        #2차원 시각화 heatmap, contour plot등에서 사용함.
        sequential_cm_list = ['Greys','Purples','Blues','Greens','Oranges','Reds','YlOrBr',
        'YlOrRd','OrRd','PuRd','RdPu','BuPu','GnBu','PuBu','YlGnBu','PuBuGn','BuGn','YlGn']
        fig, ax = plt.subplots(3,6,figsize=(25,10))
        ax=ax.flatten()
        for idx,cm in enumerate(sequential_cm_list):
            pcm = ax[idx].scatter(student_data['math score'],student_data['reading score'],
            c=student_data['reading score'],
            cmap=cm,
            vmin=0, vmax=100)
            fig.colorbar(pcm,ax=ax[idx])
            ax[idx].set_title(cm)
        plt.show()
    elif case==3:
        print("pyplot에서의 imshow를 알아보자.")
        im=np.arange(100).reshape(10,10)
        fig, ax = plt.subplots(figsize=(10,10))
        ax.imshow(im) #10x10의 숫자 데이터를 imshow로 해줌.
        plt.show()
    elif case==4:
        print("깃허브 잔디밭을 재배해보자.")
        im = np.random.randint(10,size=(7,52)) # 접속 기록, 0~9까지 숫자를 7x52로 만듬.
        fig, ax = plt.subplots(figsize=(20,5))
        ax.imshow(im, cmap="Greens") #깃허브 잔디밭 색상과 가장 유사
        ax.set_yticks(np.arange(7)+0.5, minor=True) #조정하진 않아도 됨. 테두리를 만드는 것임.
        ax.set_xticks(np.arange(52)+0.5, minor=True) #조정하진 않아도 됨. 테두리를 만드는 것임.
        ax.grid(which='minor',color='w',linestyle='-',linewidth=3) #격자로 띄우려고 이렇게함.
        plt.show() #이건 나중에 딥러닝에서 attention, highlight된 가중치들을 강조하는 방법으로도 사용.
    elif case==5:
        print("발산형 색상을 알아보자.")
        from matplotlib.colors import TwoSlopeNorm
        diverging_cm_list = ['PiYG','PRGn','BrBG','PuOr','RdGy','RdBu',
        'RdYlBu','RdYlGn','Spectral','coolwarm','bwr','seismic']
        fig, ax=plt.subplots(3,4,figsize=(20,15))
        ax=ax.flatten() #2차원 ndarray로 되어있는 ax를 1차원 배열로 만들어주는 트릭 
        offset = TwoSlopeNorm(vmin=0,vcenter=student_data['reading score'].mean(),vmax=100)
        print(student_data['reading score'].mean(), offset([0,10,20,30,50,60,69,70,85,90,95,100]))
        #0~읽기성적평균까지를 0~0.5, 읽기성적평균~100까지를 0.5~1까지로 평균화시킴 그래서 2개의 기울기
        student_sub=student_data.sample(100)
        for idx,cm in enumerate(diverging_cm_list):
            pcm = ax[idx].scatter(student_sub['math score'],student_sub['reading score'],
            c=offset(student_sub['math score']),
            cmap=cm)
            cbar = fig.colorbar(pcm,ax=ax[idx],ticks=[0,0.5,1],orientation='horizontal')
            cbar.ax.set_xticklabels([0,student_data['math score'].mean(),100])
            ax[idx].set_title(cm)
        plt.show()
        #그림에서 보이는 흰색 부분이 평균에 해당하는 부분임. 2개의 그림이 나타냄.
    elif case==6:
        print("특정 부분 강조를 위한 시각화를 해보자!")
        groups = student_data['race/ethnicity'].value_counts().sort_index()
        fig = plt.figure(figsize=(18,15))
        ax1 = fig.add_subplot(211)
        ax1.bar(groups.index, groups, width=0.5)
        ax_s1 = fig.add_subplot(2,3,4)
        ax_s2 = fig.add_subplot(2,3,5)
        ax_s3 = fig.add_subplot(2,3,6)
        ax_s1.scatter(student_data['math score'],student_data['reading score'])
        ax_s2.scatter(student_data['math score'],student_data['writing score'])
        ax_s3.scatter(student_data['writing score'],student_data['reading score'])
        for ax in [ax_s1,ax_s2,ax_s3]:
            ax.set_xlim(-2,105)
            ax.set_ylim(-2,105)
        plt.show()
        #이렇게만하면 각각의 group에 대해서는 알 수가 없음.
    elif case==7:
        print("명도 대비를 해보자")
        ac, nc = 'black', 'lightgray'#a_color, not_a_color
        colors = student_data['race/ethnicity'].apply(lambda x : ac if x =='group A' else nc)
        color_bars = [ac]+[nc]*4
        groups = student_data['race/ethnicity'].value_counts().sort_index()
        fig = plt.figure(figsize=(18,15))
        ax1 = fig.add_subplot(211)
        ax1.bar(groups.index, groups, width=0.5, color=color_bars)
        ax_s1 = fig.add_subplot(2,3,4)
        ax_s2 = fig.add_subplot(2,3,5)
        ax_s3 = fig.add_subplot(2,3,6)
        ax_s1.scatter(student_data['math score'],student_data['reading score'],color=colors,alpha=0.5)
        ax_s2.scatter(student_data['math score'],student_data['writing score'],color=colors,alpha=0.5)
        ax_s3.scatter(student_data['writing score'],student_data['reading score'],color=colors,alpha=0.5)
        for ax in [ax_s1,ax_s2,ax_s3]:
            ax.set_xlim(-2,105)
            ax.set_ylim(-2,105)
        plt.show()
    elif case==8:
        print("채도 대비를 해보자")
        ac, nc = 'orange', 'black'#a_color, not_a_color 명도도조절해주면 강조가 더 좋음(lightgray)
        colors = student_data['race/ethnicity'].apply(lambda x : ac if x =='group B' else nc)
        color_bars = [ac]+[nc]*4
        groups = student_data['race/ethnicity'].value_counts().sort_index()
        fig = plt.figure(figsize=(18,15))
        ax1 = fig.add_subplot(211)
        ax1.bar(groups.index, groups, width=0.5, color=color_bars)
        ax_s1 = fig.add_subplot(2,3,4)
        ax_s2 = fig.add_subplot(2,3,5)
        ax_s3 = fig.add_subplot(2,3,6)
        ax_s1.scatter(student_data['math score'],student_data['reading score'],color=colors,alpha=0.5)
        ax_s2.scatter(student_data['math score'],student_data['writing score'],color=colors,alpha=0.5)
        ax_s3.scatter(student_data['writing score'],student_data['reading score'],color=colors,alpha=0.5)
        for ax in [ax_s1,ax_s2,ax_s3]:
            ax.set_xlim(-2,105)
            ax.set_ylim(-2,105)
        plt.show()
    elif case==9:
        print("보색 대비를 해보자")
        ac, nc = 'tomato', 'lightgreen'#a_color, not_a_color 둘이합쳐서 흰색이면 보색관계
        colors = student_data['race/ethnicity'].apply(lambda x : ac if x =='group A' else nc)
        color_bars = [ac]+[nc]*4
        groups = student_data['race/ethnicity'].value_counts().sort_index()
        fig = plt.figure(figsize=(18,15))
        ax1 = fig.add_subplot(211)
        ax1.bar(groups.index, groups, width=0.5, color=color_bars)
        ax_s1 = fig.add_subplot(2,3,4)
        ax_s2 = fig.add_subplot(2,3,5)
        ax_s3 = fig.add_subplot(2,3,6)
        ax_s1.scatter(student_data['math score'],student_data['reading score'],color=colors,alpha=0.5)
        ax_s2.scatter(student_data['math score'],student_data['writing score'],color=colors,alpha=0.5)
        ax_s3.scatter(student_data['writing score'],student_data['reading score'],color=colors,alpha=0.5)
        for ax in [ax_s1,ax_s2,ax_s3]:
            ax.set_xlim(-2,105)
            ax.set_ylim(-2,105)
        plt.show()
if __name__=="__main__":
    case = 9
    color_example(case)