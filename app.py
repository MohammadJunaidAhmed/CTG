from flask import Flask, render_template, request, session, redirect, url_for
import main

app = Flask(__name__)
app.secret_key = 'junaidAhmed'

@app.route('/', methods=['POST', 'GET'])
def home():
    main.initialize_course_data()
    course_data = main.course_data
    ans1 = []
    ans2 = []
    if request.method == 'POST':
        c11 = request.form.get("course11")
        c12 = request.form.get("course12")
        c13 = request.form.get("course13")
        c14 = request.form.get("course14")
        c15 = request.form.get("course15")
        c16 = request.form.get("course16")
        c21 = request.form.get("course21")
        c22 = request.form.get("course22")
        c23 = request.form.get("course23")
        c24 = request.form.get("course24")
        c25 = request.form.get("course25")
        c26 = request.form.get("course26")
        if(c11 != None):
            ans1.append(str(c11))
        if(c12 != None):
            ans1.append(str(c12))
        if(c13 != None):
            ans1.append(str(c13))
        if(c14 != None):
            ans1.append(str(c14))
        if(c15 != None):
            ans1.append(str(c15))
        if(c16 != None):
            ans1.append(str(c16))
        if(c21 != None):
            ans2.append(str(c21))
        if(c22 != None):
            ans2.append(str(c22))
        if(c23 != None):
            ans2.append(str(c23))
        if(c24 != None):
            ans2.append(str(c24))
        if(c25 != None):
            ans2.append(str(c25))
        if(c26 != None):
            ans2.append(str(c26))
        print(f"ANS1: {ans1}")
        print(f"ANS2: {ans2}")
        main.setWl1(ans1)
        main.setWl2(ans2)
        if(len(ans1) == 0 or len(ans2) == 0):
            return "NOT POSSIBLE!"
        fetched_api = main.frndTT()
        # print(fetched_api[0])
        print("\n\n")
        # print(fetched_api[1])
        if len(fetched_api) == 0:
            return "NOT POSSIBLE!"
        session['fetched_api'] = fetched_api
        session['course_data'] = course_data
        return redirect('/timetable')
    return render_template("select.html", course_data = course_data)

@app.route('/timetable')
def timetable():
    fetched_api = session.get('fetched_api')
    course_data = session.get('course_data')
    # print("\n\n\n")
    # print(fetched_api[0])
    # print("\n\n\n")
    # print(fetched_api[1])
    return render_template('timetable.html', api_data = fetched_api, course_data = course_data)
    # return "TIMETABLE"

@app.route('/github-profile')
def github_profile():
    return redirect("https://github.com/MohammadJunaidAhmed")


if __name__ == "__main__":
    app.run(debug = False, host='0.0.0.0')
