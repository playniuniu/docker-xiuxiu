# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request
from .utilities import save_photo_file

main = Blueprint('main', __name__)


# url for /
@main.route('/')
def router_index():
    return render_template('index.html')


# url for /question
@main.route('question/', methods=['GET'])
def router_question():
    return render_template('question.html', ans={})


# post url for /question
@main.route('question/', methods=['POST'])
def router_question_post():
    ans = {
        "question1": request.form.get("question1"),
        "question2": request.form.get("question2"),
        "question3": request.form.get("question3", "不帅"),
        "question4": request.form.get("question4"),
    }
    print(ans)

    photo_res = save_photo_file(request)
    print(photo_res)

    if photo_res:
        ans["photo"] = photo_res

    return render_template('question.html', ans=ans)
