# git-cheatsheet

一个用 Python 写的 Git 命令速查小工具，在终端里按分类查看常用 Git 命令和说明。

## 做什么

- 按「基础配置 / 初始化与克隆 / 提交 / 分支 / 远程仓库 / 撤销」分类整理常用 Git 命令
- 每条命令都配有中文说明，适合刚学 Git 时随时查阅
- 纯 Python 标准库实现，无需安装任何依赖

## 怎样运行

需要 Python 3.8 或更高版本。

```bash
python3 git_cheatsheet.py
```

运行后会输出全部分类的命令，例如：

```text
Git 命令速查

【基础配置】
  git config --global user.name "你的名字"
      -> 设置提交者姓名
```
