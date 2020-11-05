from selenium import webdriver
import platform
import time
import re


def web_driver_paths():
    """Constructing the selenium web driver path"""
    global web_driver_path
    global appln_path
    global plat_form
    script_file_path = __file__
    plat_form = platform.system()
    if(plat_form.lower() == 'linux'):
        appln_path = '/'.join(script_file_path.split('/')[0:-1])
        if script_file_path.find('/') == -1:
            appln_path = '.'
        web_driver_path = appln_path + '/driver/chromedriver_linux'
        print(web_driver_path)
    elif(plat_form.lower() == 'windows'):
        appln_path = '\\'.join(script_file_path.split('\\')[0:-1])
        if script_file_path.find('\\') == -1:
            appln_path = '.'
        web_driver_path = appln_path + '\\driver\\chromedriver_win32.exe'
        print(web_driver_path)


def web_driver_conn():
    global driver
    driver = webdriver.Chrome(executable_path=web_driver_path)
    driver.implicitly_wait(5)
    driver.maximize_window()
    time.sleep(2)


def web_driver_close():
    driver.close()


def custom_page_url(url):
    driver.get('https://python.org')
    # print('Web driver source page', driver.page_source)
    with open(appln_path + '/page_source.html', "w") as f:
            f.write(driver.page_source)
    time.sleep(2)


def page_url_parsing(version):
    fd_r = open(appln_path + '/page_source.html', 'r')
    page_content = fd_r.read()
    print("Page contents ->",page_content)
    matched = re.findall(version, str(page_content))
    print("Matched output --> ", matched)


def main():
    web_driver_paths()
    web_driver_conn()
    # custom_page_url('https://python.org')
    page_url_parsing('version')
    
    web_driver_close()


if __name__ == '__main__':
    main()
