import numpy as np
import matplotlib as mpl

def plot_function(case):
    import matplotlib.pyplot as plt
    # Matlab과 가장 비슷한 plot을 보여줌. 확실히 Matlab이 강력하긴 하지.

    # figure를 호출하는 것. Matlab과 똑같으니 내식대로 부연설명을 하자면,
    # figure를 호출하는 행위는 마치 도화지를 꺼낸다고 보면 된다.
    # 도화지를 꺼내고, 거기에 데이터를 올린 다음, 도화지를 꾸미고 보여주면 되는 것임.
    if case == 0:
        print("Figure 꺼내보기")
        fig = plt.figure() # 도화지의 이름을 붙여주는 행위
        ax = fig.add_subplot() # 도화지를 꾸며주는 행위, 이 함수는 축을 추가해주는 것임.
        plt.show() # 도화지를 보여주는 행위
    elif case == 1:
        print("Figure의 subplot 써보기")
        fig = plt.figure(figsize=(16,9)) 
        #그래프의 size는 figure의 size로 서브플롯 ax의 size를 조절한다.
        #Figure의 사이즈는 (가로 길이[inch], 세로 길이[inch])처럼 tuple형태로 파라미터를 전달하여 조절한다.
        #notebook 같은 일부 환경에 대해서는 비율로 생각하면 됨.
        ax = fig.add_subplot(121) # 숫자를 넣으면 그래프를 넣을 수 있음. Matlab의 subplot과 완전히 기능이 같음.
        ax2 = fig.add_subplot(1,2,1) # 1부터 시작하는 것도 Matlab과 똑같음. 이거 리얼 헷갈리는데 ㅋㅋㅋㅋㅋㅋ.
        # 기본적으로는 콤마를 붙이는 매트랩 문법을 따르는데 숫자만 때려박아도 됨.
        plt.show()
    elif case == 2: #절차 지향적인 프로그래밍에 대해서..
        print("절차지향적으로 Figure에다가 선 그래프를 넣어보기")
        # 이제 데이터를 진짜 plot해보자
        x = np.array([1, 2, 3])
        y = 2 * x + 1
        z = 4 * x - 2
        fig = plt.figure(figsize=(16,9)) 
        ax1 = fig.add_subplot(221)
        plt.plot(x) # x만 출력, 이때 x축은 x의 인덱스 값이 됨.
        ax2 = fig.add_subplot(222)
        plt.plot(y) # y만 출력, 이때 x축은 y의 인덱스 값이 됨.
        ax3 = fig.add_subplot(223)
        plt.plot(x,y) # index를 공통적으로 설정하여 x축은 x의 인덱스 값으로 결정되고, y축을 y의 출력으로 결정
        ax4 = fig.add_subplot(224)
        plt.plot(x,z, color='blue') # 이게 파란선이고
        plt.plot(x,y, color='orange') # 이게 주황선임.
        # 이렇게 2개를 동시에 출력하는 것도 가능하긴 해..
        plt.show()
        #이런식으로 절차 지향적으로 plot하는 것도 가능하긴 한데.
        #이러면 pythonic하지 않음. 나는 지금까진 솔직히 사실 pythonic한 건 다른 거에 비해 상대적으로 관심없긴한데
        #plt를 절차적으로 호출하는건 그런 코딩 스타일에 대한 문제를 떠나서도 문제가 있어 보임.
        #그렇다면 어떻게 해야 이런 짓을 하지 않을까? -> 답은 ax에 있었음. ax가 객체가 되기 때문.
    elif case == 3: #객체 지향적인 pythonic한 프로그래밍으로 전환
        print("객체지향적으로 Figure에다가 선 그래프를 넣어보기")
        x = np.array([1, 2, 3])
        y = 2 * x + 1
        z = 4 * x - 2
        fig = plt.figure(figsize=(16,9)) 
        ax1 = fig.add_subplot(221)
        ax2 = fig.add_subplot(222)
        ax3 = fig.add_subplot(223)
        ax4 = fig.add_subplot(224)
        #고의적으로 절차적인 호출을 진행하지 않았음에도 잘 그리는 것을 볼 수 있음.
        ax3.plot(x,y, color='orange') 
        ax4.plot(y,z, color='green')
        ax1.plot(x) 
        ax4.plot(x,z, color='blue')
        ax2.plot(y) 
        ax4.plot(x,y, color='orange')
        ax3.plot(x,z, color='blue')
        plt.show()
        # matplotlib은 Pyplot API와같은 순차적인 호출 방법이 있고
        # 각 객체에 대해서 수정하는 Object-Orient API(객체 지향 API)를 지원함.
        # ax4를 이해하면 plt.plot을 제대로 이해하는 셈이 됨.
        # index가 동일하다는 것에 유의한다면 이해가 가능한데,
        # y값을 x축으로 두는 것을 마치 축의 스케일링과 이동이 일어난 것을 확인할 수 있음.
    elif case == 4: # 시각화의 중요성
        print("가독성이 좋은 시각화의 중요성")
        fig = plt.figure(figsize=(21,9))
        ax1 = fig.add_subplot(121)
        ax2 = fig.add_subplot(122)
        ax1.plot([1,2,3],[2,4,6])
        ax1.bar([1,2,3],[2,4,6])
        ax2.plot([1,2,3],[2,4,6], color='#000000', label='line') #black
        ax2.bar([1,2,3],[2,4,6], color='#AAAAAA', label='bar') #silver
        ax2.legend() # 범례를 추가함. 위에서 label값을 지정해주면 그 이름이 그대로 나옴.
        ax1.legend() # 범례를 추가하는데 label값이 없다면? -> 빈 상자만 출력되는 것을 확인.
        ax2.set_title('Visualization ON') # 그래프의 제목을 정해주는 함수
        ax1.set_title('Visualization OFF') #set_{}{} 는 굉장히 많이 쓰이는 함수임.
        #반대의 역할을 하는 것은 get_{}{}의 경우가 많음.
        fig.suptitle('Visualization Comparison') # Figure의 제목을 정해주는 함수는 suptitle로 super_title임.
        # 그래프 타입이 다르면 색을 그대로 지정해줌. 미리 정하는 것을 추천함.
        # 색을 쓸 때 한 글자로 정의하는 경우가 있는데 원색 계열이 많아서 눈이 아픔 추천x
        # 이름을 쓰는 방법은 웹 개발할때 색상표를 외운 경우에 쓸만한데 다외우기쉽지않아서 추천x
        # HEX 코드를 이용해 정하는 방법이 있음. RGB Hex값을 검색해서 사용하는 방법이 있음.
        # {16진수 2자리}씩 RGB가 정해진 수준임. 
        # 색말고 text를 입력하는 방법도 있음.
        plt.show()
    elif case == 5: #Visualization 끝판왕
        print("갖가지 기능들을 넣어서 시각화해보기")
        x = np.array([1, 2, 3])
        y = 2 * x + 1
        z = 4 * x - 2
        fig = plt.figure(figsize=(16,9))
        ax = fig.add_subplot()
        ax.plot(x,y,color='#FF0000',label='2x+1')
        ax.set_xticks([1,2,3]) # 축에 적히는 수의 위치를 정함(scale).
        ax.set_xticklabels(['one','two','three']) # 축에 적히는 text를 정함.
        #보면 scale이 xticks에 의해 정해지고, 그 이름이 xticklabels에 의해 영어로 바뀐 것을 확인 가능
        ax.plot(x,z,color='#00FF00',label='4x-2')
        fig.suptitle('suptitle')
        ax.set_title('set_title')
        ax.text(x=1, y=3, s="text at x=1,y=3") #해당 지점에 text를 박아넣는 함수 -> 원하는 위치에 text를 적어줌
        ax.annotate(text='Annotate at (3,7)',xy=(3,7), xytext=(3-0.2,7-4), arrowprops=dict(facecolor='#000000')) #주석의 형태로 제공. -> 원하는 위치에 text를 포인팅함.
        # 어디에 적힐지는 alignment를 정해서 구할수도 있음.
        print(f"This ax's title is {ax.get_title()}")
        ax.legend()
        plt.show()
    else:
        print(f'Case is not defined in the condition.')

if __name__=="__main__":
    case = 5 # Case별로 묶어서 plot하는 것을 구분하려고 함.
    try:
        print(f'numpy version : {np.__version__}')
    except:
        print(f'numpy loading error')

    try:
        print(f'matplotlib version : {mpl.__version__}')
    except:
        print(f'matplotlib loading error')
    plot_function(case)