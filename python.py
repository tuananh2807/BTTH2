import requests

page_id = '1062586164506537'
message = 'toi da lam duoc!'
access_token = 'EAAYcngG1ztEBOzewYdMMizi3LtiorqVwYrJINBDQ59OsHrqEj6MWwWlWy90CFjQHWTeNEmN0xkwN3m8fHIVkhJYuMf2spEPFPx2zQQj9xiKOQ6iwaFme8rkiEVs1mmfiynOdfVhiMkbOkSZCRnnB5ZCrh8LWjlgZBRFPPAlXZBB9rcmmZA7VDVB43AZCZBpM7BZCo3dxb4LDfyGnwPq6ebOuO3wG'

url = f'https://graph.facebook.com/{610446905492125}/feed'
payload = {
    'message': message,
    'access_token': access_token
}

r = requests.post(url, data=payload)
print(r.status_code)
print(r.text)