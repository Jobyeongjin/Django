from django.shortcuts import render
import random


def index(request):
    return render(request, "index.html")


def print_number(request, _number):
    return render(
        request,
        "number.html",
        {
            "number": _number,
        },
    )


def print_text(request):
    return render(
        request,
        "text.html",
        {
            "text": request.GET.get("_text"),
        },
    )


def even(request, _even):
    if _even == 0:
        check = f"{_even}은 0 입니다."
    elif _even % 2 == 0:
        check = f"{_even}은 짝수입니다."
    else:
        check = f"{_even}은 홀수입니다."

    return render(
        request,
        "even.html",
        {
            "check": check,
        },
    )


def four(reqeust, num1, num2):
    return render(
        reqeust,
        "four.html",
        {
            "plus": f"{num1} + {num2} = {num1 + num2}",
            "minus": f"{num1} - {num2} = {num1 - num2}",
            "multi": f"{num1} * {num2} = {num1 * num2}",
            "division": f"{num1} // {num2} = {num1 // num2}",
        },
    )


def name(request):
    return render(request, "name.html")


def prev_life(request):
    prev_list = ["말", "토끼", "호랑이", "독수리", "양", "사슴", "거북이", "너구리", "늑대"]
    prev_life = random.choice(prev_list)

    return render(
        request,
        "prev_life.html",
        {
            "name": request.GET.get("_name"),
            "prev_life": prev_life,
        },
    )


def lorem_input(request):
    return render(request, "lorem_input.html")


def lorem_check(request):
    count = request.GET.get("_count")
    word = request.GET.get("_text")

    lorems = [[] for _ in range(int(count))]
    lorem = ["가", "나", "다", "라", "마", "바", "사"]

    for i in range(len(lorems)):
        while len(lorems[i]) < int(word):
            s = random.choice(lorem)
            lorems[i].append(s)

    return render(
        request,
        "lorem_check.html",
        {"lorems": lorems},
    )
