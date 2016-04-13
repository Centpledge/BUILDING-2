import Tkinter,tkFileDialog

root = Tkinter.Tk()
filez = tkFileDialog.askopenfilenames(parent=root,title='Choose a file')
aa = root.tk.splitlist(filez)
for a in aa :
    b = open(a,'r')
    file_contents = b.read()
    print file_contents
    print "==========================================="
    b.close()
    
