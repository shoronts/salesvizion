from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import question, answer
from django.http import Http404
import datetime
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
                allUrlsList.append(str(x.slug))

            nextUrlIm = allUrlsList[0]
            allUrlsList.remove(nextUrlIm)

            allUrlFuture = ''

            for a in allUrlsList:
                allUrlFuture += a + ','

            userExamFile = os.path.join('/home/salesvizion/salesvizion/userexam/' + str(userName) + 'exam.txt')
            createShoron = open(userExamFile, "w")
            createShoron.write(str(allUrlFuture))
            createShoron.close()

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
            userExamInfoFile = examVirsion+ ',' + str(date)
            userExamInfo = os.path.join('/home/salesvizion/salesvizion/userexam/' + str(userName) + 'examinfo.txt')
            createShoron1 = open(userExamInfo, "w")
            createShoron1.write(str(userExamInfoFile))
            createShoron1.close()

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
                userExamInfo = os.path.join('/home/salesvizion/salesvizion/userexam/' + str(userName) + 'examinfo.txt')
                runningQuestion = open(userExamInfo, "r")
                runningQuestion1 = runningQuestion.read().split(',')
                examVersion1 = runningQuestion1[0]
                examDate1 = runningQuestion1[1]
                runningQuestion.close()

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
                userExamAnsIm = str(question1) + ',' +  str(firstAns) + ',' + str(secondAns) + ',' + str(thirdAns)
                userExamInfo = os.path.join('/home/salesvizion/salesvizion/userexam/' + str(userName) + 'examanswer.txt')
                createShoron1 = open(userExamInfo, "w")
                createShoron1.write(str(userExamAnsIm))
                createShoron1.close()

                # Read File
                userExamInfo = os.path.join('/home/salesvizion/salesvizion/userexam/' + str(userName) + 'exam.txt')
                runningUrllist = open(userExamInfo, "r")
                runningUrl = runningUrllist.read().split(',')
                nextUrl = runningUrl[0]
                runningUrl.remove(nextUrl)
                runningUrllist.close()

                nextRunningUrlList = open(userExamInfo, "w")

                runningLastUrl = ''

                for l in runningUrl:
                    runningLastUrl += l + ','

                nextRunningUrlList.write(str(runningLastUrl))
                nextRunningUrlList.close()

                if nextUrl == '':
                    userName = request.session['usernameAll']
                    userExamFile = '/home/salesvizion/salesvizion/userexam/' + str(userName) + 'exam.txt'
                    userExamInfo2 = '/home/salesvizion/salesvizion/userexam/' + str(userName) + 'examinfo.txt'
                    userExamAns = '/home/salesvizion/salesvizion/userexam/' + str(userName) + 'examanswer.txt'
                    os.remove(userExamFile)
                    os.remove(userExamInfo2)
                    os.remove(userExamAns)
                    return redirect('results')
                    
                else:
                    lastUrl = str('/questions/' + nextUrl)
                    return redirect(lastUrl)

            except:
                userName = request.session['usernameAll']
                userExamFile = '/home/salesvizion/salesvizion/userexam/' + str(userName) + 'exam.txt'
                userExamInfo2 = '/home/salesvizion/salesvizion/userexam/' + str(userName) + 'examinfo.txt'
                userExamAns = '/home/salesvizion/salesvizion/userexam/' + str(userName) + 'examanswer.txt'
                os.remove(userExamFile)
                os.remove(userExamInfo2)
                os.remove(userExamAns)
                return redirect('results')

        else:
            try:
                userName = request.session['usernameAll']
                nextQuestion = question.objects.get(slug=slug)

                userExamInfo = os.path.join('/home/salesvizion/salesvizion/userexam/' + str(userName) + 'examanswer.txt')
                userAnsGiv = open(userExamInfo, "r")
                userAnsGiv1 = userAnsGiv.read().split(',')
                retQuestion = userAnsGiv1[0]
                retFirst = userAnsGiv1[1]
                retSecond = userAnsGiv1[2]
                retThird = userAnsGiv1[3]
                userAnsGiv.close()

                contex = {
                    'nextQuestions' : nextQuestion,
                    'userAnsGiv' : userAnsGiv1,
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
        try:
            userName = request.session['usernameAll']
            userExamFile = '/home/salesvizion/salesvizion/userexam/' + str(userName) + 'exam.txt'
            userExamInfo2 = '/home/salesvizion/salesvizion/userexam/' + str(userName) + 'examinfo.txt'
            userExamAns = '/home/salesvizion/salesvizion/userexam/' + str(userName) + 'examanswer.txt'
            os.remove(userExamFile)
            os.remove(userExamInfo2)

            try:
                os.remove(userExamAns)
                return render(request, 'questions/cancelexam.html')

            except:
                return render(request, 'questions/cancelexam.html')
        
        except:
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
            