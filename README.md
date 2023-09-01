# linkedin-posts


Working on it, just uploaded to have the name


## Generate Access Token

The quickest way to get an Access Token is by using the Linkedin Token generator tool.

[https://www.linkedin.com/developers/tools/oauth/token-generator](https://www.linkedin.com/developers/tools/oauth/token-generator)




<!--


**You:**

I would like to create a python wrapper api for sharing posts in Linkedin using its official API. Could you help me out?

* * *

**ChatGPT:**

Of course, I'd be happy to help you create a Python wrapper API for sharing posts on LinkedIn using its official API. The LinkedIn API requires you to authenticate your requests using OAuth2, so I'll guide you through the steps to set up the authentication and share posts.

Before you start, make sure you have a LinkedIn Developer account and have created an application to obtain the necessary credentials.

Here's a high-level overview of the steps we'll cover:

1. Set up your LinkedIn Developer Account and App.
2. Obtain OAuth2 Access Token.
3. Create the Python Wrapper API.

Let's dive into the details:

### 1. Set up your LinkedIn Developer Account and App:

* Go to the LinkedIn Developer portal: [https://www.linkedin.com/developers/](https://www.linkedin.com/developers/)
* Create a new app and provide the necessary details.
* Note down the **Client ID** and **Client Secret**. You'll need these for authentication.

### 2. Obtain OAuth2 Access Token:

You'll need to authenticate your application and obtain an access token before making API requests.

Here's a basic example of how to obtain an access token using the `requests` library:

```python
import requests

client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
redirect_uri = 'YOUR_REDIRECT_URI'  # Set this in your LinkedIn app settings
auth_url = f'https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&state=YOUR_STATE&scope=w_member_social'

# Redirect the user to auth_url and retrieve the code after user authorization

# Exchange the code for an access token
code = 'CODE_FROM_AUTHORIZATION'  # Replace with the code you received
token_url = 'https://www.linkedin.com/oauth/v2/accessToken'
data = {
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': redirect_uri,
    'client_id': client_id,
    'client_secret': client_secret
}
response = requests.post(token_url, data=data)
access_token = response.json()['access_token']
```



Remember to replace placeholders like `'YOUR_CLIENT_ID'`, `'YOUR_CLIENT_SECRET'`, `'YOUR_REDIRECT_URI'`, and `'YOUR_PERSON_URN'` with your actual values.

This example should give you a basic idea of how to create a Python wrapper API for sharing posts on LinkedIn. Remember that handling errors, refreshing tokens, and more advanced features are necessary for a production-ready application. Additionally, LinkedIn's APIs might have evolved since my last knowledge update in September 2021, so make sure to refer to the latest official LinkedIn API documentation for any changes or updates.

* * *

**You:**

how would be the code using urllib insted of requests?

* * *

**ChatGPT:**

Sure, here's an example of how you can use the `urllib` library to achieve the same functionality of obtaining an access token and sharing a post on LinkedIn. We'll start with obtaining the access token:

```python
import urllib.parse
import urllib.request
import json

def get_access_token(client_id, client_secret, redirect_uri, authorization_code):
    token_url = 'https://www.linkedin.com/oauth/v2/accessToken'
    data = {
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(token_url, data=data, method='POST')
    response = urllib.request.urlopen(req)
    response_data = response.read().decode('utf-8')
    access_token = json.loads(response_data)['access_token']
    return access_token

# Usage
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
redirect_uri = 'YOUR_REDIRECT_URI'
authorization_code = 'CODE_FROM_AUTHORIZATION'
access_token = get_access_token(client_id, client_secret, redirect_uri, authorization_code)
```

Now, let's move on to sharing a post using the obtained access token:

```python
def share_linkedin_post(access_token, comment, visibility_code='anyone'):
    url = 'https://api.linkedin.com/v2/ugcPosts'

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'X-Restli-Protocol-Version': '2.0.0',
    }

    payload = {
        'author': 'urn:li:person:YOUR_PERSON_URN',  # Replace with your LinkedIn URN
        'lifecycleState': 'PUBLISHED',
        'specificContent': {
            'com.linkedin.ugc.ShareContent': {
                'shareCommentary': {
                    'text': comment
                },
                'shareMediaCategory': 'NONE'
            }
        },
        'visibility': {
            'com.linkedin.ugc.MemberNetworkVisibility': visibility_code
        }
    }

    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    response = urllib.request.urlopen(req)
    response_data = response.read().decode('utf-8')
    return json.loads(response_data)

# Usage
post_comment = "Check out my latest post!"
response = share_linkedin_post(access_token, post_comment)
print(response)
```

Remember to replace placeholders like `'YOUR_CLIENT_ID'`, `'YOUR_CLIENT_SECRET'`, `'YOUR_REDIRECT_URI'`, and `'YOUR_PERSON_URN'` with your actual values.

Keep in mind that using `urllib` might require more manual handling of data encoding and headers compared to `requests`, so ensure that you follow the LinkedIn API documentation closely for any additional requirements or changes.

* * *

**You:**

what if I would like to insert media (a photo or any kind of media) in the post?

* * *

**ChatGPT:**

If you want to insert media (such as a photo or other types of media) into a post when sharing it on LinkedIn, you can modify the payload of the request to include media content. The LinkedIn API allows you to include media links or URLs along with your post. Here's how you can modify the `share_linkedin_post` function to include media content:

```python
def share_linkedin_post_with_media(access_token, comment, media_url, visibility_code='anyone'):
    url = 'https://api.linkedin.com/v2/ugcPosts'

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'X-Restli-Protocol-Version': '2.0.0',
    }

    payload = {
        'author': 'urn:li:person:YOUR_PERSON_URN',  # Replace with your LinkedIn URN
        'lifecycleState': 'PUBLISHED',
        'specificContent': {
            'com.linkedin.ugc.ShareContent': {
                'shareCommentary': {
                    'text': comment
                },
                'shareMediaCategory': 'IMAGE',  # Adjust for different media types
                'media': [
                    {
                        'status': 'READY',
                        'originalUrl': media_url
                    }
                ]
            }
        },
        'visibility': {
            'com.linkedin.ugc.MemberNetworkVisibility': visibility_code
        }
    }

    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    response = urllib.request.urlopen(req)
    response_data = response.read().decode('utf-8')
    return json.loads(response_data)

# Usage
post_comment = "Check out my latest post with media!"
media_url = 'URL_TO_YOUR_MEDIA_FILE'  # Replace with the actual media URL
response = share_linkedin_post_with_media(access_token, post_comment, media_url)
print(response)
```

In the `specificContent` section of the payload, the `shareMediaCategory` specifies the type of media being shared. You can adjust this value based on the type of media you're sharing (e.g., IMAGE, VIDEO, ARTICLE).

Replace `'URL_TO_YOUR_MEDIA_FILE'` with the actual URL of the media you want to share. Also, make sure to handle potential errors and edge cases, as well as consult the latest LinkedIn API documentation for any updates or additional requirements.

Remember that the LinkedIn API and its endpoints may have evolved since my last knowledge update in September 2021, so it's always a good idea to refer to the official LinkedIn API documentation for the most accurate and up-to-date information.


-->
