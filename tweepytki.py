import tkinter
import tweepy



window = tkinter.Tk()


def tweetle():


	auth = tweepy.OAuthHandler(costumer_key, costumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	file = open("helloworld.txt", 'r')
	f = file.read()
	file.close()

	api.update_status(status=f)
	lbl.configure(text="Tweet Gönderildi.")


def alinantweet():
	il= giris.get()
	yazi.config(text="Girdiğiniz tweet: %s" % il)
	file = open("helloworld.txt", "a")

	file.write(il)
	file.write("\n")
	file.close()


yazi = tkinter.Label(window)
yazi.config(text="Buraya girilen tweet gelecek.")
yazi.pack()

giris = tkinter.Entry(window, bd=5)
giris.pack()

buton = tkinter.Button(window)
buton.config(text="Kaydet", command=alinantweet)
buton.config(command=alinantweet)
buton.pack()

button = tkinter.Button(window, text="Tweetlemek için bu tuşa basın", command=tweetle)
button.pack()

lbl = tkinter.Label(window, text="Tweet henüz gönderilmedi ...")
lbl.pack()


def kullanici():
	auth = tweepy.OAuthHandler(costumer_key, costumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	kullanıcı = entrykullanıcı.get()
	if kullanıcı == " ":
		err.config(window , text = "Kullanıcı Adı girilmedi.")
	else:



		user = api.get_user(kullanıcı)

		yazi1.config(text="Kullanıcı Adı : " + user.name)
		yazi2.config(text="Açıklama : " + user.description)
		yazi3.config(text="Lokasyon : " + user.location)
		yazi4.config(text="Time Zone : " + str(user.time_zone))
		yazi5.config(text="Takip Edilen : " + str(user.friends_count))
		yazi6.config(text="Takipçiler : " + str(user.followers_count))
		yazi7.config(text="Tweet Sayısı :" + str(user.statuses_count))
		yazi8.config(text="Favori Sayısı : " + str(user.favourites_count))
		yazi9.config(text="URL : " + str(user.url))
		yazi10.config(text="Created : " + str(user.created_at))


label = tkinter.Label(window, text="Kullanıcı ismini girin.")
entrykullanıcı = tkinter.Entry(window, bd=5)



label.pack()
entrykullanıcı.pack()
button1 = tkinter.Button(window, text="Bilgileri için bu tuşa basınız", command=kullanici)
button1.pack()

err  = tkinter.Label(window , text = "Kullanıcı Adı girin")
err.config(text = "")
err.pack()

yazi1 = tkinter.Label(window, text="Kullanıcı Adı :")
yazi1.config(text="Kullanıcı Adı")
yazi1.pack()

yazi2 = tkinter.Label(window, text="Açıklama : ")
yazi2.config(text="Açıklama :")
yazi2.pack()

yazi3 = tkinter.Label(window, text="Lokasyon : ")
yazi3.config(text="Lokasyon :")
yazi3.pack()

yazi4 = tkinter.Label(window, text="Time Zone :")
yazi4.config(text="Time Zone : ")
yazi4.pack()

yazi5 = tkinter.Label(window, text="Takip Edilen : ")
yazi5.config(text="Takip Edilen : ")
yazi5.pack()

yazi6 = tkinter.Label(window, text="Takipçiler : ")
yazi6.config(text="Takipçiler :")
yazi6.pack()

yazi7 = tkinter.Label(window, text="Tweet Sayısı : ")
yazi7.config(text="Tweet Sayısı : ")
yazi7.pack()

yazi8 = tkinter.Label(window, text="Favori Sayısı : ")
yazi8.config(text="Favori Sayısı : ")
yazi8.pack()

yazi9 = tkinter.Label(window, text="URL : ")
yazi9.config(text="URL :")
yazi9.pack()

yazi10 = tkinter.Label(window, text="Created : ")
yazi10.config(text="Created :")
yazi10.pack()







window.geometry("400x500")

window.mainloop()
