import requests

url = "https://www.kuaishou.com/graphql"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

data = {"operationName":"brilliantTypeDataQuery","variables":{"hotChannelId":"00","page":"brilliant","pcursor":"1"},"query":"fragment photoContent on PhotoEntity {\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  __typename\n}\n\nfragment feedContent on Feed {\n  type\n  author {\n    id\n    name\n    headerUrl\n    following\n    headerUrls {\n      url\n      __typename\n    }\n    __typename\n  }\n  photo {\n    ...photoContent\n    __typename\n  }\n  canAddComment\n  llsid\n  status\n  currentPcursor\n  tags {\n    type\n    name\n    __typename\n  }\n  __typename\n}\n\nfragment photoResult on PhotoResult {\n  result\n  llsid\n  expTag\n  serverExpTag\n  pcursor\n  feeds {\n    ...feedContent\n    __typename\n  }\n  webPageArea\n  __typename\n}\n\nquery brilliantTypeDataQuery($pcursor: String, $hotChannelId: String, $page: String, $webPageArea: String) {\n  brilliantTypeData(pcursor: $pcursor, hotChannelId: $hotChannelId, page: $page, webPageArea: $webPageArea) {\n    ...photoResult\n    __typename\n  }\n}\n"}

response = requests.post(url, json=data, headers=headers)
json_data = response.json()

feeds = json_data["data"]["brilliantTypeData"]["feeds"]
for feed in feeds:
    name = feed["photo"]["id"]
    mp4_url = feed["photo"]["photoUrl"]
    with open(f"快手视频/{name}.mp4", "wb") as f:
        f.write(requests.get(mp4_url, headers=headers).content)
        print(name, "下载成功")

