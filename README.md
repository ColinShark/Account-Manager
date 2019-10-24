# Account Manager

This is not a manager that organizes your accounts.
This code only updates the Steam game bans of your account(s) in a [Google Spreadsheet][TEMPLATE] via the Steam API for you.

## Setup

1. Download this repository, either as [`.zip`][ZIP] or via `git clone`
2. Install required modules with `pip install -r requirements.txt`
3. Open the [Spreadsheet template][TEMPLATE] and copy it
    * Hit "File" in the top left
    * Click on "Make a copy"
4. Create Signed Credentials for use with the Google API
    * Follow the first three steps [from gspread's documentation][GSPREAD]
5. Save the acquired `.json` as `credentials.json` into the repositorys root
6. Copy the example config to `config.ini`
7. [Set up a cronjob][CRON] for whatever is best for you.
    * *[Every 30 minutes][30M] suits best in my opinion*

If you have populated your spreadsheet with some accounts and execute the script (`python accmgr.py`) you should see the Bans column update accordingly (given you have Game Banned accounts linked).
The Template is populated with some accounts as a "Demo".

## Screenshot(s)

[<img src="https://i.imgur.com/1DDMMNj.png" alt="An Example Overview">][TEMPLATE]

## Credits

RazeN for the idea and [his template][RAZEN]

Shoutout to the [Cathook Team][CAT]
([Account Generator][ACCGEN] / [Telegram Group][SAG_TG])

## License

[WTFPL] - What The F**k to Public License

Literally do as you please. I'd kindly ask you to include credits, if you make something inspired by this, but it's by no means obligatory.


[TEMPLATE]: https://docs.google.com/spreadsheets/d/16t5A9dJL3pdU2hJNTPNl2ilquFnAw6C-O3PpkAbPCtM/edit?usp=sharing
[GSPREAD]: https://gspread.readthedocs.io/en/latest/oauth2.html#using-signed-credentials
[ZIP]: https://github.com/ColinTheShark/Account-Manager/archive/master.zip
[CRON]: https://google.com/search?q=how+to+set+up+a+cronjob
[30M]: https://crontab.guru/#*/30_*_*_*_*
[RAZEN]: https://gist.github.com/RazenIW/4e896edaea5b891b19c0c4fc556f53b7
[CAT]: https://cathook.club
[ACCGEN]: https://accgen.cathook.club
[SAG_TG]: https://t.me/sag_bot_chat
[WTFPL]: LICENSE
