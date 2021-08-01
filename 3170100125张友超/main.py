from flask import Flask,request,url_for,render_template,redirect

app=Flask(__name__)
student=[["张友超",'3170100125',"18888922183","1693933133@qq.com"]]

def findnumber(Num):                                       
    for i in range(len(student)):
        for j in range(len(student[i])):
            if student[i][j]==Num:
                return i
    return -1

def save(stu):                                           
    studentfile=open('student.txt','w')
    for i in stu:
        for j in i:
            if j !=None:
                str=j
                studentfile.write(str)
                studentfile.write(' '*3)
        studentfile.write('\n')
    studentfile.close()

@app.route('/')                                          
def index():
    save(student)
    return render_template('index.html',student=student) 

@app.route('/delstu',methods=['GET','POST'])             
def delstu():
    if request.method=='POST':
        delnumber = request.form.get('delnumber')
        if findnumber(delnumber)==-1:
            return '您输入的联系人不存在'
        else:
            del student[findnumber(delnumber)]
            save(student)
            return redirect(url_for('index'))             
    return render_template('delstu.html',student=student)

@app.route('/addstu',methods=['GET','POST'])               
def addstu():
    if request.method=='POST':
        addnumber = request.form.get('addnumber')
        if findnumber(addnumber)!=-1:
            return "您输入的联系人已存在"
        else:
            addname = request.form.get('addname')
            addmail = request.form.get('addmail')
            addschoolid = request.form.get('addschoolid')         
            student.append([addname,addschoolid ,addnumber,addmail])
            print(student)
            save(student)
            return redirect(url_for('index'))
    return render_template('addstu.html')                     

@app.route('/altstu',methods=['GET','POST'])                 
def altstu():
    if request.method=='POST':
        altnumber = request.form.get('altnumber')
        altname = request.form.get('altname')
        altschoolid = request.form.get('altschoolid')
        altmail = request.form.get('altmail')
        if findnumber(altnumber)==-1:
            return '您输入的联系人不存在'
        else:
                if altschoolid !='':                              
                    student[findnumber(schoolid)][1]=altschoolid
                if altname!='':
                    student[findnumber(altname)][0]=altname
                if altmail!='':
                    student[findnumber(altmail)][3]=altmail
                if altnumber!='':
                    student[findnumber(altnumber)][2]=altnumber
                    save(student)
                return render_template('index.html', student=student)


    return render_template('altstu.html')

@app.route('/searchstu',methods=['GET','POST'])
def searchstu():
    if request.method=='POST':
        number = request.form.get('number')
        if findnumber(number)==-1:
            return '没有您要找的联系人'
        else:
            find=student[findnumber(number)]
            return render_template('searchstu.html',find=find)      
    return render_template('searchstu.html',student=student)

if __name__ == '__main__':
    app.run(debug=True)

