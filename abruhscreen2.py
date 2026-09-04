
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from PIL import Image
green=(0,255,0)
blue=(0,0,255)
file3=open('isDiff22.py','r')
file33=file3.read()

exec(file33)

print(len(s2compare))
print(len(s2compare[0]))
#
issolitareverse=s2compare[0]
isgamecomplete=s2compare[1]
isnewgame=s2compare[2]
isnewgamedone=s2compare[3]
ismainscreen=s2compare[4]
issolution=s2compare[5]
newgame=s2compare[6]
exit=s2compare[7]
print(len(issolitareverse))





def checkSpotTP(x,y):
	l=0
	im3x = Image.open('imgToCompare.PNG')
	px2x= im3x.load()
	#pix1=px2[k,i]
	beforescreen=[]
	pazcolor =(24, 163, 255)
	for i in range(y-30,y+30):
		#print('they',y)
		for ii in range(x-30,x+30):
			#print('they',i)
			#print('thex',ii)
			beforescreen.append(px2x[k,i])
			im3x.putpixel((ii,i),pazcolor)
			#print(myos)
	#im3x.show()
	#im3x.save('imgToCompare.PNG')
	#gl=input('clicked spot$$$$$$')
	#gl=input('clicked spot&&&&&&&')
	return beforescreen
	
def createRange(x,y,imagename,im3):
	l=0
	im3x = Image.open(str(imagename))
	px2x= im3x.load()
	print('CHECKSPOT XY',x,y)
#	ba=fetchScreen()
#	print('ba',ba)
	
	
	haa= os.listdir('Download/ManualScreen')
	tyy=str('Download/ManualScreen/')+'amanualscreenFin.jpeg'
#	im3= Image.open(str(tyy))
	px2=im3.load()
	#pix1=px2[k,i]
	beforescreen=[]
	afterscreen=[]
	pazcolor =(24, 163, 255)
	range1=0
	range2=0
	range3=0
	for i in range(y-30,y+30):
		#print('they',y)
		for ii in range(x-30,x+30):
			#print('they',i)
			#print('thex',ii)
		#	if px2[ii,i][0]=0 and px2[ii,i][1]=0 and px2[ii,i][2]=0 :
			if px2x[ii,i]==px2[ii,i]:
				beforescreen.append(px2x[ii,i])
			afterscreen.append([px2[ii,i][0],px2[ii,i][1],px2[ii,i][2]])
		#	im3x.putpixel((ii,i),pazcolor)
			#print(myos)
	#im3x.show()
	#gl=input('clicked spot$$$$$$')
	#gl=input('clicked spot&&&&&&&')
	range0=0
	range1=0
	range2=0
	
	range00=255
	range11=255
	range22=255
	grlen=[]
	ci=[65, 117, 58]
	for i in afterscreen:
		
		
		if ci[0]>=i[0] and ci[1]>=i[1] and ci[2]>=i[2]:
			grlen.append(i)
		if i[0]>range0:
			range0=i[0]
		if i[1]>range1:
			range1=i[1]
		if i[2]>range2:
			range2=i[2]
			
		if i[0]<range00:
			range00=i[0]
		if i[1]<range11:
			range11=i[1]
		if i[2]<range22:
			range22=i[2]
	minmax=[[range0,range1,range2],[range00,range11,range22]]
	percentageMatch=len(beforescreen)/len(afterscreen)*100
#	print(percentageMatch)
	return minmax
def checkSpot(x,y,imagename,im3):
	l=0
	im3x = Image.open(str(imagename))
	px2x= im3x.load()
	#print('CHECKSPOT XY',x,y)
#	ba=fetchScreen()
#	print('ba',ba)
	
	
	haa= os.listdir('Download/ManualScreen')
	tyy=str('Download/ManualScreen/')+'amanualscreenFin.jpeg'
#	im3= Image.open(str(tyy))
	px2=im3.load()
	#pix1=px2[k,i]
	beforescreen=[]
	afterscreen=[]
	pazcolor =(24, 163, 255)
	range1=0
	range2=0
	range3=0
	for i in range(y-30,y+30):
		#print('they',y)
		for ii in range(x-30,x+30):
			#print('they',i)
			#print('thex',ii)
		#	if px2[ii,i][0]=0 and px2[ii,i][1]=0 and px2[ii,i][2]=0 :
			
			#ci=therange[0]
			#ci2=therange[1]
			
			if px2x[ii,i]==px2[ii,i]:
				beforescreen.append(px2x[ii,i])
			#elif px2x[ii,i]!=px2[ii,i]:
				#if ci[0]>=px2[ii,i][0] and ci[1]>=px2[ii,i][1] and ci[2]>=px2[ii,i][2] and ci2[0]<=px2[ii,i][0] and ci2[1]<=px2[ii,i][1] and ci2[2]<=px2[ii,i][2]:
					#beforescreen.append(px2x[ii,i])
					#l=0
			
			afterscreen.append(px2[ii,i])
		#	im3x.putpixel((ii,i),pazcolor)
			#print(myos)
	#im3x.show()
	#gl=input('clicked spot$$$$$$')
	#gl=input('clicked spot&&&&&&&')
	percentageMatch=len(beforescreen)/len(afterscreen)*100
#	print(percentageMatch)
	return percentageMatch
def checkSpot2(x,y):
	#afterawait
	afterscreen=[]
	l=0
	#pix1=px2[k,i]
	pazcolor =(24, 163, 255)
	for i in range(y-30,y+30):
		#print('they',y)
		for ii in range(x-30,x+30):
			#print('they',i)
			#print('thex',ii)
			afterscreen.append(px2[ii,i])
			
			#im3.putpixel((ii,i),pazcolor)
	#im3.show()
	return afterscreen
#gl=input('clicked spot$$$$$$')
#totalXiYi=[[40,555],[195,595],[350,630],[505,670],[655,705],[810,740],[970,780]]

def checkSpotWide(x,y,px2,im3):
	l=0
	#im3x = Image.open('Screenshot_20250920-164548.PNG')
	#im3x = Image.open('Screenshot_20251003-112058.png')
	
	#px2x= im3x.load()
	#pix1=px2[k,i]
	beforescreen=[]
	pazcolor =(24, 163, 255)
	ye=(255,255,0)
	for i in range(y-30,y+1200):
		#print('they',y)
		for ii in range(x-30,x+110):
			#print('they',i)
			#print('thex',ii)
			k=ii
			i=i
			if px2[k,i][0]> 195 and px2[k,i][1]> 195 and px2[k,i][2]> 195:
				l=0
				#im3.putpixel((ii,i),ye)
				beforescreen.append(ye)
			else:
				
				beforescreen.append(pazcolor)
				#im3.putpixel((ii,i),pazcolor)
			#print(myos)
	#im3.show()
	#gl=input('clicked spot$$$$$$')
	#gl=input('clicked spot&&&&&&&')
	return beforescreen
	
def checkSpotWideAce(x,y,px2,im3):
	l=0
	
	#im3x = Image.open('Screenshot_20250920-164548.PNG')
	#im3x = Image.open('Screenshot_20251003-112105.png')
	#px2x= im3x.load()
	#pix1=px2[k,i]
	beforescreen=[]
	ye= (255,255,0)
	pazcolor =(24, 163, 255)
	for i in range(y-30,y+70):
		#print('they',y)
		for ii in range(x-30,x+50):
			k=ii
			i=i
			if px2[k,i][0]> 195 and px2[k,i][1]> 195 and px2[k,i][2]> 195:
				l=0
				#im3.putpixel((ii,i),ye)
				beforescreen.append(ye)
			else:
				
				beforescreen.append(pazcolor)
				#im3.putpixel((ii,i),pazcolor)
#	im3.show()
	#gl=input('clicked spot$$$$$$')
	#gl=input('clicked spot&&&&&&&')
	return beforescreen


def ismainscreen1(ba,im6):
	ismainscreen2=[]
	print('ba IN MAINSCREEN',ba)
	fileAA=open('functionsKeyframe.py','r')
	fileR= fileAA.read()
	#exec(fileR)
	functionsKeyframe=[]
	functionsKeyframe.append(['ismainscreen1',str(ba),'checks if mainscreen'])
	fileAAA=open('functionsKeyframe.py','w')
	fileAAA.write('functionsKeyframe='+str(functionsKeyframe))
	fileAA.close()
#	gl=input('ba IN MAINSCREEN')
#	'Screenshot_20251003-112058.png'
# 'Screenshot_20251003-112058.png'
#	im3= Image.open(str(ba))
	#im3= Image.open('Screenshot_20251215-061255.png')
	#im3= Image.open('Screenshot_20251003-112058.png')# match that works above doesnt
	#im3= Image.open('Screenshot_20251215-113936.PNG')



	
	        
	
        
    
	
	ty='Download/ManualScreen/'+'amanualscreenFin.JPEG'
	#im6= Image.open(str(ty))
	
	px5= im6.load()
#	im66 = Image.open('Screenshot_20251215-113936_1.PNG')
	im66 = Image.open('Screenshot_20260821_194254_Solitaire Verse.jpg')
#	im66= Image.open(str(ty))
	px55= im66.load()
	
	#px2=im3.load()
	for es in ismainscreen:
		k=es[0]
		i=es[1]
		#print(k,i)
		#gl=input('')
		#im33.putpixel((k,i),blue)
		pix1=px5[k,i]
	#	pix11=px00[k,i]
	#	pix2=px3[k,i]
	#	pix2=px2[k,i]
	#	pix22=px33[k,i]
	#	pix3=px4[k,i]
	#	pix3=px2[k,i]
	#	pix33=px44[k,i]
		pix4=px5[k,i]
	#	pix4=px2[k,i]
		pix44=px55[k,i]
		#pix5=px6[k,i]
		#pix5=px2[k,i]
	#	pix55=px66[k,i]
	#	pix6=px7[k,i]
	#	pix6=px2[k,i]
	#	pix66=px77[k,i]
		xi=600
		yi=1950
		if k>xi-700 and k<xi+700 and i>yi-200 and i<yi+100:
			green=(0,255,0)
			#im66.putpixel((k,i),green)
		a=0
		b=0
		if px55[k,i][0]> 195 and px55[k,i][1]> 195:
			l=0
			green=(0,255,0)
			blue=(0,0,255)
			
			a=1
		#if px2[k,i] == px2[k,i]:
			#l=0
		#else:
		if px5[k,i][0]> 195 and px5[k,i][1]> 195:
			green=(0,255,0)
			blue=(0,0,255)
			#im3.putpixel((k,i),pix1)
			#gl=input('huh')
			b=1
		#if a==1 and b==0:
		if  b==0:
			green=(0,255,0)
			
			#im66.putpixel((k,i),green)
			#diff.append([k,i])
			#%diff.append(pix1)
			#if con
			xi=600
			yi=1950
			if k>xi-700 and k<xi+700 and i>yi-500 and i<yi+100:
				green=(0,255,0)
				blue=(0,0,255)
			#	im66.putpixel((k,i),blue)
				#ismainscreen2.append([k,i])
				pix1=px55[k,i]
				pix0=px5[k,i]
				if pix1 == pix0:
				#	im33.putpixel((k,i),green)
					ismainscreen2.append([k,i])
			#diff1.append(pix11) blue
	percentageMatch=len(ismainscreen2)/len(ismainscreen)*100
	print('LEN MAIN2 AND MAIN1',len(ismainscreen2),len(ismainscreen))
	print(percentageMatch,'percentage mwtch')
#	gl=input('percentage match')
	return percentageMatch



def ismulitplemainscreen1(ba,im6):
	ismainscreen2=[]
	print('ba IN MAINSCREEN',ba)
	fileAA=open('functionsKeyframe.py','r')
	fileR= fileAA.read()
	#exec(fileR)
	functionsKeyframe=[]
	functionsKeyframe.append(['ismainscreen1',str(ba),'checks if mainscreen'])
	fileAAA=open('functionsKeyframe.py','w')
	fileAAA.write('functionsKeyframe='+str(functionsKeyframe))
	fileAA.close()
#	gl=input('ba IN MAINSCREEN')
#	'Screenshot_20251003-112058.png'
# 'Screenshot_20251003-112058.png'
#	im3= Image.open(str(ba))
	#im3= Image.open('Screenshot_20251215-061255.png')
	#im3= Image.open('Screenshot_20251003-112058.png')# match that works above doesnt
	#im3= Image.open('Screenshot_20251215-113936.PNG')



	
	        
	
        
    
	
	ty='Download/ManualScreen/'+'amanualscreenFin.JPEG'
	#im6= Image.open(str(ty))
	
	px5= im6.load()
#	im66 = Image.open('Screenshot_20251215-113936_1.PNG')
	im66 = Image.open('Screenshot_20260821_194254_Solitaire Verse.jpg')
#	im66= Image.open(str(ty))
	px55= im66.load()
	
	#px2=im3.load()
	for es in ismainscreen:
		k=es[0]
		i=es[1]
		#print(k,i)
		#gl=input('')
		#im33.putpixel((k,i),blue)
		pix1=px5[k,i]
	#	pix11=px00[k,i]
	#	pix2=px3[k,i]
	#	pix2=px2[k,i]
	#	pix22=px33[k,i]
	#	pix3=px4[k,i]
	#	pix3=px2[k,i]
	#	pix33=px44[k,i]
		pix4=px5[k,i]
	#	pix4=px2[k,i]
		pix44=px55[k,i]
		#pix5=px6[k,i]
		#pix5=px2[k,i]
	#	pix55=px66[k,i]
	#	pix6=px7[k,i]
	#	pix6=px2[k,i]
	#	pix66=px77[k,i]
		xi=600
		yi=1950
		if k>xi-700 and k<xi+700 and i>yi-200 and i<yi+100:
			green=(0,255,0)
			#im66.putpixel((k,i),green)
		a=0
		b=0
		if px55[k,i][0]> 195 and px55[k,i][1]> 195:
			l=0
			green=(0,255,0)
			blue=(0,0,255)
			
			a=1
		#if px2[k,i] == px2[k,i]:
			#l=0
		#else:
		if px5[k,i][0]> 195 and px5[k,i][1]> 195:
			green=(0,255,0)
			blue=(0,0,255)
			#im3.putpixel((k,i),pix1)
			#gl=input('huh')
			b=1
		#if a==1 and b==0:
		if  b==0:
			green=(0,255,0)
			
			#im66.putpixel((k,i),green)
			#diff.append([k,i])
			#%diff.append(pix1)
			#if con
			xi=600
			yi=1950
			if k>xi-700 and k<xi+700 and i>yi-500 and i<yi+100:
				green=(0,255,0)
				blue=(0,0,255)
			#	im66.putpixel((k,i),blue)
				#ismainscreen2.append([k,i])
				pix1=px55[k,i]
				pix0=px5[k,i]
				if pix1 == pix0:
				#	im33.putpixel((k,i),green)
					ismainscreen2.append([k,i])
			#diff1.append(pix11) blue
	percentageMatch=len(ismainscreen2)/len(ismainscreen)*100
	print('LEN MAIN2 AND MAIN1',len(ismainscreen2),len(ismainscreen))
	print(percentageMatch,'percentage mwtch')
#	gl=input('percentage match')
	return percentageMatch

b=[['Screenshot_20260822_122608_Solitaire Verse.jpg',[997,190]],
['Screenshot_20260823_141708_JustPlay.jpg',[960,380]],
['Screenshot_20260822_121758_Solitaire Verse.jpg',[1010,170]],

['Screenshot_20260822_121741_Solitaire Verse.jpg',[600,1900]],

['Screenshot_20260822_121647_Solitaire Verse.jpg',[600,1900]],

['Screenshot_20260822_121043_Google Play Store.jpg',[600,1900]],
['Screenshot_20260822_121637_Solitaire Verse.jpg',[997,220]],
['Screenshot_20260822_121129_Solitaire Verse.jpg',[1010,150]],

['Screenshot_20260822_121043_Google Play Store.jpg',[1010,150]]]

ty='Download/ManualScreen/'+'amanualscreenFin.jpeg'

user = 'nazzyburpee0@gmail.com'
password = 'qntc kxxr wybp bdng'


def send_text(message, to=None):
    """Send a plain text message."""
    if to is None:
        to = user
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(user, password)
    s.sendmail(user, to, message)
    s.quit()
    print('Text message sent.')


def send_file(filepath, to=None, subject='File', body=''):
    """Send any file as a bytes attachment (images, text, etc.)."""
    if to is None:
        to = user

    filename = os.path.basename(filepath)

    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Read the file as raw bytes and attach it
    with open(filepath, 'rb') as f:
        file_bytes = f.read()

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(file_bytes)
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="{filename}"')
    msg.attach(part)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(user, password)
    s.sendmail(user, to, msg.as_string())
    s.quit()
    print(f'File sent: {filename}')
import time
def fetchScreen22():
	ut=1
	done=0
	#gl=input('fetchScreen')
	#import pygame

	while ut ==1:
		
		isready=open('isready.py','w')
		isready.write('7')
		time.sleep(3)
		
		
		res=0
		gl=input('was fetch')
		ba=AwaitNewScreen()
		px2save=open('savedpx2.py','w')
		px2save.write('savedpx2='+"'"+str(ba)+"'")
		print('ba222',ba)
		from PIL import Image

		img = Image.open(str(ba))
		original_width, original_height = img.size
		
		print(img.size)
		
		new_width = 1080 # Desired new width
		aspect_ratio = original_height / original_width
		#new_height = int(new_width * aspect_ratio)
		new_height = 2400
		
		resized_img = img.resize((new_width, new_height))
		resized_img.save("toedit2.png")


		###resuze
		im3= Image.open(str(ba))
		im3.save('screenToAppear22.png')
		#ball2 = pygame.image.load("screenToAppear22.png")
		#ball = pygame.image.load("Ashketchem2.png")
		
		px2=im3.load()
		done=ismainscreen1(ba)
		#print('was fetchdone',done)
		print(done)
		gl=input('was fetchdone')
		
		isready=open('isready.py','w')
		isready.write('22')
		isready.close()
	#	gl=input('checked mainscreeen')
		if done > 75:
			ut=0
			res=1
		#	gl=input('is main')
			print(ut)
			#gl=input('is mainscreen,check spot,if different, we moved if the same, numbers didnt match')
			print('is mainscreen,check spot,if different, we moved if the same, numbers didnt match')
		elif done < 75:    
			l=0
			print(ut)
		#	gl=input('isnt main')
			isready=open('isready.py','w')
			isready.write('3')#go home , reopen in adb

			#gl=input('didnt match 4')
			time.sleep(3)
			isready=open('isready.py','w')
			isready.write('22')
			print('didnt match 4')
			print('isnt main screen 4')
			print('done',done)
			ut=1
	return res,ba

def fetchScreen():
	ut=1
	done=0
	#gl=input('fetchScreen')
	#import pygame

	while ut ==1:
		
		isready=open('isready.py','w')
		isready.write('7')
		time.sleep(3)
		
		
		res=0
		gl=input('was fetch')
		ba=AwaitNewScreen()
		from PIL import Image

		img = Image.open(str(ba))
		original_width, original_height = img.size
		
		print(img.size)
		
		new_width = 1080 # Desired new width
		aspect_ratio = original_height / original_width
		#new_height = int(new_width * aspect_ratio)
		new_height = 2400
		
		resized_img = img.resize((new_width, new_height))
		#resized_img.save("toedit2.png")
		resized_img.save(str(ba))


		###resuze
		im3= Image.open('edited'+str(ba))
		im3.save('screenToAppear22.png')
		#ball2 = pygame.image.load("screenToAppear22.png")
		#ball = pygame.image.load("Ashketchem2.png")
		ba='edited'+str(ba)
		px2=im3.load()
		done=ismainscreen1(ba)
		#print('was fetchdone',done)
		print(done)
		gl=input('was fetchdone')
		px2save=open('savedpx2.py','w')
		px2save.write('savedpx2='+"'"+str(ba)+"'")
		print('ba222',ba)
		im3= Image.open(str(ba))
		im3.save('screenToAppear22.png')
		#ball2 = pygame.image.load("screenToAppear22.png")
		#ball = pygame.image.load("Ashketchem2.png")
		
		px2=im3.load()
		#done=ismainscreen1(ba)
		done=70
		#print('was fetchdone',done)
		print(done)
		gl=input('was fetchdone')
		
		isready=open('isready.py','w')
		isready.write('22')
		isready.close()
	#	gl=input('checked mainscreeen')
		if done > 75:
			ut=0
			res=1
		#	gl=input('is main')
			print(ut)
			#gl=input('is mainscreen,check spot,if different, we moved if the same, numbers didnt match')
			print('is mainscreen,check spot,if different, we moved if the same, numbers didnt match')
		elif done < 75:
			fileseq= open('lastseq.txt','r')
			fileseqr=fileseq.read()
			h=int(fileseqr) 
			utt=1
			while utt==1: 
				l=0
				print(ut)
				h=h+1
				isready=open('isready.py','w')
				filee= open('adbcom.txt','w')
				filee.write('3 '+h)
				filee.close()
				h=h+1
				filee= open('adbcom.txt','w')
				#filee.write('swipe 100 500 900 500  12')
				filee.write('tap 100 500 '+str(h))
				filee.close()
				fileseq= open('lastseq.txt','w+')
				fileseq.write(str(h))
				fileseq.close()
				isready.write('3')#go home , reopen in adb
				#gl=input('didnt match 4')
				time.sleep(3)
				isready=open('isready.py','w')
				isready.write('22')
				print('didnt match 4')
				print('isnt main screen 4')
				print('done',done)
				b = os.listdir()
				bbb=b
				bb=os.listdir()
				vc2 = bb 
				ut=0
				#gen=
				print('bee length',len(b))
				while ut < 30:
					ut=ut+1
					#30 pics
					isready.write(str(7))
					im3xpic = Image.open('Screenshot_test.PNG')
					im3xpic.save('Screenshot_test'+str(ut)+'.png')
					time.sleep(1)
					isready.write(str(70))
					print('did screenshot',ut,'Screenshot_test'+str(ut)+'.png')
				g2=[]
				gg=[]
				gg2=[]
				g2.append(len(b))
				b = os.listdir()
				print('dir2',len(b))
				#genScreenshot()
				#gets pics that are not taken yet which should be 30
				
				if len(b)>g2[len(g2)-1]:
					for h in b:
						if h not in vc2:
							gg2.append(h)
				print('gg2',len(gg2))
				gl=input('did we get 30?')
				if len(gg2)/2 != 0:
					ba= AwaitNewScreen()
					gg2.append(str(ba))
			#	get last two
				pic0= -1
				pic1= 0
				for i in gg2:
					pic0=pic0+1
					pic1=pic1+1
				#if last two equal
					im3= Image.open(str(gg2[pic0]))
					px2=im3.load()
					im33= Image.open(str(gg2[pic1]))
					px22=im33.load()
					#if gg2[pic0]==gg2[pic1]:
					if px2==px22:
						l=0
					if px2!=px22:
						l=0
						hj=0
						while hj==0:
							if px2[k,i]!= px22[k,i]:
								#pointstoclick.append(px22[k,i])
								#pointstoclick.append([k,i])
								if px22[k,i][0]>250 and px22[k,i][1]>250 and px22[k,i][2]>250:# is white pixel
									pointstoclick.append([k,i,px22[k,i]])
					#if gg2[len(gg2)-1]==gg2[len(gg2)-1]:
						#l=0
						
				#open photos	
				thefirstpic=Image.open(str(gg2[len(gg2)-1]))
				thesecondpic=Image.open(str(gg2[len(gg2)-2]))
				#if gg2[len(gg2)-1]!=gg2[len(gg2)-2]:
				if thefirstpic!=thesecondpic:
				
					ttu= 1
					while	ttu==1:
						#stillnot mainscreen 
						#ba=AwaitNewScreen()
						im3= Image.open(str(gg2[len(gg2)-1]))
						px2=im3.load()
						done=ismainscreen1(str(gg2[len(gg2)-1]))
						ba=AwaitNewScreen()
						gg2.append(str(ba))
						im33= Image.open(str(ba))
						px22=im33.load()
						done=ismainscreen1(ba)
						
						#if px2==gg2[len(gg2)-1]:
						if px2==px22:
							ttu=0
							break
				#if gg2[len(gg2)-1]==gg2[len(gg2)-1]:
				#else:
					#for i in last pic if greater than 245 and in pointstoclick:
							#click
					
					
					
				#ba=AwaitNewScreen()
			#	im3= Image.open(str(ba))
				#px2=im3.load()
				#done=ismainscreen1(ba)
			#	ba2=AwaitNewScreen()
				#im3= Image.open(str(ba))
				#px2=im3.load()
				#done=ismainscreen1(ba)
				lg=0
				#could do another while to check for pixels that are white and in pointsthatchanged
				while lg==0:
					#this does just white
					t=0
					k = 0
					i = -1
					while t==0:
						#thea.append()
						#theb.append
						if int(i) == im3.size[1]-1:
							#if int(i) == 1000-1:
								i=0
								k=k+1
								start=0
								#if k == 1079:
						if k == im3.size[0]-1:
							break #remove break so it keeps going
							k=0
							i=0
							
						if px22[k,i][0]>250 and px22[k,i][1]>250 and px22[k,i][2]>250:# is white pixel
							for p in pointstoclick:
								if p[0]==k and p[1]==i and p[2][0] > 250 and p[2][1] > 250 and p[2][2] > 250:
									#click 
									#go home
									#reopen solitare verse
									ba=AwaitNewScreen()
									gg2.append(str(ba))
									im3= Image.open(str(ba))
									px2=im3.load()
									done=ismainscreen1(ba)
									if done >75:
										break
										lg=1
							#click 
							#go home
							#reopen solitare verse
							ba=AwaitNewScreen()
							gg2.append(str(ba))
							im3= Image.open(str(ba))
							px2=im3.load()
							done=ismainscreen1(ba)
							if done >75:
								break
								lg=1
								utt=0
								ut=0
					for r in gg2:
						del r
			
	return res,ba
def AwaitNewScreen():

    import os
    #import clipboard
  #  gl=input('await')
    #print(os.listdir())
    
     
    #import pyclip
    #
    #import pyperclip
    
    #import kk
    
    
    #pyclip.copy('abc')
    
    b = os.listdir()
    u=0
    #if manualclipboard// listdi is54321 ready u is 0
    #filehj=open("listDi.py","r")
    #manualclipboard=filehj.read()
    
    st=0
    c = os.listdir()
    vc=c
    gg=[]
    fileseq= open('DCIM/Screenshots/lastseq.txt','r')
    fileseqr=fileseq.read()
    h=int(fileseqr) 
    #im3xpic = Image.open('Screenshot_20251117-162427.PNG')
    #ourxy()
    while u==0:
        h= h+1
        filee= open('DCIM/Screenshots/adbcom.txt','w')
        filee.write('7 '+h)
        filee.close()
        g=[]
        g.append(len(b))
       # print('yes')
        #print(g[len(g)-1])
    
        print('dir2',len(b))
        b = os.listdir()
        #genScreenshot(len(b))
        #im3xpic = Image.open('Screenshot_test.PNG')
        #im3xpic.save('Screenshot_test'+str(len(b)+1)+'.png')
        if len(b)>g[len(g)-1] :
            #print(b[len(b)-1])
            for h in b:
                if h not in vc:
                    gg.append(h)
            if "pending" not in gg[len(gg)-1]:
                #px2= that
                print('we can click random point until we cant or pop up')
                print("new screen miclarkfinal",gg[len(gg)-1],len(vc),len(b))
                u=1
                break
                
                
                
            
     
    
    print('done Await screen')
    return gg[len(gg)-1]
    
def PygameNewScreen():

    import os
   # import clipboard
    #gl=input('await')
    #print(os.listdir())
    
     
    #import pyclip
    #
    #import pyperclip
    
    #import kk
    
    
    #pyclip.copy('abc')
    b = os.listdir()
    u=0
    #if manualclipboard// listdi is54321 ready u is 0
    #filehj=open("listDi.py","r")
    #manualclipboard=filehj.read()
    
    st=0
    c = os.listdir()
    vc=c
    gg=[]
    xfile=open('xfile.py','r')
    yfile=open('yfile.py','r')
    ballposx=xfile.read()
    ballposy=yfile.read()
    while u==0:
    
        g=[]
        g.append(len(b))
       # if int(ballposx)!= ballrect2.left and int(ballposy)!= ballrect2.top:
        if ballrect2.left < int(ballposx) :
        #speed2[0] = speed2[0]+speed2[0]
            ballrect2 = ballrect2.move(speed0)
            l=0
        
        if ballrect2.left > int(ballposx) :
        #speed2[0] = speed2[0]+speed2[0]
            ballrect2 = ballrect2.move(speed00)
            l=0
        if ballrect2.top < int(ballposy):
            ballrect2 = ballrect2.move(speed1)
        if ballrect2.top > int(ballposy):
            ballrect2 = ballrect2.move(speed11)
       # print('yes')
        #print(g[len(g)-1])
    
        print('dir2',len(b))
        b = os.listdir()
        if len(b)>g[len(g)-1] :
            #print(b[len(b)-1])
            for h in b:
                if h not in vc:
                    gg.append(h)
            if "pending" not in gg[len(gg)-1]:
                #px2= that
                print('we can click random point until we cant or pop up')
                print("new screen miclarkfinal",gg[len(gg)-1],len(vc),len(b))
                u=1
                break
                
                
                
            
     
    
    print('done Await screen')
    return gg[len(gg)-1]



print('dine')

xi,yi=200, 565
xi,yi=360, 565
xi,yi=520, 565
xi,yi=690, 565
xi,yi=820, 565
xi,yi=970, 565
xi,yi=30, 566
xi,yi=30, 300
xi,yi=820, 300
xi,yi=725, 300
xi,yi=970, 300
xi,yi=970, 1800
xi,yi=970, 300

xi,yi=200, 565
xi,yi=360, 565
xi,yi=520, 565
xi,yi=690, 565
xi,yi=820, 565
xi,yi=970, 565
xi,yi=30, 566

xi,yi=970, 300
xi,yi=970, 1800
xi,yi=725, 300
xi,yi=655, 300

xiyi=[[30, 566],[200, 565],[360, 565],[520, 565],[690, 565],[820, 565],[970, 565]]
xiyiaces=[]
xiyiupper=[[655, 300],[725, 300],[725, 300]]

nextcard=[970, 300]
t=0
fileseq= open('DCIM/Screenshots/lastseq.txt','r')
fileseqr=fileseq.read()
h=int(fileseqr)
startrush=2
somei= -1
totalrush=[xiyi,xiyiupper]
firsti=0
someinc=0
import time
gamecount=0
#time.sleep(5)
import os

hh= os.listdir('Download/ManualScreen')
#print(h)
b=[['Screenshot_20260822_122608_Solitaire Verse.jpg', [997, 190], [30, 30]], ['Screenshot_20260823_141708_JustPlay.jpg', [960, 380], [30, 30]], ['Screenshot_20260822_121758_Solitaire Verse.jpg', [1010, 170], [30, 30]], ['Screenshot_20260822_121741_Solitaire Verse.jpg', [600, 1900], [30, 30]], ['Screenshot_20260822_121647_Solitaire Verse.jpg', [600, 1900], [30, 30]], ['Screenshot_20260822_121043_Google Play Store.jpg', [600, 1900], [30, 30]], ['Screenshot_20260822_121637_Solitaire Verse.jpg', [997, 220], [30, 30]], ['Screenshot_20260822_121129_Solitaire Verse.jpg', [1010, 150], [30, 30]], ['Screenshot_20260822_121043_Google Play Store.jpg', [1010, 150], [30, 30]]]

b=[['Screenshot_20260822_122608_Solitaire Verse.jpg', [997, 190], [30, 30], [[253, 252, 255], [29, 31, 34]]], ['Screenshot_20260823_141708_JustPlay.jpg', [960, 380], [30, 30], [[193, 189, 194], [22, 15, 23]]], ['Screenshot_20260822_121758_Solitaire Verse.jpg', [1010, 170], [30, 30], [[253, 252, 254], [30, 31, 35]]], ['Screenshot_20260822_121741_Solitaire Verse.jpg', [600, 1900], [30, 30], [[255, 255, 255], [117, 82, 6]]], ['Screenshot_20260822_121647_Solitaire Verse.jpg', [600, 1900], [30, 30], [[8, 2, 9], [0, 0, 0]]], ['Screenshot_20260822_121043_Google Play Store.jpg', [600, 1900], [30, 30], [[227, 228, 230], [6, 7, 4]]], ['Screenshot_20260822_121637_Solitaire Verse.jpg', [997, 220], [30, 30], [[255, 255, 255], [29, 29, 29]]], ['Screenshot_20260822_121129_Solitaire Verse.jpg', [1010, 150], [30, 30], [[255, 255, 255], [16, 111, 172]]], ['Screenshot_20260822_121043_Google Play Store.jpg', [1010, 150], [30, 30], [[67, 50, 34], [4, 6, 6]]]]
ty='Download/ManualScreen/'+'amanualscreenFin.jpeg'
ty=('Screenshot_20260903_125709_Solitaire Verse.jpg')

print('did')
temp=[]
while t ==0:
	
#	d=checkSpot(i[1][0],i[1][1],ty)
	#if d>75:
	zz=0
	index=-1
	
	while zz==0:
		index = index + 1
		try:
			# 1. Open the file pointer
			with Image.open('Download/ManualScreen/amanualscreenFin.jpeg') as img_file:
				# 2. FIX: Force copy raw pixel bytes into memory right away
				# This detaches the object from the physical Android storage lock
				im3= img_file.copy()
				wasgreat=0
				jh=checkSpot(100,1400,'dolphin15.jpeg',im3)
				
				temp.append(im3)
				#print(f"thirthy",len(temp))
				
				if len(temp)==30:
					#print(f"saving thirty")
					time.sleep(2)
					index2= len(os.listdir('Inter2/'))
					for i in temp:
						index2= index2 +1
					#	i.save(f'Inter2/dolphin{index2}.jpeg')
						#print(f"Successfully captured frame: dolphin.jpeg")
				#	temp=[]
					#zz=1
				#	t=1
					#break
				if jh>70:
					wasgreat=1
				#for i in b:
					#yt=str(i[0])
				#	d=checkSpot(i[1][0],i[1][1],yt,im3)
				#	if d>70:
						#wasgreat=1
						
				#if wasgreat==0:
					#im3.save(f'Inter/dolphin{index}.jpeg')
			
				# 3. Save the decoupled image safely
				
				zz=1
				break
				# 4. Wait for the stream file to update
				time.sleep(1)
		except OSError as e:
			# If Android or the stream locks the file, ignore it and try again on the next pass
			#print(f"Frame skip: Storage was busy or locked. Retrying...")
			# Roll back index so you don't create empty number gaps
			time.sleep(1)     # Wait a short second before retrying
	
	