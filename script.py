import requests

url = "https://www.warrants.hsbc.com.hk/tc/data/chart/cbbcBandChart?pricedetails=1&ucode=HSI&step=10&spread=100&sdate=&_=1776428303601"

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "utag_main=v_id:019d970554e10015d601405ba9b805050003b00d00914$_sn:2$_ss:0$_st:1776430103691$v_rc:NSW$v_cc:AU$v_c:SYDNEY$ses_id:1776427594476%3Bexp-session$_pn:7%3Bexp-session$_prevpage:%E7%89%9B%E7%86%8A%E8%AD%89%E8%A1%97%E8%B2%A8%E5%88%86%E5%B8%83%E5%9C%96%20-%20%E5%85%A8%E6%96%B0%E6%BB%99%E8%B1%90%E8%AA%8D%E8%82%A1%E8%AD%89%E5%8F%8A%E7%89%9B%E7%86%8A%E8%AD%89%E7%B6%B2%E9%A0%81%3Bexp-session; hsbc_agree=yes",
    "Host": "www.warrants.hsbc.com.hk",
    "Referer": "https://www.warrants.hsbc.com.hk/tc/cbbc/cbbc-map/type/outstanding",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:149.0) Gecko/20100101 Firefox/149.0",
    "X-Requested-With": "XMLHttpRequest"
}

response = requests.get(url, headers=headers)

print(response.text)
