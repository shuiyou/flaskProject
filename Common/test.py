import json
import time


t = time.time()
now = int(time.time())
productCode ='08001'
appId='0000000000'
outApplyNoPrefix='IQP'+str(now)
Single = False
renewLoans =False
historicalBiz =[]
applyAmo = 1500000
riskSubjectType ='PERSONAL'
riskSubject ={
    'certType':'ID_CARD_NO',
    'phone':'13063218576',
    'name':'顾顺军',
    'marryState':None,
    'middleSignCode':None

}

relations =[]

personalSoupObject={
    "relationType":"SPOUSE",
    "certType":"ID_CARD_NO",
    "code":"321323XXXXX0804062X",
    "name":"张岩",
    "riskSubjectType":"PERSONAL",
    "fundedRatio":None,
    "phone":"18601650799",
    "marryState":None,
    "applyAmo":1500000,
    'relations':None
}

PARENTObject={

        'relationType':'PARENT',
        'certType':'ID_CARD_NO',
        'code':'310106XXX703251219',
        'name':'赵政',
        'riskSubjectType':'PERSONAL',
        'fundedRatio':None,
        'phone':'18602158606',
        'marryState':None,
        'applyAmo':1500000,
        'relations':None

}

LegalObject={
    'relationType':'LEGAL',
    'certType':'CREDIT_CODE',
    'code':'913101XXX41232XY',
    'name':'上海承赫市XXX有限公司',
    'riskSubjectType':'COMPANY',
    'fundedRatio':None,
    'phone':None,
    'marryState':None,
    'applyAmo':1500000,
    'relations':None
}


ControllerObject={
    'relationType':'LEGAL',
    'certType':'CREDIT_CODE',
    'code':'913101XXX41232XY',
    'name':'上海承赫市XXX有限公司',
    'riskSubjectType':'COMPANY',
    'fundedRatio':None,
    'phone':None,
    'marryState':None,
    'applyAmo':1500000,
    'relations':None
}


#CREDIT_CODE 社会信用代码 REG_NO公司注册号

companyObject ={
    'certType': 'CREDIT_CODE',
    'code': '12370700F51078958R',
    'phone': None,
    'name': '潍坊市财政票据服务中心',
    'marryState': None,
    'applyAmo': 1500000,
    'riskSubjectType': 'COMPANY',
    'middleSignCode': None

}


#企业法人为企业
companyLegalOb_company={
    'relationType':'LEGAL',
    'certType':'CREDIT_CODE',
    'code':'91370700MA3N1UE859',
    'name':'潍坊港华舒适家生活服务有限公司',
    'riskSubjectType':'COMPANY',
    'fundedRatio':None,
    'phone':None,
    'marryState':None,
    'applyAmo':1500000,
    'relations':None
}

#企业法人为个人
companyLegalOb_personal={
    'relationType':'LEGAL',
    'certType':'ID_CARD_NO',
    'code':'370226196705161230',
    'name':'刘官军',
    'riskSubjectType':'PERSONAL',
    'fundedRatio':None,
    'phone':'13063338576',
    'marryState':'UNMARRIED',
    'applyAmo':1500000,
    'relations':None
}
companyControllerOb_company={
    'relationType':'CONTROLLER',
    'certType':'CREDIT_CODE',
    'code':'13124235345345',
    'name':'测试公司',
    'riskSubjectType':'COMPANY',
    'fundedRatio':None,
    'phone':None,
    'marryState':None,
    'applyAmo':1500000,
    'relations':None
}

companyControllerOb_personal={
    'relationType':'CONTROLLER',
    'certType':'ID_CARD_NO',
    'code':'370226196705161230',
    'name':'刘官军',
    'riskSubjectType':'PERSONAL',
    'fundedRatio':None,
    'phone':'13063338576',
    'marryState':'UNMARRIED',
    'applyAmo':1500000,
    'relations':None
}



RELATION_ENT={
    'relationType':'',
    'certType':'CREDIT_CODE',
    'code':'913101XXXX6241232XY',
    'name':'上海承XXXX营销有限公司',
    'riskSubjectType':'COMPANY',
    'fundedRatio':None,
    'phone':None,
    'marryState':None,
    'applyAmo':1500000,
    'relations':None
}
class ReationEnt():
    def __init__(self,relationType,code,name,**kwargs):
        RELATION_ENT.update({'relationType':relationType})
        RELATION_ENT.update({'code':code})
        RELATION_ENT.update({'name':name})
        for key in kwargs.keys():
            if RELATION_ENT.keys().__contains__(key):
                value = kwargs.get(key)
                RELATION_ENT.update({key:value})
        print('构造的关联企业中不存在属性'+key)








totalReqest={
    'productCode':productCode,
    'appId':appId,
    'timestamp':now,
    'outApplyNo':outApplyNoPrefix,
    'single':Single,
    'renewLoans':False,
    'applyAmo':1500000,
    'historicalBiz':None,
    'riskSubject':None,
    'relations':relations
}



#生成流水报告生成请求报文
'''
@Parma：MainLabel 报告主题（PERSOANL，COMPANY）
        MarryLabel 婚姻标识
        OtherRelationList（其他关系），PERSONAl（PARENT 父母，CHILD 子女，MAIN_RELATION_ENT，借款人关联企业）
        COMPANY（CONTROLLER_PERSONAL 企业实控人为个人，CONTROLLER_COMPANY（实控人为企业）
'''
def createRiskSubject(MainLabel,MarryLabel,OtherRelationList):
    if(MainLabel=='Personal'):
        if(MarryLabel==True):
            riskSubject ={
                'certType':'ID_CARD_NO',
                'code':'310115198111286873',
                'phone':'13063218576',
                'name':'顾顺军',
                'marryState':'MARRIED',
                'applyAmo':applyAmo,
                'riskSubjectType':'PERSONAL',
                'middleSignCode':None

            }
            totalReqest.update({'riskSubject':riskSubject})
            relations.append(personalSoupObject)
        else:
            riskSubject ={
                'certType':'ID_CARD_NO',
                'phone':'13063218576',
                'name':'顾顺军',
                'marryState':'UNMARRIED',
                'middleSignCode':None
            }
            totalReqest.update({'riskSubject':riskSubject})
        if(OtherRelationList.__contains__('PARENT')):
            relations.append(PARENTObject)
        if(OtherRelationList.__contains__('Legal')):
            relations.append(LegalObject)
        if(OtherRelationList.__contains__('CONTROLLER')):
            relations.append(ControllerObject)
        return totalReqest
    else:
        totalReqest.update({'riskSubject':companyObject})
        controllerRealtionList =[]
        if(OtherRelationList.__contains__('CONTROLLER_PERSONAL')):
            if(MarryLabel==True):
                companyControllerOb_personal.update({'marryState':'MARRIED'})
                personalSoupObject.update({'relationType':'CONTROLLER_SPOUSE'})
                controllerRealtionList.append(personalSoupObject)
                if(OtherRelationList.__contains__('CONTROLLER_RELATION_ENT')):
                    controllerRealtionList.append(RELATION_ENT)
            if(controllerRealtionList is not None and len(controllerRealtionList)!=0):
                companyControllerOb_personal.update({'relations':controllerRealtionList})
            relations.append(companyControllerOb_personal)
        if(OtherRelationList.__contains__('CONTROLLER_COMPANY')):
            relations.append(companyControllerOb_company)
        if(OtherRelationList.__contains__('Legal_Personal')):
            relations.append(companyLegalOb_personal)
        if(OtherRelationList.__contains__('Legal_company')):
            relations.append(companyLegalOb_company)
        return totalReqest
if __name__ == '__main__':
    # a=createRiskSubject('COMPANY',True,['CONTROLLER_PERSONAL','Legal_Personal'])
    # print(json.dumps(a))
    r =ReationEnt('CONTROLLER_RELATION_ENT','12370700F51078958R','快跑九州配送服务有限公司',certType='REG_NO',fundedRatio='0.9',a='6')
    a =createRiskSubject('COMPANY',True,['CONTROLLER_PERSONAL','CONTROLLER_RELATION_ENT','Legal_Personal'])
    print(a)
