Constantine
===================
Constantine is a [Python 3](https://www.python.org/downloads/) tool for automatically generating event posters from public Google Calendar events. It is primarily written for [HackSoc](https://hacksoc.org) of University of York to partially automate some publicity work, but is written in a very adaptable way for other uses. It uses [XeTeX](http://xetex.sourceforge.net/) for PDF typesetting.

Constantine requires Python 3.3+ and XeLaTeX.

#Installation#
First, to access Google Calendar, even just for public events, you need a Google API Key, which can be obtained by visiting Google API Console [here](https://console.developers.google.com/apis/credentials), you may wish to create a new Google API project for Constantine when prompted.

After obtaining the API Key, edit `settings.json` as required:
* `logo`: either relative path (when running the source) or absolute path (when installed as a package) of your organisation's logo, which is highly recommended to be a background-transparent PNG file.
* `url`, `email`, `irc_network`, `irc_channel`, `twitter`, `facebook`: contact information for your organisation, modify as appropriate.
* `calendar_id`: the Google Calendar ID for the calendar you want to fetch events from, a guide for finding the ID can be found [here](https://support.appmachine.com/hc/en-us/articles/203645966-Find-your-Google-Calendar-ID-for-the-Events-block).
* `google_api_key`: the Google API Key you just obtained above, the default one is access-restricted and will **not** work for you.
* `term_start_dates`: a list of dates for starts-of-terms, used for University of York's week numbering, as it appears in the generated PDF.
* `page_background_colour`, `page_normal_text_colour`, `page_emphasis_text_colour`, `page_deemphasis_text_colour`: Hex colour codes for the background and text colours in the generated PDF, modify if you would like to change the colour scheme.

Constantine only has one dependent package, [requests](http://docs.python-requests.org/en/master/), which can be installed by:

    pip install requests

It will be automatically installed if you installed Constantine with pip instead (not recommended):

    pip install Constantine

Make sure that XeLaTeX works on your system by executing `xelatex -version`, then run Constantine with:

    python main.py /path/to/output.pdf

Or for pip installed package:

    Constantine /path/to/output.pdf

**The script will always fetch next week's events, with a week starting from Monday.**

And it's done. If any error occurs outputs should provide some clue.

#Special Text#
The file `special_text.txt` contains a section that will be automatically added to the end of the main content, allowing custom text to be added. If you do not want this section to be created, make this file empty. Otherwise, the first line will be the section title (resembling the style of e.g. "Tuesday") and the rest of the lines will be the section text.

#ToDo's#
* In LaTeX, `multicols*`(multiple columns without balancing) cannot be used inside a box, without which the bottom dotted line seems difficulty to fit. I am pretty terrible at LaTeX, so if you have a better solution please do send a pull request :)
* Sorry for the horrible packaging, by the way. The lack of OOP in this hacked-together solution makes good packaging difficult.