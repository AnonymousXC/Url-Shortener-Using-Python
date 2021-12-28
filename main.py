from tkinter import *
from pyshorteners import Shortener
# from tkinter import filedialog
# import qrcode



def url_shortener():
	"""This Function Shorts URL"""
	global url_input
	url_txt = url_input.get()
	if url_txt:
		short_url = Shortener().tinyurl.short(url_txt)
		if window.clipboard_get():
			window.clipboard_clear()
			window.clipboard_append(short_url)
		output_in.delete(0.0 , END)
		output_in.insert(0.0 , short_url)


# def save_qr():
# 	url = url_input.get()
# 	if url:
# 		qr_code = qrcode.make(url)
# 		file_path = filedialog.asksaveasfilename(filetypes=[('PNG File' , '*.png')])
# 		if file_path:
# 			qr_code.save(file_path)



def widgets(window_name):
	
	guide_label = Label(window_name)
	guide_label.configure(text='Enter URL : ' , background='#282a36' , foreground='#f8f8f2' , pady=10)
	guide_label.pack()

	global url_input 
	url_input = Entry(window_name)
	url_input.configure(width=75 )
	url_input.pack(pady=10)


	global short_btn
	short_btn = Button(window_name)
	short_btn.configure(text='Short Url Using TinyUrl' , command=url_shortener)
	short_btn.pack(pady=20)


	# global qr_btn
	# qr_btn = Button(window_name)
	# qr_btn.configure(text='Save QR Code' , command=save_qr)
	# qr_btn.pack(pady=20)


	guide_label_opt = Label(window_name)
	guide_label_opt.configure(text='Output : ' ,background='#282a36' , foreground='#f8f8f2' )
	guide_label_opt.pack(pady=10)

	global output_in
	output_in = Text(window_name)
	output_in.configure(width= 58 , height=1)
	output_in.pack()





if __name__ == '__main__':
	global window
	window = Tk()
	window.configure(background='#282a36')
	window.title('Url Shortener')
	window.geometry('500x500')
	widgets(window)
	window.mainloop()





