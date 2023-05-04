from PIL import Image, ImageDraw, ImageFont
import os ,sys , time
import random

def draw(moban_path,conment,font0=r'C:\Users\75600\AppData\Local\Microsoft\Windows\Fonts\SourceHanSansSC-Bold.otf',str_volume_1=200,str_volume_2=100):
    '''在某个位置上绘画某些内容
    设置打印文字的颜色，大小，字体属性
    打开图片
    提出所有的人名和公司名并且绘画上去
    保存图片'''
    fillColor = "#000000"  # 黑色
    try:
        setFont = ImageFont.truetype(font0, str_volume_1)  # 主行
        setFont2 = ImageFont.truetype(font0,str_volume_2) #次行
        setFont3 = ImageFont.truetype(font0,50)
    except:
        print("可能你的字体路径出错了，请自行看源码解决")
        input("按回车键关闭程序")
        sys.exit(0)
    for i in conment: #依次输入打印的内容，并格式，整理，打印，保存。
        image = Image.open(moban_path)
        try:
            name,name2 = i.split(",")[0],i.split(",")[1] #分割主行和副行
            name_str = int(ChineseCharCount(name))
            name_str2 = int(ChineseCharCount(name2))
            if name_str<5:
                draw_name, draw_name2 = name.replace('', ' '), name2 #为主行加空格
            else:
                draw_name, draw_name2 = name, name2
        except:
            print(f'【{i}】格式不对，跳过')
            continue

        '''判断主行的字数并且改变字体大小'''
        if name_str<6:
            pass
        elif name_str<7:
            setFont = ImageFont.truetype(font0, int(str_volume_1*0.85))
        elif name_str<8:
            setFont = ImageFont.truetype(font0, int(str_volume_1 * 0.8))
        elif name_str<9:
            setFont = ImageFont.truetype(font0, int(str_volume_1 * 0.75))
        elif name_str<10:
            setFont = ImageFont.truetype(font0, int(str_volume_1 * 0.65))
        else:
            print(f'【{i}】字数太多，很可能出问题，需要单独处理')

        '''判断第二行的字数并且改变字体大小'''
        if name_str2<8:
            pass
        elif name_str2<10:
            setFont2 = ImageFont.truetype(font0, int(str_volume_2*0.85))
        elif name_str2<12:
            setFont2 = ImageFont.truetype(font0, int(str_volume_2 * 0.8))
        elif name_str2<14:
            setFont2 = ImageFont.truetype(font0, int(str_volume_2 * 0.75))
        elif name_str2<16:
            setFont2 = ImageFont.truetype(font0, int(str_volume_2 * 0.7))
        else:
            print(f'【{i}】字数太多，很可能出问题，需要单独处理')

        draw_txt = ImageDraw.Draw(image) #准备在图片上打印文字
        zitisize1 = draw_txt.textsize(draw_name,font=setFont) #获得打印字体的尺寸
        zitisize2 = draw_txt.textsize(draw_name2,font=setFont2) #获得打印字体的尺寸
        location1x = image.size[0] * 0.65 - (zitisize1[0] / 2) #计算打印字横坐标的位置
        location1y = image.size[1] * 0.6 #计算打印字纵坐标的位置
        location2x = image.size[0] * 0.65 - (zitisize2[0] / 2) #计算打印字横坐标的位置
        location2y = image.size[1] * 0.7 #计算打印字纵坐标的位置
        draw_txt.text((location1x,location1y), draw_name , font=setFont, fill=fillColor, direction=None)
        draw_txt.text((location2x,location2y), draw_name2 , font=setFont2, fill=fillColor, direction=None)
        image = image.transpose(Image.ROTATE_180)
        draw_txt = ImageDraw.Draw(image)
        draw_txt.text((location1x,location1y), draw_name , font=setFont, fill=fillColor, direction=None)
        draw_txt.text((location2x,location2y), draw_name2 , font=setFont2, fill=fillColor, direction=None)
        draw_txt.text((100,200), f'{time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())}_{name2}_{name}', font=setFont3, fill=fillColor, direction=None)
        freeNumber=FreeNumber() #给可能出现同名称的水牌备注不同序号，防止出现覆盖文件
        image.save(os.path.join(os.getcwd(),'输出文件夹',f'{name2}_{name}_{freeNumber}.jpg'))
        print(f'输出【{name2}_{name}_{freeNumber}.jpg】完成')
    print("全部打印完毕")
    input("回车键结束")

def FreeNumber():
    freeN=str(random.randint(123456,9999999))
    return freeN

def ChineseCharCount(str_str):
    count = 0
    if str == type(str_str):
        for str_tmp in str_str:
            if ord(str_tmp) - ord('0') >= 128:
                count += 1
    return count



def conment(txt_path=''):
    '''提取打印内容,
    判断文档能否正常打开'''
    conment_list=[] #输出的列表
    try:
        f = open(txt_path, encoding='utf-8')
    except:
        print("可能出现了TXT文件编码错误，请尝试删除TXT文件重新写入，如果还是不行，我也没办法了")
        sys.exit(0)
    for i in f.readlines():
        b=i.replace(" ", "").replace("\t","").strip() #格式化每行的输入
        conment_list.append(b) #把需要的东西写进输入的列表
    return conment_list


def new_init():
    '''分别判断需要的文件和文件夹是否存在'''
    if os.path.exists(moban_path) == False:
        print('【台卡模板.jpg】不存在！！！请再读10遍说明')
        print(moban_path)
        input("按回车键关闭程序")
        sys.exit(0)
    if os.path.exists(txt_path) == False:
        open(txt_path, 'w', encoding='utf-8').write('人名,公司名称, \n')
        print("【人员名单(可带公司名称).txt】不存在，已创建，请填写内容后再运行本程序")
        input("按回车键关闭程序")
        sys.exit(0)
    if os.path.exists('输出文件夹') == False:
        os.mkdir("输出文件夹")
        print("【输出文件夹】不存在"
              "创建【输出文件夹】完毕")

txt_path = os.path.join(os.getcwd() ,'人员名单(可带公司名称).txt')
moban_path=os.path.join(os.getcwd() ,'台卡模板.jpg')
print(txt_path,moban_path)

print("说明：\n"
      "本文件会使用当前路径下的【人员名单(可带公司名称).txt】读取文件\n"
      "和在【输出文件夹】内生成需要的文件\n"
      "如果不存在，会自动生成\n"
      "名单填写方式是一行一个【人名,公司名(可不填),】看准，是有英文标点的逗号的\n"
      "必须：还要一个【台卡模板.jpg】文件和本程序放在一起\n"
      "如果看不懂，请再读一遍\n")
input("看完了就按回车键开始")


new_init()
draw(moban_path,conment(txt_path))

