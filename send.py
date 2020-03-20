# Send to single device.
from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AIzaSyB7gma6Pyek6Hz66NveDsKxMBIsH6-1HHw")

# OR initialize with proxies


# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

registration_id = "<device registration_id>"
message_title = "Uber update"
message_body = "Hi john, your customized news for today is ready"
result = push_service.notify_single_device(registration_id="faCzEmJ9s2g:APA91bFBHbXj1jW674WHffxKPhw26UxkM7OgrX9Yts0i6qwsDIcKXERh0t6bFkYJr9vUXKvFlkcN5K6u77720gnoOyXAlK50-QGn2p_nV0MkrEiWX5Bk3aFJUevB9s8HpRNHQUcgDIoZ", message_title=message_title, message_body=message_body)


print(result)