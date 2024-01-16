# DreamSchoolTeam_we

**使用说明**:
- 这个脚本接受两个命令行参数：一个日期（格式为YYYYMMDD）和一个货币代号（如USD、EUR）。
- 你需要确保安装了Selenium库和相应的WebDriver（例如ChromeDriver）。
- 该脚本使用Chrome WebDriver，你可以根据你的浏览器偏好更改它。
- 请注意，页面的结构和元素可能会随时间变化，所以如果网站结构发生变化，脚本可能需要更新。

**异常处理**:
- 脚本包括了基本的异常处理，例如处理网络超时和输入格式错误。

运行示例：在命令行中输入 `python3 yourcode.py 20211231 USD`，将按要求输出相应日期和货币的现汇卖出价。
