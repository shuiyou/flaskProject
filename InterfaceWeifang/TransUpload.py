import requests

reqAdress =''
reqDir ='/api/open/trans/parse_verify'
requestsUrl =reqAdress+reqDir



def SecflowUpdaown(reqParams):
    rep =requests.post(requestsUrl, params=reqParams,verify=False)