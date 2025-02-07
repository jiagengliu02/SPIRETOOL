import requests
from bs4 import BeautifulSoup
from time import sleep

ICSID = ""
COOKIE = ""

############# GET Current ICStateNum #############
http_request = {
    "method": "GET",
    "url": "https://www.spire.umass.edu/psc/heproda_26/EMPLOYEE/SA/c/SSR_STUDENT_FL.SSR_SHOP_CART_FL.GBL",
    "params": {
        "Action": "U",
        "MD": "Y",
        "GMenu": "SSR_STUDENT_FL",
        "GComp": "SSR_START_PAGE_FL",
        "GPage": "SSR_START_PAGE_FL",
        "scname": "CS_SSR_MANAGE_CLASSES_NAV"
    },
    "headers": {
        "Host": "www.spire.umass.edu",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:135.0) Gecko/20100101 Firefox/135.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Referer": "https://login.microsoftonline.com/",
        "Connection": "keep-alive",
        "Cookie": COOKIE,
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Priority": "u=0, i"
    }
}
response = requests.get(http_request['url'], headers=http_request['headers'])
soup = BeautifulSoup(response.text, "html.parser")
ic_state_num_tag = soup.find("input", {"name": "ICStateNum"})
if ic_state_num_tag:
    ic_state_num = ic_state_num_tag.get("value")
    print("ICStateNum:", ic_state_num)
else:
    print("未找到 ICStateNum")


############## POST Request On your shop cart ############
http_request_post_1 = {
    "method": "POST",
    "url": "https://www.spire.umass.edu/psc/heproda_26/EMPLOYEE/SA/c/SSR_STUDENT_FL.SSR_SHOP_CART_FL.GBL",
    "headers": {
        "Host": "www.spire.umass.edu",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:135.0) Gecko/20100101 Firefox/135.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://www.spire.umass.edu",
        "Connection": "keep-alive",
        "Referer": "https://www.spire.umass.edu/psc/heproda_26/EMPLOYEE/SA/c/SSR_STUDENT_FL.SSR_MD_SP_FL.GBL"
                   "?Action=U&MD=Y&GMenu=SSR_STUDENT_FL&GComp=SSR_START_PAGE_FL&"
                   "GPage=SSR_START_PAGE_FL&scname=CS_SSR_MANAGE_CLASSES_NAV",
        "Cookie": COOKIE,
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    },
    "data":{
        "ICAJAX": 1,
        "ICNAVTYPEDROPDOWN": 0,
        "ICType": "Panel",
        "ICElementNum": 26,
        "ICStateNum": 132,
        "ICAction": "DERIVED_SSR_FL_SSR_ENROLL_FL",
        "ICModelCancel": 0,
        "ICXPos": 0,
        "ICYPos": 0,
        "ResponsetoDiffFrame": -1,
        "TargetFrameName": None,
        "FacetPath": None,
        "ICFocus": None,
        "ICSaveWarningFilter": 0,
        "ICChanged": 0,
        "ICSkipPending": 0,
        "ICAutoSave": 0,
        "ICResubmit": 0,
        "ICSID": ICSID,
        "ICActionPrompt": False,
        "ICBcDomData": "C~UnknownValue~EMPLOYEE~SA~SSR_STUDENT_FL.SSR_MD_SP_FL.GBL~..."
                    "UnknownValue*C~UnknownValue~EMPLOYEE~SA~SSR_STUDENT_FL.SSR_MD_SP_FL.GBL~..."
                    "UnknownValue*C~UnknownValue~EMPLOYEE~SA~SSR_STUDENT_FL.SSR_MD_SP_FL.GBL~...",
        "ICDNDSrc": None,
        "ICPanelHelpUrl": None,
        "ICPanelName": None,
        "ICPanelControlStyle": "pst_side1-fixed pst_panel-mode pst_side2-disabled pst_side2-hidden",
        "ICFind": None,
        "ICAddCount": None,
        "ICAppClsData": None,
        "win26hdrdivPT_SYSACT_PRVLST": None,
        "win26hdrdivPT_SYSACT_NXTLST": None,
        "win26hdrdivPT_SYSACT_RETLST": "psc_hidden",
        "win26hdrdivPT_SYSACT_HELP": "psc_hidden",
        "DERIVED_REGFRM1_SSR_SELECT$chk$0": "Y",
        "DERIVED_REGFRM1_SSR_SELECT$0": "Y"
    }
}

sleep(1)
http_request_post_1['data']['ICStateNum'] = str(int(ic_state_num))
response = requests.post(http_request_post_1['url'], headers=http_request_post_1['headers'], data=http_request_post_1['data'])

if "Are you sure you want to enroll" in response.text:
    print("Success!!!!!")
else:
    # print(response.text)
    print("Error!!!!!")

http_request_post_2 = {
    "method": "POST",
    "url": "https://www.spire.umass.edu/psc/heproda_26/EMPLOYEE/SA/c/SSR_STUDENT_FL.SSR_SHOP_CART_FL.GBL",
    "headers": {
        "Host": "www.spire.umass.edu",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:135.0) Gecko/20100101 Firefox/135.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://www.spire.umass.edu",
        "Connection": "keep-alive",
        "Referer": "https://www.spire.umass.edu/psc/heproda_26/EMPLOYEE/SA/c/SSR_STUDENT_FL.SSR_MD_SP_FL.GBL?Action=U&MD=Y&GMenu=SSR_STUDENT_FL&GComp=SSR_START_PAGE_FL&GPage=SSR_START_PAGE_FL&scname=CS_SSR_MANAGE_CLASSES_NAV",
        "Cookie": COOKIE,
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Priority": "u=0"
    },
    "data":{
        "ICAJAX": "1",
        "ICNAVTYPEDROPDOWN": "0",
        "ICType": "Panel",
        "ICElementNum": "26",
        "ICStateNum": "103",
        "ICAction": "#ICYes",
        "ICModelCancel": "0",
        "ICXPos": "0",
        "ICYPos": "0",
        "ResponsetoDiffFrame": "-1",
        "TargetFrameName": "None",
        "FacetPath": "None",
        "ICFocus": "",
        "ICSaveWarningFilter": "0",
        "ICChanged": "0",
        "ICSkipPending": "0",
        "ICAutoSave": "0",
        "ICResubmit": "0",
        "ICSID": ICSID,
        "ICActionPrompt": "false",
        "ICBcDomData": "C~UnknownValue~EMPLOYEE~SA~SSR_STUDENT_FL.SSR_MD_SP_FL.GBL~SSR_MD_TGT_PAGE_FL~Manage Classes~UnknownValue~UnknownValue~https://www.spire.umass.edu/psc/heproda_26/EMPLOYEE/SA/c/SSR_STUDENT_FL.SSR_MD_SP_FL.GBL?Action=U&MD=Y&GMenu=SSR_STUDENT_FL&GComp=SSR_START_PAGE_FL&GPage=SSR_START_PAGE_FL&scname=CS_SSR_MANAGE_CLASSES_NAV~UnknownValue*C~UnknownValue~EMPLOYEE~SA~SSR_STUDENT_FL.SSR_MD_SP_FL.GBL~SSR_MD_TGT_PAGE_FL~Manage Classes~UnknownValue~UnknownValue~https://www.spire.umass.edu/psc/heproda_26/EMPLOYEE/SA/c/SSR_STUDENT_FL.SSR_MD_SP_FL.GBL?Action=U&MD=Y&GMenu=SSR_STUDENT_FL&GComp=SSR_START_PAGE_FL&GPage=SSR_START_PAGE_FL&scname=CS_SSR_MANAGE_CLASSES_NAV~UnknownValue*C~UnknownValue~EMPLOYEE~SA~SSR_STUDENT_FL.SSR_MD_SP_FL.GBL~SSR_MD_TGT_PAGE_FL~Manage Classes~UnknownValue~UnknownValue~https://www.spire.umass.edu/psc/heproda_26/EMPLOYEE/SA/c/SSR_STUDENT_FL.SSR_MD_SP_FL.GBL?Action=U&MD=Y&GMenu=SSR_STUDENT_FL&GComp=SSR_START_PAGE_FL&GPage=SSR_START_PAGE_FL&scname=CS_SSR_MANAGE_CLASSES_NAV~UnknownValue*C~UnknownValue~EMPLOYEE~SA~SSR_STUDENT_FL.SSR_MD_SP_FL.GBL~SSR_MD_TGT_PAGE_FL~Manage Classes~UnknownValue~UnknownValue~https://www.spire.umass.edu/psc/heproda_26/EMPLOYEE/SA/c/SSR_STUDENT_FL.SSR_MD_SP_FL.GBL?Action=U&MD=Y&GMenu=SSR_STUDENT_FL&GComp=SSR_START_PAGE_FL&GPage=SSR_START_PAGE_FL&scname=CS_SSR_MANAGE_CLASSES_NAV~UnknownValue*C~UnknownValue~EMPLOYEE~SA~SSR_STUDENT_FL.SSR_MD_SP_FL.GBL~SSR_MD_TGT_PAGE_FL~Manage Classes~UnknownValue~UnknownValue~https://www.spire.umass.edu/psc/heproda_26/EMPLOYEE/SA/c/SSR_STUDENT_FL.SSR_MD_SP_FL.GBL?Action=U&MD=Y&GMenu=SSR_STUDENT_FL&GComp=SSR_START_PAGE_FL&GPage=SSR_START_PAGE_FL&scname=CS_SSR_MANAGE_CLASSES_NAV~UnknownValue*C~UnknownValue~EMPLOYEE~SA~SSR_STUDENT_FL.SSR_MD_SP_FL.GBL~SSR_MD_TGT_PAGE_FL~Manage Classes~UnknownValue~UnknownValue~https://www.spire.umass.edu/psc/heproda_26/EMPLOYEE/SA/c/SSR_STUDENT_FL.SSR_MD_SP_FL.GBL?Action=U&MD=Y&GMenu=SSR_STUDENT_FL&GComp=SSR_START_PAGE_FL&GPage=SSR_START_PAGE_FL&scname=CS_SSR_MANAGE_CLASSES_NAV~UnknownValue*C~UnknownValue~EMPLOYEE~SA~SSR_STUDENT_FL.SSR_MD_SP_FL.GBL~SSR_MD_TGT_PAGE_FL~Manage Classes~UnknownValue~UnknownValue~https://www.spire.umass.edu/psc/heproda_26/EMPLOYEE/SA/c/SSR_STUDENT_FL.SSR_MD_SP_FL.GBL?Action=U&MD=Y&GMenu=SSR_STUDENT_FL&GComp=SSR_START_PAGE_FL&GPage=SSR_START_PAGE_FL&scname=CS_SSR_MANAGE_CLASSES_NAV~UnknownValue",
        "ICDNDSrc": "",
        "ICPanelHelpUrl": "",
        "ICPanelName": "",
        "ICPanelControlStyle": "pst_side1-fixed pst_panel-mode  pst_side2-disabled pst_side2-hidden",
        "ICFind": "",
        "ICAddCount": "",
        "ICAppClsData": "",
        "win26hdrdivPT_SYSACT_PRVLST": "",
        "win26hdrdivPT_SYSACT_NXTLST": ""
    }
}

sleep(1)
http_request_post_2['data']['ICStateNum'] = str(int(ic_state_num)+1)
response = requests.post(http_request_post_2['url'], headers=http_request_post_2['headers'], data=http_request_post_2['data'])

if "This page is no longer available" in response.text:
    print("Error!!!!!")
elif "full" in response.text:
    print("Success!!!!!")


# need change ICSID and Cookie.