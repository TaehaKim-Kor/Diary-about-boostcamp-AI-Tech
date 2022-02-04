import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
def bar_plot_example(case):
    x = list('ABCDE')
    y = np.arange(1,6,1)
    student_data = pd.read_csv('StudentsPerformance.csv')
    if case == 1: #barplot vs horizontalbarplot
        print("수직막대 vs 수평막대")
        fig, ax = plt.subplots(1,2,figsize=(16,9))
        ax[0].bar(x,y)
        ax[1].barh(x,y)
        plt.show()        
    elif case == 2: #실제데이터로 bar plot 해보기
        print("실제 데이터로 bar plot해보기")
        # 1천명의 데이터, feature에 대한 정보는 head,describe,info명령어로 확인
        print('===================================')
        print(student_data.head(100))
        # 인자값을 안주면 5개, 줬으면 인자값만큼 순서대로 인덱스를 넣어 테이블 값을 보여주는 함수
        print(student_data.sample(5))
        # 이건 random하게 인자값만큼 뽑아줌. 이게 더 좋긴 함.
        print('-----------------------------------')
        print(student_data.describe())
        # 데이터를 분석하여 통계값을 알려주는 함수.
        # count(갯수)/mean(평균)/std(표준편차)/25%/50%/75%/max(최대값)
        # 더 자세히 알고 싶다면 이것도 추천
        print(student_data.describe(include='all'))
        print('-----------------------------------')
        print(student_data.info())
        # 데이터가 무엇인지 알려주는 함수
        # 기본적인 데이터의 타입/Index 범위/데이터 columns의 갯수와 종류, 타입, 결측치 유무를 알려줌
        # 시각화 과정에서, 인종같은 것들은 순서가 없는 데이터이지만 오해를 불러일으킬 수 있는 여지가 있다.
        # 이런 민감한 거 다룰 때는 소위 말하는 "알잘딱깔센" 해야 함.
        # 가끔 column에 결측치인 null값이 있는지를 알려줄 때가 있는데, 이런 것도 확인해둬야 함.
        print('===================================')
        
        # 그룹에 따른 정보의 시각화는?
        # pandas는 그룹에따라 묶는게 쉬움
        group = student_data.groupby('gender')['race/ethnicity'].value_counts() #value_counts를 안해주면 아무것도 안나옴.
        print(group)
        group=group.sort_index() #index로 sort해주는것
        print(group)

        #이걸 그려보자.
        fig, ax = plt.subplots(1,2,figsize=(16,9))
        ax[0].bar(group['male'].index, group['male'], color="#00BBBB")
        ax[0].set_title("male on race/ethnicity")
        ax[1].bar(group['female'].index, group['female'], color="#AA00AA")
        ax[1].set_title("female on race/ethnicity")
        fig.suptitle("Non-arranged y axis graph") #y축의 크기가 맞지 않음.
        plt.show()

        #y축의 크기가 맞는 graph 그리기
        #1)sharey=True를 fig선언할 때 쓰기
        #2)set_ylim(최소,최대)로 모든 ax를 정해주기
        #1번 방안
        fig, ax = plt.subplots(1,2,figsize=(16,9), sharey=True)
        ax[0].bar(group['male'].index, group['male'], color="#00BBBB")
        ax[0].set_title("male on race/ethnicity")
        ax[1].bar(group['female'].index, group['female'], color="#AA00AA")
        ax[1].set_title("female on race/ethnicity")
        fig.suptitle("Arranged y axis graph using sharey") #y축의 크기가 맞음.
        plt.show()
        #2번 방안
        fig, ax = plt.subplots(1,2,figsize=(16,9))
        ax[0].bar(group['male'].index, group['male'], color="#00BBBB")
        ax[0].set_title("male on race/ethnicity")
        ax[1].bar(group['female'].index, group['female'], color="#AA00AA")
        ax[1].set_title("female on race/ethnicity")
        for a in ax:
            a.set_ylim(0,200)
        fig.suptitle("Arranged y axis graph using set_ylim") #y축의 크기가 맞음.
        plt.show()
        # 그러나 이런 bar plot으로는 그룹간의 비교가 어렵다잉.
    elif case==3: #stacked bar plot 써보기
        print("실제 데이터로 stacked bar plot해보기")
        group_cnt=student_data['race/ethnicity'].value_counts().sort_index()
        group=student_data.groupby('gender')['race/ethnicity'].value_counts().sort_index()
        fig, ax = plt.subplots(1,2,figsize=(16,9), sharey=True)
        ax[0].bar(group_cnt.index, group_cnt, color="#AAAAAA") # 모든 데이터
        ax[0].set_title("Entire data visualization")
        #stacked 로 그리려면 bottom이라는 것을 활용한다!
        ax[1].bar(group['male'].index, group['male'], color="#00BBBB")
        ax[1].bar(group['female'].index, group['female'],bottom=group['male'], color="#AA00AA")
        #bottom이라는 파라미터는 아래의 공간을 해당 plot만큼 비워둔다고 생각하면됨.
        #바꿔생각하면 bottom에 해당하는 데이터를 출력하지 않으면 비워지는 것임. 밑에 깔 데이터를 정하는 것.
        ax[1].set_title("Stacked visualization")
        plt.show()
        #그런데 가독성은 그닥이긴 함. 가독성이 별로일 땐?
    elif case==4: #percentaged Stacked Bar Plot 써보기
        print("실제 데이터로 percentaged bar plot해보기")
        #그룹순서를 바꿔주는 이유는 barh를 써서 볼때는 위에서 아래로 내려보는게 편하기 때문에 바꿈.
        group = student_data.groupby('gender')['race/ethnicity'].value_counts().sort_index(ascending=False)
        #Pandas의 Data분석테크닉을 써서 이걸 그림.
        total = group['male']+group['female'] #데이터를 합쳐서 전체 갯수를 만들어줌. 이걸 나누면 비율이 됨.
        fig, ax = plt.subplots(1,1,figsize=(16,9))
        ax.barh(group['male'].index, group['male']/total, color="#00BBBB", label='male')
        ax.barh(group['female'].index, group['female']/total, left=group['male']/total, color="#AA00AA", label='female') # left에도 나눠줘야함.
        ax.legend()
        ax.set_title('percentage bar plot')
        ax.set_xlim(0,1)
        #그려보면 알겠지만 graph의 테두리가 거슬림 -> spines의 set_visible옵션을 꺼버려서 해결
        #spine = 변, top bottom left right가 있음.
        for s in ['top','bottom','left','right']:
            ax.spines[s].set_visible(False)
    elif case==5: #Alpha Blending을 사용해서 Overlapped Bar Plot 그리기
        print("실제 데이터로 overlapped bar plot by alpha 해보기 -> 2개")
        group = student_data.groupby('gender')['race/ethnicity'].value_counts().sort_index(ascending=True)
        fig, ax = plt.subplots(2,2,figsize=(12,12))
        ax = ax.flatten()
        for idx, alpha in enumerate([1,0.75,0.5,0.25]): # alphablending을 위한 계수값들을 list로 만들고 enumerate로 호출
            ax[idx].bar(group['male'].index, group['male'], color="#BC00FA", alpha=alpha)
            ax[idx].bar(group['female'].index, group['female'], color="#00CBAF", alpha=alpha)
            ax[idx].set_title(f"Alpha = {alpha}")
            #그런데 착각한게, 이게 겹치는 부분을 alpha blending을 하는게 아니라, 전체 값을 alpha blending하는 것임.
            #alpha blending이라기보단 RGB-A(alpha = Transparency) 계열 데이터처럼 사용하는 것이라고 보면 될듯.
        for a in ax:
            a.set_ylim(0,200)
        plt.show()
    elif case==6 : # grouped bar plot 그리기 (2개)
    print("실제 데이터로 overlapped bar plot by alpha 해보기 -> 2개")
        # 3가지 테크닉으로 구현함.
        # 1) x축을 조정한다.
        # 2) width를 조정한다.
        # 3) xticks, xticklabels로 조정한다.
        # -> 이 경우에는 x축이 0,1,2,3으로 구성될 때
        # -> 1번 그래프 : 0-width/2, 1-width/2, 2-width/2, 3-width/2
        # -> 2번 그래프 : 0+width/2, 1+width/2, 2+width/2, 3+width/2
        group = student_data.groupby('gender')['race/ethnicity'].value_counts().sort_index(ascending=True)
        fig, ax = plt.subplots(1,1,figsize=(16,9))
        idx = np.arange(len(group['male'].index)) #인덱스 할당
        width=0.35 # width를 조정한다.
        ax.bar(idx-width/2, group['male'], color="#12A58C", width=width, label = 'male') # x축을 조정한다.
        ax.bar(idx+width/2, group['female'], color="#BD24AC", width=width, label = 'female') # x축을 조정한다.
        ax.set_xticks(idx) #xticks로 조정한다.
        ax.set_xticklabels(group['male'].index) # xticklabels로 조정한다.
        ax.legend()
        plt.show()
    elif case==7 : # grouped bar plot 그리기 (N개)
        print("실제 데이터로 overlapped bar plot by alpha 해보기 -> n개")
        # ans: index(실제 index 근처 바 그래프들의 index를 의미)의 합이 0이 되도록 구현
        # ex) 2개일 때 -> -1/2 , 1/2
        # ex) 3개일 때 -> -2/2, 0/2, 2/2 => -1,0,1
        # ex) 4개일 때 -> -3/2, -1/2, 1/2, 3/2
        # 일반화하여 정규식으로 나타내면 -> x+(-N+1+2*i)/2 * Width가 됨.
        multigroup = student_data.groupby('parental level of education')['race/ethnicity'].value_counts().sort_index()
        group_list = sorted(student_data['race/ethnicity'].unique())
        edu_level = student_data['parental level of education'].unique()

        fig, ax = plt.subplots(1,1,figsize=(16,9))
        x=np.arange(len(group_list))
        width = 0.7/len(group_list) #분자가 1이면 그래프가 가득 참.
        for idx, g in enumerate(edu_level):
            ax.bar(x+(-len(edu_level)+1+2*idx)*width/2, multigroup[g], width=width, label=g) #-> x+(-N+1+2*i)/2 * Width
        ax.set_xticks(x)
        ax.set_xticklabels(group_list)
        ax.legend()
        plt.show()
    elif case==8: # Principle of Proportion Ink, 잉크양 비례 법칙 : 데이터의 수치와 plot에 필요한 잉크양은 비례한다. -> 시각적으로 기본적인 법칙
        print("실제 데이터로 잉크양 비례 법칙의 중요성을 알아보기")
        score = student_data.groupby('gender').mean().T
        print(len(score))
        idx = np.arange(len(score.index))
        width = 0.7/len(score)
        fig, ax = plt.subplots(1,2,figsize=(16,9))
        for a in ax:
            a.bar(idx-width/2, score['male'], color="royalblue", width=width, label="male")
            a.bar(idx+width/2, score['female'], color="tomato", width=width, label="female")
            a.legend()
            a.set_xticks(idx)
            a.set_xticklabels(score.index)
        ax[0].set_ylim(60,75)
        ax[0].set_title("Do not follow the principle of proportion ink")
        ax[1].set_title("Follow the principle of proportion ink")
        fig.suptitle("Principle of Proportion Ink")
        plt.show()

        #정이 극대화해서 보여주고싶으면 세로 길이를 늘리는 것도 좋음 -> fig_size 바꾸기
        fig, ax = plt.subplots(1,1,figsize=(12,14))
        ax.bar(idx-width/2, score['male'], color="royalblue", width=width, label="male")
        ax.bar(idx+width/2, score['female'], color="tomato", width=width, label="female")
        ax.legend()
        ax.set_xticks(idx)
        ax.set_xticklabels(score.index)
        ax.set_ylim(60,75)
        fig.suptitle("Change graph's proportion of size")
        plt.show()
    elif case==9 : 
        print("실제 데이터로 유용한 기술들을 익혀보고 그래프 내 남는 공간 활용해보기")
        # 데이터 정렬하기
        print("========================================")
        print(student_data.head())
        print("----------------------------------------")
        print(student_data.sort_index().head())
        print("========================================")
        # 그래프 내 남는 공간을 이용해 적절한 공간 활용하는 방법
        group_cnt=student_data['race/ethnicity'].value_counts().sort_index()
        print(group_cnt.head())
        fig = plt.figure(figsize=(16,9))
        ax_basic = fig.add_subplot(1,2,1)
        ax = fig.add_subplot(1,2,2)
        ax_basic.set_title("normal graph")
        ax.set_title("visualization applied graph")
        fig.suptitle("Visualization")
        ax_basic.bar(group_cnt.index, group_cnt)
        ax.bar(group_cnt.index,group_cnt, width=0.7, edgecolor='#000000',linewidth=2,color="#FF0000")
        #width 는 0.8이 기본
        #edgecolor는 테두리 색을 지정
        #linewidth는 테두리 두께를 지정 -> 너무 두꺼우면 실제 데이터에 대한 오해가 발생
        ax.margins(0.1,0.1) # 기본은 0.05인데, margin은 왼쪽과 위쪽의 여백을 의미함.
        for s in ['top','right']:
            ax.spines[s].set_visible(False) #위와 오른쪽 변을 제거해서 그래프를 환하게 만든다.
        ax.grid(zorder=0) # 격자를 넣어줌
        for idx, value in zip(group_cnt.index, group_cnt):
            ax.text(idx, value+5, s=value, ha='center', fontweight='bold') #ha = 정렬, fontweight = 폰트조절
        plt.show()
    elif case==10 :
        print("실제 데이터로 오차 막대 넣어보기")
        # 오차막대
        score = student_data.groupby('gender').mean().T
        score_var = student_data.groupby('gender').std().T
        print(score_var)
        fig, ax = plt.subplots(1,1,figsize=(16,9))
        idx=np.arange(len(score.index))
        width=0.3
        ax.bar(idx-width/2, score['male'], color="#00FF00", width=width, label="male",yerr=score_var['male'], capsize=10) #capsize 는 오차막대의 위 아래에도 수평선을 긋는 것임
        ax.bar(idx+width/2, score['female'], color="#FF0000", width=width, label="female",yerr=score_var['female']) #yerr이 오차막대 여기선 표준편차를 의미.
        ax.set_xticks(idx)
        ax.set_xlabel('subject', fontweight='bold', fontsize=10)
        ax.set_ylabel('score', fontsize = 10)
        ax.set_xticklabels(score.index)
        ax.set_ylim(0,100)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.legend()
        ax.set_title('Gender/Score with error bar', fontsize=20)
        plt.show()
if __name__=="__main__":
    case = 10
    bar_plot_example(case)