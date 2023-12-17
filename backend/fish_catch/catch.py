from flask import Flask, Blueprint, render_template
import requests
import matplotlib.pyplot as plt
import matplotlib
import io
import base64

fish_catch = Blueprint('catch', __name__,
                template_folder= 'templates')
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
def get_data():
    url = "https://data.moa.gov.tw/Service/OpenData/FaRss.aspx?key=073&$top=1000&$skip=0&UnitId=C71"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Can't get data!")

@fish_catch.route('/', methods=['GET', 'POST'])
def fish():
    # 获取数据
    fish_data = get_data()

    # 提取每个縣市的数据
    cities_data = {}
    for item in fish_data:
        city = item['field002']
        if city not in cities_data:
            cities_data[city] = {'years': [], 'harvests': []}
        cities_data[city]['years'].append(int(item['field003']))
        cities_data[city]['harvests'].append(float(item['field004']))

    # 使用 Matplotlib 绘制多个线条
    matplotlib.use('Agg')  # 使用非交互模式
    plt.ioff()  # 关闭 Matplotlib 的交互模式

    plt.figure(figsize=(10, 6))

    selected_cities = ['1904 高雄市']  # 选择显示的縣市

    for city, data in cities_data.items():
        if city in selected_cities:
            plt.plot(data['years'], data['harvests'], label=f'{city} ')

    plt.xlabel('年度')
    plt.ylabel('採收量(噸)')
    plt.title('各縣市單船拖網採收量年度變化')
    plt.legend()
    plt.grid(True)

    # 将绘制的图形转换为Base64格式
    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)
    img_base64 = base64.b64encode(img_buf.read()).decode('utf-8')
    plt.ioff()
    # 渲染模板并将数据传递给模板
    return render_template('catch.html', img_base64=img_base64)
