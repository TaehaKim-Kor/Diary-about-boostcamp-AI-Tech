import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

def seaborn_example(case):
    student = pd.read_csv('StudentsPerformance.csv')
    heart = pd.read_csv('heart.csv')
    iris = pd.read_csv('iris.csv')
    if case == 1:
        print("Seaborn 맛보기")
        # Seaborn은 기본적으로 5가지 분류의 시각화와 형태를 제공
        # 1. Categorical
        # 2. Distribution
        # 3. Relational
        # 4. Regression
        # 5. Matrix
        sns.countplot(x='race/ethnicity',data=student)
        #Categorical API에서 사용되는 대표적인 시각화로, 범주를 이산적으로 세서 막대 그래프로 그려주는 함수
        #여기선 race/ethnicity의 범주에서 데이터의 갯수를 이산적으로 그려줄듯.
        #parameter는 x,y,data,hue(hue_order),palette,color,saturate,ax가 있음.
        #앞의 3개는 df의 feature, dict면 key를 의미.
        plt.show()
        sns.countplot(y='race/ethnicity',data=student)
        #x와 y의 방향만 바꿈.
        plt.show()
        #만약 방향설정이 원하는대로 되지 않는다면, oriented를 v/h로 전달하여 원하는 시각화를 진행
        #데이터의 순서가 정렬되지않아서 order로 지정해줌
        sns.countplot(x='race/ethnicity',data=student,order=sorted(student['race/ethnicity'].unique()))
        plt.show()
        #hue를 지정하면 데이터 구분 기준을 정하고 색상을 통해 내용을 구분함.
        sns.countplot(x='race/ethnicity',data=student,order=sorted(student['race/ethnicity'].unique()),
        hue='gender')
        plt.show()
        #palette로 색상을 바꿀 수 있음.
        sns.countplot(x='race/ethnicity',data=student,order=sorted(student['race/ethnicity'].unique()),hue='gender',
        palette='Set2')
        plt.show()
        #hue로 지정된 그룹을 gradient 색상을 전달할 수 있음.
        sns.countplot(x='gender',data=student,hue='race/ethnicity',color='red')
        plt.show()        
        #순서가 안맞으니 순서도 정해줌
        sns.countplot(x='gender',data=student,hue='race/ethnicity',color='red',hue_order=sorted(student['race/ethnicity'].unique()))
        plt.show()
        #saturation을 넣어주면 탁하게 만들 순 있는데.. 쓰진 않음.
        sns.countplot(x='gender',data=student,hue='race/ethnicity',color='red',hue_order=sorted(student['race/ethnicity'].unique()),saturation=0.3)
        plt.show()
    elif case==2:
        print('matplotlib과 같이 써보자')
        #ax에다가 ax를 넣어주면됨!
        fig, ax= plt.subplots(1,2,figsize=(16,9))
        sns.countplot(x='gender',data=student,hue='race/ethnicity',color='red',hue_order=sorted(student['race/ethnicity'].unique()),ax=ax[0])
        sns.countplot(x='gender',data=student,hue='race/ethnicity',hue_order=sorted(student['race/ethnicity'].unique()),ax=ax[1])
        ax[0].set_title('color = red')
        ax[1].set_title('color = None')
        plt.show()
    elif case==3:
        print("Categorical API를 배워보자")
        #count / Missing value = 갯수를 세줌 / 결측치를 세줌
        #mean = 평균을 내줌
        #std = 표준편차를 내줌
        #평균과 표준편차가 정규분포에 가깝지 않은 데이터가 포함되면 이를 나눠 생각해줘야함.
        #이럴땐 데이터의 중간값,%값(중앙값, 분위값)을 뽑는게 효율적이기도 함.
        #min,25%(lower quartile),50%(median),75%(upper quartile),max를 지칭함.
        print("Box plot을 배워보자.")
        fig, ax = plt.subplots(1,1,figsize=(16,9))
        sns.boxplot(x='math score',data=student,ax=ax)
        plt.show()
        #중앙 선 = medium / 박스의 왼쪽 = 25%, 오른쪽 = 75% 이 사이의 거리를 IQR(Interquartile range)라고 함.
        #수직선 2개와 수평선 1개 = 분포를 나타내는데, IQR의 1.5배만큼 거리를 좌우로 늘린 길이가 됨.(3배가됨)
        #이를 whisker라고하며 whikser 외의 값은 outlier가 됨.
        #참고로 좌우 길이가 다른 이유는 최대값이 100인데 이는 whisker 안에 있기 때문임.
        #min,max도 모두 whisker 안에서의 최소/최대값이 됨.
        #1.5배인 이유는 정규분포의 신뢰구간에 의해서 결정됨.
        print("여러 데이터와 범주도 한 번에 볼 수 있다.")
        fig, ax = plt.subplots(1,1,figsize=(16,9))
        sns.boxplot(x='race/ethnicity',y='math score',data=student,ax=ax,order=sorted(student['race/ethnicity'].unique()))
        plt.show()
        print("여러 데이터와 범주도 다른 범주에 대해서 한 번에 볼 수 있다.")
        fig, ax = plt.subplots(1,1,figsize=(16,9))
        sns.boxplot(x='race/ethnicity',y='math score',data=student,ax=ax,order=sorted(student['race/ethnicity'].unique()),hue='gender')
        plt.show()
        print("커스텀할 수 있는 요소를 보자")
        #width/linewidth/fliersize(박스의너비,선두께,아웃라이어의크기)
        sns.boxplot(x='race/ethnicity',y='math score',data=student,ax=ax,order=sorted(student['race/ethnicity'].unique()),hue='gender',
        width=0.3,linewidth=2,fliersize=10)
        plt.show()
    elif case==4:
        print("violin plot도 알아보자")
        #box plot은 대표값은 잘 보여주는데, 실제 분포를 보여주긴 좀 그래. 정확한 분포를 모름
        #분포를 이번엔 곡선으로 표현한 violin plot임.
        fig, ax =plt.subplots(1,1,figsize=(16,9))
        sns.violinplot(x='math score',data=student,ax=ax)
        plt.show()
        # 중간에 흰 점이 median / 두꺼운 막대가 25~75 / 검정색 얇은 선이 whisker
        # 영역은 histogram을 보간한 것임.
        # 근데 데이터를 오해하기 좋음(이산적인 값인데 연속적으로 표현하고 있어서.)
        # 거기에 연속적으로 그리기 위해서 kernel density estimate를 사용하여 근사되는 표현이 부정확함.
        # 결국 데이터에 없는 범위를 표현하려고 하다보니 저렇게 됨.(최대/최소보다 큰/작은 값을 던지기도 하고)
        print("알았어, 오해를 줄여보자")
        #bw = 분포표현을 얼마나 자세히 보여줄것인가(scott,silverman,float) -> 작아질수록 세세하게 나타내고, 너무작으면 별로
        #cut = 끝부분을 얼마나 자를 것인가(float)
        #inner = 내부를 어떻게 표현할 것인가(box,quartile,point,stick,None)
        #stick은 실제 값이 있는영역에만 보여주는듯? quartile은 quartile만 stick으로 보여주고
        fig, ax =plt.subplots(1,1,figsize=(16,9))
        sns.violinplot(x='math score',data=student,ax=ax,bw=0.05,cut=0,inner='stick')
        plt.show()
        print("x,y,hue를 또 써보면 마찬가지인가?")
        fig, ax =plt.subplots(1,1,figsize=(16,9))
        sns.violinplot(x='race/ethnicity',y='math score',data=student,ax=ax,bw=0.05,cut=0,inner='stick',hue='gender')
        plt.show()
        print('사실 violin은 반갈죽하는 맛이 있다지.(나머진 필요가 없거든)')
        #split 반씩쪼개서붙일 수 있음.
        #scale = 바이올린의 종류를 정함
        #area(넓이가 같게 비교)/count(데이터 숫자에 비례하여 비교)/width(기본값인가?)
        fig, ax =plt.subplots(1,1,figsize=(16,9))
        sns.violinplot(x='race/ethnicity',y='math score',data=student,ax=ax,bw=0.2,cut=0,inner='stick',hue='gender',scale='width',split=True)
        plt.show()
    elif case==5:
        print("기타 다른 플롯들을 알아보자")
        fig, ax = plt.subplots(1,3,figsize=(15,9))
        sns.boxenplot(x='race/ethnicity',y='math score',data=student, ax=ax[0], order=sorted(student['race/ethnicity'].unique()))
        sns.swarmplot(x='race/ethnicity',y='math score',data=student, ax=ax[1], order=sorted(student['race/ethnicity'].unique()))
        sns.stripplot(x='race/ethnicity',y='math score',data=student, ax=ax[2], order=sorted(student['race/ethnicity'].unique()))
        plt.show()
        #boxen : box에다가 부족한 부분을 histogram을 더해서 violin처럼 만들어놓음. 차라리 2개를 동시에보여주는게 나음
        #swarm : 실제 데이터가 몇개인지에 따른 양/밀도를 보여줘서 violin과 같이 씀
        #strip : 직선 막대에 데이터 밀도에 따라 점을 뿌려놓은 것
        #각 부분이 못보여주는 것을 나누어 보여주는 느낌이 있음.
    elif case==6:
        print("분포형 API를 보자")
        #범주형/연속형을 다 볼수있는 Distribution API임
        #histplot(히스토그램)/kdeplot(Kernel Density Estimate)/ecdfplot(누적 밀도 함수)/rugplot(선을 사용한 밀도 함수)
        fig, ax = plt.subplots(2,2,figsize=(12,10))
        ax=ax.flatten()
        sns.histplot(x='math score',data=student,ax=ax[0]) #히스토그램
        sns.kdeplot(x='math score',data=student,ax=ax[1]) #에다가 커널씌운거
        sns.ecdfplot(x='math score',data=student,ax=ax[2]) #점진적으로 더해가면서 누적분포를보여줌
        sns.rugplot(x='math score',data=student,ax=ax[3]) #실제 데이터가 어디있는지
        plt.show()
        print("조절할 수 있는건 다 조절해보자")
        fig, ax = plt.subplots(2,2,figsize=(12,10))
        ax=ax.flatten()
        
        #1번방안
        #sns.histplot(x='math score',data=student,ax=ax[0],bins=25,element='step')
        
        #2번방안
        #sns.histplot(x='math score',data=student,ax=ax[0],binwidth=10,element='poly')
        
        #히스토그램분포는 binwidth이나 bins로 막대간격/개수를 조절함(둘중하나만)
        #숫자의 크기에 따라 trade off가 있어서 적당히 잘 조절해야함.
        #그외에 표현방식을 element로 지정가능(step=연속적인,poly=다각형형태)
        #더 나아가서 성별로 나눠서 보면, 이 다수의 데이터를 어떻게 보여줄지 정하는 multiple이 있음.
        #fill = percentaged stacked bar chart로 표시 이게 오해를 불러일으킬 수 있음.(지양)
        #layer = 기본값임 겹쳐서 표현함
        #dodge = 그룹들을 이웃되게 연속되게 보여줌
        #stack = stacked bar chart로 표현해줌
        sns.histplot(x='math score',data=student,ax=ax[0],hue='gender',binwidth=10,element='poly',multiple='fill')
        
        #sns.kdeplot(x='math score',data=student,ax=ax[1])
        #연속 밀도 함수를 보여주는 함수인데, 선만 그려선 조금 표현하기 어려움.
        #fill은 항상 true로 넣어서 밀도표현/bw_method로 자세하게 표현
        #sns.kdeplot(x='math score',data=student,ax=ax[1], fill=True, bw_method=0.05)
        #다양한 정보를 표현하려면 아래처럼
        #cumulative를 True로 주면 누적분포로 때림. ecdf가 되는 것임.
        sns.kdeplot(x='math score',data=student,ax=ax[1], fill=True, bw_method=0.05,hue='race/ethnicity',hue_order=sorted(student['race/ethnicity'].unique()),multiple='stack',cumulative=True)
        
        #sns.ecdfplot(x='math score',data=student,ax=ax[2])
        #이거 별로 안쓰지만, 그래도 보자면 stat='proportion/count'과 complementary=True가 있음
        #비율로 볼지(stat)양으로볼지와 반대로볼지로 정할 수 있음.
        sns.ecdfplot(x='math score',data=student,ax=ax[2],stat='proportion',complementary=True)
        
        #sns.rugplot(x='math score',data=student,ax=ax[3])
        #조밀한 정도를 통해 밀도를 나타내는데 ㄹㅇ 안쓰는거같음. 한정된 공간 내에서 분포를 볼때 씀.
        #data의 gap이 클때나 사용
        sns.rugplot(x='math score',data=student,ax=ax[3])#바뀐게없네
        plt.show()
    elif case==7:
        print("Bivariate Distribution, 2개이상의 변수의 분포(결합 확률 분포)를 살펴보자")
        fig, ax=plt.subplots(1,3,figsize=(16,9))
        ax[0].set_aspect(1)
        sns.histplot(x='math score', y='reading score', data=student, ax=ax[0], cbar=True, bins=(20,20),color='orange')
        #histogram으로도 볼 수 있고
        #bins는 (10,20)으로 만들면 직사각형으로 나타낼 수 있음. 사실상 몇개로 나눌것인지니까 달라지면 직사각형이됨.
        ax[1].set_aspect(1)
        sns.kdeplot(x='math score',y='reading score',data=student,ax=ax[1],fill=True,bw_method=0.1)
        #kde로도 볼 수 있음.
        ax[2].set_aspect(1)
        ax[2].scatter(x=student['math score'],y=student['reading score'],alpha=0.5)
        #scatter로 표현할 때 점들이 겹쳐서 잘 안 보일 수 있는 것을 이렇게 표현하는 것으로 overplotting을 방지
        #가독성이 더 좋아짐
        plt.show()
    elif case==8:    
        print("Relation을 알아보자")
        #갑자기 Scatter가 나오네
        #scatter의 3요소 : style/hue/size (각각에대한 order지정가능)
        fig,ax=plt.subplots(figsize=(7,7))
        sns.scatterplot(x='math score',y='reading score',data=student,style='gender',markers={'male':'s','female':'o'},hue='race/ethnicity',size='writing score')
        #다쓰니 미쳤음, 걍 따로보는게 나음.
        plt.show()
        
        #갑자기 Line도 나오네!
        #시계열 데이터가 마땅한게 없어서, seaborn에서 제공하는 데이터를 가져옴
        #항상 데이터를 가져오면 어떻게생긴건지 봐야함
        flights=sns.load_dataset("flights")
        print(flights.sample(5))
        print(flights.shape)
        flights_wide=flights.pivot("year","month","passengers")
        fig, ax = plt.subplots(2,2,figsize=(16,9))
        ax=ax.flatten()
        sns.lineplot(x='year',y='Jan',data=flights_wide,ax=ax[0]) #한 월의 데이터
        sns.lineplot(x='year',y='passengers',data=flights,ax=ax[1]) #자동으로 평균과 표준편차로 오차범위를 시각화함
        sns.lineplot(data=flights_wide,ax=ax[2]) #모든 월의 데이터
        sns.lineplot(data=flights, x='year',y='passengers',hue='month',style='month',markers=True,dashes=False,ax=ax[3]) #옆의 그래프와 같을 것임.
        plt.show()
    elif case==9:
        print("Regression을 알아보자")
        #regplot : 회귀선을 추가한 scatter plot
        fig, ax = plt.subplots(1,3,figsize=(16,9))
        sns.regplot(x='math score',y='reading score',data=student, ax=ax[0])
        sns.regplot(x='math score',y='reading score',data=student, x_estimator=np.mean, x_bins=20,ax=ax[1],order=2)
        sns.regplot(x='writing score',y='reading score',data=student, ax=ax[2], logx=True)
        #x_estimator = 한 축에 한개의 값만 보여주는 경우에 사용
        #x_bins = 보여주는 값의 개수도 지정 가능
        #order = 회귀선의 차수, order=2면 2차함수, 1로 둬도 잘 예측됨. 2로둬도 1차함수처럼보임
        #logx = 로그의 형태로 보여줌.
        plt.show()
    elif case==10:
        print('Heatmap을 알아보자')
        print("일단 student의 상관관계는?")
        print(student.corr())
        #상관관계에 대한 것은 다양한 방법이 존재해서 Pearson/Spearman/Kendall등이 있음.
        #성적은 선형성때문에 대신 다른 데이터를 사용, heart임
        print("heart의 상관관계는?")
        print(heart.corr())
        #상관관계로 히트맵을 만들어보자
        fig,ax=plt.subplots(1,1,figsize=(7,7))
        ax.set_aspect(1)
        mask=np.zeros_like(heart.corr())
        mask[np.triu_indices_from(mask)]=True #하삼각행렬만 표시
        sns.heatmap(heart.corr(),ax=ax,vmin=-1,vmax=1,center=0,cmap='coolwarm',annot=True,fmt='.2f',linewidth=0.1,square=True,mask=mask, cbar=False)
        #vmin/vmax는 상관관계가 -1~1사이값이라서 그렇고, center로 0을주면 양/음의 상관관계를 따로낼수있음.
        #색이 조금 그래, 음/양의 관계를 고려해 diverse colormap coolwarm을 사용하면 보기좋음(cmap='coolwarm')
        #annot으로 실제 데이터 값을 넣을 수 있게 할 수 있고, fmt가 그 형식을 정해줌 이러면 cbar는 필요없음.
        #linewidth를 사용해 칸사이를 나눌수 있고, square를 사용하면 정사각형으로 나타낼 수도 있음.
        #상관관계는 대칭이기때문에 아래만 가져올 수 있음. 이를 mask를 통해 지정
        plt.show()
    elif case==11:
        print('Seaborn Advanced - Facet - joint plot을 알아보자')
        #joint plot은 2개 피처의 결합확률 분포와, 각각의 분포를 동시에 나타냄.
        #subplot넣으니까 오류나는거같음. 
        sns.jointplot(x='math score',y='reading score',data=student, height=7)
        plt.show()
        #height 적절히 조절
        sns.jointplot(x='math score',y='reading score',data=student, hue='gender')
        plt.show()
        sns.jointplot(x='math score',y='reading score',data=student, hue='gender',kind='hist')
        #kind = hist/scatter/kde/hex/reg/resid 등이 있음. 표시방식을 의미
        #hex,reg는 hue와 사용불가 , kde는 fill과 사용 가능
        plt.show()
    elif case==12:
        print('Seaborn Advanced - Facet - pair plot을 알아보자')
        #데이터셋의 pairwise관계를 알려줌(combination)
        sns.pairplot(data=iris) #다보여주네?
        plt.show()
        sns.pairplot(data=iris,hue='Species') #hue도 지정 가능.
        plt.show()
        #pairplot도 2가지 조절 변수가 있음.
        #kind : 주대각 요소 외에 보여주는 방식(scatter,kde,hist,reg)
        #diag_kind : 주대각요소의 보여주는 방식(auto,hist,kde,None)
        sns.pairplot(data=iris,hue='Species',diag_kind='kde') #kde fill True안되는데?;;
        plt.show()
        sns.pairplot(data=iris,hue='Species',diag_kind='kde',kind='reg',corner=True)
        #corner=True하면 상삼각행렬 정보를 지워버림
        plt.show()
    elif case==13:
        print('Seaborn Advanced - Facet - facet grid을 알아보자')
        #다중패널을 사용하는 시각화(pairplot같이)
        #catplot :categorical
        #         - stripplot(kind="strip") / swarmplot(kind="swarm")
        #         - boxplot(kind="box") / violinplot(kind="violin")
        #         - boxenplot(kind="boxen") / pointplot(kind="point")
        #         - barplot(kind="bar") / countplot(kind="count")
        sns.catplot(x='race/ethnicity',y='math score',hue='gender',data=student,order=sorted(student['race/ethnicity'].unique()),kind='box')
        plt.show()
        sns.catplot(x='race/ethnicity',y='math score',hue='gender',data=student,order=sorted(student['race/ethnicity'].unique()),kind='box',col='lunch',row='test preparation course')
        plt.show() #row/col을 지정해주니까 그거에 해당하는 plotting을 해줌. categorical한 내용들을 다 보여주네;;
        #displot :distribution
        #         - histplot(kind="hist")
        #         - kdeplot(kind="kde")
        #         - ecdfplot(kind="ecdf",univariate only)
        sns.displot(x="math score",hue='gender',data=student)
        plt.show()
        sns.displot(x="math score",hue='gender',data=student,col='race/ethnicity',col_order=sorted(student['race/ethnicity'].unique()),kind='kde',fill=True)
        plt.show()
        #relplot :relational
        #         - scatterplot(kind="scatter")
        #         - lineplot(kind="line")
        sns.relplot(x='math score',y='reading score',hue='gender',data=student,col='lunch')
        plt.show()
        sns.relplot(x='math score',y='reading score',hue='gender',data=student,col='lunch',kind='line')
        plt.show()
        #lmplot :regression
        #         - regplot
        sns.lmplot(x='math score',y='reading score',hue='gender',data=student)
        plt.show()
if __name__=="__main__":
    case=13
    if sns.__version__ != "0.11.0":
        print("Error may happen because of the different version.")
    seaborn_example(case)