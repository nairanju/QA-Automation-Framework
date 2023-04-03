import sys
# sys.path.insert(1, r'C:\Users\Administrator\PycharmProjects\QA-Automation-Framework\CustomLibs')
from awsDUlibs import xml_DUconfig
import os
import pathlib
# from configparser import ConfigParser
# config = ConfigParser()
# config.sections()
class awsdu_util:
    """
    This class contains ssh connection automation code functions
    def open_con
    def close_con
    """
    def __init__(self):
        self.Path__ = pathlib.Path.cwd()
        self.Path_=self.Path__.absolute()
        self.xml_path = str(self.Path_) + "\Config\DU_config.xml"
        self.host= xml_DUconfig(self.xml_path,"gnb_DU", "AWS_DU_SETUP3", "mgmt_ip")
        self.username= xml_DUconfig(self.xml_path,"gnb_DU", "AWS_DU_SETUP3", "username")

    def gethost(self):
        print(self.xml_path)
        return self.host

    def getusername(self):
        return self.username


# a=awsdu_util()
# a.gethost()


