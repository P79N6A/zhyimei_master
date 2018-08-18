import requests
import json
lp={"username":"13000000000","password":"123456"}
rd=requests.get("http://172.16.4.120/wuye/public/index.php/index/index//login?",params=lp)
print(rd.status_code)
print(rd.text)
data=json.loads(rd.text)
# print(data["message"])
cellphone=data["content"]["username"]
print(cellphone)





# lp1={"username":"13000000000"}
# rd1=requests.get("http://172.16.4.120/wuye/public/index.php/index/index//oauthAccount?",params=lp1)
# print(rd1.status_code)
# print(rd1.text)
#
# lp2={"token":"e10adc3949ba59abbe56e057f20f8824","username":"13000000000"}
# rd2=requests.get("http://172.16.4.120/wuye/public/index.php/index/index//allCommunityId?",params=lp2)
# print(rd2.status_code)
# print(rd2.text)
#
# lp3={"username":"13000000000","token":"e10adc3949ba59abbe56e057f20f8824","communityId":"1","pageNum":"1","pageSize":"2"}
# rd3=requests.get("http://172.16.4.120/wuye/public/index.php/index/index//taskInfoListByCondition?")
# print(rd3.status_code)
# print(rd3.text)


# print ("He is %d years old"%(25))
# print ("His height is %f m"%(1.83))
# print ("His height is %.2f m"%(1.83))
# print ("Name:%10s Age:%8d Height:%8.2f"%("Aviad",25,1.83))
# print ("Name:%-10s Age:%-8d Height:%-8.2f"%("Aviad",25,1.83))
# print ("Name:%-10s Age:%08d Height:%08.2f"%("Aviad",25,1.83))
# format(0.0015,'.2e')
list=[3,9,90,1]
# t=list.sort(reverse=True)
print sorted(list)