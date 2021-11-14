from datetime import datetime


def get_datetime() -> datetime:
    """
    Returns the current datetime object.
    :return: datetime object
    """
    return datetime.now()


def calc_uptime(wokeup_time: datetime) -> str:
    """
    Calculates the uptime of the system.
    :param wokeup_time: datetime object of the last wakeup
    :return: str of the uptime
    """
    now = datetime.now()
    delta = now - wokeup_time
    return str(delta)


def get_yyyymmdd_str() -> str:
    """
    Returns the current date in yyyymmdd format.
    :return: str of the current date
    """
    return datetime.now().strftime("%Y%m%d")
