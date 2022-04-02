# RedditPlaceBluePrinter
Work with tempermonkey script https://greasyfork.org/zh-TW/scripts/442549-%E5%86%B2%E6%B5%AA%E6%8C%87%E5%8D%97

## 使用说明 User Guide

### 1
安装python，并用以下命令安装pillow。

install python and install pillow with the folowing line:

`pip install pillow`

### 2
打开 config.json ，修改xz.png为你的素材名称，并在下面两行填写你素材的左上角坐标。

Open config.json, modify xz.png to your pattern file name, and set target upper left coordinate in the following 2 lines.

### 3
运行以下命令或直接双击bluePrinter.py.

run the following command:

 `python blue_print.py`

### 4
将生成的blue_print.png上传到图床，安装脚本后修改脚本中的这一行中的网址为你的图床地址，刷新 r/place 。

upload the blue_print.png to picture bed, and replace the url in this line of the script you installed with your priture url, and refresh r/place.

`i.src = "https://preview.redd.it/qvkbj6rmr3r81.png?width=3000&format=png&auto=webp&s=889a126a491e94faf8e8b1008727d4544924e74a";`
