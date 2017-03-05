import os
import datetime
import string, random
import json
import re

def get_project_full_path():
    """ Return the full path of the project for navigation."""

    projectDirectory = os.path.dirname(os.path.realpath(__file__))

    return projectDirectory


def check_date_string(date):
    """ Return True if the input string is a valid YYYY-MM-DD date, False
        otherwise. """

    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return False

    return True


def read_config():
    """ Return the configuration value of requestedKey. """

    full_path = get_project_full_path()
    configFile = full_path + "/settings.json"

    if not os.path.isfile(configFile):
        raise ValueError("The configuration file settings.json does not exist!")

    try:
        with open(configFile) as SettingsFile:
            SettingsData = json.load(SettingsFile)
            if not os.path.isfile(full_path + "/" + SettingsData['logo']):
                raise ValueError("The logo file does not exist!")
            if not any([check_date_string(i) for i in SettingsData['term_start_dates']]):
                raise ValueError("Invalid date(s) found in 'term_start_dates' of settings.json!")
            return SettingsData
    except:
        print("Error reading settings.json, JSON probably not valid.")
        raise

    return False


def get_closest_date_time(current_date, date_list):
    """ Given a datetime, find the closest previous datetime in list. Adapted from:
        http://stackoverflow.com/a/17249470/846892
    """

    def func(x):
       d = datetime.datetime.strptime(x, "%Y-%m-%d")
       delta = current_date - d if d < current_date else datetime.timedelta.max
       return delta

    return min(date_list, key = func)


def tex_escape(text):
    """
        Adapted from http://stackoverflow.com/a/25875504
        :param text: a plain text message
        :return: the message escaped to appear correctly in LaTeX
    """
    conv = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\^{}',
        '\\': r'\textbackslash{}',
        '<': r'\textless',
        '>': r'\textgreater',
    }
    regex = re.compile('|'.join(re.escape(str(key)) for key in sorted(conv.keys(), key = lambda item: - len(item))))
    return regex.sub(lambda match: conv[match.group()], str(text))


def settings_to_formatting(settings):
    """ Given a settings dictionary, return a dictionary for formatting the
        LaTeX template except week_number, events and special text.
        Certain items needs to be split to different keys due to LaTeX
        formatting.
    """

    formatting = {}
    for key, val in settings.items():

        if key == "logo" and val.startswith('tex/'):
            formatting["logo_file"] = val[4:]
        elif key == "url":
            formatting["domain_main"] = val.rsplit('.', 1)[0]
            formatting["domain_tld"] = "." + val.rsplit('.', 1)[1]
        elif key == "email":
            formatting["email_user"] = val.rsplit('@', 1)[0]
            formatting["email_domain"] = "@" + val.rsplit('@', 1)[1]
        else:
            formatting[key] = val

    # Escape TeX special characters.
    formatting = {i:tex_escape(formatting[i]) for i in formatting}

    return formatting