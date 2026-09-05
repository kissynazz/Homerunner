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

while t ==0:
	
#	d=checkSpot(i[1][0],i[1][1],ty)
	#if d>75:
	zz=0
	while zz==0:
		try:
			# 1. Open the file pointer
			with Image.open('Download/ManualScreen/amanualscreenFin.jpeg') as img_file:
				# 2. FIX: Force copy raw pixel bytes into memory right away
				# This detaches the object from the physical Android storage lock
				im3= img_file.copy()
				# 3. Save the decoupled image safely
				print(f"Successfully captured frame: dolphin.jpeg")
				zz=1
				break
				# 4. Wait for the stream file to update
				time.sleep(1)
		except OSError as e:
			# If Android or the stream locks the file, ignore it and try again on the next pass
			print(f"Frame skip: Storage was busy or locked. Retrying...")
			# Roll back index so you don't create empty number gaps
			time.sleep(1)     # Wait a short second before retrying
	
	jh=ismainscreen1(ty,im3)
	#im3= Image.open('dolphin15.jpeg')
							
	#jh=checkSpot(100,1400,'dolphin15.jpeg',im3,[[253, 252, 255], [29, 31, 34]])
	#jh=checkSpot(100,1400,'dolphin15.jpeg',im3,[[253, 252, 255], [29, 31, 34]])
	print('ismainscreen1' ,jh)
	time.sleep(1)
	theindex= -1
	for i in b:
		theindex= theindex+1
		yt=str(i[0])
	#	im3= Image.open(yt)
		#d=checkSpot(i[1][0],i[1][1],yt,im3,i[3])
		d=checkSpot(i[1][0],i[1][1],yt,im3)
		print(d)
		#d=createRange(i[1][0],i[1][1],yt,im3,)
		#b[theindex].append(d)
	#print(b)
#	break
#	jh=ismainscreen1(ty,im3)
#	jh=checkSpot(100,1400,'dolphin15.jpeg',im3,[[253, 252, 255], [29, 31, 34]])
	jh=checkSpot(100,1400,'dolphin15.jpeg',im3)
	print('ismainscreen1' ,jh)
	time.sleep(5)
	if jh>87:
	
		l=0
		
	if jh<70:
		matchindex= -1
		accindex=0
		allunderthirty= 0
		for i in b:
			matchindex= matchindex +1
		#	yt='Download/ManualScreen/'
			yt=str(i[0])
			d=checkSpot(i[1][0],i[1][1],yt,im3)
			if d > allunderthirty:
				allunderthirty= 1
			accuracy=0
			if d >= accuracy:
				
				accuracy=d
				accindex= matchindex
		if allunderthirty==30:
			# gohome clickverse
			filee= open('DCIM/Screenshots/adbcom.txt','w')
			h=h+1
			filee.write('3 '+str(h))
			filee.close()
			fileseq= open('DCIM/Screenshots/lastseq.txt','w+')
			fileseq.write(str(h))
			fileseq.close()
			time.sleep(2)
			filee= open('DCIM/Screenshots/adbcom.txt','w')
					#filee.write('swipe 100 500 900 500  12')
			h=h+1
			filee.write('tap 100 500 '+str(h))
			filee.close()
			fileseq= open('DCIM/Screenshots/lastseq.txt','w+')
			fileseq.write(str(h))
			fileseq.close()
			time.sleep(10)
			break
					
					

		matchindex= -1
		for i in b:
			matchindex= matchindex +1
			
		#	d=checkSpot(i[1][0],i[1][1],yt)
			if d== accuracy:
			#	click str(i[1][0]),str(i[1][1])

				if matchindex== 5 :
					
					
					filee= open('DCIM/Screenshots/adbcom.txt','w')
					h=h+1
					filee.write('3 '+str(h))
					filee.close()
					fileseq= open('DCIM/Screenshots/lastseq.txt','w+')
					fileseq.write(str(h))
					fileseq.close()
					time.sleep(2)
					filee= open('DCIM/Screenshots/adbcom.txt','w')
					#filee.write('swipe 100 500 900 500  12')
					h=h+1
					filee.write('tap 100 500 '+str(h))
					filee.close()
					fileseq= open('DCIM/Screenshots/lastseq.txt','w+')
					fileseq.write(str(h))
					fileseq.close()
					time.sleep(10)
					break
				if matchindex== 8 :
					
					
				
					filee= open('DCIM/Screenshots/adbcom.txt','w')
					h=h+1
					filee.write('3 '+str(h))
					filee.close()
					fileseq= open('DCIM/Screenshots/lastseq.txt','w+')
					fileseq.write(str(h))
					fileseq.close()
					time.sleep(2)
					filee= open('DCIM/Screenshots/adbcom.txt','w')
					#filee.write('swipe 100 500 900 500  12')
					h=h+1
					filee.write('tap 100 500 '+str(h))
					filee.close()
					fileseq= open('DCIM/Screenshots/lastseq.txt','w+')
					fileseq.write(str(h))
					fileseq.close()
					time.sleep(10)
					break
					
				if matchindex!= 5 and matchindex != 8:
					#click
					filee= open('DCIM/Screenshots/adbcom.txt','w')
				#filee.write('swipe 100 500 900 500  12')
			#	filee.write('tap 100 500 '+str(h))
					h=h+1
					#filee.write('tap '+str(970)+' '+str(300)+' '+str(h))
					filee.write('tap '+str(i[1][0])+' '+str(i[1][1])+' '+str(h))
					filee.close()
					fileseq= open('DCIM/Screenshots/lastseq.txt','w+')
					fileseq.write(str(h))
					fileseq.close()
					break
		time.sleep(2)
	#	jh2=ismainscreen1(ty)
		#jh2=checkSpot(100,1400,'dolphin15.jpeg',im3,[[253, 252, 255], [29, 31, 34]])
		jh2=checkSpot(100,1400,'dolphin15.jpeg',im3)
		if jh2 <73:
			#go home
			#verse
			filee= open('DCIM/Screenshots/adbcom.txt','w')
			h=h+1
			filee.write('3 '+str(h))
			filee.close()
			fileseq= open('DCIM/Screenshots/lastseq.txt','w+')
			fileseq.write(str(h))
			fileseq.close()
			time.sleep(2)
			filee= open('DCIM/Screenshots/adbcom.txt','w')
			#filee.write('swipe 100 500 900 500  12')
			h=h+1
			filee.write('tap 100 500 '+str(h))
			filee.close()
			fileseq= open('DCIM/Screenshots/lastseq.txt','w+')
			fileseq.write(str(h))
			fileseq.close()
			time.sleep(10)
			
	if jh>73:
		if gamecount==15:
			t=0
			break
		somei=somei+1
		#if somei ==len(totalrush[firsti])
		if somei== len(totalrush[firsti]):
			somei=0
			gamecount=gamecount+1
			print(gamecount)
			someinc=someinc+10
			#clicks next card then first spot,four times
			filee= open('DCIM/Screenshots/adbcom.txt','w')
		#filee.write('swipe 100 500 900 500  12')
	#	filee.write('tap 100 500 '+str(h))
			h=h+1
			filee.write('tap '+str(970)+' '+str(300)+' '+str(h))
			print('tap '+str(totalrush[1][somei][0])+' '+str(totalrush[1][somei][1])+' '+str(h))
			filee.close()
			fileseq= open('DCIM/Screenshots/lastseq.txt','w+')
			fileseq.write(str(h))
			fileseq.close()
			
			for i in range(0,4):
				filee= open('adbcom.txt','w')
			#filee.write('swipe 100 500 900 500  12')
		#	filee.write('tap 100 500 '+str(h))
				h=h+1
				#filee.write('tap '+str(970)+' '+str(300)+' '+str(h))
				filee.write('tap '+str(totalrush[firsti][2][0])+' '+str(totalrush[firsti][2][1]+someinc)+' '+str(h))
				filee.close()
				
				fileseq= open('DCIM/Screenshots/lastseq.txt','w')
				fileseq.write(str(h))
				fileseq.close()
			
			if someinc ==1000:
				someinc=0
			if firsti== len(totalrush):
				firsti=0
	#	go home open verse
			if startrush==0:
				filee= open('DCIM/Screenshots/adbcom.txt','w')
				h=h+1
				filee.write('3 '+str(h))
				filee.close()
				fileseq= open('DCIM/Screenshots/lastseq.txt','w')
				fileseq.write(str(h))
				fileseq.close()
				time.sleep(2)
				filee= open('DCIM/Screenshots/adbcom.txt','w')
				#filee.write('swipe 100 500 900 500  12')
				h=h+1
				filee.write('tap 100 500 '+str(h))
				filee.close()
				fileseq= open('DCIM/Screenshots/lastseq.txt','w+')
				fileseq.write(str(h))
				fileseq.close()
				time.sleep(10)
				startrush=1
		time.sleep(2)
		filee= open('DCIM/Screenshots/adbcom.txt','w')
		#filee.write('swipe 100 500 900 500  12')
	#	filee.write('tap 100 500 '+str(h))
		h=h+1
		filee.write('tap '+str(totalrush[firsti][somei][0])+' '+str(totalrush[firsti][somei][1]+someinc)+' '+str(h))
		print('tap '+str(totalrush[firsti][somei][0])+' '+str(totalrush[firsti][somei][1]+someinc)+' '+str(h))
		filee.close()
		fileseq= open('DCIM/Screenshots/lastseq.txt','w+')
		fileseq.write(str(h))
		fileseq.close()
	
	
	print('done')
