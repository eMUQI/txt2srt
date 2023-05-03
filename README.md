# txt2srt

根据文本文件自动根据字数计算时长，生成srt字幕格式的文件，方便用户导入到剪映软件中进行配音。

## 用法
安装好python环境并将python添加到环境变量。参考：[安装python教程](https://github.com/HDCodePractice/MakePythonProject/blob/main/%E7%AC%AC%E4%B8%80%E8%AF%BE%20%E5%AE%89%E8%A3%85Python%E5%92%8CVSCode%20(Windows).md#%E5%AE%89%E8%A3%85python)

双击运行`运行.bat`, 输入Y确认生成srt。 程序会自动检测同目录下所有 txt 文件，逐个生成 srt。

![example](./example.png)

## 计算方法
遇到`。！~？`就断句，每个字0.25秒，句子之间间隔两秒。