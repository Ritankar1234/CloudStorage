import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
        print("File Uploaded")
def main():
    access_token = 'MtX788qTicYAAAAAAAAAAeufxWUkR0BaaRTUSz4QbJnK9NKlp6bviQNxR3p6tnZS'
    transferData = TransferData(access_token)
    print("Object Created")
    file_from = 'Test.txt'
    file_to = '/test_dropbox/test.txt' 
    transferData.upload_file(file_from, file_to)
    print("File has been moved")

main()