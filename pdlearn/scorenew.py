import time
from pdlearn import mydriver

firsttime = True

def get_score(driver):
    try:
        '''
        driver = mydriver.Mydriver(nohead=True)
        driver.get_url('https://www.xuexi.cn')
        driver.set_cookies(cookies)
        '''
        driver.get_url('https://pc.xuexi.cn/points/my-points.html')
        driver.web_wait(270, u"我的积分")
        time.sleep(3)
        driver1 = driver.in_driver()
        total = driver1.find_element_by_css_selector('div.my-points-block')
        total = total.text.splitlines()
        #for i in total:
        #    print(i)
        myscores = {'总积分': int(total[total.index('成长总积分')+1]), '今日积分': int(total[total.index('今日累积积分')+1])}
        each = driver1.find_elements_by_css_selector('div.my-points-card-text')
        name = ['登录', '阅读文章', '视听学习', '文章时长', '视听学习时长']
        for i in range(len(name)):
            myscores.update({name[i]: int(each[i].text[0])})
        for i in range(len(name)):
            myscores.update({name[i]+'目标': int(each[i].text[3])})
        return myscores
    except:
        # driver.close()
        print("=" * 120)
        print("get_score获取失败")
        print("=" * 120)
        raise
def get_diandian(driver):
    try:
        '''
        driver = mydriver.Mydriver(nohead=True)
        driver.get_url('https://www.xuexi.cn')
        driver.set_cookies(cookies)
        '''
        driver.get_url('https://pc.xuexi.cn/points/ptp.html')
        driver.web_wait(270, u"我的点点通")
        driver2 = driver.in_driver()
        global firsttime
        if firsttime:
            driver2.find_element_by_css_selector('div.ant-modal-confirm-btns').click()
            firsttime = False
        time.sleep(3)
        total = driver2.find_element_by_css_selector('div.my-points-block')
        total = total.text.splitlines()
        # print(total)
        # for i in total:
        #    print(i)
        mydian = {'点点通': int(total[total.index('我的点点通')+1]), '今日点点通': int(total[total.index('今日累积点点通')+1])}
        each1 = driver2.find_elements_by_css_selector('div.my-points-card-text')
        each2 = driver2.find_elements_by_css_selector('div.my-points-card-subtitle')
        name = ['有效浏览', '有效视听']
        for i in range(len(name)):
            a = int(each1[i].text[0])
            if a < 2:
                mydian.update({name[i]:a *6 + int(each2[i].text[19])})
            else:
                mydian.update({name[i]:(a-1) *6 + int(each2[i].text[19])})
        for i in range(len(name)):
            mydian.update({name[i]+'目标': int(each1[i].text[3]) * 6})
        return mydian
    except:
        print("=" * 120)
        print("get_diandian获取失败")
        print("=" * 120)
        raise

