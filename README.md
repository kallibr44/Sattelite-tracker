Satellite tracker


This Open Source Python program can locate weather satellites NOAA family and predict approach.
Programm have CLI interface and created to make projects like a antenna tracker etc.
Requirement:
 pip install pypredict
TO DO list:

1. Simple interface (ready)
2. Updating TLE automatically (ready)
3. Show simple location with normal interface (ready)
4. Create DB for all TLE of NOAA(about 50%)
5. Menu to choose the satellite
6. add API for work with other projects (e.g. antenna dish auto-track)
7. ???
...

Known bugs:
1. If we will update DB second time, all data will clone himself into DB. (Maybe crash DB) (Solved!)
2. track just for NOAA-19 (Working on it) (Solved!)

How to use:
 1.Install requirements 
 pip install -r requirements.txt
 2.Run the program
 python sattrack.py
