# aptestr
Test multi-window network application using Python


## Open-and-paste test.

Here’s an example Python script open_and_paste.py

    1. Opens CLI window
    2. Keys in 2 command into new window: `cd` and `dir`
```python
   pld=['cd c:\\tmp\n', 'dir\n']
   OpenCliAndSendPayload(pld,'Python test', pos)
```

### Run it

```
C:\\Python35-64\\python.exe ..\\aptestr\open_and_paste.py
```


### Result

New CLI windows opens and 2 commands execute in predefined order.



## Open-Putty-and-send-payload test.

Here’s an example Python script open_and_paste.py

    1. Opens Putty window
    2. Keysa command into new window: `ls -al`
```python
	pld=['ls -al\n']
	puttywin= OpenPuttyAndSendPayload(pld=pld,title='Putty test', user='bicadmin', pwd='bicadmin', host='ny5lsctgbiuniv1', pos=pos)
```

### Run it

```
C:\\Python35-64\\python.exe ..\\aptestr\open_putty_and_send_payload.py
```


### Result

New Putty window opens and command is executed.



## Open-and-snap test.

Here’s an example Python script open_and_snap.py

    1. Opens CLI window
    2. Keys in 2 command into new window: `cd` and `dir`
    3. It creates 50 snapshots of Putty process in 10 seconds (5/sec)

### Run it

```
C:\\Python35-64\\python.exe ..\\aptestr\open_and_snap.py
```


### Result

New Putty window opens and 50 JPEG snapshots created.



## Create-gif test.

Python script create_gif.py will create GIF file from your jpeg files.

    

### Run it

```
C:\\Python35-64\\python.exe ..\\aptestr\create_gif.py
```


### Result


![gif](https://github.com/pydemo/aptestr/blob/master/aptestr.gif?raw=true)


