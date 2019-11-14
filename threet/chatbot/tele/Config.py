import os,yaml

class Config:
    def __init__(self, file_name):
        self.file_name = file_name
        if  not(os.path.exists(file_name)):
            raise Exception('Config file {} does not exist'.format(self.file_name))
        with open(self.file_name, 'r') as config:
            self.cfg = yaml.full_load(config)

    # Get host from config
    def get_host_name(self):
        try:
            return self.cfg['host']['hostname']
        except Exception:
            raise Exception ('Hostname does not exists. Review config file {}'.format(self.file_name))

    # Get port from config
    def get_port(self):
        try:
            return self.cfg['host']['port']
        except Exception:
            raise Exception('Hostname does not exists. Review config file {}'.format(self.file_name))

    # Get telegram credential
    def get_credential(self):
        try:
            token = self.cfg['telegram_credentials']['token']
            if token:
                return token
            else:
                raise Exception('Token is invalid. Review config file {}'.format(self.file_name))
        except Exception:
            raise Exception('Token does not exists. Review config file {}'.format(self.file_name))