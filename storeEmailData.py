import glob, os, email, dateparser, re


class storeEmailData:

    def __init__(self, strDownloadEmailPath = None):
        self.setDownloadEmailPath(strDownloadEmailPath)

    def _cleanMessageId(self, strMessageId):
        if strMessageId.startswith('<'):
            strMessageId = strMessageId[1:]

        if strMessageId.endswith('>'):
            strMessageId = strMessageId[:-1]

        return strMessageId




    def _convertDate(self, strDate):
        objRegexTz = re.search('\([A-Z]{3}\)', strDate)
        # Remove timezone name if time difference is provided as well.
        if re.search('\+|-\d{4}', strDate) != None and  objRegexTz != None:
            strDate = strDate.replace(objRegexTz[0], '')

        # Strip any starting or trailing spaces
        strDate = strDate.strip()

        # Clean -0000 to +0000 for date parse
        strDate = strDate.replace('-0000', '+0000')

        # Convert everything into the same timezone
        objDate = dateparser.parse(strDate, settings={'TIMEZONE': 'UTC'})
        return objDate.isoformat()


    def process(self, objStorage = None):
        if not os.path.isdir(self.strDownloadEmailPath):
            raise Exception('Download path does not exist')

        lstEmailData = []
        for strFilename in glob.glob(os.path.join(self.strDownloadEmailPath, '*.msg')):
            strFullFilePath = os.path.join(self.strDownloadEmailPath, strFilename)
            objFile = open(strFullFilePath, 'r')
            objEmail = email.message_from_file(objFile)
            strFromName, strFromEmail = self._splitName(objEmail['From'])
            strToName, strToEmail = self._splitName(objEmail['To'])
            lstEmailData.append({
                'messageId': self._cleanMessageId(objEmail['Message-ID']),
                'to': strToName,
                'toEmail': strToEmail,
                'from': strFromName,
                'fromEmail': strFromEmail,
                'date': self._convertDate(objEmail['Date']),
                'subject': objEmail['Subject']
            })

        if objStorage != None:
            objStorage.setData(lstEmailData)
            objStorage.save()

        # Remove files after processing
        self._removeFiles()

        return lstEmailData

    def _removeFiles(self):
        for strFilename in glob.glob(os.path.join(self.strDownloadEmailPath, '*.msg')):
            strFullFilePath = os.path.join(self.strDownloadEmailPath, strFilename)
            os.remove(strFullFilePath)

    def setDownloadEmailPath(self, strDownloadEmailPath):
        self.strDownloadEmailPath = strDownloadEmailPath

    def _splitName(self, strName):
        lstNameData = strName.split('<')
        strEmail = lstNameData.pop()
        if strEmail.endswith('>'):
            strEmail = strEmail[:-1]


        return ('<'.join(lstNameData), strEmail)
