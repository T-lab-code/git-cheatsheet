#!/usr/bin/env python3
"""Git 命令速查工具：在终端快速查看常用 Git 命令及其说明。"""

CHEATSHEET = {
    "基础配置": [
        ('git config --global user.name "你的名字"', "设置提交者姓名"),
        ('git config --global user.email "你的邮箱"', "设置提交者邮箱"),
        ("git config --global --list", "查看全局配置"),
    ],
    "初始化与克隆": [
        ("git init", "在当前目录初始化一个本地仓库"),
        ("git clone <仓库地址>", "把远程仓库完整复制到本地"),
    ],
    "查看状态与提交": [
        ("git status", "查看工作区与暂存区的状态"),
        ("git add .", "把所有改动加入暂存区"),
        ('git commit -m "提交说明"', "把暂存区内容提交到本地仓库"),
        ("git log --oneline", "以单行形式查看提交历史"),
    ],
    "分支操作": [
        ("git branch", "列出本地分支"),
        ("git checkout -b <分支名>", "新建并切换到指定分支"),
        ("git switch <分支名>", "切换到已有分支"),
        ("git merge <分支名>", "把指定分支合并到当前分支"),
    ],
    "远程仓库": [
        ("git remote add origin <仓库地址>", "关联远程仓库，并命名为 origin"),
        ("git push -u origin main", "首次推送 main 分支并建立追踪关系"),
        ("git push", "把本地提交推送到远程仓库"),
        ("git pull", "拉取远程更新并合并到本地"),
    ],
    "查看与撤销": [
        ("git diff", "查看尚未暂存的改动"),
        ("git restore <文件名>", "丢弃工作区中某个文件的修改"),
        ("git reset --hard <提交号>", "把仓库回退到指定提交（会丢失改动）"),
    ],
}


def show_all():
    """按分类打印全部命令。"""
    for category, items in CHEATSHEET.items():
        print(f"\n【{category}】")
        for command, desc in items:
            print(f"  {command}")
            print(f"      -> {desc}")


def main():
    print("Git 命令速查")
    show_all()


if __name__ == "__main__":
    main()
