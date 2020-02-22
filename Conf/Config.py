from configparser import ConfigParser
import os

class Config:

    def __init__(self):
        self.config = ConfigParser()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        
        self.token = self.get_conf('login', 'token')
        self.header = self.get_conf('web', 'header')

    def get_conf(self, title, value):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """
        配置文件修改
        :param title:
        :param value:
        :param text:
        :return:
        """
        self.config.set(title, value, text)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def add_conf(self, title):
        """
        配置文件添加
        :param title:
        :return:
        """
        self.config.add_section(title)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)
