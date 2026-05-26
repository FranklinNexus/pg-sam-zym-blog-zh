---
type: material
area: startup
author: Paul Graham
source: paulgraham.com
tags:
  - Paul Graham
  - essay
---

# 快照：1998 年 6 月的 Viaweb

> 原文：<https://paulgraham.com/vw.html>
> 来源：[paulgraham.com](https://paulgraham.com/)
> 英文标题：Snapshot: Viaweb, June 1998
> 年代：2012 年 1 月

1998 年 6 月雅虎收购宣布前几个小时，我截了 [Viaweb 站点](http://ycombinator.com/viaweb) 的一张快照。我想有一天翻出来会挺有意思。那是拨号上网的年代，用户愿意耐心读完一整页推销文案；贸易媒体迷信「版本号」，搜索引擎还没被 Google 改写。下面按主题拆解那张截图里还能读出什么。

### 页面很小

第一眼会注意到：**页面极小**。1998 年的屏幕小得多。若我没记错，首页刚好能塞进当时大家常用的窗口尺寸。

那时的浏览器（IE 6 还要三年才问世）字体很少，也没有抗锯齿。若想让页面好看，得把展示文字渲成图片。

### 红圈与 John McArtyem

你可能注意到 Viaweb 和 [Y Combinator](http://ycombinator.com/) 的 logo 有点像。我们创办 YC 时故意搞的内部笑话。红圈这么基础，我惊讶于 Viaweb 时代竟没几家公司拿它当 logo——后来才明白 [为什么](https://paulgraham.com/zero.html)。

在 [公司简介页](http://www.ycombinator.com/viaweb/com.html) 上有个神秘人物 **John McArtyem**。Robert Morris（Rtm）在 [蠕虫](http://en.wikipedia.org/wiki/Morris_worm) 事件后对曝光极其抗拒，不想名字出现在站上。我争取到折中：可以用他的简介，但不能署名。他后来在这点上 [放松](http://ycombinator.com/people.html) 了一些。

### Trevor 与「托里诺·巴格韦尔」

Trevor 差不多在收购交割时毕业，**四天内**从穷研究生变成百万富翁博士。我写新闻稿生涯的巅峰，是一篇 [庆祝他毕业](http://ycombinator.com/viaweb/trevor.html) 的稿，配图是开会时我给他画的素描。

（Trevor 还以 [Trevino Bagwell](http://ycombinator.com/viaweb/tlbwebdesign.html) 出现在我们「商家可雇用的网页设计师」名录里。我们把他插进去当**内定的好手**，以防竞争对手往名录里灌垃圾；我们以为他的 logo 能吓跑真客户，**并没有**。）

### 公关、SEO 与 Google

九十年代要获客，得靠杂志和报纸提及——当时没有今天这些线上被发现的路径。所以我们每月付 [公关公司](https://paulgraham.com/submarine.html) 一万六千美元上版面。幸好记者 [挺喜欢我们](http://ycombinator.com/viaweb/presquot.html)。

在 [搜索引擎引流建议](http://ycombinator.com/viaweb/se.html) 里（那时大概还没 SEO 这个词），我们说真正重要的只有七个：Yahoo、AltaVista、Excite、WebCrawler、InfoSeek、Lycos、HotBot。缺了什么？**Google 那年九月才成立。**

### Cybercash 与漏斗

在线交易靠 [Cybercash](http://en.wikipedia.org/wiki/CyberCash,_Inc.)——没有这功能会在产品对比里被打死。但 Cybercash 太烂、多数店订单量又低，**不如让商家像接电话单一样处理订单**。我们专门有一页 [劝商家别做实时授权](http://www.ycombinator.com/viaweb/cybercash.html)。

整站像漏斗，把人导向 [试驾](http://ycombinator.com/viaweb/tesdriv.html)。在线试用软件当时很新鲜。我们在动态 URL 里加 `cgi-bin`，好误导竞争对手我们的实现方式。

### 带宽与「热水浴缸」

我们有一些 [知名用户](http://ycombinator.com/viaweb/us.html)。不用说，Frederick's of Hollywood 流量最大。大店统一收 **300 美元/月**，所以流量巨大的用户有点吓人——我算过 Frederick's 的带宽成本，大约也是 300/月。

我们托管所有店铺，1998 年 6 月合计刚超 **每月一千万次页面浏览**，在当时算吃带宽。办公室拉了两条 T1（3 Mb/s）。那时还没有公有云服务；托管也嫌风险高——机器老出事。于是服务器放在办公室，更准确说在 **Trevor 的办公室**。作为与六台尖叫塔式服务器同屋、且不与别人共享办公室的特权，他的房间绰号「热水浴缸」——机器散热惊人。多数日子靠一摞窗式空调勉强顶住。

### RTML 与「4.0」

描述页面用模板语言 [RTML](http://ycombinator.com/viaweb/rtml.html)，名义上代表什么，其实是我用 Rtm 的名字起的。RTML 是 Common Lisp 加宏和库，外面包一层结构化编辑器，看起来像有语法。

我们持续发布，软件其实没有版本；但当年贸易媒体认版本号，我们就 **编**。想大动静时，版本号就 [取整数](http://www.ycombinator.com/viaweb/rel4.html)。那个「4.0」图标还是我们自己的按钮 生成器做的。整个 Viaweb 站都用自家软件搭——虽不是网店，因为我们想 **体验用户所体验的**。

1997 年底我们做了通用购物搜索引擎 [Shopfind](http://ycombinator.com/viaweb/shoprel.html)，当时很超前：可编程爬虫，能爬多数在线店并抽出商品。


---

## 相关

- [[Paul Graham]]
- [[文章与材料库]]
- [[大佬的博客视频]]
- [[创业]]
- [[PG_另一条前路]]
- [[PG_ycombinator]]
