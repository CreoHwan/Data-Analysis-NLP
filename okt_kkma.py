# NLP(Natural Language Processing)

from konlpy.tag import * 
okt = Okt() 
kkma = Kkma( )

First= '데이터 읽기'
data_read = open("KOREAN_TEXT/한국어_분석_예제_1.txt").read( )
# string 타입으로 존재

kkma_sentence = kkma.sentences(data_read)
# string 타입의 데이터를 하나씩 처리하면서 리스트 타입으로

data_readlines = open("KOREAN_TEXT/한국어_분석_예제_1.txt").readlines( )
# 데이터를 읽어서 list 타입으로 리턴
# 이때 줄바꿈은 \n 으로 나타남


Second = '품사 및 명사 추출'
# pos()함수는 문장에서 품사 정보를 출력하는 함수이다.
# pos()는 okt, kkma 모든 모듈에서 사용가능하다.

# pos()함수의 입력은 string 타입, 리턴은 list 타입이다.

#  okt.pos()의 경우, 리턴 값은 Noun : 명사, Josa : 조사, Punctuation : 구두점, Adjective : 형용사, Verb : 동사 등등..

# kkma.pos()의 경우, 리턴 값은 NP : 대명사, JX : 보조사, NNG : 보통명사, NNP: 고유명사, SP : 쉼표,가운뎃점,콜론,빗금, JKS : 주격조사, VA : 형용사, VV : 동사, EFN : 평서형 종결 어미 등등..

# okt()
okt_nouns=[]
line=0

for i in data_readlines :  
        print(line,"line", type(i))     
        print("문장 출력 : ", i)
        
        #품사 출력 부분
        print("품사 출력 : ", end='') 
        print(okt.pos(i), "\n") #문장의 품사 출력, pos(i)에서 i는 string타입의 문장 데이터
        
        #명사 출력 부분
        data = okt.nouns(i)  #okt.nouns()를 활용하여 명사를 모두 추출하여 data 리스트에 저장 
        print("문장에서 명사 출력 : ", end='') 
        print(data, "\n")    
  
        for j in range(0,len(data)) : 
            print("명사", [j], ": ", end='')
            print(data[j])
            
            #치환 명사가 있다면 (가령 "젤"을 '제일'로 치환한다면)
            if data[j] == '젤' :  
                count = 0
                data_j = okt.nouns(data[j].replace('젤','제일'))  #okt.nouns()를 활용하여 '젤'명사를 '제일'명사로 치환
                print('●', data[j], "→" , data_j, "로 치환됨")  
                okt_nouns.append(data_j[count])
                count += 1
            else :    
                okt_nouns.append(data[j])
            
            
            print("치환 명사를 고려한 최종 명사 리스트 : ", end='' )           
            print(okt_nouns, "\n")
            
        line += 1  
        print("치환 명사를 고려한 최종 명사 리스트 길이 : ",len(okt_nouns)) 
        print('-'*100, '\n')

# kkma.pos()
# kkma.nouns()의 경우 : 문장에서 중복된 명사는 1번만 출력한다.
# 꼭 sting을 인자로

kkma_nouns =[]
line= 0

for i in data_readlines :
        print(line,"line", type(i))     
        print("문장 출력 : ", i)
        
        #품사 출력 부분
        print("품사 출력 : ", end='') 
        print(kkma.pos(i), "\n") #문장의 품사 출력, pos(i)에서 i는 string타입의 문장 데이터
        
        #명사 출력 부분
        data = kkma.nouns(i)  #kkma.nouns()를 활용하여 명사를 모두 추출하여 data 리스트에 저장 
        print("문장에서 명사 출력 : ", end='') 
        print(data, "\n")       
        
        for j in range(0,len(data)) : 
            print("명사", [j], ": ", end='')
            print(data[j])                       
            
            #치환 명사가 있다면 (가령 "젤"을 '제일'로 치환한다면)
            if data[j] == '짱' :                 
                data_j = kkma.nouns(data[j].replace('짱','제일'))  #kkma.nouns()를 활용하여 '젤'명사를 '제일'명사로 치환
                print('●', data[j], "→" , data_j, "로 치환됨")  
                kkma_nouns.append(data_j[0])
            else :    
                kkma_nouns.append(data[j])            
            
            print("치환 명사를 고려한 최종 명사 리스트 : ", end='' )           
            print(kkma_nouns, "\n")        

        line += 1 
        print("리스트 길이 : ",len(kkma_nouns)) 
        print('-'*100)
        #4라인 '짱'을 'NNG(보통명사)'로 해석하여 명사로 추출됨
        #5라인'블루베리'가 ('블루', 'NNG'), ('베리', 'NNP')으로 파싱된 후, '블루', '블루베리', '베리'가 명사로 추출됨        

Third = '의미 없는 단어 제거'
#  "나" or "저" 는 의미가 없는 명사라고 생각하여 제거
#제거할 명사가 여러개인 경우, 집합을 생성해서 제거

remove_set = {'나', '저'}
kkma_nouns = [i for i in kkma_nouns if i not in remove_set]
print(kkma_nouns)

Fourth= '명사의 빈도수 출력하기'
#  collections 모듈에서 제공되는 Counter 함수를 사용하여 명사의 빈도수를 출력

#  okt.nouns()를 대상으로 Counter()로 명사 빈도수 
from collections import Counter
okt_nouns_count = Counter(okt_nouns)  

#  kkma.nouns()를 대상으로 Counter()로 명사 빈도수 출력하기
data_kkma_count = Counter(kkma_nouns) 


Five = '불용어 사전을 이용한 불필요한 명사 제거하기'

stop_word = open("KOREAN_TEXT/불용어목록.txt").read()
#불용어 목록 : '최고\n역시\n가장\n제일\n나'

# okt
print("● okt.nouns()를 활용하여 추출된 명사 : %d 개" %len(okt_nouns))
print(okt_nouns,'\n')

stop_okt = [ each_word for each_word in okt_nouns if each_word in stop_word ] 
#each_word가 stop_word에 있으면 each_word를 stop_okt에 할당한다. 
#stop_word는 \n 단위로 비교된다.

non_stop_okt = [ each_word for each_word in okt_nouns if each_word not in stop_word ] 
#each_word가 stop_word(불용어)에 없으면 each_word를 non_stop_okt에 할당한다. 
#stop_word는 \n 단위로 비교된다.

# kkma
print("● kkma.nouns()를 활용하여 추출된 명사 : %d 개" %len(kkma_nouns))
print(kkma_nouns,'\n')

stop_kkma = [ each_word for each_word in kkma_nouns if each_word in stop_word ] 
#each_word가 remove_word에 있으면 each_word를 remove_kkma에 할당한다. 
#stop_word는 \n 단위로 비교된다.

non_stop_kkma = [ each_word for each_word in kkma_nouns if each_word not in stop_word ] 
#each_word가 remove_word(불용어)에 없으면 each_word를 non_remove_kkma에 할당한다. 
#stop_word는 \n 단위로 비교된다.


Six =  '글자 수 제한으로 불용어 제거 추가하기'
# okt
refine_okt = []
for i in non_stop_okt :  #불용어에 해당하지 않는 단어를 대상으로 
    if len(i) >= 2 and len(i) <= 10 :  #글자수가 2자 ~ 10자에 해당되는 단어만 추출하여 final_okt에 추가한다.
        refine_okt.append(i) 

# kkma
refine_kkma = []
for i in non_stop_kkma :  #불용어에 해당하지 않는 단어를 대상으로     
    if len(i) >= 2 and len(i) <= 10 :  #글자수가 2자 ~ 10자에 해당되는 단어만 추출하여 final_kkma에 추가한다.
        refine_kkma.append(i) 


Seven = '7. 불용어가 제거된 명사를 대상으로 빈도수 다시 출력하기'
# okt
final_okt = Counter(refine_okt)
final_okt_sort = final_okt.most_common(10) 
#most_common() 내림차순으로 정렬한다.()안의 숫자는 상위 몇개를 추출할것인지에 해당
final_okt_sort_dic = dict(final_okt_sort)

# kkma
final_kkma = Counter(refine_kkma)
final_kkma_sort = final_kkma.most_common(10) 
#most_common() 내림차순으로 정렬한다.()안의 숫자는 상위 몇개를 추출할것인지에 해당
final_kkma_sort_dic = dict(final_kkma_sort)

