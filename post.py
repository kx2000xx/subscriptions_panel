import requests
import time
from bs4 import BeautifulSoup
import re
url = "https://arabnzb.co/"
def change_role(name, expiry_date, role):

    cookies = {
        'PHPSESSID': '44d72bd5261eae37f013b890b97810c2',
        'cf_clearance': 'RFi.iqCBlr7IX3V.buukqhQjjwlzV.wc_Z9yOd6Px7A-1733465363-1.2.1.1-ImDxhEKdGfRLyLlbsuOo0vIETW8UKIBI3vrPrQ997Gi2gvCwyd4jiney4GugGgb5fqh2.1vV.XlplrNP03Ig_hFaAxnw3ExwRPYgbzgBss8Tnpi5Iar7vvcxuhy6YEL_1OCZD1TpxWwcZ7NaBnB9opewvJGLJlKf3Qb10Suh9Ibs6x94hmnrnvrCK2l9.zLFcaviAKQKpE7bMvKsrRFplbzOpsjyiMDLTlXpeMTdPh4nlLtuE5Y1BzVL5YIogUQKD48yKStioiqmiAmHmHcmvopNf1pv7kwuzlgsfzcHAVMehnT8sq.W89nPNz5j4R6ogm9QBtq9nsJSxRh7D0TFgguYun2hyk3qEtQUyXnnomJUzRqnxm0nzY93JOcJRLQEIJ8Op_qsshKF.AsbHru5JP8ZSW.A0TTkIFERwsZ8IZl6ZJbMzv47EZwRkAj2DbIe',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Basic cGlyYXRlOjIpT1lJRGIjM2NVUQ==',
        'cache-control': 'no-cache',
        # 'cookie': 'cf_clearance=Jt1696ZLxaNw.5PeUJkGVav6FHnwBJ.dnCry_S7NFqk-1733461190-1.2.1.1-M4g9FtAHooeDnYzefTwOOZQZFFh7ho6khGcm0pM_VkGUJdpBjiMSiOR2mrw_O8XFb134MSuhZgZukl6o_iq8uWY9TyCBfOECFuJTgdtHmKbm7qTPMawrI3LormKcItqzbnTi7tRY0PXB6NVGsGbSUw.YKLGBhcD8UrkAyfvgQsxLcbZIE2XN8IY16o7ZkNULmvtnPwvDtfSM9HzxKN1ExA44XQz5nGU.e.But_yqPOtXtloUwpy4CzZTZZXuwmuC46EKjhcMnSMHdGP6RKBKYvqvn_4NB_LPRGDngg3yubGGh_0SX2nc6zFCc1KkVzCljT.MsIK24NNNOa_AsRGfOv7uczW6ZNc1dDhRsLaxVgW37eAYMBsC5YTAOpeLJHQv25xuQ._TDNACptEyB0lL62flfsjUUddPi1hIF7_yonAH7c66cMF.kLFnMeENPgpu; PHPSESSID=44d72bd5261eae37f013b890b97810c2',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://arabnzb.co/admin/user-list.php',
        'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version-list': '"Brave";v="131.0.0.0", "Chromium";v="131.0.0.0", "Not_A Brand";v="24.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    params = {
        'username': name,
        'email': '',
        'host': '',
        'role': '',
    }

    response = requests.get(f'{url}admin/user-list.php', params=params, cookies=cookies, headers=headers).content
    soup = BeautifulSoup(response, 'html.parser')
    anchor_tag = soup.find('a', title="Edit user")
    href_value = None
    if anchor_tag:
        href_value = anchor_tag['href']
        print(href_value)  # Output: /admin/user-edit.php?id=48

    userid = href_value.split('id=')[1]
    print(userid)



    response = requests.get(f'{url}{href_value}', params=params, cookies=cookies, headers=headers).content

    soup = BeautifulSoup(response, 'html.parser')

    # Find all <td> tags
    td_tags = soup.find_all('td')

    # Find all <input> tags inside <td> tags
    input_tags = []
    for td in td_tags:
        inputs_in_td = td.find_all('input')
        input_tags.extend(inputs_in_td)

    # Print the results
    for input_tag in input_tags:
        print(input_tag)

    regex = r'value="([^"]*)"'
    #2 email
    email = re.search(regex, str(input_tags[2])).group(1)
    #4 grabs
    grabs = re.search(regex, str(input_tags[4])).group(1)
    #5 invites
    invites = re.search(regex, str(input_tags[5])).group(1)

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Basic cGlyYXRlOjIpT1lJRGIjM2NVUQ==',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'cf_clearance=Jt1696ZLxaNw.5PeUJkGVav6FHnwBJ.dnCry_S7NFqk-1733461190-1.2.1.1-M4g9FtAHooeDnYzefTwOOZQZFFh7ho6khGcm0pM_VkGUJdpBjiMSiOR2mrw_O8XFb134MSuhZgZukl6o_iq8uWY9TyCBfOECFuJTgdtHmKbm7qTPMawrI3LormKcItqzbnTi7tRY0PXB6NVGsGbSUw.YKLGBhcD8UrkAyfvgQsxLcbZIE2XN8IY16o7ZkNULmvtnPwvDtfSM9HzxKN1ExA44XQz5nGU.e.But_yqPOtXtloUwpy4CzZTZZXuwmuC46EKjhcMnSMHdGP6RKBKYvqvn_4NB_LPRGDngg3yubGGh_0SX2nc6zFCc1KkVzCljT.MsIK24NNNOa_AsRGfOv7uczW6ZNc1dDhRsLaxVgW37eAYMBsC5YTAOpeLJHQv25xuQ._TDNACptEyB0lL62flfsjUUddPi1hIF7_yonAH7c66cMF.kLFnMeENPgpu; PHPSESSID=44d72bd5261eae37f013b890b97810c2',
        'origin': 'https://arabnzb.co',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': f'https://arabnzb.co/admin/user-edit.php?id={userid}',
        'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version-list': '"Brave";v="131.0.0.0", "Chromium";v="131.0.0.0", "Not_A Brand";v="24.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    params = {
        'action': 'submit',
    }
    #print(userid, name, email, grabs, invites)

    data = {
        'id': str(userid),
        'username': str(name),
        'email': str(email),
        'password': '',
        'grabs': str(grabs),
        'invites': str(invites),
        'movieview': '1',
        'role': str(role),
        'notes': str(expiry_date),
    }

    response = requests.post('https://arabnzb.co/admin/user-edit.php', params=params, cookies=cookies, headers=headers, data=data).content
    print(response)


#change_role("testacc", "2024-12-10", '7')