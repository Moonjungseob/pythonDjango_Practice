from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    #단순 문자열만 리턴
    # return HttpResponse("Hello, world")
    #화면 연결해서 응답하기
    return render(request, 'main.html')


def main2(request):
    return render(request, 'main2.html')

# 터미널에서 단위 테스트 연습해보기
# python
