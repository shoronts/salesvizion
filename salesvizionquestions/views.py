from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import question, answer
from django.http import Http404
import datetime
import pickle
import os


class IndexView(TemplateView):

    template_name = 'Mark Steele Users Questions'

        
    @login_required
    def question(request):
        if request.method == 'POST':
            userName = request.POST['username']
            allUrls = question.objects.all()

            # Find Next Urls
            allUrlsList = []
            for x in allUrls:
                allUrlsList.append(x.slug)

            nextUrlIm = allUrlsList[0]
            allUrlsList.remove(nextUrlIm)

            userExamFile = 'userexam/' + str(userName) + 'exam.dat'
            pickle.dump(allUrlsList, open(userExamFile, "wb"))

            # Find User Versions
            date = datetime.date.today()

            allvirsion = answer.objects.all()
            virsion = []

            for y in allvirsion:
                if userName == y.user:
                    virsion.append(y.examVersion[len(userName + 'virsion'):])

            allVirsion = list(dict.fromkeys(virsion))

            try:
                examVirsionCount = int(allVirsion[-1]) + 1
                examVirsion = userName + 'virsion' + str(examVirsionCount)
            except:
                examVirsion = userName + 'virsion1'

            #User Exam Version
            userExamInfoFile = [examVirsion, str(date)]
            userExamInfo = 'userexam/' + str(userName) + 'examinfo.dat'
            pickle.dump(userExamInfoFile, open(userExamInfo, "wb"))

            return redirect('allquestion', nextUrlIm)

        else:
            allQuestion = question.objects.all()
            contex = {
                'questions' : allQuestion,
                'totalQuestions' : allQuestion.count()
                }
            return render(request, 'questions/question.html', contex)


    @login_required
    def allquestion(request, slug):
        if request.method == 'POST':
            try:
                userName = request.session['usernameAll']
                question1 = request.POST['runningQues']
                firstAns = request.POST['firAns']
                secondAns = request.POST['secAns']
                thirdAns = request.POST['tirAns']

                # Read File
                userExamInfo1 = 'userexam/' + str(userName) + 'examinfo.dat'
                runningQuestion = pickle.load(open(userExamInfo1, "rb"))
                examVersion1 = runningQuestion[0]
                examDate1 = runningQuestion[1]

                saveAns = answer(
                    user = userName,
                    examVersion = examVersion1,
                    examDate = examDate1,
                    question= question1,
                    firstAnswer = firstAns,
                    secondAnswer = secondAns,
                    thirdAnswer = thirdAns)
                saveAns.save()

                # Write File
                userExamAnsIm = [str(question1), str(firstAns), str(secondAns), str(thirdAns)]
                userExamAns = 'userexam/' + str(userName) + 'examanswer.dat'
                pickle.dump(userExamAnsIm, open(userExamAns, "wb"))

                # Read File
                userExamFile = 'userexam/' + str(userName) + 'exam.dat'
                runningQuestion = pickle.load(open(userExamFile, "rb"))

                nextUrl = runningQuestion[0]
                runningQuestion.remove(nextUrl)

                pickle.dump(runningQuestion, open(userExamFile, "wb"))
                lastUrl = str('/questions/' + nextUrl)
                return redirect(lastUrl)

            except:
                userExamFile = 'userexam/' + str(userName) + 'exam.dat'
                userExamAns = 'userexam/' + str(userName) + 'examanswer.dat'
                userExamInfo2 = 'userexam/' + str(userName) + 'examinfo.dat'
                os.remove(userExamFile)
                os.remove(userExamAns)
                os.remove(userExamInfo2)
                return redirect('results')

        else:
            try:
                userName = request.session['usernameAll']
                nextQuestion = question.objects.get(slug=slug)
                userExamAns = 'userexam/' + str(userName) + 'examanswer.dat'
                userAnsGiv = pickle.load(open(userExamAns, "rb"))

                retQuestion = userAnsGiv[0]
                retFirst = userAnsGiv[1]
                retSecond = userAnsGiv[2]
                retThird = userAnsGiv[3]

                contex = {
                    'nextQuestions' : nextQuestion,
                    'userAnsGiv' : userAnsGiv,
                    'retQuestion' : retQuestion,
                    'retFirst' : retFirst,
                    'retSecond' : retSecond,
                    'retThird' : retThird,
                    }
                return render(request, 'questions/allquestions.html', contex)

            except:
                nextQuestion = question.objects.get(slug=slug)

                contex = {
                    'nextQuestions' : nextQuestion
                    }
                return render(request, 'questions/allquestions.html', contex)

    @login_required
    def cancelexam(request):
        userName = request.session['usernameAll']
        userExamFile = 'userexam/' + str(userName) + 'exam.dat'
        userExamInfo2 = 'userexam/' + str(userName) + 'examinfo.dat'
        userExamAns = 'userexam/' + str(userName) + 'examanswer.dat'
        os.remove(userExamFile)
        os.remove(userExamInfo2)

        try:
            os.remove(userExamAns)

        except:
            pass

        return render(request, 'questions/cancelexam.html')


    @login_required
    def result(request):
        userName = request.session.get('usernameAll')
        res = answer.objects.all()
        allusersversionlist = []
        alluserDatelist = []

        for r in res:
            if r.user == userName:
                allusersversionlist.append(r.examVersion)
                alluserDatelist.append(r.examDate)

        currentUserExamList = list(dict.fromkeys(allusersversionlist))
        currentUserExamDate = list(dict.fromkeys(alluserDatelist))
        contex = {
            'result' : currentUserExamList,
            'date' : currentUserExamDate
        }
        return render(request, 'questions/result.html', contex)

    @login_required
    def singleresult(request, slug):
        results = answer.objects.all()
        contex = {
            "results" : results,
            "resultCount" : slug
        }
        shoron = []
        for r in results:
            if r.examVersion == slug:
                shoron.append(r.examVersion)

        if len(shoron) > 0:
            return render(request, 'questions/singleresults.html', contex)
        else:
            raise Http404