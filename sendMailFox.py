#!python
#_*_coding:UTF-8 _*_
"""
使用selenium框架，模拟浏览器发送邮件
"""
from selenium import webdriver
import time

class AutoSendMail():

    __sendInfo = {}

    def __init__(self,filepath='.\\maInfo.ma', toAddress='xxxx@sina.com'):
        self.__getInfo(filepath)
        self.__targetAddress = toAddress

    def __getInfo(self,filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                self.__sendInfo['username'] = f.readline().split(":")[1].strip()
                self.__sendInfo['password'] = f.readline().split(":")[1].strip()
        except IOError:
            print("mail file open error")
        else:
            f.close()

    def __setDriverProfile(self):
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("brower.download.folderList", 2)
        firefox_profile.set_preference("permissions.default.stylesheet", 2)
        firefox_profile.set_preference("permissions.default.image",2)
        firefox_profile.set_preference("javascript.enable", False)

        return firefox_profile

    def sendMail(self, msg):
        '''
        找到相应的输入节点，并且输出相应的信息 html文件为163邮箱
        :param msg:
        :return:
        '''
        #brower = webdriver.Firefox(firefox_profile=self.__setDriverProfile())
        brower = webdriver.Firefox()
        brower.get('http://mail.163.com')
        brower.find_element_by_id('idInput').send_keys(self.__sendInfo['username'])
        brower.find_element_by_id('pwdInput').send_keys(self.__sendInfo['password'])
        brower.find_element_by_id('loginBtn').click()
        brower.implicitly_wait(10)
        brower.find_element_by_id('_mail_component_59_59').click()
        address = brower.find_element_by_class_name('nui-editableAddr-ipt')
        address.send_keys(self.__targetAddress)

        # subject_father = brower.find_element_by_class_name('bz0')
        # subject = subject_father.find_element_by_class_name('nui-ipt-input')
        # subject.send_keys('error warn')
        content = brower.find_element_by_class_name('APP-editor-iframe')
        content.click()
        content.send_keys(msg)
        send_father = brower.find_element_by_class_name("nui-toolbar-item")
        send = send_father.find_element_by_class_name("nui-btn-text")
        send.click()
        brower.implicitly_wait(1)
        brower.find_element_by_class_name('nui-msgbox-ft-btns').find_element_by_class_name('nui-btn-text').click()
        brower.implicitly_wait(100000)
        time.sleep(1)
        brower.close()


if __name__ == "__main__":
    AutoSendMail().sendMail("this is a test again")
