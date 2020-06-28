# club-scheduler
A python script that outputs the best timeslots for a club activity to minimize conflict with club members' schedules using Excel .xlsx workbooks

### prerequisites
The only requirements needed are Python 3 and the openpyxl python module pre-installed. The latter can be installed by typing `pip3 install openpyxl` on the command line after Python is installed.

### formatting
The workbook should have two worksheets labelled "Schedules", where the schedules of the club members are to be inputted, and "Settings" where extra parameters are inputted for customization. After the code runs, a new worksheet will be made in the input workbook titled "Output", where the best club activity times are displayed.

### schedules
The club members' schedules are taken from the worksheet labelled "Schedules" in the file `schedules.xlsx`.

If `n` is the number of days considered for scheduling the club activity, then `n+1` consecutive lines are to be delegated for each club member.
In these `n+1` blocks, the first line should only have the leftmost cell filled with the member's name. Shortened names are preferred so that the output formatting is better.

The `i`th line of the next `n` lines should contain the schedule for that member on the `i`th day. Particularly, the leftmost cell should be blank, and the next cells to the right, from the second column onwards, should each be filled with a time interval, which represents a block of time which the member is busy/unavailable for a club activity. Use as many cells as needed to describe the member's schedule on that day. Either 12-hour or 24-hour format is fine.

Example member schedule:

| Name | Time intervals | | | |
| --- | --- | --- | --- | --- |
| Spongebob Squarepants |  |  |  | |
| | 7:30 AM - 9:30 AM | 9:50 AM - 12:00 PM | 2:00 PM - 3:00 PM | |
| | 8:30 AM - 9:30 AM | 9:50 AM - 12:10 PM | 1:00 PM - 1:30 PM | 3:30 PM - 4:30 PM |
| | ‎ | | | | 
| | 10:00 AM - 12:00 PM | 12:30 PM - 4:00 PM | | |
| | 9:00 AM - 11:00 AM | | | |

In which case, `n` = 5 days, and the member has the whole day free on the third day (the headers aren't included in the input).

### parameters
The parameters that adjust the program settings can be modified in the "Settings" worksheet of `schedules.xlsx`. Currently, the parameters that can be adjusted are:
- Days of the week: List out which days of the week are considered for scheduling the club activity. One cell for each day on the first row.
- 24-hour format: Type `Y` on the second cell if times are inputted in 24-hour format and `N` for 12-hour format.
- Time window for activities: What times can the club activity be held? The program will only consider club schedules within the time period set here.
- Duration of activity: This sets the desired length of time (in minutes) of the club activity.
- Block length: This sets the number of minutes all start and end times (of schedules and club activities) are rounded off to. Generally, the higher it is, the more efficient and quicker the execution.
- Number of choices to display: This sets the number of top choices of club activity timeslots that the program outputs.

### output
Output is found in the newly created "Output" worksheet of `schedules.xlsx`. The "Output" worksheet doesn't have to be deleted every time the code is run, as the code will automatically clear the output.

The program first outputs the number of members and days detected. This is so that the user can confirm that the program parsed the input correctly and has the right number of members and days.

Then, the worksheet will contain the top choices. For each choice, the following info can be found:
- first row: choice number, day of the week, timeslot
- second row: number of members without conflict out of the total number of members
- third row onwards: list of members that have part of their schedule in conflict with the given timeslot
