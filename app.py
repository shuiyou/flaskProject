from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import csrf, CSRFProtect

from Common.FormVaild import FileVaild, TransFileVaild, CommonVaild
from InterfaceWeifang.TransUpload import SecflowUpdaown

csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = '08ca781b2517402ea4bcad6af63f881b'
    Bootstrap(app)
    csrf.init_app(app)
    return app

app = create_app()

@app.route('/')
def view_index():
    return render_template("navbar.html", title="Home page")

@app.route('/first')
def view_first_page():
    return render_template('secflowUpdate.html', title="first page")

@app.route('/URLencode')
def view_urlEncode_page():
    return render_template('URLencodeAndDencode.html', title="URLencode page")

@app.route('/')
def view_parselLocal_page():
    return render_template('ParseLocalTransFile.html', title="parse page")


@app.route('/handleFile',methods=['post'])
def handleFileUploar():
    formdata = TransFileVaild(formdata=request.form)
    formdataFile =FileVaild(formdata=request.files)
    if formdata.validate_on_submit() and formdataFile.validate_on_submit():
        requestparms =(request.form).to_dict()
        requestparms.add('formFile',request.file.get('formFile'))
        repsone =SecflowUpdaown(requestparms)
        return repsone
    else:
        e =''
        if len(formdata.errors)!=0:
                for i in formdata.errors:
                    ele = formdata.errors[i]
                    for i in range(len(ele)):
                        error_msg = str(ele[i])+','
                        e+=error_msg
        if len(formdataFile.errors)!=0:
            for i in formdata.errors:
                ele = formdata.errors[i]
                for i in range(len(ele)):
                    error_msg = str(ele[i])+','
                    e+=error_msg

        return e



if __name__ == '__main__':
    app.run()
