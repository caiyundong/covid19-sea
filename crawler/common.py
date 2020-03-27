from datetime import datetime, timedelta


def previous_date(current_date, days=1):
    """
    Return the previous_date
    :param current_date:
    :return:
    """
    previous_date = datetime.strptime(current_date, "%Y-%m-%d")-timedelta(days=days)
    return previous_date.strftime("%Y-%m-%d")



