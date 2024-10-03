from tkinter import *
from tkintermapview import TkinterMapView

root = Tk()

root.geometry('880x450') ## Width , hight
root.title('Rakwan[الصيدليات المناوبة]')
root.iconbitmap('icon.ico')
root.configure(background='white')

def determineLocation(latitude, longitude, marker_text):
    map=TkinterMapView(root,width=450,height=400,corner_radius=0)
    map.place(x=400,y=45)
    map.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png", max_zoom=19)
    map.set_position(latitude, longitude)
    map.set_zoom(15)
    marker=map.set_marker(latitude, longitude)
    marker.set_text(marker_text)

def cu():
    country=En.get()
    map.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png", max_zoom=19)
    map.set_address(country,marker=True)

#===== Title ======
title1=Label(
    root,
    text='مشروع صيدليات المناوبة',
    fg='white',
    background='black',
    font=('Tajawal',18),
    )
title1.pack(fill=X)

#===== Logo =====
logo=PhotoImage(file='medicine.png')
lab_log=Label(root,image=logo,bd=0,bg='white')
lab_log.place(x=30,y=40)

#==== Label =====
labl=Label(
    root,
    text='Country : ',
    fg='black',
    background='white',
    font=('Tajawal',16))
labl.place(x=10,y=200)

#==== Entry =====
En =Entry(
    root,
    font=('Tajawal',14),
    width=10,
    bd=2,
    relief=GROOVE)
En.place(x=120,y=203)

#==== Button =====
btn=Button(
    root,
    text='Get country',
    font=('Tajawal',10),
    bg='black',
    fg='white',
    bd=1,
    relief=SOLID,
    width=10,cursor='hand2',command=cu)
btn.place(x=250,y=203)

#===== Pharmacy Buttons =====

b=Button(
    root,
    text='صيدلية مركزية',
    cursor='hand2',
    bg='white',
    fg='black',
    bd=1,
    relief=SOLID,
    font=('Tajawal',12),
    width=13,
    command=lambda: determineLocation(30.088427905900826, 31.20924308911176,'صيدلية مركزية الجيزة')
)
b.place(x=10,y=260)


b1=Button(
    root,
    text='صيدلية الجبيلي',
    cursor='hand2',
    bg='white',
    fg='black',
    bd=1,
    relief=SOLID,
    font=('Tajawal',12),
    width=13,
    command=lambda: determineLocation(29.311236452485822, 30.84939298232051, 'صيدلية الجبيلي الفيوم')
)
b1.place(x=140,y=260)

b2=Button(
    root,
    text='صيدلية الشفاء',
    cursor='hand2',
    bg='white',
    fg='black',
    bd=1,
    relief=SOLID,
    font=('Tajawal',12),
    width=13,
    command=lambda:determineLocation(29.315321609515905, 30.847083529725932,'صيدلية الحداد الجديدة الفيوم')
)
b2.place(x=270,y=260)

b3=Button(
    root,
    text='صيدلية انس بن مالك',
    cursor='hand2',
    bg='white',
    fg='black',
    bd=1,
    relief=SOLID,
    font=('Tajawal',12),
    width=13,
    command=lambda: determineLocation(24.87363170261978, 46.5084595796462,'صيدلية انس بن مالك السعودية')
)
b3.place(x=10,y=300)

b4=Button(
    root,
    text='صيدلية الشرق',
    cursor='hand2',
    bg='white',
    fg='black',
    bd=1,
    relief=SOLID,
    font=('Tajawal',12),
    width=13
)
b4.place(x=140,y=300)

b5=Button(
    root,
    text='صيدلية العلاج',
    cursor='hand2',
    bg='white',
    fg='black',
    bd=1,
    relief=SOLID,
    font=('Tajawal',12),
    width=13
)
b5.place(x=270,y=300)

b6=Button(
    root,
    text='صيدلية العلاج',
    cursor='hand2',
    bg='white',
    fg='black',
    bd=1,
    relief=SOLID,
    font=('Tajawal',12),
    width=13
)
b6.place(x=10,y=340)

b7=Button(
    root,
    text='صيدلية العلاج',
    cursor='hand2',
    bg='white',
    fg='black',
    bd=1,
    relief=SOLID,
    font=('Tajawal',12),
    width=13
)
b7.place(x=140,y=340)

b8=Button(
    root,
    text='صيدلية العلاج',
    cursor='hand2',
    bg='white',
    fg='black',
    bd=1,
    relief=SOLID,
    font=('Tajawal',12),
    width=13
)
b8.place(x=270,y=340)


map = TkinterMapView(
    root,
    width=450,
    height=400,
    corner_radius=0,
    )
map.place(x=400,y=45)
root.mainloop()  
