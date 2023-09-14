import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, folder_from, folder_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(folder_from, 'rb') 
        dbx.files_upload(f.read(), folder_to)

def main():
    access_token = 'sl.BlvAzoNNxhXmwVQ9eZDPJq2jC8f51_f30yi7v_JFS17ebJ6gu4mJgduhPG49gDCUm6dof-bzoEYi7y2C3ZOoTVCs1cotmvZk8Im-w8EAytHtLjlVgi_uMAejNwIJ-YMnn9r8TclvSqCF'
    transferData = TransferData(access_token)

    folder_from = input("enter the file path to transfer")
    folder_to = input("enter the full path to upload to dropbox")

    transferData.upload_folder(folder_from, folder_to)
    
    print("folder has been moved")

if __name__ == '__main__':
    main()

