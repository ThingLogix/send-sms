import boto3


def lambda_handler(request, context):
    if 'recipientPhone' not in request or request['recipientPhone'] == '':
        raise Exception("Recipient phone not provided!")

    if 'message' not in request or request['message'] == '':
        raise Exception("Message not provided!")

    recipient_phone = request['recipientPhone']
    message = request['message']
    subject = None
    if 'subject' in request:
        subject = request['subject']

    send_sms(recipient_phone, message, subject)


def send_sms(phone_number, message, subject):
    sns_client = boto3.client('sns')
    if subject:
        sns_client.publish(PhoneNumber=phone_number, Subject=subject, Message=message)
    else:
        sns_client.publish(PhoneNumber=phone_number, Message=message)
