### 문제 한줄평

자 저걸 보다보면 이제 15의 배수판별법이 필요하겠죠? 
15는 3과 5의 배수를 모두 만족하면 되기 때문에 두가지를 만족해야함.
1) 각 자리의 수의 합이 3의 배수이다.
2) 맨 끝자리 수가 5 혹은 0이다 -> 이 문제에서는 맨 끝자리가 5인 경우만 존재
따라서 dp는 각 자리 수의 합을 3으로 나누었을 때의 나머지로 설정해주고 진행하면 된다.
이를 따라서 풀었을 때 코드처럼 풀면 된다는 결과네요~


# [Gold V] Ezreal 여눈부터 가네 ㅈㅈ - 20500 

[문제 링크](https://www.acmicpc.net/problem/20500) 

### 성능 요약

메모리: 109544 KB, 시간: 92 ms

### 분류

다이나믹 프로그래밍, 수학, 정수론

### 제출 일자

2025년 2월 10일 15:45:34

### 문제 설명

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/684c689a-991b-4463-a78d-881f541985d5/-/preview/" style="width: 600px; height: 88px;"></p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/813fa3e8-e15d-4f20-86fd-95e27645b127/-/preview/" style="height: 117px; width: 600px;"></p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/980f8c5f-4ee1-4896-853b-c2710736bec1/-/preview/" style="height: 74px; width: 600px;"></p>

<p>욱제는 15라는 수를 굉장히 싫어한다. 그래서 0으로 시작하지 않고 1과 5로만 구성된 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>자리 양의 정수 중에서, 15의 배수가 몇 개인지 궁금해졌다.</p>

<p>참가자 여러분도 궁금하지요?</p>

<p>안 궁금함? 15ㄱ</p>

### 입력 

 <p><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다.</p>

### 출력 

 <p>문제의 답을 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c37"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>007</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1\,000\,000\,007$</span></mjx-container>로 나눈 나머지를 출력한다.</p>

