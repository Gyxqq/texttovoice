import copy
import edge_tts
import tkinter
import asyncio
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import ttk
import playsound
# Create a window


##隐藏window1
def save ():
    text = inputbox.get("1.0", "end")
    print(text)
    print("Saving...")
    save_name = savebox.get()
    print(save_name)
    asyncio.run(savem(text,save_name))

def save1 ():
    text = inputbox.get("1.0", "end")
    print(text)
    print("Saving...")
    save_name = savebox.get()
    print(save_name)
    asyncio.run(saveandplay(text,save_name))

async def savem(text,save_name):
    voice1=''
    str1=choose.get()
    for i in range(0,len(str1)):
        if str1[i]=="#":
            break
        voice1+=str1[i]   
    com=edge_tts.Communicate(text,voice1)
    path=save_name+".mp3"
    if save_name=="":path="output.mp3"
    await com.save(path)
    #清除输入框
    inputbox.delete("1.0", "end")
    savebox.delete(0, "end")
    messagebox.showinfo("Edge TTS", "已保存为"+save_name+".mp3")

async def savems(text,save_name):
    try:
        f1=open("config.txt","r",encoding="utf-8")
        voice=f1.read()
    except:
        voice="zh-CN-XiaoyiNeural"
    com=edge_tts.Communicate(text,voice)
    path=save_name+".mp3"
    if save_name=="":path="output.mp3"
    await com.save(path)
    #清除输入框
    text1.insert("end",save_name+".mp3\n")
    window1.update()

async def saveandplay(text,save_name):
    voice1=''
    str1=choose.get()
    for i in range(0,len(str1)):
        if str1[i]=="#":
            break
        voice1+=str1[i]   
    com=edge_tts.Communicate(text,voice1)
    path=save_name+".mp3"
    if save_name=="":path="output.mp3"
    await com.save(path)
    #清除输入框
    inputbox.delete("1.0", "end")
    savebox.delete(0, "end")
    messagebox.showinfo("Edge TTS", "已保存为"+save_name+".mp3")
    #播放
    playsound.playsound(path)
    #清除输入框
    inputbox.delete("1.0", "end")
    savebox.delete(0, "end")
    messagebox.showinfo("Edge TTS", "已播放")




def load ():
    path = filedialog.askopenfilename() 
    try:
        f=open(path,"r",encoding=choose2.get())
    except:
        messagebox.showinfo("Edge TTS", "文件打开失败,请检查文件路径或编码")
        return
    try:
        ftext=f.read()
    except:
        messagebox.showinfo("Edge TTS", "文件读取失败,请检查文件编码")
        return
    f.close()
    inputbox.insert("1.0",ftext)
   
    messagebox.showinfo("Edge TTS", "已从"+path+"加载文本")


def savesplit():
    window1.deiconify()
    window1.update()
    # input()
    text = inputbox.get("1.0", "end") 
    print("Saving...")
    save_name = savebox.get()
    if save_name=="":save_name="output"   
    #隐藏window
    #window.withdraw()
    try:
        min=int(minbox.get())
    except:
        min=200
    count = 0
    split=0
    name=0
    for i in range(0,len(text)):
        if text[i]=="." or text[i]=="?" or text[i]=="!" or text[i]=="。" or text[i]=="？" or text[i]=="！":
            if count > min:

                asyncio.run(savems(text[split:i+1],save_name+"_"+str(name)))
                label2["text"]="保存进度："+str(round(float(i+1)/float(len(text))*100,len(str(len(text)//min))))+"%"
                window1.update()       
                split=i+1
                name+=1
                count=0
        if i==len(text)-1:
            asyncio.run(savems(text[split:i+1],save_name+"_"+str(name)))
            
        count+=1
    messagebox.showinfo("Edge TTS", "保存完成")
    #显示window
    window1.withdraw()
    text1.delete("1.0", "end")
    window.deiconify()
def search():
    text=choose.get()
    list2=[]
    for i in range(0,len(list)):
        #忽略大小写的字符串匹配
        if text.lower() in list[i].lower():
            list2.append(list[i])
    choose["values"]=list2

voice='''Name: af-ZA-AdriNeural
Gender: Female

Name: af-ZA-WillemNeural
Gender: Male

Name: am-ET-AmehaNeural
Gender: Male

Name: am-ET-MekdesNeural
Gender: Female

Name: ar-AE-FatimaNeural
Gender: Female

Name: ar-AE-HamdanNeural
Gender: Male

Name: ar-BH-AliNeural
Gender: Male

Name: ar-BH-LailaNeural
Gender: Female

Name: ar-DZ-AminaNeural
Gender: Female

Name: ar-DZ-IsmaelNeural
Gender: Male

Name: ar-EG-SalmaNeural
Gender: Female

Name: ar-EG-ShakirNeural
Gender: Male

Name: ar-IQ-BasselNeural
Gender: Male

Name: ar-IQ-RanaNeural
Gender: Female

Name: ar-JO-SanaNeural
Gender: Female

Name: ar-JO-TaimNeural
Gender: Male

Name: ar-KW-FahedNeural
Gender: Male

Name: ar-KW-NouraNeural
Gender: Female

Name: ar-LB-LaylaNeural
Gender: Female

Name: ar-LB-RamiNeural
Gender: Male

Name: ar-LY-ImanNeural
Gender: Female

Name: ar-LY-OmarNeural
Gender: Male

Name: ar-MA-JamalNeural
Gender: Male

Name: ar-MA-MounaNeural
Gender: Female

Name: ar-OM-AbdullahNeural
Gender: Male

Name: ar-OM-AyshaNeural
Gender: Female

Name: ar-QA-AmalNeural
Gender: Female

Name: ar-QA-MoazNeural
Gender: Male

Name: ar-SA-HamedNeural
Gender: Male

Name: ar-SA-ZariyahNeural
Gender: Female

Name: ar-SY-AmanyNeural
Gender: Female

Name: ar-SY-LaithNeural
Gender: Male

Name: ar-TN-HediNeural
Gender: Male

Name: ar-TN-ReemNeural
Gender: Female

Name: ar-YE-MaryamNeural
Gender: Female

Name: ar-YE-SalehNeural
Gender: Male

Name: az-AZ-BabekNeural
Gender: Male

Name: az-AZ-BanuNeural
Gender: Female

Name: bg-BG-BorislavNeural
Gender: Male

Name: bg-BG-KalinaNeural
Gender: Female

Name: bn-BD-NabanitaNeural
Gender: Female

Name: bn-BD-PradeepNeural
Gender: Male

Name: bn-IN-BashkarNeural
Gender: Male

Name: bn-IN-TanishaaNeural
Gender: Female

Name: bs-BA-GoranNeural
Gender: Male

Name: bs-BA-VesnaNeural
Gender: Female

Name: ca-ES-EnricNeural
Gender: Male

Name: ca-ES-JoanaNeural
Gender: Female

Name: cs-CZ-AntoninNeural
Gender: Male

Name: cs-CZ-VlastaNeural
Gender: Female

Name: cy-GB-AledNeural
Gender: Male

Name: cy-GB-NiaNeural
Gender: Female

Name: da-DK-ChristelNeural
Gender: Female

Name: da-DK-JeppeNeural
Gender: Male

Name: de-AT-IngridNeural
Gender: Female

Name: de-AT-JonasNeural
Gender: Male

Name: de-CH-JanNeural
Gender: Male

Name: de-CH-LeniNeural
Gender: Female

Name: de-DE-AmalaNeural
Gender: Female

Name: de-DE-ConradNeural
Gender: Male

Name: de-DE-KatjaNeural
Gender: Female

Name: de-DE-KillianNeural
Gender: Male

Name: el-GR-AthinaNeural
Gender: Female

Name: el-GR-NestorasNeural
Gender: Male

Name: en-AU-NatashaNeural
Gender: Female

Name: en-AU-WilliamNeural
Gender: Male

Name: en-CA-ClaraNeural
Gender: Female

Name: en-CA-LiamNeural
Gender: Male

Name: en-GB-LibbyNeural
Gender: Female

Name: en-GB-MaisieNeural
Gender: Female

Name: en-GB-RyanNeural
Gender: Male

Name: en-GB-SoniaNeural
Gender: Female

Name: en-GB-ThomasNeural
Gender: Male

Name: en-HK-SamNeural
Gender: Male

Name: en-HK-YanNeural
Gender: Female

Name: en-IE-ConnorNeural
Gender: Male

Name: en-IE-EmilyNeural
Gender: Female

Name: en-IN-NeerjaExpressiveNeural
Gender: Female

Name: en-IN-NeerjaNeural
Gender: Female

Name: en-IN-PrabhatNeural
Gender: Male

Name: en-KE-AsiliaNeural
Gender: Female

Name: en-KE-ChilembaNeural
Gender: Male

Name: en-NG-AbeoNeural
Gender: Male

Name: en-NG-EzinneNeural
Gender: Female

Name: en-NZ-MitchellNeural
Gender: Male

Name: en-NZ-MollyNeural
Gender: Female

Name: en-PH-JamesNeural
Gender: Male

Name: en-PH-RosaNeural
Gender: Female

Name: en-SG-LunaNeural
Gender: Female

Name: en-SG-WayneNeural
Gender: Male

Name: en-TZ-ElimuNeural
Gender: Male

Name: en-TZ-ImaniNeural
Gender: Female

Name: en-US-AnaNeural
Gender: Female

Name: en-US-AriaNeural
Gender: Female

Name: en-US-ChristopherNeural
Gender: Male

Name: en-US-EricNeural
Gender: Male

Name: en-US-GuyNeural
Gender: Male

Name: en-US-JennyNeural
Gender: Female

Name: en-US-MichelleNeural
Gender: Female

Name: en-US-RogerNeural
Gender: Male

Name: en-US-SteffanNeural
Gender: Male

Name: en-ZA-LeahNeural
Gender: Female

Name: en-ZA-LukeNeural
Gender: Male

Name: es-AR-ElenaNeural
Gender: Female

Name: es-AR-TomasNeural
Gender: Male

Name: es-BO-MarceloNeural
Gender: Male

Name: es-BO-SofiaNeural
Gender: Female

Name: es-CL-CatalinaNeural
Gender: Female

Name: es-CL-LorenzoNeural
Gender: Male

Name: es-CO-GonzaloNeural
Gender: Male

Name: es-CO-SalomeNeural
Gender: Female

Name: es-CR-JuanNeural
Gender: Male

Name: es-CR-MariaNeural
Gender: Female

Name: es-CU-BelkysNeural
Gender: Female

Name: es-CU-ManuelNeural
Gender: Male

Name: es-DO-EmilioNeural
Gender: Male

Name: es-DO-RamonaNeural
Gender: Female

Name: es-EC-AndreaNeural
Gender: Female

Name: es-EC-LuisNeural
Gender: Male

Name: es-ES-AlvaroNeural
Gender: Male

Name: es-ES-ElviraNeural
Gender: Female

Name: es-GQ-JavierNeural
Gender: Male

Name: es-GQ-TeresaNeural
Gender: Female

Name: es-GT-AndresNeural
Gender: Male

Name: es-GT-MartaNeural
Gender: Female

Name: es-HN-CarlosNeural
Gender: Male

Name: es-HN-KarlaNeural
Gender: Female

Name: es-MX-DaliaNeural
Gender: Female

Name: es-MX-JorgeNeural
Gender: Male

Name: es-NI-FedericoNeural
Gender: Male

Name: es-NI-YolandaNeural
Gender: Female

Name: es-PA-MargaritaNeural
Gender: Female

Name: es-PA-RobertoNeural
Gender: Male

Name: es-PE-AlexNeural
Gender: Male

Name: es-PE-CamilaNeural
Gender: Female

Name: es-PR-KarinaNeural
Gender: Female

Name: es-PR-VictorNeural
Gender: Male

Name: es-PY-MarioNeural
Gender: Male

Name: es-PY-TaniaNeural
Gender: Female

Name: es-SV-LorenaNeural
Gender: Female

Name: es-SV-RodrigoNeural
Gender: Male

Name: es-US-AlonsoNeural
Gender: Male

Name: es-US-PalomaNeural
Gender: Female

Name: es-UY-MateoNeural
Gender: Male

Name: es-UY-ValentinaNeural
Gender: Female

Name: es-VE-PaolaNeural
Gender: Female

Name: es-VE-SebastianNeural
Gender: Male

Name: et-EE-AnuNeural
Gender: Female

Name: et-EE-KertNeural
Gender: Male

Name: fa-IR-DilaraNeural
Gender: Female

Name: fa-IR-FaridNeural
Gender: Male

Name: fi-FI-HarriNeural
Gender: Male

Name: fi-FI-NooraNeural
Gender: Female

Name: fil-PH-AngeloNeural
Gender: Male

Name: fil-PH-BlessicaNeural
Gender: Female

Name: fr-BE-CharlineNeural
Gender: Female

Name: fr-BE-GerardNeural
Gender: Male

Name: fr-CA-AntoineNeural
Gender: Male

Name: fr-CA-JeanNeural
Gender: Male

Name: fr-CA-SylvieNeural
Gender: Female

Name: fr-CH-ArianeNeural
Gender: Female

Name: fr-CH-FabriceNeural
Gender: Male

Name: fr-FR-DeniseNeural
Gender: Female

Name: fr-FR-EloiseNeural
Gender: Female

Name: fr-FR-HenriNeural
Gender: Male

Name: ga-IE-ColmNeural
Gender: Male

Name: ga-IE-OrlaNeural
Gender: Female

Name: gl-ES-RoiNeural
Gender: Male

Name: gl-ES-SabelaNeural
Gender: Female

Name: gu-IN-DhwaniNeural
Gender: Female

Name: gu-IN-NiranjanNeural
Gender: Male

Name: he-IL-AvriNeural
Gender: Male

Name: he-IL-HilaNeural
Gender: Female

Name: hi-IN-MadhurNeural
Gender: Male

Name: hi-IN-SwaraNeural
Gender: Female

Name: hr-HR-GabrijelaNeural
Gender: Female

Name: hr-HR-SreckoNeural
Gender: Male

Name: hu-HU-NoemiNeural
Gender: Female

Name: hu-HU-TamasNeural
Gender: Male

Name: id-ID-ArdiNeural
Gender: Male

Name: id-ID-GadisNeural
Gender: Female

Name: is-IS-GudrunNeural
Gender: Female

Name: is-IS-GunnarNeural
Gender: Male

Name: it-IT-DiegoNeural
Gender: Male

Name: it-IT-ElsaNeural
Gender: Female

Name: it-IT-IsabellaNeural
Gender: Female

Name: ja-JP-KeitaNeural
Gender: Male

Name: ja-JP-NanamiNeural
Gender: Female

Name: jv-ID-DimasNeural
Gender: Male

Name: jv-ID-SitiNeural
Gender: Female

Name: ka-GE-EkaNeural
Gender: Female

Name: ka-GE-GiorgiNeural
Gender: Male

Name: kk-KZ-AigulNeural
Gender: Female

Name: kk-KZ-DauletNeural
Gender: Male

Name: km-KH-PisethNeural
Gender: Male

Name: km-KH-SreymomNeural
Gender: Female

Name: kn-IN-GaganNeural
Gender: Male

Name: kn-IN-SapnaNeural
Gender: Female

Name: ko-KR-InJoonNeural
Gender: Male

Name: ko-KR-SunHiNeural
Gender: Female

Name: lo-LA-ChanthavongNeural
Gender: Male

Name: lo-LA-KeomanyNeural
Gender: Female

Name: lt-LT-LeonasNeural
Gender: Male

Name: lt-LT-OnaNeural
Gender: Female

Name: lv-LV-EveritaNeural
Gender: Female

Name: lv-LV-NilsNeural
Gender: Male

Name: mk-MK-AleksandarNeural
Gender: Male

Name: mk-MK-MarijaNeural
Gender: Female

Name: ml-IN-MidhunNeural
Gender: Male

Name: ml-IN-SobhanaNeural
Gender: Female

Name: mn-MN-BataaNeural
Gender: Male

Name: mn-MN-YesuiNeural
Gender: Female

Name: mr-IN-AarohiNeural
Gender: Female

Name: mr-IN-ManoharNeural
Gender: Male

Name: ms-MY-OsmanNeural
Gender: Male

Name: ms-MY-YasminNeural
Gender: Female

Name: mt-MT-GraceNeural
Gender: Female

Name: mt-MT-JosephNeural
Gender: Male

Name: my-MM-NilarNeural
Gender: Female

Name: my-MM-ThihaNeural
Gender: Male

Name: nb-NO-FinnNeural
Gender: Male

Name: nb-NO-PernilleNeural
Gender: Female

Name: ne-NP-HemkalaNeural
Gender: Female

Name: ne-NP-SagarNeural
Gender: Male

Name: nl-BE-ArnaudNeural
Gender: Male

Name: nl-BE-DenaNeural
Gender: Female

Name: nl-NL-ColetteNeural
Gender: Female

Name: nl-NL-FennaNeural
Gender: Female

Name: nl-NL-MaartenNeural
Gender: Male

Name: pl-PL-MarekNeural
Gender: Male

Name: pl-PL-ZofiaNeural
Gender: Female

Name: ps-AF-GulNawazNeural
Gender: Male

Name: ps-AF-LatifaNeural
Gender: Female

Name: pt-BR-AntonioNeural
Gender: Male

Name: pt-BR-FranciscaNeural
Gender: Female

Name: pt-PT-DuarteNeural
Gender: Male

Name: pt-PT-RaquelNeural
Gender: Female

Name: ro-RO-AlinaNeural
Gender: Female

Name: ro-RO-EmilNeural
Gender: Male

Name: ru-RU-DmitryNeural
Gender: Male

Name: ru-RU-SvetlanaNeural
Gender: Female

Name: si-LK-SameeraNeural
Gender: Male

Name: si-LK-ThiliniNeural
Gender: Female

Name: sk-SK-LukasNeural
Gender: Male

Name: sk-SK-ViktoriaNeural
Gender: Female

Name: sl-SI-PetraNeural
Gender: Female

Name: sl-SI-RokNeural
Gender: Male

Name: so-SO-MuuseNeural
Gender: Male

Name: so-SO-UbaxNeural
Gender: Female

Name: sq-AL-AnilaNeural
Gender: Female

Name: sq-AL-IlirNeural
Gender: Male

Name: sr-RS-NicholasNeural
Gender: Male

Name: sr-RS-SophieNeural
Gender: Female

Name: su-ID-JajangNeural
Gender: Male

Name: su-ID-TutiNeural
Gender: Female

Name: sv-SE-MattiasNeural
Gender: Male

Name: sv-SE-SofieNeural
Gender: Female

Name: sw-KE-RafikiNeural
Gender: Male

Name: sw-KE-ZuriNeural
Gender: Female

Name: sw-TZ-DaudiNeural
Gender: Male

Name: sw-TZ-RehemaNeural
Gender: Female

Name: ta-IN-PallaviNeural
Gender: Female

Name: ta-IN-ValluvarNeural
Gender: Male

Name: ta-LK-KumarNeural
Gender: Male

Name: ta-LK-SaranyaNeural
Gender: Female

Name: ta-MY-KaniNeural
Gender: Female

Name: ta-MY-SuryaNeural
Gender: Male

Name: ta-SG-AnbuNeural
Gender: Male

Name: ta-SG-VenbaNeural
Gender: Female

Name: te-IN-MohanNeural
Gender: Male

Name: te-IN-ShrutiNeural
Gender: Female

Name: th-TH-NiwatNeural
Gender: Male

Name: th-TH-PremwadeeNeural
Gender: Female

Name: tr-TR-AhmetNeural
Gender: Male

Name: tr-TR-EmelNeural
Gender: Female

Name: uk-UA-OstapNeural
Gender: Male

Name: uk-UA-PolinaNeural
Gender: Female

Name: ur-IN-GulNeural
Gender: Female

Name: ur-IN-SalmanNeural
Gender: Male

Name: ur-PK-AsadNeural
Gender: Male

Name: ur-PK-UzmaNeural
Gender: Female

Name: uz-UZ-MadinaNeural
Gender: Female

Name: uz-UZ-SardorNeural
Gender: Male

Name: vi-VN-HoaiMyNeural
Gender: Female

Name: vi-VN-NamMinhNeural
Gender: Male

Name: zh-CN-XiaoxiaoNeural
Gender: Female

Name: zh-CN-XiaoyiNeural
Gender: Female

Name: zh-CN-YunjianNeural
Gender: Male

Name: zh-CN-YunxiNeural
Gender: Male

Name: zh-CN-YunxiaNeural
Gender: Male

Name: zh-CN-YunyangNeural
Gender: Male

Name: zh-CN-liaoning-XiaobeiNeural
Gender: Female

Name: zh-CN-shaanxi-XiaoniNeural
Gender: Female

Name: zh-HK-HiuGaaiNeural
Gender: Female

Name: zh-HK-HiuMaanNeural
Gender: Female

Name: zh-HK-WanLungNeural
Gender: Male

Name: zh-TW-HsiaoChenNeural
Gender: Female

Name: zh-TW-HsiaoYuNeural
Gender: Female

Name: zh-TW-YunJheNeural
Gender: Male

Name: zu-ZA-ThandoNeural
Gender: Female

Name: zu-ZA-ThembaNeural
Gender: Male
'''
f0=open("voice.txt","w",encoding="utf-8")
f0.write(voice)
f0.close()
voicepro=""
for i in range(0,len(voice),1):
    if voice[i:i+6]=="Name: ":
        i=i+6
        while voice[i]!="\n":
            voicepro=voicepro+voice[i]
            i=i+1
        voicepro+='#'
        i=i+1
        while voice[i]!="\n":
            voicepro=voicepro+voice[i]
            i=i+1
            
        voicepro+='\n'
window = tkinter.Tk()
window.title("Edge TTS")
window.geometry("800x900")
window.resizable(False, False)

inputbox=tkinter.Text(window, height=18, width=92, font=("Microsoft YaHei", 15))
rol=tkinter.Scrollbar()
rol.pack()
rol.place(x=780, y=0, height=500)
rol.config(command=inputbox.yview)
inputbox.config(yscrollcommand=rol.set)
inputbox.pack()
inputbox.place(x=0, y=0, width=780)
input_text = tkinter.Label(window, text="保存文件名:", font=("Microsoft YaHei", 15))
input_text.pack(anchor="w")
input_text.place(x=0, y=500)
savebox=tkinter.Entry(window, width=40, font=("Microsoft YaHei", 15))
savebox.pack(anchor="w")
savebox.place(x=10, y=540)
botton = tkinter.Button(window, text="生成音频并保存", font=("Microsoft YaHei", 15), command=save)
botton.pack()
botton.place(x=540, y=537, width=200, height=35)
l4=tkinter.Label(window, text="最小分割字符数:(default=200)", font=("Microsoft YaHei", 15),)
l4.pack(anchor="w")
l4.place(x=0, y=600)
minbox=tkinter.Entry(window, width=15, font=("Microsoft YaHei", 15))
minbox.pack(anchor="w")
minbox.place(x=300, y=600)
botton2 = tkinter.Button(window, text="自动分割保存", font=("Microsoft YaHei", 15), command=savesplit)
botton2.pack()
botton2.place(x=540, y=597, width=150, height=35)
fin=tkinter.Label(window, text="从txt文件加载:", font=("Microsoft YaHei", 15),)
fin.pack(anchor="w")
fin.place(x=0, y=660)
choose2=ttk.Combobox(window,font=("Microsoft YaHei", 15),width=10)
list2=['utf-8','gbk','ansi','utf-16']
choose2['values']=list2
choose2.pack(anchor="w")
choose2.place(x=320, y=660)
choose2.current(0)
finbotton = tkinter.Button(window, text="加载文件", font=("Microsoft YaHei", 15), command=load)
finbotton.pack()
finbotton.place(x=200, y=660, width=100, height=35)
l3=tkinter.Label(window, text="config file=config.txt", font=("Microsoft YaHei", 15),)
l3.pack(anchor="n")
l3.place(x=580, y=830)
l2=tkinter.Label(window, text="Powered by Edge TTS", font=("Microsoft YaHei", 15),)
l2.pack(anchor="n")
l2.place(x=580, y=860)
choose=ttk.Combobox(window,font=("Microsoft YaHei", 15),width=30)
list=voicepro.split('\n')
list.insert(0,"zh-CN-XiaoyiNeural")
choose['values']=list
choose.current(0)
choose.pack()
choose.place(x=200, y=700)
l5=tkinter.Label(window, text="选择发音人:", font=("Microsoft YaHei", 15),)
l5.pack(anchor="w")
l5.place(x=0, y=700)
but1=tkinter.Button(window, text="搜索", font=("Microsoft YaHei", 15),command=search)
but1.pack()
but1.place(x=590, y=697, width=50, height=35)
but2=tkinter.Button(window, text="保存", font=("Microsoft YaHei", 15))
but2.pack()
but2.place(x=650, y=697, width=50, height=35)
but3=tkinter.Button(window, text="生成保存并播放", font=("Microsoft YaHei", 15),command=save1)
but3.pack()
but3.place(x=540, y=497, width=200, height=35)
window1=tkinter.Toplevel(window)
window1.title("Edge TTS")
window1.geometry("300x460")
window1.resizable(0,0)
label1=tkinter.Label(window1,text="正在保存...",font=("Microsoft YaHei", 10))
text1=tkinter.Text(window1,font=("Microsoft YaHei", 10),width=30,height=18)
botton4=tkinter.Button(window1,text="关闭",font=("Microsoft YaHei", 10),command=window1.destroy)
label2=tkinter.Label(window1,text=" ",font=("Microsoft YaHei", 10))
label2.pack()
label1.pack()
text1.pack()
botton4.pack()
window1.withdraw()
window.mainloop()

