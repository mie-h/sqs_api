import json
import boto3

def main():
    sqs_client = boto3.client('sqs')
    response = sqs_client.get_queue_url(QueueName='queue_name')
    print(f"get_queue_url response: {response}")
    lv_queue_url = response['QueueUrl']

    lv_message_body = {
        "arg1": "arg1",
        "arg2": "arg2",
        "arg3": "arg3"
    }

    response = sqs_client.send_message(
        QueueUrl=lv_queue_url,
        MessageBody=json.dumps(lv_message_body)
    )
    print(f"response from sending a message to {lv_queue_url}: {response}")



if __name__ == "__main__":
    main()