import requests
import json

url = "http://192.168.10.1/api/aaaLogin.json"

payload = "{\n\t\"aaaUser\":\t{\n\t\t\"attributes\":\t{\n\t\t\t\"name\"\t:\t\"admin\",\n\t\t\t\"pwd\"\t:\t\"ciscoapic\"\n\t\t}\n\t}\n}"
headers = {'Authorization': 'Basic YWRtaW46Y2lzY29hcGlj'}

response = requests.request("POST", url, data=payload, headers=headers)

json_response = json.loads(response.text)

print(response.text)

tokenfromlogin =(json_response['imdata'][0]['aaaLogin']['attributes']['token'])

url = "http://192.168.10.1/api/node/mo/uni/tn-acme.json"

payload = "{\r\n\t\"fvTenant\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"dn\": \"uni/tn-acme\",\r\n\t\t\t\"name\": \"acme\",\r\n\t\t\t\"rn\": \"tn-acme\",\r\n\t\t\t\"status\": \"created\"\r\n\t\t},\r\n\t\t\"children\": []\r\n\t}\r\n}"
cookie = {"APIC-cookie": tokenfromlogin}

response = requests.request("POST", url, data=payload, cookies=cookie)

print(response.text)

payload = "{\r\n\t\"totalCount\": \"1\",\r\n\t\"imdata\": [{\r\n\t\t\"fvAp\": {\r\n\t\t\t\"attributes\": {\r\n\t\t\t\t\"descr\": \"\",\r\n\t\t\t\t\"dn\": \"uni/tn-acme/ap-Accounting\",\r\n\t\t\t\t\"name\": \"Accounting\",\r\n\t\t\t\t\"ownerKey\": \"\",\r\n\t\t\t\t\"ownerTag\": \"\",\r\n\t\t\t\t\"prio\": \"unspecified\"\r\n\t\t\t},\r\n\t\t\t\"children\": [{\r\n\t\t\t\t\"fvAEPg\": {\r\n\t\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\t\"descr\": \"\",\r\n\t\t\t\t\t\t\"matchT\": \"AtleastOne\",\r\n\t\t\t\t\t\t\"name\": \"Payroll\",\r\n\t\t\t\t\t\t\"prio\": \"unspecified\"\r\n\t\t\t\t\t},\r\n\t\t\t\t\t\"children\": [{\r\n\t\t\t\t\t\t\"fvRsCustQosPol\": {\r\n\t\t\t\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\t\t\t\"tnQosCustomPolName\": \"\"\r\n\t\t\t\t\t\t\t}\r\n\t\t\t\t\t\t}\r\n\t\t\t\t\t}, {\r\n\t\t\t\t\t\t\"fvRsBd\": {\r\n\t\t\t\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\t\t\t\"tnFvBDName\": \"unspecified\"\r\n\t\t\t\t\t\t\t}\r\n\t\t\t\t\t\t}\r\n\t\t\t\t\t}, {\r\n\t\t\t\t\t\t\"fvCrtrn\": {\r\n\t\t\t\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\t\t\t\"descr\": \"\",\r\n\t\t\t\t\t\t\t\t\"name\": \"default\",\r\n\t\t\t\t\t\t\t\t\"ownerKey\": \"\",\r\n\t\t\t\t\t\t\t\t\"ownerTag\": \"\"\r\n\t\t\t\t\t\t\t}\r\n\t\t\t\t\t\t}\r\n\t\t\t\t\t}, {\r\n\t\t\t\t\t\t\"fvRsProv\": {\r\n\t\t\t\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\t\t\t\"matchT\": \"AtleastOne\",\r\n\t\t\t\t\t\t\t\t\"prio\": \"unspecified\",\r\n\t\t\t\t\t\t\t\t\"tnVzBrCPName\": \"unspecified\"\r\n\t\t\t\t\t\t\t}\r\n\t\t\t\t\t\t}\r\n\t\t\t\t\t}]\r\n\t\t\t\t}\r\n\t\t\t}, {\r\n\t\t\t\t\"fvAEPg\": {\r\n\t\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\t\"descr\": \"\",\r\n\t\t\t\t\t\t\"matchT\": \"AtleastOne\",\r\n\t\t\t\t\t\t\"name\": \"Bills\",\r\n\t\t\t\t\t\t\"prio\": \"unspecified\"\r\n\t\t\t\t\t},\r\n\t\t\t\t\t\"children\": [{\r\n\t\t\t\t\t\t\"fvRsCons\": {\r\n\t\t\t\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\t\t\t\"prio\": \"unspecified\",\r\n\t\t\t\t\t\t\t\t\"tnVzBrCPName\": \"unspecified\"\r\n\t\t\t\t\t\t\t}\r\n\t\t\t\t\t\t}\r\n\t\t\t\t\t}, {\r\n\t\t\t\t\t\t\"fvRsCustQosPol\": {\r\n\t\t\t\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\t\t\t\"tnQosCustomPolName\": \"\"\r\n\t\t\t\t\t\t\t}\r\n\t\t\t\t\t\t}\r\n\t\t\t\t\t}, {\r\n\t\t\t\t\t\t\"fvRsBd\": {\r\n\t\t\t\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\t\t\t\"tnFvBDName\": \"unspecified\"\r\n\t\t\t\t\t\t\t}\r\n\t\t\t\t\t\t}\r\n\t\t\t\t\t}, {\r\n\t\t\t\t\t\t\"fvCrtrn\": {\r\n\t\t\t\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\t\t\t\"descr\": \"\",\r\n\t\t\t\t\t\t\t\t\"name\": \"default\",\r\n\t\t\t\t\t\t\t\t\"ownerKey\": \"\",\r\n\t\t\t\t\t\t\t\t\"ownerTag\": \"\"\r\n\t\t\t\t\t\t\t}\r\n\t\t\t\t\t\t}\r\n\t\t\t\t\t}]\r\n\t\t\t\t}\r\n\t\t\t}]\r\n\t\t}\r\n\t}]\r\n}"
response = requests.request("POST", url, data=payload, cookies=cookie)

print(response.text)