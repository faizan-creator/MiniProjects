from django.shortcuts import render,HttpResponse,redirect
from .models import Contact
from django.contrib import messages
from .models import Test,Contact
import ast , requests
from bs4 import BeautifulSoup

questions = list(Test.objects.values('question'))
#print(questions)
conversation=[]
for m in range(0,len(questions)):
    conversation.append(str(questions[m]['question']).strip())
    #print(conversation[m])

op = list(Test.objects.values('options'))
#print(op)
options = []
for m in range(0,len(op)):
    options.append(op[m]['options'])
    options[m]=ast.literal_eval(options[m])
    #options[m]=[n.strip() for n in options[m]]
    #print(options[m])
#options=[n.strip() for n in options]
#print(options)

prior = list(Test.objects.values('priority'))
#print(prior)
pr = []
for m in range(0,len(prior)):
    pr.append(prior[m]['priority'])
    pr[m]=ast.literal_eval(pr[m])
    #print(pr[m])
#print(pr)

#from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
#englishBot  = ChatBot('ChatterBot',storage_adapter='chatterbot.storage.SQLStorageAdapter')
#trainer1 = ChatterBotCorpusTrainer(englishBot )
#trainer1.train('chatterbot.corpus.english')
#conversation = { 'hi1':'hi2' , 'hi2':'hi3' , 'hi4':'hi5' , 'hi6':'hi7' , 'hi8':'hi9' }
#chatbot = ChatBot("My Bot")
#trainer2 = ListTrainer(chatbot)
#trainer2.train(conversation)
#q1 = 'Please select your age group :<br> 1.Below 15 , 2. 16-24 , 3. 25-55 , 4. Above 55'
#q2 = 'May I know your Gender :<br> Male. Female. Others'
#q2 = 'Have you travelled to any pandemic area recently ? <br> Yes. No. '
#q3 = 'Is any of your immediate family member diagnosed with covid ? <br> Yes. No.'
#q4 = "Do you have symptoms of 'High Fever' ? <br> Yes. No. "
#q5 = "Do you have symptoms of 'Dry Cough' ? <br> Yes. No. "
#q6 = "Do you have symptoms of 'Running Nose' ? <br> Yes. No. "
#q7 = "Do you have symptoms of 'Headache' ? <br> Yes. No. "
#q8 = "Do you have symptoms of 'Chest Pain' ? <br> Yes. No. "
#q9 = "Do you have symptoms of 'Tiredness' ? <br> Yes. No. "
#q10 = "Do you know someone who later became covid positive after your meeting with that person recently ? <br> Yes. No. "

#conversation = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]
#options = [ [1,2,3,4] , ['Yes','No'] , ['Yes','No'] , ['Yes','No'] , ['Yes','No'] , ['Yes','No'] , ['Yes','No'] , ['Yes','No'] , ['Yes','No'] , [ 'Yes','No' ] ]
#print(options)
#pr = [ [0,0,2,5] , [10,0] , [10,0] , [25,0] , [10,0] , [10,0] , [5,0] , [10,0] , [5,0] , [10,0] ]


per = 0
ans = []
i = -1
# Create your views here.
def test(self):
    global i,per,ans
    i = -1
    ans.clear()
    per = 0
    return render(self,'test.html')

def get(self):
    global per,i,ans
    userText = str(self.GET.get('msg')).strip().upper()
    if userText is not None:
        i = i + 1
        if i > len(conversation):
            i = -1
            #print(ans)
            ans.clear()
            #print(ans)
            per = 0
            return HttpResponse(str("Hello Dear! I'm your Friend ChatBot"))
            #return HttpResponse(str(conversation[i]))
        else:
            if i == 0 :
                return HttpResponse(str(conversation[i]))
            #print(userText)
            #print(options[i-1])
            #print(i)
            #print(options[i-1][1])
            #print(type(options[i-1][1]))
            chk = [ j for j in range(0,len(options[i-1])) if str(options[i-1][j]).strip().upper()==userText ]-------------
            #print(chk)
            if ( len(chk) != 0 ) :
                #print('Faizan1')
                ans.append(userText)
                #print(ans)
                if (i == len(conversation)):
                    for j in range(0,i):
                        ind = [k for k in range(0,len(list(options[j]))) if str(options[j][k]).strip().upper() == str(ans[j]) ]
                        #print(ind)
                        per = per + pr[j][ind[0]]
                    if ( str(per) == str(0) ) :
                        return HttpResponse("<b>As per the Input, You don't have symptoms of Corona. So just chill...</b>")
                    elif(int(per)>=60):
                        return HttpResponse(str("<b>As per the Input, You may have near about " + str(
                            per) + " percentage of symptoms of Corona. It's critical, Kindly visit for test asap.</b>"))
                    return HttpResponse(str("<b>As per the Input, You may have near about "+str(per)+" percentage of symptoms of Corona.</b>"))
                return HttpResponse(str(conversation[i]))
            else:
                #print('Faizan2')
                i = i-1
                return HttpResponse(str('Kindly provide correct option.<br>'+conversation[i]))
        #op1=englishBot.get_response(userText)
        #print(op1)
        #op2=chatbot.get_response(userText)
        #print(op2)
        #return HttpResponse(str(op2))
    else:
        return redirect('/')

def count(self):
    print('FAIZAN1')
    #myhtmldata = requests.get("https://www.covidhotspots.in/").text
    #myhtmldata = requests.get("http://www.mohfw.gov.in/").text
    #print(myhtmldata)
    print('FAIZAN2')
    #soup = BeautifulSoup(myhtmldata, 'html.parser')
    #print(soup.prettify())
    #for table in soup.find('tbody'):
        #print(table)
    #myDatastr=""
    #for table in soup.find_all('tr')[1:-4]:
        #print(table.get_text())
        #myDatastr+=table.get_text()
    #myDatastr = myDatastr[1:]
    #print(myDatastr.split("\n"))
    #itemlist = myDatastr.split("\n\n")
    #for item in itemlist[0:35]:
        #print(item)
        #print(item.split('\n'))
    return render(self, 'count.html')

#def fund(self):
    #return render(self,'fund.html')

def edit(self):
    if self.method == 'POST':
        cnt = 0
        firstname = self.POST.get('FName').strip()
        lastname = self.POST.get('LName').strip()
        userid = self.user
        pass1 = self.POST.get('pass1').strip()
        pass2 = self.POST.get('pass2')
        if pass1 != pass2:
            messages.error(self, "New Passwords do not match OR May contain white spaces at starting or ending positions.")
            return render(self,'edit.html')
        emailing = self.POST.get('Email').strip()
        #print(emailing)
        if firstname != '':
            userid.first_name = firstname
            cnt = cnt + 1
        if lastname != '':
            userid.last_name = lastname
            cnt = cnt + 1
        if pass1 != '':
            userid.set_password(pass1)
            cnt = cnt + 1
        if emailing != '':
            #print(emailing)
            userid.email=emailing
            #print(emailing)
            cnt = cnt + 1
        userid.save()
        if cnt > 0:
            messages.success(self, 'Your account has been successfully Updated.')
            cnt = 0
    return render(self,'edit.html')

def contact(self):
    thank = False
    params = []
    if self.method == 'POST':
        #print(self)
        userid = self.POST.get('userid', '')
        name = self.POST.get('Name', '')
        phone = self.POST.get('Phone', '')
        email = self.POST.get('Email', '')
        desc = self.POST.get('Desc', '')
        contact = Contact(userid=userid, name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    cont = Contact.objects.filter(userid=self.user)
    #print(cont)
    params.append([cont,thank])
    return render(self, 'contact.html', {'params': params})