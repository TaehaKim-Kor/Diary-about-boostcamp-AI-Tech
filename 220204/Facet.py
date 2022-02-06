import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


def facet_example(case):
    if case == 1:
        print("이건 너무 많이 했다. 살짝 변형을 줘보자.")
        #facecolor, dpi등등을 알아보자.
        #facecolor = 배경색 지정
        #fig에 한 경우에는 축배경이설정되고
        #ax에 한 경우에는 그래프배경이설정됨.
        #dpi = dots per inch -> 기본값은 100이고 이는 해상도를 의미.
        #figure를 저장하려면 fig.savefig하면됨. 여기서도 dpi지정 가능
        fig = plt.figure(dpi=150)
        ax = fig.add_subplot(121)
        ax.set_facecolor('tomato') #배경색지정
        ax = fig.add_subplot(122)
        ax.set_facecolor('royalblue')
        fig.set_facecolor('purple') #fig,ax다됨.
        plt.show()
        fig.savefig('file_name.png',dpi=300)
    elif case==2:
        print("sharex,sharey 해보자")
        np.random.seed(950718)
        #fig, ax = plt.subplots(1,2,figsize=(16,9),dpi=150, sharex=True, sharey=True)
        fig = plt.figure(figsize=(16,9),dpi=150)
        ax1 = fig.add_subplot(121)
        ax1.scatter(np.arange(10)+20,np.random.rand(10)+20,c='royalblue')
        ax1.set_xlim(-2,32)
        ax1.set_ylim(-2,32)
        ax2 = fig.add_subplot(122,sharex=ax1,sharey=ax1)
        ax2.scatter(np.arange(10),np.random.rand(10),c='royalblue')
        plt.show()
        #ax2는 축 한계를 지정해주지 않아도 ax1을 따라서 그리게 됨.
    elif case==3:
        print("Squeeze와 Flatten을 해보자")
        n,m = 1,3
        fig, ax = plt.subplots(n,m,squeeze=False,figsize=(n*2,m*2),dpi=150)
        #squeeze를 해제하지않으면 2차원배열로 읽지 못해 오류가 발생
        idx = 0
        for i in range(n):
            for j in range(m):
                ax[i][j].set_title(idx)
                ax[i][j].set_xticks([])
                ax[i][j].set_yticks([])
                idx += 1
        plt.show()
        fig, ax = plt.subplots(n,m,figsize=(n*2,m*2),dpi=150)
        #squeeze와 달리 flatten은 여기서 해주는거 아님.
        ax = ax.flatten()
        idx = 0
        for i, a in enumerate(ax):
            ax[i].set_title(idx)
            ax[i].set_xticks([])
            ax[i].set_yticks([])
            idx += 1
        plt.show()
    elif case==4:
        print("aspect는 어떨까?")
        fig=plt.figure(figsize=(16,9))
        ax1=fig.add_subplot(131,aspect=1)
        ax1.set_title("aspect=1")
        ax2=fig.add_subplot(132,aspect=0.5)
        ax2.set_title("aspect=0.5")
        ax3=fig.add_subplot(133,aspect=2)
        ax3.set_title("aspect=2")
        plt.show()
    elif case==5:
        print('gridspec을 써보자')
        #step 1 : figure 선언
        fig = plt.figure(figsize=(16,9))
        #step 2 : grid 선언
        gs = fig.add_gridspec(5,3)
        #step 2 : 원하는 grid별로 ax 선언
        ax1 = fig.add_subplot(gs[0,:]) #제일 윗줄 하나를 먹음
        ax1.set_facecolor("tomato")
        ax2 = fig.add_subplot(gs[1:,:2]) #1,0~3,1까지 정사각형으로 먹음
        ax2.set_facecolor("lightgreen")
        ax3 = fig.add_subplot(gs[1,2]) # 1,2쪽 그리드 한칸을 먹음
        ax3.set_facecolor("royalblue")
        ax4 = fig.add_subplot(gs[2:5,2]) # 2,1 ~ 4,1까지 직사각형으로 먹음
        ax4.set_facecolor("darkgrey")
        plt.show()
    elif case==6:
        print('subplot2grid를 써보자')
        fig = plt.figure(figsize=(16,9))
        ax = [None for _ in range(3)]
        ax[0] = plt.subplot2grid((2,3),(0,0),colspan=2, rowspan=1)
        ax[0].set_facecolor('tomato')
        ax[1] = plt.subplot2grid((2,3),(0,2),colspan=1, rowspan=2)
        ax[1].set_facecolor('royalblue')
        ax[2] = plt.subplot2grid((2,3),(1,0),colspan=2, rowspan=1)
        ax[2].set_facecolor('lightgreen')
        plt.show()
    elif case==7:
        print("원하는 위치에 그래프를 놓는것도 가능은 한데...추천하진않음.")
        fig = plt.figure(figsize=(8,5))
        ax = [None for _ in range(3)]
        ax[0]=fig.add_axes([0.1,0.1,0.8,0.4])
        ax[1]=fig.add_axes([0.15,0.6,0.25,0.6])
        ax[2]=fig.add_axes([0.5,0.6,0.4,0.3])
        plt.show()
        #벌써부터 짜증이...
    elif case==8:
        print('inset_axes를 써보자, 그래프 속 그래프, 미니맵같은걸 떠올려')
        fig, ax = plt.subplots()
        axin = ax.inset_axes([0.8,0.8,0.2,0.2])
        plt.show()
        print("이런 식으로도 활용가능하지. 2개의 그래프를 활용")
        fig, ax = plt.subplots()
        color=['purple','green']
        ax.bar(['A','B'],[1,2],color=color)
        ax.margins(0.2)
        axin = ax.inset_axes([0.8,0.8,0.2,0.2])
        axin.pie([1,2],colors=color,autopct='%1.0f%%')
        plt.show()
    elif case==9:
        from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
        print('make_axes_locatable을 사용해서 colorbar를 넣어보자.')
        fig, ax = plt.subplots()
        ax_divider = make_axes_locatable(ax)
        ax = ax_divider.append_axes("right",size="7%",pad="2%") #%로 값을 줌. 어디에 붙이느냐에 결정
        plt.show()
        fig, ax = plt.subplots()
        im = ax.imshow(100-np.arange(100).reshape((10,10)))
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right",size="5%",pad=0.05)
        fig.colorbar(im,cax=cax)
        plt.show()
if __name__=="__main__":
    case = 9
    facet_example(case)