# Account Manager

This is not a manager that organizes the accounts for you. This project just aims to get the amount of game bans into your Google Spreadsheet you (should have) obtained from the template linked below.

Don't touch the files in the methods folder, those are critical and rows/colums are hard-coded.

## Usage

Install the required Python Packages.

* `requests`
* `gspread`
* `oauth2client` (deprecated)
  * `oauthlib`
  * `google-auth`

Set up your Spreadsheet from the template. You will need an access token file from Google to access your Spreadsheet with this.
Obtain them from your Google Projects page.

* Create a copy of the Template and save the Sheet Key from the URL into the [AccountManager.py](AccountManager.py#L8).
  * (Example: `7RItXr-RybUchxTXFtTPbAGKim-PbEe6oiGVkJP8NoJ2`)
* Go [here](https://console.cloud.google.com/apis/dashboard) and create a new project, if you don't want to use an existing one.
  * Download the credentials and put the filename as a string into the [AccountManager.py](AccountManager.py#L9).
* Go [here](https://steamcomunity.com/dev/apikey) and get your own API Key for use with this script.
  * Put the API Key from Steam in the [AccountManager.py](AccountManager.py#L13).
* If you want the script to be executed automatically, put the files on a remote server and set up a [cronjob](https://google.com/search?q=how+to+set+up+a+cronjob).

If all went well, the Sheet get's updated with the current amount of game bans on the account. This should happen instantly.

## Credits

RazeN for the idea. That's pretty much it :P

## License

**[GPLv3](COPYING)**
