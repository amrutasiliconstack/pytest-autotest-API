import boto3

session = boto3.Session(profile_name='default')
sns_client = session.client('sns')

response = sns_client.list_subscriptions()

for key in response['Subscriptions']:
    print(key)
    print('-----------------------------')
