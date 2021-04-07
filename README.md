# Algorithm
Python Alogorithm Study

## Table of contents
- [Intermediate-Python](#Intermediate-Python)
- [Inflearn](#Inflearn)
- [이코테](#이코테)
- [Programmers](#Programmers)

## Intermediate-Python
### 실전에서 유용한 표준 라이브러리
|라이브러리|기능|
|:---:|:---:|
|내장 함수|기본 입출력 함수부터 정렬 함수까지 기본적인 함수 제공|
|itertools|반복되는 형태의 데이터를 처리하기 위한 유용한 기능 제공(특히 순열과 조합 라이브러리가 자주 사용됨)|
|heapq|Heap 자료구조 제공(일반적으로 우선순위 큐 기능을 구현하기 위해 제공)|
|bisect|이진 탐색 기능 제공|
|collections|Deque, Counter 등의 유용한 자료구조 포함|
|math|필수적인 수학적 기능 제공(팩토리얼, 제곱근, 최대공약수)|


## Inflearn
### 코드구현력 기르기
|Date|Problem|Check1|Check2|Check3|Note|
|:---:|:---:|:---:|:---:|:---:|:---:|
|210108|k번째 약수|O| | |for else 구문|
|210108|k번째 수|O| | | |
|210112|k번째 큰 수| X| | | set과 3중 for문|
|210126|대표값|O| | |소수 첫째에서 반올림|
|210202|정다면체|O| | |인덱스를 합으로 활용하기|
|210202|자릿수의 합|O| | ||
|210202|소수의 개수|X| | |배수 간격으로 움직이기|
|210205|뒤집은 소수|*| | |예외처리, 소수 구하기|
|210205|주사위 게임|O| | |정렬과 비교|
|210207|점수계산|O| | ||

### 탐색&시뮬레이션(string, 1차원, 2차원 리스트 탐색)
|Date|Problem|Check1|Check2|Check3|Note|
|:---:|:---:|:---:|:---:|:---:|:---:|
|210207|회문 문자열 검사|*| | |대소문 자 구별(.upper)|
|210209|숫자만 추출|O| | |변수.isdecimal() -> 0부터 9까지 숫자만 확인(return True or False)  변수.isdigit -> 숫자형태 다 찾음(return True or False) |
|210210|카드 역배치|*| | |index swap|
|210210|두 리스트 합치기|O| | |이미 정렬된 두 데이터를 합할 때(포인터 활용)|
|210212|수의 합|*| | |index 활용|
|210213|격자판 최대합|X| | |List Comprehension|
|210214|사과나무|*| | |index 활용|
|210215|곳감|X| | |pop(default는 뒤, 앞도가능), append(뒤에 붙임), insert(앞에 붙임)|
|210216|봉우리|X| | |padding, all|
|210217|스도쿠 검사|X| | |sum(list)|
|210222|격자판 회문수|*| | ||

### 이분탐색(결정알고리즘) & 그리디 알고리즘
```text
그리디 알고리즘
문제를 풀어나가는 과정에서 현재 단계에서 가장 좋은 것을 선택하는 방식으로 품
보통의 그리드 문제는 정렬을 한 후 차례차례 선택해 나감
```
|Date|Problem|Check1|Check2|Check3|Note|
|:---:|:---:|:---:|:---:|:---:|:---:|
|210224|이분 검색|*| | |이진 탐색으로 풀 것, 탈출 조건|
|210224|랜선 자르기|*| | |최대 lt를 찾는 방법|
|210225|뮤직 비디오|X| | ||
|210226|마구간 정하기|*| | ||
|210301|회의실 배정|*| | |sort(lambda x : (x[1],x[0])|
|210301|씨름 선수|*| | ||
|210303|창고정리|O| | ||
|210309|침몰하는 타이타닉|O| | |while lst(참이면 실행, 비어있음 멈춤), list와 deque의 차이 |
|210314|증가 수열 만들기|O| | |list.clear() : 리스트 비우기 |
|210315|역수열(그리디)|O| | | |

## 이코테
### 탐색&시뮬레이션(string, 1차원, 2차원 리스트 탐색)
|Date|Problem|Check1|Check2|Check3|Note|
|:---:|:---:|:---:|:---:|:---:|:---:|
|210216|거스름돈 문제|O| | ||
|210218|상하좌우|O| | ||
|210219|시각|X| | ||
|210223|stack,queue,revursive|O| | ||
|210226|큰 수의 법칙|*| | ||
|210227|숫자 카드 게임|O| | ||
|210227|1이 될 때까지|O| | ||
|210303|왕실의 나이트|*| | ||
|210304|게임 개발|X| | ||
|210306|음료수 얼려 먹기|*| | |ord() 아스키 코드로 변환, chr() 아스키 코드를 문자로 변환|
|210310|두 배열의 원소 교체|O| | |Swap : a[i], b[i] = b[i], a[i]|
|210310|부품 찾기|O| | |이진 탐색|
|210311|떡볶이 떡 만들기|O| | |이진 탐색|
|210312|1로 만들기|X| | |다이나믹 프로그래밍|
|210318|개미 전사|*| | |다이나믹 프로그래밍|
|210318|바닥공사|X| | |다이나믹 프로그래밍|
|210322|효율적인 화폐 구성|*| | |다이나믹 프로그래밍|
|210327|전보|O| | |dijkstra 알고리즘|
|210327|팀 결성|O| | |서로소 집합 알고리즘|
|210329|도시 분할 계획|*| | |크루스칼 알고리즘|
|210330|커리큘럼|*| | |위상정렬|
|210405|모험가 길드|O| | |그리드|
|210405|곱하기 또는 더하기|O| | |그리드|
|210405|문자열 뒤집기|*| | |그리드|
|210406|만들 수 없는 금액|X| | |그리드|


## Programmers
|Date|Problem|Check1|Check2|Check3|Note|
|:---:|:---:|:---:|:---:|:---:|:---:|
|210308|h-index|*| | |num_iter+1|
|210308|조이스틱|*| | ||
