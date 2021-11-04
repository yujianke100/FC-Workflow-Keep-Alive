# FC-Workflow-Keep-Alive
利用云函数实现给workflow无限续杯

用workflow时间不长，最近才注意到这玩意儿60天停一次。看来只要是能薅的羊毛，没点防护措施谁都会受不了hhh。
## 受[Workflow-Keep-Alive](https://github.com/zhzhzhy/Workflow-Keep-Alive)启发写的这个云函数

讲道理，拿workflow续杯workflow实在是有点。。。

而且这个项目不能比较方便地实现多个workflow续杯，所以我自己动手了。

## 使用方法

1. 腾讯云或者阿里云搞个云函数
2. 代码扔进去
3. 整个token扔进去。给一个[token创建传送门](https://github.com/settings/tokens)。原则上给个`workflow`权限就行.
4. 修改url。格式为：`https://api.github.com/repos/你的用户名/你的仓库名/actions/workflows/你的.yml文件名/enable`
5. 别忘了给云函数搞个定时运行。60天掉一次嘛，一个月跑一次就够了。
6. 我这边的是腾讯云上的写法，扔的时候注意改成符合你用的云函数规范的写法。
