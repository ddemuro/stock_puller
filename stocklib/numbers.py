"""Module to operate with numbers."""


def convert_number_to_string_text(number):
    """Simple function to convert a number to a string with a suffix.

    :param number: A number to convert.
    :type number: String or Integer
    :return: A string with the number and the suffix.
    :rtype: String
    """
    powers = {'M': 10 ** 9, 'B': 10 ** 12, 'T': 10 ** 16, 'Q': 10 ** 15}
    for suffix, power in powers.items():
        if number >= power:
            return str(round(number / power, 2)) + suffix
    return str(number)
