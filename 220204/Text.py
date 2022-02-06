import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

def text_example(case):
    student_data = pd.read_csv('StudentsPerformance.csv')
    if case==1:
        print("각 text는 어디에서 어떻게 보일까?")
        fig, ax = plt.subplots()
        fig.suptitle("Figure Title")
        ax.plot([1,3,2], label='legend')
        ax.set_title('Ax Title')
        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.text(x=1,y=2,s='Text')
        ax.legend()
        fig.text(0.5,0.6,s='Figure Text')
        plt.show()
    elif case==2:
        print("Text의 구성 요소들을 알아보자!")
        #text에서 쉽게 바꿀 수 있는 요소(Text properties)
        # family : 글씨체 (family에 따라서 밑의 옵션들의 일부가 동일한 경우도 있음.)
        # size or fontsize : 글자 크기
        # style or fontstyle : 글씨 형태(normal vs italic)
        # weight or fontweight : 글씨 굵기(normal vs semibold vs bold)
        fig , ax = plt.subplots()
        ax.set_xlim(0,1)
        ax.set_ylim(0,1)
        ax.text(x=0.5,y=0.5,s='Text is\nimportant', fontsize = 20, fontweight='bold',fontfamily='serif')
        plt.show()
    elif case == 3:
        print("Text의 글자 자체의 특성을 제외한 다른 요소들을 알아보자!")
        #text 외적인 요소들은 아래와 같다.
        # color = 색상
        # linespacing = 줄간의 간격
        # backgroundcolor = 글자 배경색(하이라이트)
        # alpha = 투명도(작을수록 투명하게 보임)
        # zorder = text의 z축으로 순서, 무엇을 먼저 보이게 할 것인가(클수록 먼저 보임)
        # visible = 보이게할건지 말건지, 왜 안 보일 텍스트를 적어놓음?...
        fig , ax = plt.subplots()
        ax.set_xlim(0,1)
        ax.set_ylim(0,1)
        ax.text(x=0.5,y=0.5,s='Zorder is 1', fontsize = 20, fontweight='bold',fontfamily='serif',
        color = "#bb00bb", linespacing=2, backgroundcolor="#007777", alpha = 0.5, zorder=1)
        ax.text(x=0.5,y=0.55,s='Zorder is 2', fontsize = 20, fontweight='semibold',fontfamily='serif',
        color = "#aa00aa", linespacing=2, backgroundcolor="#003333", alpha = 0.8, zorder=2)
        plt.show()
    elif case == 4:
        print("text에서 alignment는 어떨까?")
        # va = vertical alignement,verticalalignment라고 적어도 됨. 시작점의 수직위치를 정함.
        # ha = horizontal alignment, 글자의 가로/중앙/세로 정렬을 정함.
        # rotation = horizontal/vertical 이 있는데, 글자를 가로로쓸지 세로로쓸지 정하는 옵션.
        # 이걸 숫자로 적으면 degree로 계산하여 회전해서 적어줌.
        fig , ax = plt.subplots()
        ax.set_xlim(0,1)
        ax.set_ylim(0,1)
        ax.text(x=0.5,y=0.5,s='Zorder is 1', fontsize = 20, fontweight='bold',fontfamily='serif',
        color = "#bb00bb", linespacing=2, backgroundcolor="#007777", alpha = 0.5, zorder=1,
        va='center',ha='center',rotation='horizontal')
        ax.text(x=0.4,y=0.6,s='Zorder is 2', fontsize = 20, fontweight='semibold',fontfamily='serif',
        color = "#aa00aa", linespacing=2, backgroundcolor="#003333", alpha = 0.8, zorder=2,
        va='top',ha='left',rotation='vertical')
        plt.show()
    elif case == 5:
        print('bbox를 해보자, 텍스트 테두리에 박스를 씌우는 거지!')
        #bbox는 dictionary형태로 제공
        #boxstyle : box타입은 뭐로?
        #facecolor : box안쪽 색은 뭐로?
        #alpha : 투명도
        #ec : 테두리색은 뭐로(edge color)?
        #pad : 박스와 글자 사이 여유공간은 얼마나?
        fig , ax = plt.subplots()
        ax.set_xlim(0,1)
        ax.set_ylim(0,1)
        ax.text(x=0.5,y=0.5,s='Zorder is 1', fontsize = 20, fontweight='bold',fontfamily='serif',
        color = "#bb00bb", linespacing=2, backgroundcolor="#007777", alpha = 0.5, zorder=1,
        va='center',ha='center',rotation='horizontal',
        bbox=dict(boxstyle='round',facecolor='wheat',alpha=0.4,ec='royalblue',pad=1)) #bbox를 씌우니 backgroundcolor가 사라짐!
        #그래서 bbox가 background를 대신하는 옵션이 됨.
        plt.show()
    elif case==6:
        fig, ax= plt.subplots(1,1,figsize=(16,9))
        print('text api별 추가 사용법을 알아보자!')
        print("학생 데이터 중에 수학성적과 읽기 성적에대한 비교를 해볼 계획임.")
        for g,c in zip(['male','female'],['royalblue','tomato']): #g=gender c=color -> 성별에 따라 색이 지정됨
            student_sub = student_data[student_data['gender']==g] #gender가 일치하는 데이터만 뽑음
            ax.scatter(x=student_sub ['math score'], y=student_sub['reading score'], #그 gender의 x축은 수학성적 y축은 읽기성적으로 뽑음
            c = c, alpha=0.5, label=g) #scatter 옵션은 이렇게 넣어줌
        ax.set_xlim(-3,102)
        ax.set_ylim(-3,102)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.set_xlabel('Math Score', fontweight = 'semibold', color = '#CC0000')
        ax.set_ylabel('Reading Score', fontweight = 'semibold', color= "#00CC00")
        ax.set_title('Score Relation between\n Math and Reading',
        va = 'center', ha='center', color='green', fontweight='bold', loc='left',#location, 어디에 배치할지 결정함. 대강 정하면 시스템이 나머진 알아서 정해줌 잘 보이도록
        bbox=dict(boxstyle='round',facecolor='wheat',alpha=0.4,ec='gray',pad=1)) 
        ax.legend(labelspacing=1.2, shadow=True, title='Gender', bbox_to_anchor=[1,0.2], ncol=2)#bbox to anchor -> bbox의 위치 loc과는 대립되는 옵션임. , ncol은 한 행에 몇개의 열을 배치할 것인지
        #title,legend같은 요소에도 위에서 정한 요소들을 사용할 수 있음.
        plt.show()
    elif case==7:
        print("축과 텍스트의 조정")
        print("수학 성적만 좀 보자!")
        def score_band(x):
            temp = (x+9)//10
            if temp <=1:
                return '0-10'
            return f'{temp*10-9}-{temp*10}'
        student_data['math-range'] = student_data['math score'].apply(score_band)
        # 함수를 정의하면 그 다음에 판다스에서 데이터에 넣어주고 이를 dataframe에 넣어줌.
        print(student_data['math-range'].value_counts().sort_index())
        math_grade = student_data['math-range'].value_counts().sort_index()
        fig, ax = plt.subplots(1,3,figsize=(16,9))
        ax[0].bar(math_grade.index, math_grade, color='royalblue',width=0.65,linewidth=1,edgecolor='black')
        #ax[0].margin(0.07) #subplot에서는 안보임.
        ax[0].set_title("Complicated Data")
        ax[1].bar(math_grade.index, math_grade, color='royalblue',width=0.65,linewidth=1,edgecolor='black')
        #ax[1].margin(0.07)
        ax[1].grid(color = 'tomato', alpha=0.3)
        ax[1].set_title("Still complicated Data with grid")
        ax[2].bar(math_grade.index, math_grade, color='royalblue',width=0.65,linewidth=1,edgecolor='black')
        ax[2].set(frame_on=False) # 4개의 변 자체를 없애줌 splines 그거 없앤다는 뜻
        ax[2].set_yticks([]) #왼쪽에 있는 축 눈금을 지움. 대괄호만 줬기 때문에 표현할 게 없음.
        ax[2].set_xticks(np.arange(len(math_grade))) #tick label을 조절함.
        ax[2].set_xticklabels(math_grade.index, fontsize=7)#사실 출력은 같은데 이렇게 하는 이유는 fontsize등을 조절 가능함.
        ax[2].set_title('Simple Data without grid and axis label')
        for idx, val in math_grade.iteritems(): #index와 value을 다 받아올수 있도록 구현된 메소드
            ax[2].text(x=idx, y=val+3, s=val, va='bottom', ha='center', fontsize=11, fontweight='semibold',
            #기본값이 우측으로 편향되어있기때문에 va,ha를 조절하고 y에다가 살짝 더 더함. 패딩을 더하면 더 복잡해지긴하지만 가능함.
            bbox = dict(boxstyle='round',facecolor='wheat',ec='black',alpha=0.4)) #annotation은 화살표도 정해야되서 조금 복잡해
        fig.suptitle('Math Score Distribution')
        plt.show()
    elif case==8:
        print('text vs annotation')
        print('무슨 시빌워 같은 긴장감이 도는데, 둘의 차이점을 한 번 보도록 하자.')
        fig, ax = plt.subplots(1,2,figsize=(18,9))
        i = 13
        for a in ax:
            a.scatter(x=student_data['math score'], y=student_data['reading score'], c='lightgray', alpha=0.9, zorder=5)
            a.scatter(x=student_data['math score'][i], y=student_data['reading score'][i], c='tomato', alpha=1, zorder=10)
            a.set_xlim(-3, 102)
            a.set_ylim(-3, 102)
            a.spines['top'].set_visible(False)
            a.spines['right'].set_visible(False)
            a.set_xlabel('Math Score', fontweight = 'semibold', color = '#CC0000')
            a.set_ylabel('Reading Score', fontweight = 'semibold', color= "#00CC00")
            a.plot([-3, student_data['math score'][i]], [student_data['reading score'][i]]*2,
            color='gray', linestyle='--', zorder=8)
            a.plot([student_data['math score'][i]]*2, [-3, student_data['reading score'][i]],
            color='gray', linestyle='--', zorder=8)
        bbox = dict(boxstyle='round',fc='wheat',pad=0.2) #bbox 선언
        arrowprops = dict(arrowstyle="->") #화살표 선언
        ax[0].text(x=student_data['math score'][i]+3,y=student_data['reading score'][i]+3,s=f'This is #{i} student',va='center',ha='center',bbox=bbox,zorder=9)
        ax[0].set_title('Score Relation between\n Math and Reading\nusing Text API')
        ax[1].annotate(text=f'This is #{i} student', 
        xy=(student_data['math score'][i],student_data['reading score'][i]),
        xytext=[student_data['math score'][i]+20,student_data['reading score'][i]-20],
        bbox=bbox,
        arrowprops=arrowprops,
        zorder=9)
        ax[1].set_title('Score Relation between\n Math and Reading\nusing Annotate API')  
        plt.show()
    elif case==9:
        print('text vs annotation')
        print('둘의 차이점을 다른 그래프에서도 보도록 하자.')
        def score_band(x):
            temp = (x+9)//10
            if temp <=1:
                return '0-10'
            return f'{temp*10-9}-{temp*10}'
        student_data['math-range'] = student_data['math score'].apply(score_band)
        math_grade = student_data['math-range'].value_counts().sort_index()
        fig, ax = plt.subplots(1,2,figsize=(16,9))
        ax[0].bar(math_grade.index, math_grade, color='royalblue',width=0.65,linewidth=1,edgecolor='black')
        ax[0].set(frame_on=False) # 4개의 변 자체를 없애줌 splines 그거 없앤다는 뜻
        ax[0].set_yticks([]) #왼쪽에 있는 축 눈금을 지움. 대괄호만 줬기 때문에 표현할 게 없음.
        ax[0].set_xticks(np.arange(len(math_grade))) #tick label을 조절함.
        ax[0].set_xticklabels(math_grade.index, fontsize=7)#사실 출력은 같은데 이렇게 하는 이유는 fontsize등을 조절 가능함.
        ax[0].set_title('Text',loc='left',fontweight='bold',fontsize=11)
        for idx, val in math_grade.iteritems(): #index와 value을 다 받아올수 있도록 구현된 메소드
            ax[0].text(x=idx, y=val+3, s=val, va='bottom', ha='center', fontsize=11, fontweight='semibold',
            #기본값이 우측으로 편향되어있기때문에 va,ha를 조절하고 y에다가 살짝 더 더함. 패딩을 더하면 더 복잡해지긴하지만 가능함.
            bbox = dict(boxstyle='round',facecolor='wheat',ec='black',alpha=0.4)) #annotation은 화살표도 정해야되서 조금 복잡해
        ax[1].bar(math_grade.index, math_grade, color='royalblue',width=0.65,linewidth=1,edgecolor='black')
        ax[1].set(frame_on=False) # 4개의 변 자체를 없애줌 splines 그거 없앤다는 뜻
        ax[1].set_yticks([]) #왼쪽에 있는 축 눈금을 지움. 대괄호만 줬기 때문에 표현할 게 없음.
        ax[1].set_xticks(np.arange(len(math_grade))) #tick label을 조절함.
        ax[1].set_xticklabels(math_grade.index, fontsize=7)#사실 출력은 같은데 이렇게 하는 이유는 fontsize등을 조절 가능함.
        ax[1].set_title('Annotation',loc='left',fontweight='bold',fontsize=11)
        for idx, val in math_grade.iteritems(): #index와 value을 다 받아올수 있도록 구현된 메소드
            ax[1].annotate(xy=(idx,val),xytext=(idx,val+15), text=val, va='bottom', ha='center', fontsize=11, fontweight='semibold',
            #기본값이 우측으로 편향되어있기때문에 va,ha를 조절하고 y에다가 살짝 더 더함. 패딩을 더하면 더 복잡해지긴하지만 가능함.
            bbox = dict(boxstyle='round',facecolor='wheat',ec='black',alpha=0.4),
            arrowprops=dict(arrowstyle="->")) #annotation은 화살표도 정해야되서 조금 복잡해
        fig.suptitle('Math Score Distribution')
        plt.show()
if __name__=="__main__":
    case = 9
    text_example(case)