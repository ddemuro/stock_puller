"""General functions that are used throughout the project."""
import datetime

# Debug flag
DEBUG = False


def debug_print(msg):
    """If debug mode is on, print the message.

    :param msg: The message to print.
    :type msg: String
    """
    if DEBUG:
        print(msg)


def convert_epoch_to_date(epoch):
    """Convert epoch to date.

    :param epoch: Epoch to convert.
    :type epoch: String
    :return: Date
    :rtype: String
    """
    return datetime.datetime.fromtimestamp(int(epoch)).strftime('%Y-%m-%d')