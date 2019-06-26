import logging

# logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)
# logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
# logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
# logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


# It should be noted that calling basicConfig() to configure the root logger works only if the root logger
# has not been configured before. Basically, this function can only be called once.


# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')


#############Logging Variable Data#############
# name = 'John'
# logging.error('%s raised an error', name)
#
#
#
# Capturing Stack Traces
# The logging module also allows you to capture the full stack traces in an application.
# Exception information can be captured if the exc_info parameter is passed as True
# import logging
# a = 5
# b = 0
# try:
#   c = a / b
# except Exception as e:
#   logging.error("Exception occurred", exc_info=True)


# To put it more simply, calling logging.exception() is like calling logging.error(exc_info=True).
# But since this method always dumps exception information, it should only be called from an exception handler.

#
# import logging
# a = 5
# b = 0
# try:
#   c = a / b
# except Exception as e:
#   logging.exception("Exception occurred")



# Handlers come into the picture when you want to configure your own loggers and send the logs to multiple places when they are generated.
# Handlers send the log messages to configured destinations like the standard output stream or a file or over HTTP or to your email via SMTP.
#
# Like loggers, you can also set the severity level in handlers.
# This is useful if you want to set multiple handlers for the same logger but want different severity levels for each of them.
# For example, you may want logs with level WARNING and above to be logged to the console, but everything with level ERROR and above should also be saved to a file.
# Here’s a program that does that:
# import logging

# Create a custom logger
# logger = logging.getLogger(__name__)
# print(logger)  ###Prints - <Logger __main__ (WARNING)>###

# unlike the root logger, a custom logger can’t be configured using basicConfig(). You have to configure it using Handlers and Formatters


# # logging_example.py
# import logging
# # Create a custom logger
# logger = logging.getLogger(__name__)
# # Create handlers
# c_handler = logging.StreamHandler()
# f_handler = logging.FileHandler('file.log')
# c_handler.setLevel(logging.WARNING)
# f_handler.setLevel(logging.ERROR)
#
# # Create formatters and add it to handlers
# c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# c_handler.setFormatter(c_format)
# f_handler.setFormatter(f_format)
#
# # Add handlers to the logger
# logger.addHandler(c_handler)
# logger.addHandler(f_handler)
#
# logger.warning('This is a warning')
# logger.error('This is an error')


# You can configure logging as shown above using the module and class functions or by creating a config file or a dictionary and
# loading it using fileConfig() or dictConfig() respectively. These are useful in case you want to change your logging configuration
# in a running application.

#################Config File#######################
# [loggers]
# keys=root,sampleLogger
#
# [handlers]
# keys=consoleHandler
#
# [formatters]
# keys=sampleFormatter
#
# [logger_root]
# level=DEBUG
# handlers=consoleHandler
#
# [logger_sampleLogger]
# level=DEBUG
# handlers=consoleHandler
# qualname=sampleLogger
# propagate=0
#
# [handler_consoleHandler]
# class=StreamHandler
# level=DEBUG
# formatter=sampleFormatter
# args=(sys.stdout,)
#
# [formatter_sampleFormatter]
# format=%(asctime)s - %(name)s - %(levelname)s - %(message)s

# To load this config file, you have to use fileConfig():
# import logging
# import logging.config
#
# logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)
#
# # Get the logger specified in the file
# logger = logging.getLogger(__name__)
#
# logger.debug('This is a debug message')



