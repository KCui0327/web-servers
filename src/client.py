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
    f = open("data.txt", "w")
    for value in result:
        f.write(value["content"] + '\n')
    f.close()

def main():
    url = "http://localhost:9000"
    response = requests.get(url)
    if response.status_code == 200:
        print("Response from server:")
        print(response.text)
    else:
        print(f"Failed to get response from server. Status code: {response.status_code}")
    
    retrieve_messages('1060348161547317388', config.authorization)
    
    r = requests.put(url, data='./data.txt')
    if r.status_code == 200:
        print("File uploaded sucessfully to server.")
    else:
        print("File was not able to be uploaded to server...")
        print(r.content)

if __name__ == "__main__":
    main()