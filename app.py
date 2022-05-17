import requests
from flask import Flask, render_template, request
import pyimgur
import json
from base64 import b64encode


def postFacebookQuote(caption):
    page_id_1 = 104983414515616

    facebook_access_token_1 ='EAA7tDWUReZBsBAFauxZAnVkBabsBsMGsKQ1MEE4cA83jOVlZAVn74jcPvaUXqU06PxYguWXtfFBEVyN3hBL1hLvDLTdfN4qfrFBfZBfWn9cxOZCGBgGGBndcnZAAC0un48HCLbcCp7muAO1MaQrLgkuNTZBKY2NKoyGNPf5G8OxSdsTvhZCVwZCMmhPHlNrn9DSkZD'
    post_url = 'https://graph.facebook.com/v10.0/{}/feed'.format(page_id_1)
    payload = {
    'message': caption,
    'access_token': facebook_access_token_1
    }
    r = requests.post(post_url, data=payload)

def postFacebookImage(imagelink, caption):
    page_id_1 = 104983414515616

    facebook_access_token_1 ='EAA7tDWUReZBsBAFauxZAnVkBabsBsMGsKQ1MEE4cA83jOVlZAVn74jcPvaUXqU06PxYguWXtfFBEVyN3hBL1hLvDLTdfN4qfrFBfZBfWn9cxOZCGBgGGBndcnZAAC0un48HCLbcCp7muAO1MaQrLgkuNTZBKY2NKoyGNPf5G8OxSdsTvhZCVwZCMmhPHlNrn9DSkZD'

    post_url = 'https://graph.facebook.com/v10.0/{}/photos'.format(page_id_1)
    payload = {
    'url': imagelink,
    'message': caption,
    'access_token': facebook_access_token_1
    }
    r = requests.post(post_url, data=payload)
def postInstagramQuote(imagelink, caption):
#Post the Image
    image_location_1 = 'https://i.imgur.com/Bs5dkj6.jpeg'
    post_url = 'https://graph.facebook.com/v10.0/{}/media'.format(17841436525643570)
    payload = {
    'image_url': imagelink,
    'caption': caption,#career #hiring #jobs #job #jobssouthafrica #hiringnow,
    'access_token': 'EAA7tDWUReZBsBAFauxZAnVkBabsBsMGsKQ1MEE4cA83jOVlZAVn74jcPvaUXqU06PxYguWXtfFBEVyN3hBL1hLvDLTdfN4qfrFBfZBfWn9cxOZCGBgGGBndcnZAAC0un48HCLbcCp7muAO1MaQrLgkuNTZBKY2NKoyGNPf5G8OxSdsTvhZCVwZCMmhPHlNrn9DSkZD'
    }
    r = requests.post(post_url, data=payload)
    print(r.text)
    result = json.loads(r.text)
    if 'id' in result:
        creation_id = result['id']
        second_url = 'https://graph.facebook.com/v10.0/{}/media_publish'.format(17841436525643570)
        second_payload = {
        'creation_id': creation_id,
        'access_token': 'EAA7tDWUReZBsBAFauxZAnVkBabsBsMGsKQ1MEE4cA83jOVlZAVn74jcPvaUXqU06PxYguWXtfFBEVyN3hBL1hLvDLTdfN4qfrFBfZBfWn9cxOZCGBgGGBndcnZAAC0un48HCLbcCp7muAO1MaQrLgkuNTZBKY2NKoyGNPf5G8OxSdsTvhZCVwZCMmhPHlNrn9DSkZD'
        }
        r = requests.post(second_url, data=second_payload)
        print(r.text)
        print('--------Just posted to instagram--------')

    else:
        print('HOUSTON we have a problem')

app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        venue = request.form.get('venue')
        caption = request.form.get('caption')

        if request.files['file'].filename != '':

            data = b64encode(request.files['file'].read())
            im = pyimgur.Imgur('58b5cfe926aab2d')
            uploaded_image = im._send_request('https://api.imgur.com/3/image', method='POST', params={'image': data})
            imagelink = uploaded_image['link']
        if venue == "insta":
            postInstagramQuote(imagelink, caption)
        else:
            if request.files['file'].filename != '':
                postFacebookImage(imagelink, caption)
            else:
                postFacebookQuote(caption)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
