import boto3
from decimal import *

class dynamoDbStorage:

    def __init__(self, strDbTable, lstData = []):
        self.setData(lstData)
        self.setDbTable(strDbTable)

    # Clean up data for dynamodb
    def _clean(self, dictData):
        dictCleanData = {}
        for key in dictData:
            value_type = type(dictData[key])
            if value_type == float:
                dictCleanData[key] = Decimal(str(dictData[key]))
            elif value_type == bool:
                if dictData[key]:
                    dictCleanData[key] = 1
                else:
                    dictCleanData[key] = 0

            elif value_type == str:
                if dictData[key] != '':
                    dictCleanData[key] = dictData[key]
            else:
                dictCleanData[key] = dictData[key]

        return dictCleanData

    def save(self):
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(self.strDbTable)

        with table.batch_writer() as batch:
            for data in self.lstData:
                batch.put_item(self._clean(data))
                # print(data)
    def setData(self, lstData):
        self.lstData = lstData

    def setDbTable(self, strTable):
        self.strDbTable = strTable
