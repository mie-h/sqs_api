import boto3

def main():
    
    sqs_client = boto3.client('sqs')
    response = sqs_client.get_queue_url(QueueName='test_queue')
    print(f"get_queue_url response: {response}")
    lv_queue_url = response['QueueUrl']

    response = sqs_client.purge_queue(
        QueueUrl=lv_queue_url
    )
    print(response)


if __name__ == "__main__":
    main()