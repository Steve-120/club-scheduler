# club-schedulerrrererer
A python script that outputs the best timeslots for a club activity to minimize conflict with club members' schedules

### parameters
The parameters that adjust the input and output settings are the global variables of at the top of `scheduler.py`. Currently, the following parameters can be adjusted:
- `is_24_hour_format`: sets how times are formatted. `True` for 24-hour format and `False` (default) for 12-hour format.
- `start_time`: sets lower bound of the schedules of club members and the potential club activity. `"7:00 AM"` by default.
- `end_time`: sets upper bound of the schedules of club members and the potential club activity. `"9:00 PM"` by default, but is set to `"10:00 AM"` for the sample.
- `activity_length`: sets the desired length of time (in minutes) of the club activity. `180` by default, but is set to `60` for the sample.
- `block_length`: sets the number of minutes all start and end times (of schedules and club activities) are rounded off to. Generally, the higher it is, the more efficient and quicker the execution. `5` by default.
- `num_choices`: sets the number of top choices of club activity timeslots that the program outputs.`5` by default, but is set to `10` for the sample.

### input
Input is taken from the file `schedules.txt`.
The first line should contain the days of the week when the club members' schedules and club activities take place. For example:
If schedules and activities occur on weekdays, then the first line should be `Monday Tuesday Wednesday Thursday Friday`.
But if they occur on the whole week, it should instead be `Monday Tuesday Wednesday Thursday Friday Saturday Sunday`.

The next lines would contain the schedules of each club member.
Club member's schedules are arranged in blocks:
```
<Name of member (recommended to be less than 25 characters to have nice output formatting)>
<Day 1 time intervals that member  cannot participate in>
<Day 2 time intervals that member  cannot participate in>
...
<Day n time intervals that member  cannot participate in>
```
where `n` is the number of days in the first line.

Example member schedule:
```
Spongebob Squarepants
7:30 AM - 9:30 AM, 9:50 AM - 12:00 PM, 2:00 PM - 3:00 PM
8:30 AM - 9:30 AM, 9:50 AM - 12:10 PM, 1:00 PM - 1:30 PM, 3:30 PM - 4:30 PM

10:00 AM - 12:00 PM, 12:30 PM - 4:00 PM
9:00 AM - 11:00 AM
```
In which case, `n` = 5 and the member has the whole day free on the third day.

### output
Output is found in the file `choices.txt`
For each choice, the following info can be found for each choice:
- first line: choice number, day of the week, timeslot
- second line: number of members without conflict out of the total number of members
- third line onwards: list of members that have part of their schedule in conflict with the given timeslot.
