import boto3

def main():
    sqs_client = boto3.client('sqs')
    response = sqs_client.get_queue_url(QueueName='queue_name')
    print(f"get_queue_url response: {response}")
    lv_queue_url = response['QueueUrl']


    lv_sqs_response = sqs_client.receive_message(
            QueueUrl=lv_queue_url,
            MaxNumberOfMessages=10,
    )
    lv_messages = lv_sqs_response.get('Messages', [])
    print(f"Number of messages received: {len(lv_messages)}")
    
    if len(lv_messages) > 0:
        for message in lv_messages:
            print(f"message from sqs: {message}")
            lv_receipt_handle = message['ReceiptHandle']

            response = sqs_client.delete_message(
                QueueUrl=lv_queue_url,
                ReceiptHandle=lv_receipt_handle,
            )
            print(response)


if __name__ == "__main__":
    main()