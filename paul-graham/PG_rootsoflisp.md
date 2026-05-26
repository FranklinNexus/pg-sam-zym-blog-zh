---
type: material
area: startup
author: Paul Graham
source: paulgraham.com
tags:
  - Paul Graham
  - essay
  - tech
---

# Lisp 的根源

> 原文：<https://paulgraham.com/rootsoflisp.html>
> 来源：[paulgraham.com](https://paulgraham.com/)
> 英文标题：The Roots of Lisp
> 年代：2001 年 5 月

（本文写来帮自己准确理解 McCarthy 的发现。用 Lisp 编程不必背这些，但对想理解 Lisp **本质**——起源与语义核心——的人应有帮助。拥有这样一个「核心」是 Lisp 的显著特征，也是各 Lisp 方言仍彼此相近的原因。）

### McCarthy 做了什么

1960 年，John McCarthy 发表的工作，有人说像 **欧几里得之于几何**：他展示如何用少数简单运算符与函数记号，构造 **完整的编程语言**。

这种语言叫 Lisp（List Processing），关键思想之一是用 **列表** 这一简单结构同时处理 **代码与数据**。

### 两种模型与沼泽

McCarthy 的发现值得理解：它既是计算机史里程碑，也是我们时代编程趋势的 **模型**。在我看来，迄今有两种真正干净、一致的编程模型：**C 模型** 与 **Lisp 模型**——像两处高地，中间是沼泽。随着机器变强，新语言一直在 **向 Lisp 模型靠拢**。

过去二十年流行配方：取 C 的计算模型，逐步加入 Lisp 模型的部分（运行时类型、垃圾回收等）。下文用最简术语解释 McCarthy 的发现——不只为了四十年前有趣的理论，也为了看清 **语言往哪走**。

### 能描述自身

Lisp 的不寻常之处——事实上 **定义性品质**——是它能 **用自身书写**。为理解 McCarthy 的意思，我们将把他的数学记号 **翻译成可运行的 Common Lisp**。


---

## 相关

- [[Paul Graham]]
- [[文章与材料库]]
- [[大佬的博客视频]]
- [[创业]]
- [[PG_diff]]
- [[PG_书呆子的反击]]
- [[AI 与技术]]
