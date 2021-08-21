from Common.test import companyObject, companyLegalOb_company, companyLegalOb_personal, companyControllerOb_personal, \
    RELATION_ENT


class CompanyOb():
    def __init__(self,name,Code):
        companyObject.update({'code':Code})
        companyObject.update({'name':name})

class ComLegOb_RealtionCom():
    def __init__(self,name,Code):
        companyLegalOb_company.update({'code':Code})
        companyLegalOb_company.update({'name':name})

class ComLegOb_RealtionPer():
    def __init__(self,name,Code):
        companyLegalOb_personal.update({'code':Code})
        companyLegalOb_personal.update({'name':name})

class ComControllerOb_RealtionCom():
    def __init__(self,name,Code):
        companyControllerOb_personal.update({'code':Code})
        companyControllerOb_personal.update({'name':name})


class RELATION_ENT_Ob():
    def __init__(self,relationType,Code,Name):
        RELATION_ENT.update({'relationType':relationType})
        RELATION_ENT.update({'code':Code})
        RELATION_ENT.update({'name':Name})
        self._relationEnt =RELATION_ENT

    def getRealtionEnt(self):
        return self._relationEnt