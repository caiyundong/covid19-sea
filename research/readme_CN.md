# 疫情相关资源总结

## 数据网页 (Dashboard)
* 约翰霍普金斯 https://coronavirus.jhu.edu/map.html (基于arcgis开发）
* https://ncov2019.live/data （17岁高中生独立开发全球最火疫情追踪网站）
* [新加坡疫情](https://experience.arcgis.com/experience/7e30edc490a5441a874f9efe67bd8b89)

## 传染病方舱模型/[传染病模型](https://baike.baidu.com/item/%E4%BC%A0%E6%9F%93%E7%97%85%E6%A8%A1%E5%9E%8B)
* 人群分类
    1. S 类，易感者 (Susceptible)，指未得病者，但缺乏免疫能力，与感染者接触后容易受到感染；
    2. E 类，暴露者 (Exposed)，指接触过感染者，但暂无能力传染给其他人的人，对潜伏期长的传染病适用；
    3. I 类，感病者 (Infectious)，指染上传染病的人，可以传播给 S 类成员，将其变为 E 类或 I 类成员；
    4. R 类，康复者 (Recovered)，指被隔离或因病愈而具有免疫力的人。如免疫期有限，R 类成员可以重新变为 S 类。
* SEIR模型
    * ![方程](https://bkimg.cdn.bcebos.com/pic/5366d0160924ab18fbdab0573afae6cd7a890b85)

## 仿真程序
* [VirusBroadcast](https://github.com/KikiLetGo/VirusBroadcast)  - 一个基于java的模拟仿真程序
* [Virtual School](https://github.com/YunxiuXu/Virus-School)
    * Unity模拟病毒在校园中传播 Unity版本 2017.4.36c1 Win10
* 基于元胞自动机模型的在线仿真 [Going Critical by Kevin Simler](https://www.meltingasphalt.com/interactive/going-critical/)
* [斯坦福发布“防疫公司”模拟器：“照明开关法”或为美国社交隔离最优解](https://new.qq.com/omn/20200331/20200331A0CSUW00.html)
    * [Potential Long-Term Intervention Strategies for COVID-19](https://covid-measures.github.io/)
    * [在线仿真](https://morganpkain.shinyapps.io/covid/)
    * ![alt 模型](https://covid-measures.github.io/model_schematic.png)
    * 基于SIER，加入了两个干预 （“照明开关方法” 和 "社交距离"）
* [用Python实现经典传染病模型]{https://zhuanlan.zhihu.com/p/104091330}, [用Python实现经典传染病模型（R0值实时更新）]{https://bbs.pinggu.org/thread-7759400-1-1.html}

## 数据集
* [约翰霍普金斯 CSSE](https://github.com/CSSEGISandData/COVID-19) 15.5k Star
* [2019新型冠状病毒疫情实时爬虫 - 丁香园数据](https://github.com/BlankerL/DXY-COVID-19-Crawler) 1.4k Star
* [新冠病毒项目合集](https://github.com/soroushchehresa/awesome-coronavirus) - API, 数据集, 模型, 算法等

## 国内外趋势指数
* Google Trends 
   * https://trends.google.com/trends/?geo=US
   * API: pytrends (https://github.com/GeneralMills/pytrends)
* 百度指数
    * http://index.baidu.com/v2/index.html#/
    * 百度舆情API （https://cloud.baidu.com/doc/TRENDS/index.html）
* 头条指数
    * https://index.toutiao.com/
* 清博指数
    * http://yuqing.gsdata.cn
    * API （http://databus.gsdata.cn/open/index）
* 其他
    * [360趋势](https://trends.so.com)， [搜狗指数](http://index.sogou.com)， [阿里指数](https://index.1688.com)
    
## 新闻
* [打击“信息病毒”科技巨头努力消除“内容鸿沟”](https://www.yicai.com/news/100507246.html)
    * 每一次疫情的暴发，随之而来的是信息的大爆炸，尤其是当我们进入了一个如此发达的信息社会。我们都知道病毒的传播有一个叫R0的基本传染数，R0高于1时，意味着病毒仍在不断传播。而研究发现，信息在网络上的传播也可以参照这个R0指数，信息在网上传播的R0值约等于2，和目前新型冠状病毒的R0值相似。
* [调研报告：中国人工智能产业发展联盟《人工智能助力新冠疫情防控调研报告》正式发布](http://www.cww.net.cn/article?id=467759)
