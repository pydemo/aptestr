import os, sys
import ctypes
import datetime
from pprint import pprint
import win32gui, win32api, win32con
import win32process
from time import sleep
from subprocess import Popen, CREATE_NEW_CONSOLE

e=sys.exit



#home=os.path.dirname(sys.argv[0])
#if not home :
home=os.path.dirname(os.path.abspath(__file__))
putty_loc=os.path.join(home,'Putty')	
	
LONG = ctypes.c_long
DWORD = ctypes.c_ulong
ULONG_PTR = ctypes.POINTER(DWORD)
WORD = ctypes.c_ushort

class MOUSEINPUT(ctypes.Structure):
	_fields_ = (('dx', LONG),
				('dy', LONG),
				('mouseData', DWORD),
				('dwFlags', DWORD),
				('time', DWORD),
				('dwExtraInfo', ULONG_PTR))

class KEYBDINPUT(ctypes.Structure):
	_fields_ = (('wVk', WORD),
				('wScan', WORD),
				('dwFlags', DWORD),
				('time', DWORD),
				('dwExtraInfo', ULONG_PTR))

class HARDWAREINPUT(ctypes.Structure):
	_fields_ = (('uMsg', DWORD),
				('wParamL', WORD),
				('wParamH', WORD))

class _INPUTunion(ctypes.Union):
	_fields_ = (('mi', MOUSEINPUT),
				('ki', KEYBDINPUT),
				('hi', HARDWAREINPUT))

class INPUT(ctypes.Structure):
	_fields_ = (('type', DWORD),
				('union', _INPUTunion))

def SendInput(*inputs):
	nInputs = len(inputs)
	LPINPUT = INPUT * nInputs
	pInputs = LPINPUT(*inputs)
	cbSize = ctypes.c_int(ctypes.sizeof(INPUT))
	return ctypes.windll.user32.SendInput(nInputs, pInputs, cbSize)

INPUT_MOUSE = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARD = 2

def Input(structure):
	if isinstance(structure, MOUSEINPUT):
		return INPUT(INPUT_MOUSE, _INPUTunion(mi=structure))
	if isinstance(structure, KEYBDINPUT):
		return INPUT(INPUT_KEYBOARD, _INPUTunion(ki=structure))
	if isinstance(structure, HARDWAREINPUT):
		return INPUT(INPUT_HARDWARE, _INPUTunion(hi=structure))
	raise TypeError('Cannot create INPUT structure!')

WHEEL_DELTA = 120
XBUTTON1 = 0x0001
XBUTTON2 = 0x0002
MOUSEEVENTF_ABSOLUTE = 0x8000
MOUSEEVENTF_HWHEEL = 0x01000
MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_MOVE_NOCOALESCE = 0x2000
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010
MOUSEEVENTF_MIDDLEDOWN = 0x0020
MOUSEEVENTF_MIDDLEUP = 0x0040
MOUSEEVENTF_VIRTUALDESK = 0x4000
MOUSEEVENTF_WHEEL = 0x0800
MOUSEEVENTF_XDOWN = 0x0080
MOUSEEVENTF_XUP = 0x0100

def MouseInput(flags, x, y, data):
	return MOUSEINPUT(x, y, data, flags, 0, None)

VK_LBUTTON = 0x01               # Left mouse button
VK_RBUTTON = 0x02               # Right mouse button
VK_CANCEL = 0x03                # Control-break processing
VK_MBUTTON = 0x04               # Middle mouse button (three-button mouse)
VK_XBUTTON1 = 0x05              # X1 mouse button
VK_XBUTTON2 = 0x06              # X2 mouse button
VK_BACK = 0x08                  # BACKSPACE key
VK_TAB = 0x09                   # TAB key
VK_CLEAR = 0x0C                 # CLEAR key
VK_RETURN = 0x0D                # ENTER key
VK_SHIFT = 0x10                 # SHIFT key
VK_CONTROL = 0x11               # CTRL key
VK_MENU = 0x12                  # ALT key
VK_PAUSE = 0x13                 # PAUSE key
VK_CAPITAL = 0x14               # CAPS LOCK key
VK_KANA = 0x15                  # IME Kana mode
VK_HANGUL = 0x15                # IME Hangul mode
VK_JUNJA = 0x17                 # IME Junja mode
VK_FINAL = 0x18                 # IME final mode
VK_HANJA = 0x19                 # IME Hanja mode
VK_KANJI = 0x19                 # IME Kanji mode
VK_ESCAPE = 0x1B                # ESC key
VK_CONVERT = 0x1C               # IME convert
VK_NONCONVERT = 0x1D            # IME nonconvert
VK_ACCEPT = 0x1E                # IME accept
VK_MODECHANGE = 0x1F            # IME mode change request
VK_SPACE = 0x20                 # SPACEBAR
VK_PRIOR = 0x21                 # PAGE UP key
VK_NEXT = 0x22                  # PAGE DOWN key
VK_END = 0x23                   # END key
VK_HOME = 0x24                  # HOME key
VK_LEFT = 0x25                  # LEFT ARROW key
VK_UP = 0x26                    # UP ARROW key
VK_RIGHT = 0x27                 # RIGHT ARROW key
VK_DOWN = 0x28                  # DOWN ARROW key
VK_SELECT = 0x29                # SELECT key
VK_PRINT = 0x2A                 # PRINT key
VK_EXECUTE = 0x2B               # EXECUTE key
VK_SNAPSHOT = 0x2C              # PRINT SCREEN key
VK_INSERT = 0x2D                # INS key
VK_DELETE = 0x2E                # DEL key
VK_HELP = 0x2F                  # HELP key
VK_LWIN = 0x5B                  # Left Windows key (Natural keyboard)
VK_RWIN = 0x5C                  # Right Windows key (Natural keyboard)
VK_APPS = 0x5D                  # Applications key (Natural keyboard)
VK_SLEEP = 0x5F                 # Computer Sleep key
VK_NUMPAD0 = 0x60               # Numeric keypad 0 key
VK_NUMPAD1 = 0x61               # Numeric keypad 1 key
VK_NUMPAD2 = 0x62               # Numeric keypad 2 key
VK_NUMPAD3 = 0x63               # Numeric keypad 3 key
VK_NUMPAD4 = 0x64               # Numeric keypad 4 key
VK_NUMPAD5 = 0x65               # Numeric keypad 5 key
VK_NUMPAD6 = 0x66               # Numeric keypad 6 key
VK_NUMPAD7 = 0x67               # Numeric keypad 7 key
VK_NUMPAD8 = 0x68               # Numeric keypad 8 key
VK_NUMPAD9 = 0x69               # Numeric keypad 9 key
VK_MULTIPLY = 0x6A              # Multiply key
VK_ADD = 0x6B                   # Add key
VK_SEPARATOR = 0x6C             # Separator key
VK_SUBTRACT = 0x6D              # Subtract key
VK_DECIMAL = 0x6E               # Decimal key
VK_DIVIDE = 0x6F                # Divide key
VK_F1 = 0x70                    # F1 key
VK_F2 = 0x71                    # F2 key
VK_F3 = 0x72                    # F3 key
VK_F4 = 0x73                    # F4 key
VK_F5 = 0x74                    # F5 key
VK_F6 = 0x75                    # F6 key
VK_F7 = 0x76                    # F7 key
VK_F8 = 0x77                    # F8 key
VK_F9 = 0x78                    # F9 key
VK_F10 = 0x79                   # F10 key
VK_F11 = 0x7A                   # F11 key
VK_F12 = 0x7B                   # F12 key
VK_F13 = 0x7C                   # F13 key
VK_F14 = 0x7D                   # F14 key
VK_F15 = 0x7E                   # F15 key
VK_F16 = 0x7F                   # F16 key
VK_F17 = 0x80                   # F17 key
VK_F18 = 0x81                   # F18 key
VK_F19 = 0x82                   # F19 key
VK_F20 = 0x83                   # F20 key
VK_F21 = 0x84                   # F21 key
VK_F22 = 0x85                   # F22 key
VK_F23 = 0x86                   # F23 key
VK_F24 = 0x87                   # F24 key
VK_NUMLOCK = 0x90               # NUM LOCK key
VK_SCROLL = 0x91                # SCROLL LOCK key
VK_LSHIFT = 0xA0                # Left SHIFT key
VK_RSHIFT = 0xA1                # Right SHIFT key
VK_LCONTROL = 0xA2              # Left CONTROL key
VK_RCONTROL = 0xA3              # Right CONTROL key
VK_LMENU = 0xA4                 # Left MENU key
VK_RMENU = 0xA5                 # Right MENU key
VK_BROWSER_BACK = 0xA6          # Browser Back key
VK_BROWSER_FORWARD = 0xA7       # Browser Forward key
VK_BROWSER_REFRESH = 0xA8       # Browser Refresh key
VK_BROWSER_STOP = 0xA9          # Browser Stop key
VK_BROWSER_SEARCH = 0xAA        # Browser Search key
VK_BROWSER_FAVORITES = 0xAB     # Browser Favorites key
VK_BROWSER_HOME = 0xAC          # Browser Start and Home key
VK_VOLUME_MUTE = 0xAD           # Volume Mute key
VK_VOLUME_DOWN = 0xAE           # Volume Down key
VK_VOLUME_UP = 0xAF             # Volume Up key
VK_MEDIA_NEXT_TRACK = 0xB0      # Next Track key
VK_MEDIA_PREV_TRACK = 0xB1      # Previous Track key
VK_MEDIA_STOP = 0xB2            # Stop Media key
VK_MEDIA_PLAY_PAUSE = 0xB3      # Play/Pause Media key
VK_LAUNCH_MAIL = 0xB4           # Start Mail key
VK_LAUNCH_MEDIA_SELECT = 0xB5   # Select Media key
VK_LAUNCH_APP1 = 0xB6           # Start Application 1 key
VK_LAUNCH_APP2 = 0xB7           # Start Application 2 key
VK_OEM_1 = 0xBA                 # Used for miscellaneous characters; it can vary by keyboard.
								# For the US standard keyboard, the ';:' key
VK_OEM_PLUS = 0xBB              # For any country/region, the '+' key
VK_OEM_COMMA = 0xBC             # For any country/region, the ',' key
VK_OEM_MINUS = 0xBD             # For any country/region, the '-' key
VK_OEM_PERIOD = 0xBE            # For any country/region, the '.' key
VK_OEM_2 = 0xBF                 # Used for miscellaneous characters; it can vary by keyboard.
								# For the US standard keyboard, the '/?' key
VK_OEM_3 = 0xC0                 # Used for miscellaneous characters; it can vary by keyboard.
								# For the US standard keyboard, the '`~' key
VK_OEM_4 = 0xDB                 # Used for miscellaneous characters; it can vary by keyboard.
								# For the US standard keyboard, the '[{' key
VK_OEM_5 = 0xDC                 # Used for miscellaneous characters; it can vary by keyboard.
								# For the US standard keyboard, the '\|' key
VK_OEM_6 = 0xDD                 # Used for miscellaneous characters; it can vary by keyboard.
								# For the US standard keyboard, the ']}' key
VK_OEM_7 = 0xDE                 # Used for miscellaneous characters; it can vary by keyboard.
								# For the US standard keyboard, the 'single-quote/double-quote' key
VK_OEM_8 = 0xDF                 # Used for miscellaneous characters; it can vary by keyboard.
VK_OEM_102 = 0xE2               # Either the angle bracket key or the backslash key on the RT 102-key keyboard
VK_PROCESSKEY = 0xE5            # IME PROCESS key
VK_PACKET = 0xE7                # Used to pass Unicode characters as if they were keystrokes. The VK_PACKET key is the low word of a 32-bit Virtual Key value used for non-keyboard input methods. For more information, see Remark in KEYBDINPUT, SendInput, WM_KEYDOWN, and WM_KEYUP
VK_ATTN = 0xF6                  # Attn key
VK_CRSEL = 0xF7                 # CrSel key
VK_EXSEL = 0xF8                 # ExSel key
VK_EREOF = 0xF9                 # Erase EOF key
VK_PLAY = 0xFA                  # Play key
VK_ZOOM = 0xFB                  # Zoom key
VK_PA1 = 0xFD                   # PA1 key
VK_OEM_CLEAR = 0xFE             # Clear key

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP = 0x0002
KEYEVENTF_SCANCODE = 0x0008
KEYEVENTF_UNICODE = 0x0004

KEY_0 = 0x30
KEY_1 = 0x31
KEY_2 = 0x32
KEY_3 = 0x33
KEY_4 = 0x34
KEY_5 = 0x35
KEY_6 = 0x36
KEY_7 = 0x37
KEY_8 = 0x38
KEY_9 = 0x39
KEY_A = 0x41
KEY_B = 0x42
KEY_C = 0x43
KEY_D = 0x44
KEY_E = 0x45
KEY_F = 0x46
KEY_G = 0x47
KEY_H = 0x48
KEY_I = 0x49
KEY_J = 0x4A
KEY_K = 0x4B
KEY_L = 0x4C
KEY_M = 0x4D
KEY_N = 0x4E
KEY_O = 0x4F
KEY_P = 0x50
KEY_Q = 0x51
KEY_R = 0x52
KEY_S = 0x53
KEY_T = 0x54
KEY_U = 0x55
KEY_V = 0x56
KEY_W = 0x57
KEY_X = 0x58
KEY_Y = 0x59
KEY_Z = 0x5A

def KeybdInput(code, flags):
	return KEYBDINPUT(code, code, flags, 0, None)

def HardwareInput(message, parameter):
	return HARDWAREINPUT(message & 0xFFFFFFFF,
						 parameter & 0xFFFF,
						 parameter >> 16 & 0xFFFF)

def Mouse(flags, x=0, y=0, data=0):
	return Input(MouseInput(flags, x, y, data))

def Keyboard(code, flags=0):
	return Input(KeybdInput(code, flags))

def Hardware(message, parameter=0):
	return Input(HardwareInput(message, parameter))

################################################################################

import string

UPPER = frozenset('~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?')
LOWER = frozenset("`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./")
ORDER = string.ascii_letters + string.digits + ' \b\r\t'
ALTER = dict(zip('!@#$%^&*()', '1234567890'))
OTHER = {'`': VK_OEM_3,
		 '~': VK_OEM_3,
		 '-': VK_OEM_MINUS,
		 '_': VK_OEM_MINUS,
		 '=': VK_OEM_PLUS,
		 '+': VK_OEM_PLUS,
		 '[': VK_OEM_4,
		 '{': VK_OEM_4,
		 ']': VK_OEM_6,
		 '}': VK_OEM_6,
		 '\\': VK_OEM_5,
		 '|': VK_OEM_5,
		 ';': VK_OEM_1,
		 ':': VK_OEM_1,
		 "'": VK_OEM_7,
		 '"': VK_OEM_7,
		 ',': VK_OEM_COMMA,
		 '<': VK_OEM_COMMA,
		 '.': VK_OEM_PERIOD,
		 '>': VK_OEM_PERIOD,
		 '/': VK_OEM_2,
		 '?': VK_OEM_2}

def keyboard_stream(string):
	mode = False
	for character in string.replace('\r\n', '\r').replace('\n', '\r'):
		#print(character)
		
		if mode and character in LOWER or not mode and character in UPPER:
			yield Keyboard(VK_SHIFT, mode and KEYEVENTF_KEYUP)
			mode = not mode
		character = ALTER.get(character, character)
		if character in ORDER:
			code = ord(character.upper())
		elif character in OTHER:
			code = OTHER[character]
		else:
			continue
			raise ValueError('String is not understood!')
		yield Keyboard(code)
		yield Keyboard(code, KEYEVENTF_KEYUP)
	if mode:
		yield Keyboard(VK_SHIFT, KEYEVENTF_KEYUP)
		
		
def get_hwnds_for_pid ( pid):
	def callback (hwnd, hwnds):
		if win32gui.IsWindowVisible (hwnd) and win32gui.IsWindowEnabled (hwnd):
			_, found_pid = win32process.GetWindowThreadProcessId (hwnd)
			if found_pid == pid:
				hwnds.append (hwnd)
		return True

	hwnds = []
	win32gui.EnumWindows (callback, hwnds)
	#print hwnds
	return hwnds
def send_str( window, q):		
	if 1:
		for event in keyboard_stream(q):
			SendInput(event)
			rv = ctypes.windll.user32.SendInput( event )
			
def OpenCliAndSendPayload(pld,title, pos):
	
	win=open_CLI(title, pos)
	sleep(0.2)
	for i,p in enumerate(pld):
		
		win32gui.SetForegroundWindow(win)
		send_str( win, p)

	return win
	
def open_CLI(title, pos):
	if 1:
		p = Popen(["cmd.exe"],  creationflags=CREATE_NEW_CONSOLE)

	if 1:
		if 1:
			hwnd=None
			while not hwnd:
				hwnd=get_hwnds_for_pid(p.pid)
				#print (hwnd)
			assert hwnd
			win=hwnd[0]
			#print(window1)
			if 0:
				(x,y) = win.GetScreenPosition()
				print('GetScreenPosition: ', x,y)
				(l,w) =win.GetClientSize()
				print ('GetClientSize: ',l,w)
				dl,dw= win.GetSize()
				print ('GetSize:', dl,dw)
			if 1:
				win32gui.SetWindowText(win, title)
				win32gui.SetForegroundWindow(win)
				
				win32gui.MoveWindow(win,*pos , True)	
	return win
	
	
def OpenPutty(path, host, user='bicadmin', pwd='manage', pos=[150, 100, 12000, 800]):
	#client_loc=''
	login=''
	assert host,'Host is not set'
	assert user
	assert pwd
	ts=datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f')
	os.chdir(path)

	my_env = os.environ
	p = Popen(["putty.exe",'%s@%s' % (user, host),'-pw', pwd],  creationflags=CREATE_NEW_CONSOLE)# , #, env=my_env) #stderr=PIPE, stdout=PIPE,	
		


	if 1:
		hwnd=None
		while not hwnd:
			hwnd=get_hwnds_for_pid(p.pid)
			#print (hwnd)
		win=hwnd[0]
	else:
		hwnd = win32api.OpenProcess(
			win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ,
			0,
			p.pid)
			
		win=hwnd
	win32gui.MoveWindow(win,*pos , True)
	return win	

import pywintypes
import win32gui

displays = [[-10,0,980,530],
        [954,0,980,530],
        [-10,515,980,530],
        [954,515,980,530]] #these are the x1,y1,x2,y2 to corner all 4 videos on my res (1920x1080)

def enumHandler(hwnd, lParam):
	if win32gui.IsWindowVisible(hwnd):
		print(win32gui.GetWindowText(hwnd)) #this will print all the processes title
		if 'Putty test' in win32gui.GetWindowText(hwnd): #it checks if the process I'm looking for is running
			print(123)
			win32gui.MoveWindow(hwnd,0,0,300, 800,True) #resizes and moves the process

def callback(hwnd, extra):
	if win32gui.IsWindowVisible(hwnd):
		#print(win32gui.GetWindowText(hwnd)) #this will print all the processes title
		if 'Putty test' in win32gui.GetWindowText(hwnd): #it checks if the process I'm looking for is running
			rect = win32gui.GetWindowRect(hwnd)
			x = rect[0]
			y = rect[1]
			w = rect[2] - x
			h = rect[3] - y
			print ("Window %s:" % win32gui.GetWindowText(hwnd))
			print ("\tLocation: (%d, %d)" % (x, y))
			print ("\t    Size: (%d, %d)" % (w, h))
			
def OpenPuttyAndSendPayload(pld, host, user, pwd, title, pos=[150, 100, 1200, 800]):
	global putty_loc
	win=OpenPutty(putty_loc, host=host, user=user, pwd=pwd, pos=pos)
	#sleep(1)
	

	if 1:
		win32gui.SetWindowText(win, title)
	sleep(1)
	if 1:
		rect = win32gui.GetWindowRect(win)
		x = rect[0]
		y = rect[1]
		w = rect[2] - x
		h = rect[3] - y
		print ("Window %s:" % win32gui.GetWindowText(win))
		print ("\tLocation: (%d, %d)" % (x, y))
		print ("\t    Size: (%d, %d)" % (w, h))
			
	#win32gui.EnumWindows(callback, None) 
	#e(0)	
	win32gui.SetForegroundWindow(win)
	sleep(0.2)
	send_str( win, 'bash\n')
	sleep(0.2)	
	for i,p in enumerate(pld):
		
		#print(i,p)
		#time.sleep(.1)
	
		win32gui.SetForegroundWindow(win)
		send_str( win, p)
		if p.startswith(pwd):
			sleep(1)
	return win,(x, y, w, h)
def OpenApp(dir,pld, pos, title):

	global home
	
	if 1:
		os.chdir(dir)
		p = Popen(["cmd.exe",'/c']+pld,  creationflags=CREATE_NEW_CONSOLE)
		os.chdir(home)
	if 1:
		if 1:
			hwnd=None
			while not hwnd:
				hwnd=get_hwnds_for_pid(p.pid)
				#print (hwnd)
			assert hwnd
			win=hwnd[0]
			#print(window1)
			if 0:
				(x,y) = win.GetScreenPosition()
				print('GetScreenPosition: ', x,y)
				(l,w) =win.GetClientSize()
				print ('GetClientSize: ',l,w)
				dl,dw= win.GetSize()
				print ('GetSize:', dl,dw)
			if 1:
				win32gui.SetWindowText(win, title)
				win32gui.SetForegroundWindow(win)
				
				win32gui.MoveWindow(win,*pos , True)	
			if 1:
				rect = win32gui.GetWindowRect(win)
				x = rect[0]
				y = rect[1]
				w = rect[2] - x
				h = rect[3] - y
				print ("Window %s:" % win32gui.GetWindowText(win))
				print ("\tLocation: (%d, %d)" % (x, y))
				print ("\t    Size: (%d, %d)" % (w, h))
		
	return win, (x, y, w, h)	
def SnapTheApp(putty_rect):
	if 1:
		import wx
		
		print(wx.version())
		app=wx.App()  # Need to create an App instance before doing anything
		dc=wx.Display.GetCount()
		print(dc)
		#e(0)
		displays = (wx.Display(i) for i in range(wx.Display.GetCount()))
		sizes = [display.GetGeometry().GetSize() for display in displays]

		for (i,s) in enumerate(sizes):
			print("Monitor{} size is {}".format(i,s))	
		screen = wx.ScreenDC()
		#pprint(dir(screen))
		size = screen.GetSize()
		
		print("Width = {}".format(size[0]))
		print("Heigh = {}".format(size[1]))

		width=size[0]
		height=size[1]
		x,y,w,h =putty_rect
		print(x,y)
		#e(0)
		bmp = wx.Bitmap(w,h)
		mem = wx.MemoryDC(bmp)
		
		for i in range(98):
			if 1:
				#1-st display:

				#pprint(putty_rect)
				#e(0)
				
				mem.Blit(-x,-y,w+x,h+y, screen, 0,0)
				
			if 0:
				#2-nd display:
				mem.Blit(0, 0, x,y, screen, width,0)
			#e(0)

			if 0:
				#3-rd display:
				mem.Blit(0, 0, width, height, screen, width*2,0)
			
			bmp.SaveFile(os.path.join(home,"image_%s.jpg" % i), wx.BITMAP_TYPE_JPEG)	
			print (i)
			sleep(0.2)
		del mem
		e(0)
if __name__=='__main__':

		
	
	if 1:
		putty_pos=[150, 100, 1200, 800]
		pld=['cd /Bic/home/bicadmin/reporting/utils/pysqr/dly_foma_activity\n', 'sleep 3; time ./nctest.sh\n']
		puttywin, putty_rect1= OpenPuttyAndSendPayload(pld=pld,title='Putty test', user='bicadmin', pwd='bicadmin', host='ny5lsctgbiuniv1', pos=putty_pos)
	sleep(1)
	#Windows app

	#Linux /Putty
	if 1:
		pos=[400, 100, 1200, 800]
		path='C:\\tmp\\cygwin64\\home\\abuzunov\\reporting2\\utils\\aplogr'
		pld=['%s\\python.bat' % path, '%s\\aplogr.py' % path]
		appwin, putty_rect= OpenApp(path, pld,pos, 'aplogr')	




	#Windows CLI
	if 0:
		pos=[150, 100, 1200, 800]
		pld=['cd C:\\tmp\\cygwin64\\home\\abuzunov\\reporting2\\utils\\aplogr\n','python aplogr.py\n']
		cliwin= OpenCliAndSendPayload(pld,'ApLogr', pos)
	sleep(1)	




	if 1:
		SnapTheApp(putty_rect1)


	
	if 0:
		for i in range(1,6):
			posi= pos
			posi[0:2]=[150+i*50, 100+i*50]
			open_CLI(title= 'Test CLI #{}'.format(i), pos=posi)
			