import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

def moretips_example(case):
    np.random.seed(950718)
    student=pd.read_csv("StudentsPerformance.csv")
    if case==1:
        print("grid를 살펴보자")
        #그리드를 이루는 5가지
        # which : major ticks, minor ticks(주 보조선, 부 보조선)
        # axis : 축방향
        # linestyle
        # linewidth
        # zorder
        x=np.random.rand(20)
        y=np.random.rand(20)
        fig = plt.figure(figsize=(16,9))    
        ax = fig.add_subplot(1,1,1,aspect=1)
        ax.scatter(x,y,s=150,c="#1ABDE9",linewidth = 1.5, edgecolor='black', zorder=10)
        ax.set_xlim(0,1.1)
        ax.set_ylim(0,1.1)
        ax.set_xticks(np.linspace(0,1.1,12,endpoint=True),minor=True) #minor를 어떻게할지도 선언.
        ax.grid(zorder=0,linestyle='--',which='both',axis='both',linewidth=2) #which, axis 모두 both, minor, major 셋다 설정가능
        ax.set_title("Grid example")
        plt.tight_layout()
        plt.show()
        #scatter의 사이즈에따라 grid의 어느 구간에 있는지 안 보일수있음. 이게 상성이 안좋은 이유임.
    elif case==2:
        print("다양한 그리드를 그려보자.")
        x=np.random.rand(20)
        y=np.random.rand(20)
        fig = plt.figure(figsize=(16,9))    
        ax = fig.add_subplot(1,1,1,aspect=1)
        ax.scatter(x,y,s=150,c=["#1ABDE9" if xx+yy <1.0 else "#9EDBA1" for xx,yy in zip(x,y)],linewidth = 1.5, edgecolor='black', zorder=10)
        ax.set_xlim(0,1.1)
        ax.set_ylim(0,1.1)
        ax.set_title("Various grid")

        #grid_part : x+y=c
        x_start = np.linspace(0,2.2,12,endpoint=True) #절편을 선언해서 x절편/y절편끼리 이음.
        for xs in x_start:
            ax.plot([xs,0],[0,xs], linestyle='--',color='#AAAAAA',alpha=0.5,linewidth=1)
        
        #grid_part : y=cx 
        radian = np.linspace(0,np.pi/2,10,endpoint=True)#극좌표계와 유사하게 각좌표를 선언
        for rad in radian:
            ax.plot([0,2],[0,2*np.tan(rad)], linestyle='--',color='#777777',alpha=0.5,linewidth=1)
            #기울기가 tan(rad)가 되고, rad마다 2를 곱한것까지계산하면 그래프밖까지 grid를 그려서 다 보이게 됨.
        
        #grid_part : 동심원
        radius = np.linspace(0.1, 0.8, 8, endpoint=True)#반지름을 선언
        for r in radius:
            xx=r*np.cos(np.linspace(0,2*np.pi,100))
            yy=r*np.sin(np.linspace(0,2*np.pi,100))
            ax.plot(xx+x[2],yy+y[2],linestyle='--',color="#DDDDDD",alpha=0.5,linewidth=1)
            #x[2],y[2]를 중심으로 r만큼 떨어져있는 점의 집합을 잇는다.
            #반지름마다 값마킹
            ax.text(x[2]+r*np.cos(np.pi/4),y[2]-r*np.sin(np.pi/4),f'{r:.1}',color='#DDDDDD')
        #중심에 마킹
        ax.text(x[2],y[2]+0.05,s='Center',fontweight='semibold',bbox=dict(boxstyle='round',fc='wheat',ec='black'),ha='center',va='center')
        ax.scatter(x[2],y[2],s=150,color="#FF0000",linewidth=1.5,edgecolor='black',zorder=11,alpha=0.3)

        plt.tight_layout()
        plt.show()
    elif case==3:
        print("Line과 Span을 그려보자!")
        fig, ax = plt.subplots()
        ax.set_aspect(1)
        #Line 일부분만 그리기
        ax.axvline(0,ymin=0.3,ymax=0.7, color='#110000', alpha=0.5, zorder=10)
        ax.axhline(0,xmin=0.3,xmax=0.7, color='#001100', alpha=0.5, zorder=10)
        #Line 쭉 그리기
        ax.axvline(0, color='#FF0000', alpha=0.5, zorder=9)
        ax.axhline(0, color='#00FF00', alpha=0.5, zorder=9)
        #Span 그리기
        ax.axvspan(-0.2,0.2,color='red', alpha=0.3, zorder=8)
        ax.axhspan(-0.2,0.2,color='green', alpha=0.3, zorder=8)
        ax.set_xlim(-1,1)
        ax.set_ylim(-1,1)
        plt.show()
    elif case==4:
        print("실제 데이터로 그려보자!")
        # Line을 기준으로 데이터를 나눠보자!
        fig, ax = plt.subplots(figsize=(9,9))
        math_mean = student['math score'].mean()
        read_mean = student['reading score'].mean()
        color = ['#FFFF00' if m>math_mean and r>read_mean else 
        ("#FF0000" if m > math_mean and r <= read_mean else 
        ("#00FF00" if m <= math_mean and r>read_mean else 
        "#000000") ) for m,r in zip(student['math score'], student['reading score'])]
        #ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
        ax.scatter(student['math score'],student['reading score'],c=color,alpha=0.35,zorder=11)
        ax.set_aspect(1)
        ax.set_xlabel('Math Score')
        ax.set_ylabel('Reading Score')
        ax.set_xlim(-3,103)
        ax.set_ylim(-3,103)
        #평균에 대해서 선 그리기 강조를 위해 무채색으로 안 그림.
        ax.axvline(math_mean,color='#FF0000', linestyle='--',linewidth=1.5, alpha=0.5,zorder=2)
        ax.axhline(read_mean,color='#00FF00', linestyle='--',linewidth=1.5, alpha=0.5,zorder=2)
        #평균의 50%보다 낮은 영역을 표시해보자!
        ax.axvspan(0,math_mean/2,color='gray',alpha=0.5,zorder=1,linestyle=':')
        ax.axhspan(0,read_mean/2,color='gray',alpha=0.5,zorder=1,linestyle=':')
        fig.suptitle("Score correlation between\nmath score and reading score")
        plt.show()
    elif case==5:
        print("바깥쪽 테두리를 조절해보자!")    
        fig, ax = plt.subplots(1,2,figsize=(9,9))
        math_mean = student['math score'].mean()
        read_mean = student['reading score'].mean()
        color = ['#BBBB00' if m>math_mean and r>read_mean else 
        ("#BB0000" if m > math_mean and r <= read_mean else 
        ("#00BB00" if m <= math_mean and r>read_mean else 
        "#000000") ) for m,r in zip(student['math score'], student['reading score'])]
        ax[0].scatter(student['math score'],student['reading score'],c=color,alpha=0.35,zorder=11)
        ax[0].spines['top'].set_visible(False)
        ax[0].spines['right'].set_visible(False)
        ax[0].spines['left'].set_linewidth(1.5)
        ax[0].spines['bottom'].set_linewidth(1.5)
        ax[1].scatter(student['math score'],student['reading score'],c=color,alpha=0.35,zorder=11)
        ax[1].spines['top'].set_position('center')
        ax[1].spines['right'].set_position('center') #선이 움직인 것을 볼 수 있음.
        #저 값들은 center = ('axes', 0.5) , zero = ('data',0) 이런식으로 바꿔서 넣어줄 수도 있음.
        ax[1].spines['left'].set_linewidth(1.5)
        ax[1].spines['bottom'].set_linewidth(1.5)
        plt.show()
        print("현실적으로 활용해볼까?")
        fig, ax = plt.subplots(1,2,figsize=(16,9))
        x = np.linspace(-np.pi,np.pi,1001,endpoint=True)
        y1 = np.cos(x)
        y2 = np.tanh(x)+1
        ax[0].plot(x,y1)
        ax[1].plot(x,y2)
        for a in ax:
            a.spines['top'].set_visible(False)
            a.spines['right'].set_visible(False)
        ax[0].spines['left'].set_position('center')
        ax[0].spines['bottom'].set_position('center')
        ax[1].spines['left'].set_position(('data',0)) #=center지만, 뭐 그래도 값으로도 정할 수 있다.
        ax[1].spines['bottom'].set_position(('axes',0)) #=center지만, 뭐 그래도 값으로도 정할 수 있다.
        ax[0].set_xlim(-np.pi-1,np.pi+1)
        ax[0].set_ylim(-2,2)
        ax[1].set_xlim(-np.pi-1,np.pi+1)
        ax[1].set_ylim(0,2)
        plt.show()
    elif case==6:
        print("세팅 일괄 변경을 사용해보자!")
        #matplotlib에서 잘 나와있긴한데.
        #rcparams -> 실행전에 앞서서 실행되는 parameter 설정,
        #rc = run commands라는 의미로 라이브러리 실행과 동시에 실행됨.
        print("이건 예시이다!")
        
        #이러면 기본값이 저렇게 바뀜.
        mpl.rcParams['lines.linewidth']=2
        mpl.rcParams['lines.linestyle']='--'
        #plt라고 써도 가능함.
        fig, ax = plt.subplots(1,3,figsize=(16,9))
        x = np.linspace(-np.pi,np.pi,1001,endpoint=True)
        y1 = np.cos(x)
        y2 = np.tanh(x)+1
        y3 = np.sin(x)
        ax[0].plot(x,y1)
        ax[0].spines['left'].set_position('center')
        ax[0].spines['bottom'].set_position('center')
        ax[0].set_xlim(-np.pi-1,np.pi+1)
        ax[0].set_ylim(-2,2)
        ax[0].set_title("RCParams Changed")
        #이것도 가능
        mpl.rc('lines', linewidth=4, linestyle=":")
        ax[1].plot(x,y2)
        ax[1].spines['left'].set_position(('data',0)) 
        ax[1].spines['bottom'].set_position(('axes',0)) 
        ax[1].set_xlim(-np.pi-1,np.pi+1)
        ax[1].set_ylim(0,2)
        ax[1].set_title("RCParams Rechanged")
        #다시 원래대로 되돌려줌.
        mpl.rcParams.update(plt.rcParamsDefault)
        ax[2].plot(x,y3)
        ax[2].spines['left'].set_position('center')
        ax[2].spines['bottom'].set_position('center')
        ax[2].set_xlim(-np.pi-1,np.pi+1)
        ax[2].set_ylim(-2,2)
        ax[2].set_title("RCParams Returned")
        for a in ax:
            a.spines['top'].set_visible(False)
            a.spines['right'].set_visible(False)
        fig.suptitle("Text default changed!")
        plt.show()
    elif case==7:
        print("테마를 사용해보자!")
        print("사용가능한 테마는 아래와 같다.")
        print(mpl.style.available)
        print("사용 하는 방법을 알아보자")
        #1번 seaborn, ggplot, fivethirtyeight 등등도 가능
        mpl.style.use('ggplot')
        plt.plot([1,2,3])
        plt.show()
        #2번
        with plt.style.context('fivethirtyeight'):
            plt.plot(np.sin(np.linspace(0,2*np.pi)))
        plt.show()
        #3번 같은건데 seaborn도 보자
        with plt.style.context('seaborn'):
            plt.plot(np.sin(np.linspace(0,2*np.pi)))
        plt.show()



if __name__=="__main__":
    case = 7
    moretips_example(case)