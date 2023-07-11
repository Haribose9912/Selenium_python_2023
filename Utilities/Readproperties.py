import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class readconfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common login credentials', 'baseURL')
        return url

    @staticmethod
    def getmobilenumber():
        mobile_number = config.get('common login credentials', 'mobilenumber')
        return mobile_number

    @staticmethod
    def getpassword():
        Password = config.get('common login credentials', 'password')
        return Password

    @staticmethod
    def getlogindemo_url():
        url2 = config.get('common login credentials', 'Login_demo_Url')
        return url2
