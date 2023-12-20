import math

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from ..models import Question
import logging

logger = logging.getLogger('pybo')

def index(request):
    """
    pybo 목록 출력
    """
    logger.info("INFO 레벨로 출력")
    kw = request.GET.get('kw', '')
    question_list = Question.objects.order_by('-create_date') #'-create_date = 등록 역순
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색  
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
        # 언더바 두개 "__"을 통해 모델의 하위속성에 접근할 수 있음.
        
    page = request.GET.get('page', '1') #페이지를 가져올떄 사용, page값이 없이 호출 된경우 디폴트로 1    
    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page) #페이지에 해당하는 페이지 객체
    page_range = 5
    current_block = math.ceil(int(page)/page_range)
    start_block = (current_block-1) * page_range
    end_block = start_block + page_range
    p_range = paginator.page_range[start_block:end_block] # paginator.page_range는 리스트기 때문에 [0:4]
    context = {'question_list': page_obj, 'page':p_range, 'kw':kw} # context는 딕셔너리 형태
    return render(request, 'pybo/question_list.html', context)
    # render 함수는 파이썬 데이터를 템플릿에 적용하여 HTML로 반환하는 함수이다.

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)