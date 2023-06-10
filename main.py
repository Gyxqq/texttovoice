import edge_tts
import tkinter
import asyncio
from tkinter import messagebox
# Create a window

def save ():
    text = inputbox.get("1.0", "end")
    print(text)
    print("Saving...")
    save_name = savebox.get()
    print(save_name)
    asyncio.run(savem(text,save_name))

async def savem(text,save_name):
    com=edge_tts.Communicate(text,"zh-CN-XiaoyiNeural")
    path=save_name+".mp3"
    if save_name=="":path="output.mp3"
    await com.save(path)
    #清除输入框
    inputbox.delete("1.0", "end")
    savebox.delete(0, "end")
    messagebox.showinfo("Edge TTS", "已保存为"+save_name+".mp3")
def load ():
    path=finbox.get()
    try:
        f=open(path,"r",encoding="utf-8")
    except:
        messagebox.showinfo("Edge TTS", "文件打开失败")
        return
    ftext=f.read()
    f.close()
    inputbox.insert("1.0",ftext)
    finbox.delete(0, "end")
    messagebox.showinfo("Edge TTS", "已从"+path+"加载文本")
window = tkinter.Tk()
window.title("Edge TTS")
window.geometry("800x800")
window.resizable(False, False)
inputbox=tkinter.Text(window, height=20, width=100, font=("Microsoft YaHei", 15))
inputbox.pack()
input_text = tkinter.Label(window, text="保存文件名:", font=("Microsoft YaHei", 15),)
input_text.pack(anchor="w")
savebox=tkinter.Entry(window, width=100, font=("Microsoft YaHei", 15))
savebox.pack(anchor="w")
botton = tkinter.Button(window, text="生成音频并保存", font=("Microsoft YaHei", 15), command=save)
botton.pack()
fin=tkinter.Label(window, text="从txt文件加载(utf-8):", font=("Microsoft YaHei", 15),)
fin.pack(anchor="w")
finbox=tkinter.Entry(window, width=100, font=("Microsoft YaHei", 15))
finbox.pack(anchor="w")
finbotton = tkinter.Button(window, text="加载文件", font=("Microsoft YaHei", 15), command=load)
finbotton.pack()
window.mainloop()

