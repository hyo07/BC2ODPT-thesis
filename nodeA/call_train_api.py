import requests
import json

API_KEY = "6a294592f92c6adf7c749f4934ace3a23dceeecef46d82f65f01b9218cdacc26"

API_TYPE = "odpt:Train"
URL = "https://api-tokyochallenge.odpt.org/api/v4/{api_type}?acl:consumerKey={api_key}". \
    format(api_type=API_TYPE, api_key=API_KEY)


def call_api():
    resp = requests.get(URL)
    resp_j = resp.json()

    buses = []
    for re in resp_j:
        delay = re.get("odpt:delay")
        if (delay != 0) and delay:
            buses.append(
                {
                    "date": re.get("dc:date"),
                    "sameAs": re.get("owl:sameAs"),
                    "railDirection": re.get("odpt:railDirection"),
                    # 以下、存在しない場合あり
                    "fromStation": re.get("odpt:fromStation"),
                    "toStation": re.get("odpt:toStation"),
                    "originStation": re.get("odpt:originStation"),
                    "destinationStation": re.get("odpt:destinationStation"),
                    "delay": re.get("odpt:delay"),
                }
            )
        else:
            pass

    return json.dumps(buses)


if __name__ == "__main__":
    pass
    print(call_api())
