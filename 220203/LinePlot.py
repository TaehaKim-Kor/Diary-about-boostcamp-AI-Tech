import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

def line_plot_example(case):
    stock = pd.read_csv("prices.csv") # kaggle에 있는 주식데이터셋
    #stock.set_index("date", inplace=True) 
    #날짜 데이터순으로 정렬하기 위해서 아래처럼 작성
    stock['date'] = pd.to_datetime(stock['date'],format='%Y-%m-%d', errors='raise') # 날짜가 문자열이라 정렬이 잘 안 되는 것을 수정
    stock.set_index("date", inplace=True) # 날짜순으로 데이터 정렬
    #회사별 주식 뽑기
    apple = stock[stock['symbol']=="AAPL"]
    google = stock[stock['symbol']=="GOOGL"]       
    if case == 1:
        print("기본적인 line plot 그려보기")
        x1 = [1,2,3,4,5] #x 좌표
        x2 = [1,3,2,4,5] #x 좌표가 조금 이상해!
        # line을 그릴 때는 x값에 들어가는 것은 정렬해두는것이 좋음.
        y= [1,3,2,1,5] # 관측치
        fig, ax = plt.subplots(1,2,figsize=(16,9))
        ax[0].plot(x1,y, marker="o", color="#AAAA00") #line plot은 plot으로 그림(line 아님!)
        # (1,1) (2,3) (3,2) (4,1) (5,5)
        ax[1].plot(x2,y, marker='x', color="#0000BB") #각 리스트에서 하나씩 뽑아서 리스트 순서대로 (x,y)에 점을찍고 이전 점과 잇는 방식임.
        # (1,1) (3,3) (2,2) (4,1) (5,5)
        plt.show()
    elif case == 2:
        print("line plot의 특성을 이용해서 line plot으로 정n각형 그리기")
        n = 10 # n-1각형을 그리기 1000쯤 주니 원같음.
        x = np.sin(np.linspace(0,2*np.pi,n)) #0부터 2pi 사이에 n개의 점을 찍고 sin을 줌.
        y = np.cos(np.linspace(0,2*np.pi,n)) #0부터 2pi 사이에 n개의 점을 찍고 cos을 줌.
        # 이제보니 원리가.. step = t에서의 (x(t),y(t)) = (sin(t/{2*pi*n}),cos(t/{2*pi*n}))이네
        # sin,cos 바꿔도 됨. 사실 각좌표계에선 이게 더 보편적이긴 하지.
        fig = plt.figure(figsize=(9,9))
        ax = fig.add_subplot(111, aspect=1)
        ax.plot(x,y)
        plt.show()
    elif case == 3:
        print("마커, 선종류를 정해보기")
        np.random.seed(7) # 난수 발생용 seed 결정
        fig, ax = plt.subplots(1,1,figsize=(5,5))
        x = np.arange(7)
        y = np.random.rand(7)
        ax.plot(x,y, color="royalblue", marker="*", linestyle=":")
        # marker 는 지원하는게 많음.
        # linestyle은 모양을 주거나 이름을 주는 방법이 있음.
        # None도 있고(=scatter, 안 씀), solid = 실선(안 씀, 기본값임), dashed = 점선(:), dashdot = 점선긴선점선(-.)
        plt.show()
    elif case == 4:
        print("실제 데이터 가지고 해보자.")
        print(google.sample(5))
        fig, ax = plt.subplots(1,1,figsize=(16,9))
        ax.plot(google.index, google['close'], color="tomato", label='google')
        ax.plot(apple.index, apple['close'], color="royalblue",label='apple')
        ax.legend()
        plt.show()
    elif case == 5:
        print("이동 평균을 활용한 데이터 전처리로 noise를 제거해보자.")
        window_num = 20
        google_rolling = google.rolling(window=window_num).mean() #굳이 반복문으로 데이터를 처리하지 않아도
        print(google_rolling.head(window_num+5))
        #rolling이 window에 할당된 데이터만큼 평균내서 값을 알려줌. -> 단 window를 만족 못하는 앞의 데이터는 삭제됨.
        apple_rolling = apple.rolling(window=window_num).mean()
        fig, ax = plt.subplots(2,1,figsize=(16,9), dpi = 100, sharex=True) #dpi = 해상도
        ax[0].plot(google.index, google['close'], color="tomato", label='google')
        ax[0].plot(apple.index, apple['close'], color="royalblue",label='apple')
        ax[0].set_title("original_data")
        ax[0].legend()
        ax[1].plot(google_rolling.index, google_rolling['close'], color="tomato", label='google')
        ax[1].plot(apple_rolling.index, apple_rolling['close'], color="royalblue",label='apple')
        ax[1].set_title(f"moving_slide_data, window_size is {window_num}")
        ax[1].legend()
        plt.show()
    elif case==6:
        print("추세(information)에 집중하거나 기록(clean)에 집중해서 보는 방법을 활용해 data를 분석")
        from matplotlib.ticker import MultipleLocator
        fig = plt.figure(figsize=(16,9))
        np.random.seed(950718)
        length = 10
        x = np.arange(length)
        y = np.random.rand(len(x))
        #기록에 집중해서 보자!
        ax1 =fig.add_subplot(121)
        ax1.plot(x,y,marker='o',linewidth=2,color='#00FF00')
        ax1.xaxis.set_major_locator(MultipleLocator(1))
        ax1.yaxis.set_major_locator(MultipleLocator(0.05))
        ax1.grid(linewidth=0.3)
        ax1.set_title("clean version", loc='left', fontsize=12, va='bottom', fontweight='semibold')
        #추세에 집중해서 보자!
        ax2 = fig.add_subplot(122)
        ax2.plot(x,y,linewidth=2,color='#00FF00')
        ax2.spines['top'].set_visible(False)
        ax2.spines['right'].set_visible(False)
        ax2.set_title("information version", loc='left', fontsize=12, va='bottom', fontweight='semibold')
        plt.show()
    elif case==7:
        print("간격을 조절해보자.")
        x=[2,3,5,7,9]
        y=[2,3,4,7,10]
        #plot할 떄 x값을 명시하지않으면 index에 때려넣기때문에 x도 명시해주자.
        fig,ax=plt.subplots(1,3,figsize=(15,9))
        ax[0].plot([str(i) for i in x],y)
        ax[1].plot(x,y)
        ax[2].plot(x,y,marker='*')
        plt.show()
    elif case==8:
        print("보간을 조절해보자.")
        # 여기 링크에 보간 방법에 대해 적어놓았다. 궁금하면 읽기
        # https://www.delftstack.com/howto/matplotlib/matplotlib-plot-smooth-curve/
        from scipy.interpolate import make_interp_spline, interp1d
        import matplotlib.dates as dates
        fig, ax = plt.subplots(1,2,figsize=(20,7),dpi=100)
        date_np = google.index
        value_np = google['close']
        date_num = dates.date2num(date_np)
        #smooth(이동평균과 크게 다르진 않음.)
        date_num_smooth = np.linspace(date_num.min(),date_num.max(), 50)
        spl = make_interp_spline(date_num,value_np,k=3)
        value_np_smooth = spl(date_num_smooth)
        #print
        ax[0].plot(date_np,value_np, marker="*")
        ax[1].plot(dates.num2date(date_num_smooth),value_np_smooth, marker="*")
        plt.show()
    elif case==9:
        print("twinx로 이중 축을 사용해보자")
        #twinx = 다른 정보를 사용할때
        #secondary-xaxis = 같은 정보를 사용할때
        fig, ax1 = plt.subplots(figsize=(12,7), dpi=150)
        ax1.plot(google.index,google['close'],color="#AA00BB")
        ax1.set_xlabel('date')
        ax1.set_ylabel('close price', color="#AA00BB")
        ax1.tick_params(axis='y',labelcolor="#AA00BB")
        ax2 = ax1.twinx() # twinx는 ax에 대해서 선언 보조축개념인듯
        ax2.plot(google.index,google['volume'],color="#00CC00")
        ax2.set_ylabel('volume',color="#00CC00")
        ax2.tick_params(axis='y',labelcolor="#00CC00") # 축에 값을 표시하는 것을 수정하는것임.
        ax1.set_title('google close price and volume', loc='left', fontsize=15, fontweight='bold')
        plt.show()
    elif case==10:
        print("secondary-xaxis로 이중 축을 사용해보자")
        def deg2rad(x): return x*np.pi/180
        def rad2deg(x): return x*180/np.pi
        fig, ax = plt.subplots()
        x = np.arange(0,360)
        y = np.sin(2*deg2rad(x))
        ax.plot(x,y)
        ax.set_xlabel('angle [degress]')
        ax.set_ylabel('signal')
        ax.set_title('sine wave')
        secax = ax.secondary_xaxis('top',functions=(deg2rad, rad2deg))
        # 축은 top에 배치하고, 기존 x축과의 변화는 아래의 두함수 순서대로 배치(주축->보조축)
        # 이런 느낌인가 functions는 잘 느낌이 안오네.
        secax.set_xlabel('angle [rads]')
        plt.show()
    elif case==11:
        print("범례 대신 그래프의 끝자락에 이름 표시하는 것을 해보자")
        fig = plt.figure(figsize=(16,9))
        x = np.linspace(-1*np.pi,np.pi,1000)
        y1 = np.sin(x)
        y2 = np.cos(x)
        y3 = np.tanh(x)
        #아주 그냥 레전드(?)야.
        ax1 = fig.add_subplot(121,aspect=1)
        ax1.plot(x,y1,color='#FF0000',linewidth=2,label='sine')
        ax1.plot(x,y2,color='#00FF00',linewidth=2,label='cosine')
        ax1.plot(x,y3,color='#0000FF',linewidth=2,label='hyperbolic tangent')
        ax1.spines['top'].set_visible(False)
        ax1.spines['right'].set_visible(False)
        ax1.legend()
        ax1.set_title("legend")
        #이걸 조금 깔끔하게 바꿔보면?
        ax2 = fig.add_subplot(122,aspect=1)
        ax2.plot(x,y1,color='#FF0000',linewidth=2,label='sine')
        ax2.plot(x,y2,color='#00FF00',linewidth=2,label='cosine')
        ax2.plot(x,y3,color='#0000FF',linewidth=2,label='hyperbolic tangent')
        ax2.spines['top'].set_visible(False)
        ax2.spines['right'].set_visible(False)
        ax2.text(x[-1]+0.1,y1[-1],s='sine',fontweight='bold',va='center',ha='left',bbox=dict(boxstyle='round,pad=0.3',fc='#AA0000',ec='black',alpha=0.3))
        ax2.text(x[-1]+0.1,y2[-1],s='cosine',fontweight='bold',va='center',ha='left',bbox=dict(boxstyle='round,pad=0.3',fc='#00AA00',ec='black',alpha=0.3))
        ax2.text(x[-1]+0.1,y3[-1],s='hyperbolic tangent',fontweight='bold',va='center',ha='left',bbox=dict(boxstyle='round,pad=0.3',fc='#0000AA',ec='black',alpha=0.3))
        #위치를 마지막 데이터 주변에 지정하고 필요한 변수들을 설정하여 생성.
        ax2.set_title("Label at end point")
        fig.suptitle("Where is legend?")
        plt.show()
    elif case==12:
        print("그래프 내 최댓값,최솟값과 같은 특정 데이터를 강조해보자")
        np.random.seed(950718)
        length=20
        x=np.arange(length)
        y=np.random.rand(length)
        fig=plt.figure(figsize=(16,9))
        ax=fig.add_subplot(111)
        ax.plot(x,y,color='#AAAAAA',linewidth=2)
        #이름을 그냥 쓰는건 가독성이 떨어질 것 같아서 점선과 점으로 표시했다고 하심.
        ax.plot([-1,x[np.argmax(y)]],[np.max(y)]*2,linestyle='--',color="tomato")
        ax.scatter(x[np.argmax(y)],np.max(y),c='tomato',s=50,zorder=20)
        ax.plot([-1,x[np.argmin(y)]],[np.min(y)]*2,linestyle='--',color="royalblue")
        ax.scatter(x[np.argmin(y)],np.min(y),c='royalblue',s=50,zorder=20)
        #그래도 한번 내가 직접 연습겸 넣어봄.
        ax.text(x[np.argmax(y)]+1,np.max(y),s='Maximum\nValue',fontweight='bold',va='center',ha='center',bbox=dict(boxstyle='round,pad=0.3',fc='tomato',ec='black',alpha=0.3))
        ax.text(x[np.argmin(y)]+1,np.min(y),s='Minimum\nValue',fontweight='bold',va='center',ha='center',bbox=dict(boxstyle='round,pad=0.3',fc='royalblue',ec='black',alpha=0.3))
        plt.show()
        #해보면 다른 plot방법들과의 융합이 필요할 때가 많음.
if __name__=="__main__":
    case = 12
    line_plot_example(case)