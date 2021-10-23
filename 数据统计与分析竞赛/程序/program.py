import numpy as np
import pandas as pd
from pandas import DataFrame,Series
import matplotlib.pyplot as plt
from collections import Counter

from sklearn import neighbors
from sklearn.neighbors import KNeighborsClassifier
import pylab as pl
from pandas.plotting import scatter_matrix
from sklearn.model_selection import train_test_split
import matplotlib.cm as cm
from matplotlib.colors import ListedColormap, BoundaryNorm
import matplotlib.patches as mpatches

#读取数据
from sklearn.preprocessing import MinMaxScaler

user_data = DataFrame(pd.read_csv('user_info.csv'))
login_data = DataFrame(pd.read_csv('login_day.csv'))
visit_data = DataFrame(pd.read_csv('visit_info.csv'))
result_data = DataFrame(pd.read_csv('result.csv'))

#任务一：获取数据并进行预处理，提高数据质量

# 根据id合并表格
# 四张表格合并，以id为键值，result_final为最终购买的用户信息，result_one为已登录的用户信息,result_two为已登录、已浏览的用户信息
def merge_data_login(user_data, login_data, visit_data):
    result_one = pd.merge(user_data, login_data, on="user_id")
    result_two = pd.merge(result_one, visit_data, on="user_id")
    return result_one

def merge_data_vist(user_data,login_data,visit_data):
    result_one = pd.merge(user_data,login_data,on="user_id")
    result_two = pd.merge(result_one,visit_data,on="user_id")
    return result_two

def merge_data_buy(user_data,login_data,visit_data):
    result_one = pd.merge(user_data,login_data,on="user_id")
    result_two = pd.merge(result_one,visit_data,on="user_id")
    result_final = pd.merge(result_two,result_data,on="user_id")
    return result_final

# 将筛选的数据转换为csv文件
def transform_form(result,string):
    DataFrame(result).to_csv(string,encoding="utf_8_sig")

# 数据清洗：把缺失的数据、数据异常的删除；
def clear_data(data):
    result1=DataFrame(data).dropna()
    result=result1[(result1['city_num']!='error')
    & (result1['login_day']>=0)
    & (result1['login_diff_time']>=0)
    & (result1['distance_day']>=0)
    & (result1['login_time']>=0)
    & (result1['launch_time']>=0)
    & (result1['add_friend']>=0)
    & (result1['add_group']>=0)
    & (result1['camp_num']>=0)
    & (result1['learn_num']>=0)
    & (result1['coupon']>=0)
    &(result1['age_month']<120)]
    return result


# 判断相关系数函数
def Judge_corr(corr,object1,object2):
    result = corr[[object1, object2]].corr().iloc[0, 1]
    if result == 0:
        print("%s和%s是无相关，其相关系数："%(object1,object2),result)
    elif result > 0 and result <= 0.2:
        print("%s和%s是极弱相关，其相关系数："%(object1,object2),result)
    elif result > 0.2 and result <= 0.4:
        print("%s和%s是弱相关，其相关系数："%(object1,object2),result)
    elif result > 0.4 and result <= 0.6:
        print("%s和%s是中等程度相关，其相关系数："%(object1,object2),result)
    elif result > 0.6 and result <= 0.8:
        print("%s和%s是强相关，其相关系数："%(object1,object2),result)
    elif result > 0.8 and result <= 1:
        print("%s和%s是极强相关，其相关系数："%(object1,object2),result)

#已经登录的用户信息
havelogin_result=merge_data_login(user_data, login_data, visit_data)
transform_form(havelogin_result,"已经登录的用户信息.csv")
#已经登录的用户数目
havelogin_person = havelogin_result.shape[0]
print("已经登录的用户数目:",havelogin_person)

#信息完全的、已经登录的用户信息
login_result=clear_data(merge_data_login(user_data, login_data, visit_data))
transform_form(login_result,"信息完全的、已经登录的用户信息.csv")
#信息完全的、已经登录的用户数目
login_person = login_result.shape[0]
print("信息完全的、已经登录的用户数目:",login_person)

# 信息完全的、已经登录的、已经浏览的用户信息
visit_result=clear_data(merge_data_vist(user_data, login_data, visit_data))
transform_form(visit_result,"信息完全的、已经登录的、已经浏览的用户信息.csv")
# 信息完全的、已经登录的、已经浏览的用户数目
visit_person = visit_result.shape[0]
print("信息完全的、已经登录的、已经浏览的用户数目:",visit_person)

#信息完全的、已经登录的、已经浏览的、已经购买的用户信息
buy_result = clear_data(merge_data_buy(user_data,login_data,visit_data))
transform_form(buy_result,'信息完全的、已经登录的、已经浏览的、已经购买的用户信息.csv')
#信息完全的、已经登录的、已经浏览的、已经购买的用户数目
buy_person = buy_result.shape[0]
print("信息完全的、已经登录的、已经浏览的、已经购买的用户数目:",buy_person)


# 任务 2：对用户的各城市分布情况、登录情况进行分析，并分别将结果进行多种形式的可视化展现；
def plotCity(login_result,plotType):
    #设置图像风格，网格型
    plt.style.use('ggplot')

    # 解决中文乱码，坐标轴显示不出现负值的问题
    plt.rcParams['font.sans-serif']=['Microsoft YaHei']
    plt.rcParams['axes.unicode_minus']=False

    # 可视化的标题
    plot_title=['用户登录天数统计','用户登录时长统计','用户学习课节数与用户完成课节数统计','领券数量与学习课节数比较统计','领券数量与课程未购买弹窗访问数比较统计','领券数量与课程访问数比较统计','用户年龄统计']

    # 登录情况:
    # (1)login_day登录天数的最大值与最小值
    login_day_min=login_result['login_day'].min()
    login_day_max=login_result['login_day'].max()
    #login_day以5为差距划分的块数
    login_day_num=(login_day_max//2)+1
    # y轴的数据
    login_day_y_data_list = []
    login_day_x_data_list=[]
    #进行y轴的划分，x轴的划分
    for i in range(0,login_day_num):
        login_day_y_data = login_result[(login_result['login_day']>=(i*2))&(login_result['login_day']<(i+1)*2)].shape[0]
        login_day_y_data_list.append(login_day_y_data)
        login_day_x_data_list.append(str(i*2)+"-"+str((i+1)*2)+"天")

    # (2)login_time登录时长的最大值与最小值
    login_time_min = login_result['login_time'].min()
    login_time_max = login_result['login_time'].max()
    # login_time以24小时（1天）为差距划分的块数
    login_time_num = (login_time_max // 24) + 1
    # y轴的数据
    login_time_y_data_list = []
    login_time_x_data_list = []
    # 进行y轴的划分，x轴的划分
    for i in range(0, login_time_num):
        login_time_y_data = login_result[(login_result['login_time'] >= (i * 24)) & (login_result['login_time'] < (i + 1) * 24)].shape[0]
        login_time_y_data_list.append(login_time_y_data)
        login_time_x_data_list.append(str(int((i * 24)/24)) + "-" + str(int(((i + 1) * 24)/24)) + "天")

    #(3)learn_num学习课节数的最大值与最小值
    learn_num_min = login_result['learn_num'].min()
    learn_num_max = login_result['learn_num'].max()

    # finish_num完成课节数的最大值与最小值
    finish_num_min = login_result['finish_num'].min()
    finish_num_max = login_result['finish_num'].max()

    # learn_num以2节课为差距划分的块数
    learn_num = (learn_num_max // 2) + 1
    finish_num = (finish_num_max//2) + 1
    # y轴的数据
    learn_num_y_data_list = []
    learn_num_x_data_list = []
    finish_num_y_data_list = []
    finish_num_x_data_list = []
    # 进行y轴的划分，x轴的划分
    for i in range(0, learn_num):
        learn_num_y_data = login_result[(login_result['learn_num'] >= (i * 2)) & (login_result['learn_num'] < (i + 1) * 2)].shape[0]
        learn_num_y_data_list.append(learn_num_y_data)
        learn_num_x_data_list.append(str(i * 2) + "-" + str((i + 1) * 2) + "节")
    print("人数：",learn_num_y_data_list)
    print("学习课节数：",learn_num_x_data_list)

    for i in range(0, finish_num):
        finish_num_y_data = login_result[(login_result['finish_num'] >= (i * 2)) & (login_result['finish_num'] < (i + 1) * 2)].shape[0]
        finish_num_y_data_list.append(finish_num_y_data)
        finish_num_x_data_list.append(str(i * 2) + "-" + str((i + 1) * 2) + "节")
    print("人数:",finish_num_y_data_list)
    print("完成课节数：",finish_num_x_data_list)

    # (4)coupon领券数量与learn_num学习课节数的关系比较统计 与click_notunlocked课程未购买弹窗访问数的关系比较统计  与schoolReportPage课程访问数的关系比较统计
    coupon_num = buy_result['coupon']
    learn_num = buy_result['learn_num']

    click_notunlocked_num = buy_result['click_notunlocked']
    schoolReportPage_num = buy_result['schoolreportpage']

    # coupon领卷数量的最大值与最小值
    coupon_min = login_result['coupon'].min()
    coupon_max = login_result['coupon'].max()

    # click_notunlocked课程未购买弹窗访问数的最大值与最小值
    click_notunlocked_min=visit_result['click_notunlocked'].min()
    click_notunlocked_max = visit_result['click_notunlocked'].max()

    # schoolReportPage课程访问数的最大值与最小值
    schoolReportPage_min=visit_result['schoolreportpage'].min()
    schoolReportPage_max = visit_result['schoolreportpage'].max()


    # age_month年龄的最大值与最小值
    age_month_min=login_result['age_month'].min()
    age_month_max =login_result['age_month'].max()
    # age_month以10岁为差距划分的块数
    age_month_num = (age_month_max // 10) + 1
    # y轴的数据
    age_month_y_data_list = []
    age_month_x_data_list = []
    # 进行y轴的划分，x轴的划分
    for i in range(0, age_month_num):
        age_month_y_data = login_result[(login_result['age_month'] >= (i * 10)) & (login_result['age_month'] < (i + 1) * 10)].shape[0]
        age_month_y_data_list.append(age_month_y_data)
        age_month_x_data_list.append(str(i*10)+"-"+str((i+1)*10)+"岁")


    # (2)对用户的各城市分布情况进行分析
    c = Counter()
    t = buy_result['city_num']
    for i in t:
        c[i] = c[i] + 1
    city_num=list(dict(c).values())
    city=list(c)
    print("城市的数量:", list(dict(c).values()))
    print("城市:", list(c))

    #-----------------------------------------------------------------------
    # 1.在没有指明绘制图形类型情况下，采用默认方式
    if plotType == None:
        text = print("""温馨提示:你还没有选择绘制图形的类型.....\n类型如下..
        plot\t线性图
        pie\t饼图
        barth1\t'用户登录时长横向条形图
        barth2\t城市分布横向条形图
        bar\t直方图
        scatter\t散点图
        \n例子\n----------"""
        + "\nplot(data=data, plotType=' plot')")
        return text

    plt.figure(figsize=(10,8))

    if plotType == 'pie1':
        plt.pie(login_day_y_data_list,labels=login_day_x_data_list,autopct='%1.1f%%',shadow=False,startangle=150)
        plt.title(plot_title[0])
        plt.show()
        print("login_day登录天数的最小值:",login_day_min,"天")
        print("login_day登录天数的最大值:",login_day_max,"天")
        print("login_day登录天数的平均值：",np.mean(login_result['login_day']),"天")
        print("login_day登录天数的中位数：", np.median(login_result['login_day']),"天")
        print("login_day登录天数的众数：", np.argmax(np.bincount(login_result['login_day'])),"天")

    if plotType == 'pie2':
        plt.pie(age_month_y_data_list,labels= age_month_x_data_list,autopct='%1.1f%%',shadow=False,startangle=150)
        plt.title(plot_title[6])
        plt.show()
        print("age_month年龄的最小值:",age_month_min,"岁")
        print("age_month年龄的最大值:",age_month_max,"岁")
        print("age_month年龄的平均值：",np.mean(login_result['age_month']),"岁")
        print("age_month年龄的中位数：", np.median(login_result['age_month']),"岁")
        print("age_month年龄的众数：", np.argmax(np.bincount(login_result['age_month'])),"岁")

    if plotType == 'barth1':
        y=[]
        for i in range(0,len(login_time_x_data_list)):
            y.append(i+1)

        width = login_time_y_data_list  # 给出具体每个直方图的数值
        label = login_time_x_data_list  # 直方图信息
        plt.barh(y, width, facecolor='tan', height=0.5, edgecolor='r', alpha=0.6, tick_label=label)  # 绘制水平直方图
        plt.title(plot_title[1])
        plt.xlabel('人数', fontsize=14)
        plt.ylabel('天数', fontsize=14)
        plt.show()  # 显示图像

        print("login_time登录时长的最小值:",login_time_min,"小时")
        print("login_time登录时长的最大值：",login_time_max,"小时")
        print("login_time登录时长的平均值：",np.mean(login_result['login_time']),"小时")
        print("login_time登录时长的中位数：", np.median(login_result['login_time']),"小时")
        print("login_time登录时长的众数：", np.argmax(np.bincount(login_result['login_time'])),"小时")

    if plotType=='bar':
        x = np.arange(1, len(learn_num_y_data_list)+1)
        plt.bar(x, learn_num_y_data_list, width=0.2, label='用户学习课节数')
        plt.bar(x + 0.2, finish_num_y_data_list, width=0.2, label='用户完成课节数')
        plt.xlabel('课程节数', fontsize=14)
        plt.ylabel('人数', fontsize=14)
        plt.title(plot_title[2])
        plt.xticks(x + 0.1,learn_num_x_data_list, fontsize=10)
        plt.grid()
        plt.legend(loc=0)
        plt.show()

        print("learn_num学习课节数的最小值:",learn_num_min,"节")
        print("learn_num学习课节数的最大值：",learn_num_max,"节")
        print("learn_num学习课节数的平均值：",np.mean(login_result['learn_num']),"节")
        print("learn_num学习课节数的中位数：", np.median(login_result['learn_num']),"节")
        print("learn_num学习课节数的众数：", np.argmax(np.bincount(login_result['learn_num'])),"节")

        print("finish_num学习课节数的最小值:",finish_num_min,"节")
        print("finish_num学习课节数的最大值：",finish_num_max,"节")
        print("finish_num学习课节数的平均值：",np.mean(login_result['finish_num']),"节")
        print("finish_num学习课节数的中位数：", np.median(login_result['finish_num']),"节")
        print("finish_num学习课节数的众数：", np.argmax(np.bincount(login_result['finish_num'])),"节")

        Judge_corr(login_result, 'learn_num', 'finish_num')

    if plotType=='scatter':
        plt.subplot(221)
        plt.title(plot_title[3])
        plt.xlabel('领券数量', fontsize=14)
        plt.ylabel('学习课节数', fontsize=14)
        plt.scatter(coupon_num, learn_num, c='r', marker=None, label='学习课节数')
        plt.legend(loc=0)
        plt.subplot(222)
        plt.title(plot_title[4])
        plt.ylabel('课程未购买弹窗访问数', fontsize=14)
        plt.xlabel('领券数量', fontsize=14)
        plt.scatter(coupon_num, click_notunlocked_num, c='g', marker=None, label='课程未购买弹窗访问数')
        plt.legend(loc=0)
        plt.subplot(223)
        plt.title(plot_title[5])
        plt.xlabel('领券数量', fontsize=14)
        plt.ylabel('课程访问数', fontsize=14)
        plt.subplots_adjust(hspace=0.3,wspace=0.3)
        plt.scatter(coupon_num, schoolReportPage_num, c='b', marker=None, label='课程访问数')
        plt.legend(loc=0)
        plt.show()

        print(" click_notunlocked课程未购买弹窗访问数的最小值:",click_notunlocked_min,"次")
        print(" click_notunlocked课程未购买弹窗访问数的最大值：",click_notunlocked_max,"次")
        print(" click_notunlocked课程未购买弹窗访问数的平均值：",np.mean(visit_result['click_notunlocked']),"次")
        print(" click_notunlocked课程未购买弹窗访问数的中位数：", np.median(visit_result['click_notunlocked']),"次")
        print(" click_notunlocked课程未购买弹窗访问数的众数：", np.argmax(np.bincount(visit_result['click_notunlocked'])),"次")

        print(" schoolReportPage课程访问数的最小值:",schoolReportPage_min, "次")
        print(" schoolReportPage课程访问数的最大值：", schoolReportPage_max, "次")
        print(" schoolReportPage课程访问数的平均值：", np.mean(visit_result['schoolreportpage']), "次")
        print(" schoolReportPage课程访问数的中位数：", np.median(visit_result['schoolreportpage']), "次")
        print(" schoolReportPage课程访问数的众数：", np.argmax(np.bincount(visit_result['schoolreportpage'])), "次")

    if plotType == 'barth2':
        y=[]
        for i in range(0,len(city)):
            y.append(i+1)

        width = city_num  # 给出具体每个直方图的数值
        label = city  # 直方图信息
        plt.barh(y, width, facecolor='tan', height=0.2, edgecolor='r', alpha=0.6, tick_label=label)  # 绘制水平直方图
        plt.title(plot_title[1])
        plt.xlabel('人数', fontsize=14)
        plt.ylabel('城市', fontsize=14)
        plt.show()  # 显示图像


# 任务3：构建模型判断用户最终是否会下单购买或下单购买的概率，并将模型结果输出为 csv 文件（参照结果输出样例sample_output.csv）。要求模型的效果达到 85%以上

# KNN算法
visit_and_buy_result  = pd.merge(visit_result,result_data,how='left',on='user_id')
transform_form(visit_and_buy_result,'信息完全的、已经登录的、已经浏览的、有结果的用户信息.csv')
#信息完全的、已经登录的、已经浏览的、有结果的用户数目
visit_and_buy_num = visit_and_buy_result.shape[0]
print("信息完全的、已经登录的、已经浏览的、有结果的用户数目：",visit_and_buy_num )

for i in range(0,visit_and_buy_num):
    if visit_and_buy_result['result'][i]!=1.0:
        visit_and_buy_result['result'][i]=0

#读取数据集
# (1)可视化
buy_result.hist(bins=10, figsize=(10,10))
pl.suptitle("Histogram for each numeric input variable")
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1,wspace=0.3,hspace=0.743)
plt.savefig('buyer_hist')
plt.show()

X = visit_and_buy_result[['age_month','camp_num','learn_num','finish_num', 'ppt','task','video_read','answer_task','baby_info','share']]
y = visit_and_buy_result['result']
cmap = cm.get_cmap('gnuplot')
scatter =  pd.plotting.scatter_matrix(X, c = y,marker = 'o', s=40, hist_kwds={'bins':15}, figsize=(10,10), cmap = cmap)
plt.suptitle('Scatter-matrix for each input variable')
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
plt.savefig('buyer_scatter_matrix')

# (2)创建训练集和数据集，并进行缩放
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# (3)搭建模型
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
print('Accuracy of K-NN classifier on training set: {:.5f}'
    .format(knn.score(X_train, y_train)))
print('Accuracy of K-NN classifier on test set: {:.5f}'
    .format(knn.score(X_test, y_test)))

# (4)绘出K-NN分类器的决策边界
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=0)

# 在GH18458这个补丁中，已经把DataFrame对象和Series对象的as_matrix方法都删除了，所以使用的时候自然就报错了。
# 在GH18458（https://github.com/pandas-dev/pandas/pull/18458）这个补丁中有说明，使用values来代替。

def plot_buyer_knn(X, y, n_neighbors, weights):
    X_mat = X[['learn_num','finish_num']].values
    y_mat = Series(y).values
# Create color maps
    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF','#AFAFAF'])
    cmap_bold  = ListedColormap(['#FF0000', '#00FF00', '#0000FF','#AFAFAF'])
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X_mat, y_mat)
# Plot the decision boundary by assigning a color in the color map
   # to each mesh point.
    mesh_step_size = .01  # step size in the mesh
    plot_symbol_size = 50

    x_min, x_max = X_mat[:, 0].min() - 1, X_mat[:, 0].max() + 1
    y_min, y_max = X_mat[:, 1].min() - 1, X_mat[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, mesh_step_size),np.arange(y_min, y_max, mesh_step_size))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
# Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
# Plot training points
    plt.scatter(X_mat[:, 0], X_mat[:, 1], s=plot_symbol_size, c=y, cmap=cmap_bold, edgecolor = 'black')
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    patch0 = mpatches.Patch(color='#FFAAAA', label='buyer')
    patch1 = mpatches.Patch(color='#00FF00', label='no_buyer')
    plt.legend(handles=[patch0, patch1])
    plt.title("2-Class classification (k = %i, weights = %s)" % (n_neighbors, weights))
    plt.xlabel('learn_num')
    plt.ylabel('finish_num')
    plt.show()
plot_buyer_knn(X_train, y_train, 10, 'uniform')

# 在该数据集情况中，当 K 等于 10 时，我们获得了最高的准确率。
k_range = range(1, 20)
scores = []
for k in k_range:
   knn = KNeighborsClassifier(n_neighbors = k)
   knn.fit(X_train, y_train)
   scores.append(knn.score(X_test, y_test))
plt.figure()
plt.xlabel('k')
plt.ylabel('accuracy')
plt.scatter(k_range, scores)
plt.xticks([0,5,10,15,20])
plt.show()

# 预测
features = ['age_month','learn_num','finish_num','ppt','task','share']
#划分训练集和测试集，90%作为训练集，10%作为测试集
transform_form(buy_result[0:2985].drop(columns=['first_order_time','first_order_price','city_num','platform_num','model_num','app_num','login_day','login_diff_time','distance_day','login_time','launch_time','chinese_subscribe_num','math_subscribe_num','add_friend','add_group','camp_num','study_num','coupon','course_order_num','main_home','main_home2','mainpage','schoolreportpage','main_mime','lightcoursetab','main_learnpark','partnergamebarrierspage','evaulationcenter','coupon_visit','click_buy','progress_bar','video_play','video_read','next_nize','answer_task','chapter_module','course_tab','slide_subscribe','baby_info','click_notunlocked','click_dialog']),'训练集.csv')
transform_form(buy_result[2985:].drop(columns=['first_order_time','first_order_price','city_num','platform_num','model_num','app_num','login_day','login_diff_time','distance_day','login_time','launch_time','chinese_subscribe_num','math_subscribe_num','add_friend','add_group','camp_num','study_num','coupon','course_order_num','main_home','main_home2','mainpage','schoolreportpage','main_mime','lightcoursetab','main_learnpark','partnergamebarrierspage','evaulationcenter','coupon_visit','click_buy','progress_bar','video_play','video_read','next_nize','answer_task','chapter_module','course_tab','slide_subscribe','baby_info','click_notunlocked','click_dialog']),'测试集.csv')

train = DataFrame(pd.read_csv('训练集.csv'))
test = DataFrame(pd.read_csv('测试集.csv'))

knn = KNeighborsClassifier(n_neighbors=10) #默认n_neighbors=5，取前5个最相近的样本。
knn.fit(train[features], train['age_month']) #传入训练集指标下的数据和标签，fit()拟合功能
predict1 = knn.predict(test[features])
knn.fit(train[features], train['learn_num']) #传入训练集指标下的数据和标签，fit()拟合功能
predict2 = knn.predict(test[features])
knn.fit(train[features], train['finish_num']) #传入训练集指标下的数据和标签，fit()拟合功能
predict3 = knn.predict(test[features])
knn.fit(train[features], train['ppt']) #传入训练集指标下的数据和标签，fit()拟合功能
predict4 = knn.predict(test[features])
knn.fit(train[features], train['task']) #传入训练集指标下的数据和标签，fit()拟合功能
predict5 = knn.predict(test[features])
knn.fit(train[features], train['share']) #传入训练集指标下的数据和标签，fit()拟合功能
predict6 = knn.predict(test[features])

df_result=pd.DataFrame({'user_id':test['user_id'],'age_month':predict1,'learn_num':predict2,'finish_num':predict3,'ppt':predict4,'task':predict5,'share':predict6,'result':1})
transform_form(df_result,'预测数据.csv')




































