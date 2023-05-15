import logging
from logging.handlers import TimedRotatingFileHandler


class LogSystem(object):
    handlerList = []
    showOnCmd = True
    loggingLevel = logging.INFO
    loggingFile = None
    def __init__(self):
        self.logger = logging.getLogger('itchat')
        self.logger.addHandler(logging.NullHandler())
        self.logger.setLevel(self.loggingLevel)
        self.cmdHandler = logging.StreamHandler()
        self.fileHandler = None
        self.logger.addHandler(self.cmdHandler)
    def set_logging(self, showOnCmd=True, loggingFile=None,
            loggingLevel=logging.INFO):
        if showOnCmd != self.showOnCmd:
            if showOnCmd:
                self.logger.addHandler(self.cmdHandler)
            else:
                self.logger.removeHandler(self.cmdHandler)
            self.showOnCmd = showOnCmd
        if loggingFile != self.loggingFile:
            if self.loggingFile is not None: # clear old fileHandler
                self.logger.removeHandler(self.fileHandler)
                self.fileHandler.close()
            if loggingFile is not None: # add new fileHandler
                self.fileHandler = logging.FileHandler(loggingFile)
                self.logger.addHandler(self.fileHandler)
            self.loggingFile = loggingFile
        if loggingLevel != self.loggingLevel:
            self.logger.setLevel(loggingLevel)
            self.loggingLevel = loggingLevel

ls = LogSystem()
set_logging = ls.set_logging
# 创建一个 logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # 设置日志级别为 DEBUG

# 创建一个 handler，用于写入日志文件，并在每天午夜，创建新的日志文件
fh = TimedRotatingFileHandler('logfile.log', when='midnight', interval=1, backupCount=7)
fh.setLevel(logging.DEBUG)  # 设置 handler 的日志级别为 DEBUG

# 定义 handler 的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

# 给 logger 添加 handler
logger.addHandler(fh)

# 使用 logger
logger.debug('This is a debug message')