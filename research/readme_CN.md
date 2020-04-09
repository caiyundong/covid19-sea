# 疫情相关资源总结

## 数据展示 (Dashboard)
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
* [斯坦福发布“防疫公司”模拟器：“照明开关法”或为美国社交隔离最优解](https://new.qq.com/omn/20200331/20200331A0CSUW00.html)
    * [Potential Long-Term Intervention Strategies for COVID-19](https://covid-measures.github.io/)
    * [在线仿真](https://morganpkain.shinyapps.io/covid/)
    * ![alt 模型](https://covid-measures.github.io/model_schematic.png)
    * 基于SIER，加入了两个干预 （“照明开关方法” 和 "社交距离"）
    * 代码基于R，没有其他实现
* [用Python实现经典传染病模型](https://zhuanlan.zhihu.com/p/104091330), [用Python实现经典传染病模型（R0值实时更新）](https://bbs.pinggu.org/thread-7759400-1-1.html), [基于SIR模型的武汉新型冠状病毒动力学建模与参数辨识（附Python代码）](https://zhuanlan.zhihu.com/p/104645873)
* 研究
   * 面向新冠疫情的数据可视化分析与模拟预测， 陈宝权 北京大学前沿计算研究中心， https://arxiv.org/pdf/2002.07096.pdf  基于C-SEIR模型
   * 基于改进的SEIR+CAQ传染病动力学模型进行新型冠状病毒肺炎疫情趋势分析, 魏永越, http://html.rhhz.net/zhlxbx/012.htm SEIR+CAQ (SEIR with Infected Components，Asymptomatic infected，and Quarantined)
   * Nature Physics，美国传染病预测新模型：社会现象影响传播规模, https://www.nature.com/articles/s41567-020-0791-2
      *Hébert-Dufresne表示，这项研究显示，疾病流行的预测模型应超越单个传染病的研究。针对近期COVID-19疫情预测，因为正好与流感季重叠，因此了解流感的流行情形，以及哪些病例有多重感染就非常重要。

## 仿真程序
* [VirusBroadcast](https://github.com/KikiLetGo/VirusBroadcast)  - 一个基于java的模拟仿真程序
* [Virtual School](https://github.com/YunxiuXu/Virus-School)
    * Unity模拟病毒在校园中传播 Unity版本 2017.4.36c1 Win10
* 基于元胞自动机模型的在线仿真 [Going Critical by Kevin Simler](https://www.meltingasphalt.com/interactive/going-critical/)
   * [cellpylib](https://github.com/lantunes/cellpylib) - 元胞自动机的python库

## 数据集
* [约翰霍普金斯 CSSE](https://github.com/CSSEGISandData/COVID-19) 15.5k Star
* [2019新型冠状病毒疫情实时爬虫 - 丁香园数据](https://github.com/BlankerL/DXY-COVID-19-Crawler) 1.4k Star
* [新冠病毒项目合集](https://github.com/soroushchehresa/awesome-coronavirus) - API, 数据集, 模型, 算法等
* [Covid-19 相关CT图片数据集以及AI papers](https://github.com/HzFu/COVID19_imaging_AI_paper_list) - 数据集，文章

## 其他
* [从新冠肺炎可视化说起，数据展示如何简约但不简单](https://cloud.tencent.com/developer/article/1591632) - 梅鸿辉, 阿里云

## 研究报道
* [2019-nCoV-全球简报](https://github.com/Academic-nCoV/2019-nCoV/wiki)
* [全球疫情形势数据分析：拐点预测和长尾特征](https://mp.weixin.qq.com/s/nDgAp3tkH9eyJLvmlfC4HA) - 恒大研究院 任泽平 李建国
   * 1) 新冠肺炎传染性强， R0值在3.1左右，高于SARS和西班牙流感。30%-60%的新冠病毒感染者无症状或者症状轻微，但具有传染性，是其防控难度大的突出原因。2)新增确诊拐点和现有确诊拐点的出现是疫情缓解的前提，两大拐点是观察疫情的关键。只有第二个拐点达到之后，整体疫情才有可能缓解。3) 意大利、西班牙、德国在3月下旬达到新增确诊的高点，即第一拐点，目前正在靠近第二拐点，有望于4月底逐步缓解，但存在“长尾特征”。
    
## 新闻
* [打击“信息病毒”科技巨头努力消除“内容鸿沟”](https://www.yicai.com/news/100507246.html)
    * 每一次疫情的暴发，随之而来的是信息的大爆炸，尤其是当我们进入了一个如此发达的信息社会。我们都知道病毒的传播有一个叫R0的基本传染数，R0高于1时，意味着病毒仍在不断传播。而研究发现，信息在网络上的传播也可以参照这个R0指数，信息在网上传播的R0值约等于2，和目前新型冠状病毒的R0值相似。
* [调研报告：中国人工智能产业发展联盟《人工智能助力新冠疫情防控调研报告》正式发布](http://www.cww.net.cn/article?id=467759)


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
