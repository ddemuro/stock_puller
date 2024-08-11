"""This module is used to process M1 data from CSV file from Holdings" tab."""

from stocklib.general import debug_print


def join_m1_when_quote(data1, data2):
    """This function is used to join data from M1 CSV file when there is a quote in the data.

    :param data1: First data to join
    :type data1: String
    :param data2: Second data to join
    :type data2: String
    :return: Joined data
    :rtype data1 for rows 1 and 2: String
    :rtype data1 for rows 3-7: Float
    """

    if data2 is None:
        return float(data1.replace(",", ""))
    if "," in data1:
        data1 = data1.replace(",", "")
        try:
            return float(data1)
        except:
            return str(data1)
    if "." in data1:
        try:
            return float(data1)
        except:
            return str(data1)
    return data1


def sanitize_m1(row):
    """ This function is used to sanitize M1 data from CSV file from Holdings" tab.

    :param row: Field to sanitize
    :type row: String
    :return: Sanitized field
    :rtype: Dictionary
    """
    append = {
        "Name in M1": join_m1_when_quote(row[1], row[2]),
        "Shares": join_m1_when_quote(row[2], row[3]),
        "Avg Price $": join_m1_when_quote(row[3], row[4]),
        "Cost Basis $": join_m1_when_quote(row[4], row[5]),
        "Unrealized Gain/Loss $": join_m1_when_quote(row[5], row[6]),
        "Unrealized Gain/Loss %": join_m1_when_quote(row[6], row[7]),
        "Value $": join_m1_when_quote(row[7], None),
    }

    debug_print(append)

    return append
