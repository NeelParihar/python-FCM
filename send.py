# Send to single device.
from pyfcm import FCMNotification

push_service = FCMNotification(api_key="<api_key>")

# OR initialize with proxies


# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

registration_id = "<device registration_id>"
message_title = "TEST"
message_body = "TESTDESC"
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)


print(result)
