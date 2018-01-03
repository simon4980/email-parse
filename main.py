import os
from storeEmailData import storeEmailData
from dynamoDbStorage import dynamoDbStorage

os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'

strDownloadEmailPath = '/tmp/email-download/'
strTable = 'email_data'
objDbStorage = dynamoDbStorage(strTable)
objParseEmails = storeEmailData(strDownloadEmailPath)
objParseEmails.process(objDbStorage)


