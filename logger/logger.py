# coding: utf-8

from logging import getLogger, Formatter, FileHandler, DEBUG, INFO

class Logger(object):

    filename  = "DEBUG.log"
    level     = DEBUG
    fmt = "%(asctime)s %(name)s %(levelname)s %(message)s"

    def __init__(self, name, **kwargs):

        if kwargs.has_key("filename"):
            self.filename = kwargs['filename']

        if kwargs.has_key('level'):
            self.level = kwargs['level']

        if kwargs.has_key('fmt'):
            self.fmt = kwargs['fmt']

        self.logger = getLogger(name)

        self.logger.setLevel(self.level)

        handler = FileHandler(self.filename)
        handler.setLevel(self.level)
        handler.setFormatter(Formatter(self.fmt))

        self.logger.addHandler(handler)

if __name__ == "__main__":

    log1 = Logger("log1")
    log1.logger.debug("debug")
    log1.logger.info("info")
    log1.logger.critical("critical")
    log1.logger.error("error")

    log2 = Logger("log2", filename="DEBUG2.log")
    log2.logger.debug("debug")
    log2.logger.info("info")
    log2.logger.critical("critical")
    log2.logger.error("error")
