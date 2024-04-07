import config
import requests
import json

def retrieve_messages(channelId, auth_key):
    headers = {
        'authorization': auth_key
    }
    
    r = requests.get(
        f'https://discord.com/api/v9/channels/{channelId}/messages',
        headers=headers
    )
    result = json.loads(r.text)
    f = open("./test/data.txt", "w")
    for value in result:
        f.write(value["content"] + '\n')
    f.close()

def main():
    url = "http://127.0.0.1:8000"
    response = requests.get(url)
    if response.status_code == 200:
        print("Response from server:")
        print(response.text)
    else:
        print(f"Failed to get response from server. Status code: {response.status_code}")
    
    retrieve_messages(config.channel_id, config.authorization)
    
    file = {'file': open('./test/data.txt', 'rb')}
    
    r = requests.put(url, data=file)
    if r.status_code == 201:
        print("File uploaded successfully to server.")
    else:
        print("File was not able to be uploaded to server...")
        print(r.content)


if __name__ == "__main__":
    main()