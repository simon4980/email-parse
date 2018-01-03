from storeEmailData import storeEmailData
from dynamoDbStorage import dynamoDbStorage


strDownloadEmailPath = '/tmp/email-download/'
strTable = 'email_data'
objDbStorage = dynamoDbStorage(strTable)
objParseEmails = storeEmailData(strDownloadEmailPath)
objParseEmails.process(objDbStorage)


