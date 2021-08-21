from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, FileField, validators
from wtforms.validators import DataRequired, ValidationError, InputRequired

IdNoRegex ='^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$'


def field_check(form, field):
    if field.data is None and field.data =='':
        raise ValidationError('输入项不可为null或者为空字符')
    if len(field.data) > 20:
        raise ValidationError('输入大于20字符')





class TransFileVaild(FlaskForm):

    appid = StringField('appid',
                        [InputRequired(message='appid不可为null')])

    outReqNo = StringField('outReqNo',
                           [InputRequired(message='outReqNo不可为null'),
                            field_check])

    outApplyNo = StringField('outApplyNo',
                             [InputRequired(message='outApplyNo不可为null'),
                              field_check])

    cusType = StringField('cusType',
                          [InputRequired(message='cusType不可为null'),
                           field_check])

    idNo = StringField('idNo',
                       [validators.Regexp(regex=IdNoRegex,message='身份证格式不正确')])


class FileVaild(FlaskForm):
        formFile = FileField('formFile', validators=[
            FileRequired(message='文件不能为null'),
            FileAllowed(['xls','xlsx'], '文件必须是excel后缀的格式文件')
        ])

'''
表单通用校验类
'''
class CommonVaild(FlaskForm):


    @staticmethod
    def vaildFormList(data,vaildDict):
        if(type(data).__name__=='ImmutableMultiDict'):
            formFieldNames = list(data.keys())
            print(formFieldNames)
        for key in formFieldNames:
            if(vaildDict.get(key)=='Y'):
                key = StringField(key,
                              [InputRequired(message='appid不可为null')])