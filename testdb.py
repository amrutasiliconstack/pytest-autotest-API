import boto3
from boto3.dynamodb.conditions import Key

table_name = 'da-stage-prediction-platform-model-prediction'

session = boto3.session.Session(profile_name='default')
dynamodb = session.resource('dynamodb')
table = dynamodb.Table(table_name)
"""""
response = table.get_item(
    Key={
        'channelIdVehicleId': 'IAU#autotest-example-vehicle-id',
        'correlationId': 'e8807f19-9ff6-483c-8944-d53b3cdd1fad'
    }
)
print(type(response))

"""""
result = table.query(
    KeyConditionExpression=Key('channelIdVehicleId').eq('IAU#autotest-example-vehicle-id')
)

print(type(result))

#print(result['Items'])

for key in result['Items']:
    if key['correlationId'] == 'b24880be-151f-45fa-b9af-a3ec4bbcda30':
        print(key['prediction'] ,key['algorithmName'])
        



