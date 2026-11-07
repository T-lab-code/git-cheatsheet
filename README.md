# git-cheatsheet

一个用 Python 写的 Git 命令速查小工具，在终端里按分类查看常用 Git 命令和说明。

## 做什么

- 按「基础配置 / 初始化与克隆 / 查看状态与提交 / 分支操作 / 远程仓库 / 查看与撤销」分类整理常用 Git 命令
- 每条命令都配有中文说明，适合刚学 Git 时随时查阅
- 支持关键词搜索，不用记住命令属于哪个分类
- 纯 Python 标准库实现，无需安装任何依赖

## 怎样运行

需要 Python 3.8 或更高版本。

```bash
git clone <本仓库地址>
cd git-cheatsheet
python3 git_cheatsheet.py
```

运行后会输出全部分类的命令，例如：

```text
Git 命令速查

【基础配置】
  git config --global user.name "你的名字"
      -> 设置提交者姓名
```

### 按关键词搜索

```bash
python3 git_cheatsheet.py push
```

会输出所有与 `push` 相关的命令和说明。

### 查看所有分类

```bash
python3 git_cheatsheet.py --list
```

### 示例输出

```text
【远程仓库】
  git push -u origin main
      -> 首次推送 main 分支并建立追踪关系
  git push
      -> 把本地提交推送到远程仓库
```

## 项目结构

```text
git-cheatsheet/
├── git_cheatsheet.py   # 主程序与命令数据
├── README.md           # 项目说明
└── .gitignore          # 忽略 Python 缓存等文件
```

## 常用 Git 命令（本项目用到的）

```bash
git add .
git commit -m "提交说明"
git push
```
