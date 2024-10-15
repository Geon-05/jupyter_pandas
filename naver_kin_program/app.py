import tkinter as tk
from tkcalendar import DateEntry
from babel.numbers import *

def naver_kin(search,start_date,end_date,page_num=1):
    import time
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    import pandas as pd

    options=Options()
    options.add_experimental_option('detach',True)
    options.add_argument('--start-maximized')
    service=Service(ChromeDriverManager().install())

    driver=webdriver.Chrome(service=service, options=options)
    
    # search_date_length = (dt.datetime.strptime(end_date,"%Y.%m.%d")-dt.datetime.strptime(start_date,"%Y.%m.%d")).days
    # search = '부동산'
    # start_date = '2024.02.01'
    # end_date = '2024.02.08'
    res = [{'질문':""}]
    for page in range(1, page_num+1):
        url = f'https://kin.naver.com/search/list.naver?query={search}&section=qna&period={start_date}.|{end_date}.&sort=none&page={page}'

        driver.get(url)
        time.sleep(1)
        
        for list_num in range(1,11):
            try:
                tmp={}
                driver.find_element(By.XPATH,f'//*[@id="s_content"]/div[3]/ul/li[{list_num}]/dl/dt/a').click()
                time.sleep(1)
                driver.switch_to.window(driver.window_handles[-1])
                tmp['질문'] = driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[1]/div[1]').text.replace('질문\n','')
                tmp['상세질문'] = driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[1]/div[3]').text.replace('\n','')
                tmp['답변개수'] = driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[7]/div[1]/div/div/div[1]/span').text
                tmp['답변'] = [i.text for i in driver.find_elements(By.CLASS_NAME,'se-component-content')]
                driver.close()
                driver.switch_to.window(driver.window_handles[-1])
                if tmp['질문'] == res[-1]['질문']:
                    break
                res.append(tmp)
            except:
                print(f"{page}페이지 {list_num}번째 자료 오류로인하여 수집되지 않았습니다.")
    driver.quit()
    res = res[1:]
    df = pd.DataFrame(res)
    print(f'데이터 {df.shape} 처리되었습니다.')
    df.to_csv(f'네이버지식인_{search}_{start_date}_{end_date}_{page_num}.csv')
    return df

# 구동부
def search_btn():
    search = ent1.get()
    page = int(ent2.get())
    start_date = s_cal.get_date().strftime("%Y.%m.%d")
    end_date = e_cal.get_date().strftime("%Y.%m.%d")
    
    naver_kin(search,start_date,end_date,page)

win = tk.Tk()

win.geometry('600x900')
win.title('네이버 지식인 검색')
win.option_add('*Font','맑은고딕 20')

f1 = tk.Frame(win,width=1500,height=100,relief=tk.SUNKEN,bd=4,bg='light steel blue')
f1.pack(side=tk.TOP)
f2 = tk.Frame(win,width=1500,height=550,relief=tk.SUNKEN,bd=4,bg='white')
f2.pack()
f3 = tk.Frame(win,width=1600,height=100,relief=tk.SUNKEN,bd=4,bg='white')
f3.pack(side=tk.BOTTOM)

# 네이버 지식인 로고
img = tk.PhotoImage(file='./img/네이버 지식인 로고.png', master=f1).subsample(1)
lab_d = tk.Label(f1, image=img)
lab_d.grid()

# 검색창
lab1 = tk.Label(f2, text='검색어')
lab1.grid(row=0,column=0)

ent1 = tk.Entry(f2)
ent1.grid(row=0,column=1)

# 시작날짜
lab2 = tk.Label(f2, text='시작날짜')
lab2.grid(row=1,column=0)

s_cal = DateEntry(f2, locale='ko', date_pattern='Y.mm.dd')
s_cal.grid(row=2,column=0)

# 끝날짜
lab2 = tk.Label(f2, text='끝날짜')
lab2.grid(row=1,column=1)

e_cal = DateEntry(f2, locale='ko', date_pattern='Y.mm.dd')
e_cal.grid(row=2,column=1)

# 페이지수
lab2 = tk.Label(f2, text='페이지 수(1~100)')
lab2.grid(row=3,column=0)

ent2 = tk.Entry(f2)
ent2.grid(row=3,column=1)

btn = tk.Button(f2, text='검색', command=search_btn)
btn.grid(row=4,column=0,columnspan=2)

win.mainloop()