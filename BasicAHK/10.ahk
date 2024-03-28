Gui, Show, w700 h440
Gui, Font, s22, Intro
Gui Add, Text, x265 y20, Attention!
Gui, Font, s11, 
Gui Add, Text, x310 y50, Readme
Gui, Font, s12, Arial
Gui Add, Text, x20 y80, Welcome to Cleaner.cache!
Gui Add, Text, x20 y100, The first open-source program that help you to clean the temporary file (cache) of all program.
Gui Add, Text, x20 y130, •It's very simple: you select program you want to clean and press CLEAN!
Gui Add, Text, x20 y150,  In a few second the cache will be empty and your pc faster!
Gui Add, Text, x20 y180, •ATTENTION! The program works correctly only if you haven't edited the cache path.
Gui Add, Text, x20 y200,  If you've edited it you must change the path in the code.
Gui Add, Text, x20 y230, •The program is developed with AutoHotKey, you can find the code at: 12345.
Gui Add, Text, x20 y250,  To see and edit the code you must have AutoHotKey installed on your pc.
Gui Add, Text, x20 y280, •Some programs may not work correctly after the cache cleaning or they require log-in.
Gui Add, Text, x20 y300,  I take no responsibility in case of malfunction.
Gui Add, Text, x20 y320,  It's always recommended to make a backup of the data of the programs before cleaning.
Gui Add, Text, x20 y350, •If you don't see an app you want, tell me it clicking here: 
Gui Add, Link, x420 y350, <a href="https://bit.ly/2WDBxb2">https://bit.ly/2WDBxb2</a>
Gui Add, Button, w150 y50 x280 y380 gOK, OK
return

Ok:

UrlDownloadToFile,https://i.imgur.com/2e7qjVs.png, %USERPROFILE%\Premiere.png
UrlDownloadToFile,https://i.imgur.com/GindCEX.png, %USERPROFILE%\Lightroom.png
UrlDownloadToFile,https://i.imgur.com/pnJD2tY.png, %USERPROFILE%\DaVinci.png
UrlDownloadToFile,https://i.imgur.com/hxXpn3l.png, %USERPROFILE%\Affinity.png
UrlDownloadToFile,https://i.imgur.com/ld52CX7.png, %USERPROFILE%\Chrome.png
UrlDownloadToFile,https://i.imgur.com/AuJWxBA.png, %USERPROFILE%\Edge.png
UrlDownloadToFile,https://i.imgur.com/u09xezk.png, %USERPROFILE%\Firefox.png
UrlDownloadToFile,https://i.imgur.com/nvMDxyJ.png, %USERPROFILE%\Obs.png
UrlDownloadToFile,https://i.imgur.com/QV3fNUG.png, %USERPROFILE%\Spotify.png
UrlDownloadToFile,https://i.imgur.com/0G2yhSg.png, %USERPROFILE%\Telegram.png
UrlDownloadToFile,https://i.imgur.com/fg9NclG.png, %USERPROFILE%\Whatsapp.png
UrlDownloadToFile,https://i.imgur.com/iBABVaW.png, %USERPROFILE%\Teams.png
UrlDownloadToFile,https://i.imgur.com/0Do4BHN.png, %USERPROFILE%\Zoom.png
UrlDownloadToFile,https://i.imgur.com/CtsXU8Z.png, %USERPROFILE%\Store.png
UrlDownloadToFile,https://i.imgur.com/g4TKW1S.png, %USERPROFILE%\Dns.png
UrlDownloadToFile,https://i.imgur.com/6PtfjpK.png, %USERPROFILE%\Bin.png
UrlDownloadToFile,https://i.imgur.com/FnxJ3LO.png, %USERPROFILE%\Explorer.png

Gui, Hide
Gui, 2:Show, w500 h500
Gui, 2:Font, s15
Gui, 2:Add, Text, x120 y1, Cleaning programs' cache files

Gui, 2:Add, Picture, w18 h-1 x15 y82, %USERPROFILE%\Premiere.png
Gui, 2:Add, Picture, w18 h-1 x15 y105, %USERPROFILE%\Lightroom.png
Gui, 2:Add, Picture, w18 h-1 x15 y130, %USERPROFILE%\DaVinci.png
Gui, 2:Add, Picture, w18 h-1 x15 y152, %USERPROFILE%\Affinity.png
Gui, 2:Add, Picture, w18 h-1 x15 y202, %USERPROFILE%\Chrome.png
Gui, 2:Add, Picture, w18 h-1 x15 y225, %USERPROFILE%\Edge.png
Gui, 2:Add, Picture, w18 h-1 x15 y249, %USERPROFILE%\Firefox.png
Gui, 2:Add, Picture, w18 h-1 x15 y305, %USERPROFILE%\Obs.png
Gui, 2:Add, Picture, w18 h-1 x15 y330, %USERPROFILE%\Spotify.png
Gui, 2:Add, Picture, w18 h-1 x15 y355, %USERPROFILE%\Spotify.png
Gui, 2:Add, Picture, w18 h-1 x250 y82, %USERPROFILE%\Telegram.png
Gui, 2:Add, Picture, w18 h-1 x250 y107, %USERPROFILE%\Whatsapp.png
Gui, 2:Add, Picture, w18 h-1 x250 y130, %USERPROFILE%\Teams.png
Gui, 2:Add, Picture, w18 h-1 x250 y152, %USERPROFILE%\Zoom.png
Gui, 2:Add, Picture, w18 h-1 x250 y202, %USERPROFILE%\Store.png
Gui, 2:Add, Picture, w18 h-1 x250 y225, %USERPROFILE%\Dns.png
Gui, 2:Add, Picture, w18 h-1 x250 y249, %USERPROFILE%\Bin.png
Gui, 2:Add, Picture, w18 h-1 x250 y273, %USERPROFILE%\Explorer.png

Gui, 2:Font, s10
Gui, 2:Add, Text, x165 y30, Select program you want to clean
Gui, 2:Font, bold s10, Nexa Bold
Gui, 2:Add, Text, x15 y60, Video/Photo Editing
Gui, 2:Font,
Gui, 2:Add, Text, x40 y60,
Gui, 2:Add, Checkbox, vPremiere , Adobe Premiere
Gui, 2:Add, Checkbox, vLightroom, Adobe Lightroom
Gui, 2:Add, Checkbox, vDaVinci, DaVinci Resolve
Gui, 2:Add, Checkbox, vAffinity, Affinity Photo
Gui, 2:Font, bold s10, Nexa Bold
Gui, 2:Add, Text, x15 y180, Browser
Gui, 2:Font, 
Gui, 2:Add, Text, x40 y180,
GUi, 2:Add, Checkbox, vChrome, Google Chrome
GUi, 2:Add, Checkbox, vEdge, Microsoft Edge
GUi, 2:Add, Checkbox, vFirefox, Mozilla Firefox
Gui, 2:Font, bold s10, Nexa Bold
Gui, 2:Add, Text, x15 y285, Multimediality
Gui, 2:Font, 
Gui, 2:Add, Text, x40 y285,
Gui, 2:Add, Checkbox, vObs, OBS Studio
Gui, 2:Add, Checkbox, vSpotify, Spotify (MS Store)
Gui, 2:Add, Checkbox, vSpotify2, Spotify (EXE)
Gui, 2:Font, bold s10, Nexa Bold
Gui, 2:Add, Text, x250 y60, Social
Gui, 2:Font, 
Gui, 2:Add, Text, x275 y60,
Gui, 2:Add, Checkbox, vTelegram, Telegram
Gui, 2:Add, Checkbox, vWhatsapp, Whatsapp
Gui, 2:Add, Checkbox, vTeams, Microsoft Teams
Gui, 2:Add, Checkbox, vZoom, Zoom
Gui, 2:Font, bold s10, Nexa Bold
Gui, 2:Add, Text, x250 y180, System
Gui, 2:Font, 
Gui, 2:Add, Text, x275 y180,
Gui, 2:Add, Checkbox, vStore, Microsoft Store
Gui, 2:Add, Checkbox, vDns, DNS Cache
Gui, 2:Add, Checkbox, vBin, Windows Bin
Gui, 2:Add, Checkbox, vExplorer, Explorer (Cache and Thumbmail)
Gui, 2:Font, s15
Gui, 2:Add, Button, w200 h50 x140 y400 gEnd, Clean!
Gui, 2:Font, s8
Gui, 2:Add, Button, w100 h25 x370 y425 gEsc, Exit

GuiControl, Focus, SearchTerm
return

End:               
Gui Submit, NoHide

If Lightroom
CacheFolder = %USERPROFILE%\AppData\Local\Adobe\CameraRaw\Cache2\
IfExist, %CacheFolder%
{
    FileDelete, %USERPROFILE%\AppData\Local\Adobe\CameraRaw\Cache2\*
    MsgBox, Done! Your Adobe Lightroom cache is empty
}
If Lightroom
IfNotExist, %CacheFolder%
{
    MsgBox, LIGHTROOM ERROR! You may haven't the program installed or you've changed the cache folder
}
--------------------------------------
If Premiere
CacheFolder2 = %USERPROFILE%\AppData\Roaming\Adobe\Common\Media Cache\
IfExist, %CacheFolder2%
{
    FileDelete, %USERPROFILE%\AppData\Roaming\Adobe\Common\Media Cache\*
    FileDelete, %USERPROFILE%\AppData\Roaming\Adobe\Common\Media Cache Files\*
    MsgBox, Done! Your Adobe Premiere cache is empty
}
If Premiere
IfNotExist, %CacheFolder2%
{
    MsgBox, PREMIERE ERROR! You may haven't the program installed or you've changed the cache folder
}
----------------------------------------
If DaVinci
CacheFolder14 = C:\CacheClip
IfExist, %CacheFolder14%
{
    FileDelete, C:\CacheClip\*
    MsgBox, Done! Your DaVinci Resolve cache is empty
}
If DaVinci
IfNotExist, %CacheFolder14%
{
    MsgBox, DAVINCI ERROR! You may haven't the program installed or you've changed the cache folder
}


----------------------------
If Affinity
CacheFolder15 = AFFINITY PATH
IfExist, %CacheFolder15%
{
    FileDelete, AFFINITY PATH
    MsgBox, Done! Your Affinity cache is empty
}
If Affinity
IfNotExist, %CacheFolder15%
{
    MsgBox, AFFINITY ERROR! You may haven't the program installed or you've changed the cache folder
}
--------------------------------------
If Edge
CacheFolder4 = %USERPROFILE%\AppData\Local\Microsoft\Edge\User Data\Default\Cache\
IfExist, %CacheFolder4%
{
    FileDelete, %USERPROFILE%\AppData\Local\Microsoft\Edge\User Data\Default\Cache\*
    MsgBox, Done! Your Microsoft Edge cache is empty
}
If Edge
IfNotExist, %CacheFolder4%
{
    MsgBox, EDGE ERROR! You may haven't the program installed or you've changed the cache folder
}
-----------------------------------
If Chrome
CacheFolder5 = %USERPROFILE%\AppData\Local\Google\Chrome\User Data\Default\Cache\
IfExist, %CacheFolder5%
{
    FileDelete, %USERPROFILE%\AppData\Local\Google\Chrome\User Data\Default\Cache\*
    MsgBox, Done! Your Google Chrome cache is empty
}
If Chrome
IfNotExist, %CacheFolder5%
{
    MsgBox, CHROME ERROR! You may haven't the program installed or you've changed the cache folder
}
---------------------------------
If Firefox
CacheFolder6 = %USERPROFILE%\AppData\Local\Mozilla\Firefox\
IfExist, %CacheFolder6%
{
    IniRead, ProfilePath, %USERPROFILE%\AppData\Roaming\Mozilla\Firefox\profiles.ini, Profile0, Path
    FileDelete, %USERPROFILE%\AppData\Local\Mozilla\Firefox\%ProfilePath%\Cache2\*
    MsgBox, Done! Your Mozilla Firefox cache is empty
}
If Firefox
IfNotExist, %CacheFolder6%
{
    MsgBox, FIREFOX ERROR! You may haven't the program installed or you've changed the cache folder
}
--------------------------------------
If Obs
CacheFolder7 = %USERPROFILE%\AppData\Roaming\obs-studio\plugin_config\obs-browser\Cache
IfExist, %CacheFolder7%
{
    FileDelete, %USERPROFILE%\AppData\Roaming\obs-studio\plugin_config\obs-browser\Cache\*
    FileDelete, %USERPROFILE%\AppData\Roaming\obs-studio\plugin_config\obs-browser\Code Cache\*
    MsgBox, Done! Your Obs Studio cache is empty
}
If Obs
IfNotExist, %CacheFolder7%
{
    MsgBox, OBS ERROR! You may haven't the program installed or you've changed the cache folder
}
---------------------------------------------
If Spotify
CacheFolder8 = %USERPROFILE%\AppData\Local\Packages\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\LocalCache\Spotify\Data\
IfExist, %CacheFolder8%
{
    FileDelete, %USERPROFILE%\AppData\Local\Packages\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\LocalCache\Spotify\Data\*
    MsgBox, Done! Your Spotify STORE cache is empty
}
If Spotify
IfNotExist, %CacheFolder8%
{
    MsgBox, SPOTIFY STORE ERROR! You may haven't the program installed or you've changed the cache folder
}
----------------------------------------
If Spotify2
CacheFolder13 = %USERPROFILE%\AppData\Local\Spotify\Data\
IfExist, %CacheFolder13%
{
    FileDelete, %USERPROFILE%\AppData\Local\Spotify\Data\*
    MsgBox, Done! Your Spotify EXE cache is empty
}
If Spotify2
IfNotExist, %CacheFolder13%
{
    MsgBox, SPOTIFY EXE ERROR! You may haven't the program installed or you've changed the cache folder
}
------------------------------------------
If Telegram
CacheFolder9 = %USERPROFILE%\AppData\Roaming\Telegram Desktop\tdata\
IfExist, %CacheFolder9%
{
    FileDelete, %USERPROFILE%\AppData\Roaming\Telegram Desktop\tdata\*
    MsgBox, Done! Your Telegram cache is empty. You might re-login
}
If Telegram
IfNotExist, %CacheFolder9%
{
    MsgBox, TELEGRAM ERROR! You may haven't the program installed or you've changed the cache folder
}
-----------------------------------------------
If Whatsapp
CacheFolder10 = %USERPROFILE%\AppData\Local\Packages\5319275A.WhatsAppDesktop_cv1g1gvanyjgm\LocalCache\Roaming\WhatsApp\Cache\
IfExist, %CacheFolder10%
{
    FileDelete, %USERPROFILE%\AppData\Local\Packages\5319275A.WhatsAppDesktop_cv1g1gvanyjgm\LocalCache\Roaming\WhatsApp\Cache\*
    MsgBox, Done! Your Whatsapp cache is empty
}
If WhatsApp
IfNotExist, %CacheFolder10%
{
    MsgBox, WHATSAPP ERROR! You may haven't the program installed or you've changed the cache folder
}
---------------------------------------------------
If Teams
CacheFolder11 = %USERPROFILE%\AppData\Roaming\Microsoft\Teams\cache\
IfExist, %CacheFolder11%
{
    FileDelete, %USERPROFILE%\AppData\Roaming\Microsoft\Teams\cache\*
    MsgBox, Done! Your Microsoft Teams cache is empty
}
If Teams
IfNotExist, %CacheFolder11%
{
    MsgBox, TEAMS ERROR! You may haven't the program installed or you've changed the cache folder
}
--------------------------------------------------
If Zoom
CacheFolder12 = %USERPROFILE%\AppData\Roaming\Zoom\logs\
IfExist, %CacheFolder12%
{
    FileDelete, %USERPROFILE%\AppData\Roaming\Zoom\logs\*
    MsgBox, Done! Your Zoom cache is empty
}
If Zoom
IfNotExist, %CacheFolder12%
{
    MsgBox, ZOOM ERROR! You may haven't the program installed or you've changed the cache folder
}
---------------------------------------------------
If Store
{
    Run, WSReset.exe
    Sleep, 200
    MsgBox, Done! Don't close CMD and wait for the Microsoft Store open
}
-----------------------------------------------------
If Dns 
{
    Run, cmd.exe
    Sleep, 200
    SendInput, ipconfig/flushDNS {Enter}
    Sleep, 1000
    Send, !{F4}
    MsgBox, Done! The DNS cache is empty
}
--------------------------------------------------
If bin
{
    FileRecycleEmpty
    Sleep, 200
    MsgBox, Done! Your Recycle Bin is empty
}
----------------------------------------------
If Explorer
{
    FileDelete, %USERPROFILE%\AppData\Local\Microsoft\Windows\Explorer\*.db
    FileDelete, %USERPROFILE%\AppData\Local\IconCache.db
    MsgBox, Done! Your Explorer cache is empty
}
-------------------------------
Filedelete, %USERPROFILE%\Premiere.png
Filedelete, %USERPROFILE%\DaVinci.png
Filedelete, %USERPROFILE%\Lightroom.png
Filedelete, %USERPROFILE%\Affinity.png
Filedelete, %USERPROFILE%\Chrome.png
Filedelete, %USERPROFILE%\Edge.png
Filedelete, %USERPROFILE%\Firefox.png
Filedelete, %USERPROFILE%\Obs.png
Filedelete, %USERPROFILE%\Spotify.png
Filedelete, %USERPROFILE%\Telegram.png
Filedelete, %USERPROFILE%\Whatsapp.png
Filedelete, %USERPROFILE%\Zoom.png
Filedelete, %USERPROFILE%\Teams.png
Filedelete, %USERPROFILE%\Store.png
Filedelete, %USERPROFILE%\Dns.png
Filedelete, %USERPROFILE%\Bin.png
Filedelete, %USERPROFILE%\Explorer.png
ExitApp
reload
return

Esc:
Filedelete, %USERPROFILE%\Premiere.png
Filedelete, %USERPROFILE%\DaVinci.png
Filedelete, %USERPROFILE%\Lightroom.png
Filedelete, %USERPROFILE%\Affinity.png
Filedelete, %USERPROFILE%\Chrome.png
Filedelete, %USERPROFILE%\Edge.png
Filedelete, %USERPROFILE%\Firefox.png
Filedelete, %USERPROFILE%\Obs.png
Filedelete, %USERPROFILE%\Spotify.png
Filedelete, %USERPROFILE%\Telegram.png
Filedelete, %USERPROFILE%\Whatsapp.png
Filedelete, %USERPROFILE%\Zoom.png
Filedelete, %USERPROFILE%\Teams.png
Filedelete, %USERPROFILE%\Store.png
Filedelete, %USERPROFILE%\Dns.png
Filedelete, %USERPROFILE%\Bin.png
Filedelete, %USERPROFILE%\Explorer.png
ExitApp
return

GuiClose:
Filedelete, %USERPROFILE%\Premiere.png
Filedelete, %USERPROFILE%\DaVinci.png
Filedelete, %USERPROFILE%\Lightroom.png
Filedelete, %USERPROFILE%\Affinity.png
Filedelete, %USERPROFILE%\Chrome.png
Filedelete, %USERPROFILE%\Edge.png
Filedelete, %USERPROFILE%\Firefox.png
Filedelete, %USERPROFILE%\Obs.png
Filedelete, %USERPROFILE%\Spotify.png
Filedelete, %USERPROFILE%\Telegram.png
Filedelete, %USERPROFILE%\Whatsapp.png
Filedelete, %USERPROFILE%\Zoom.png
Filedelete, %USERPROFILE%\Teams.png
Filedelete, %USERPROFILE%\Store.png
Filedelete, %USERPROFILE%\Dns.png
Filedelete, %USERPROFILE%\Bin.png
Filedelete, %USERPROFILE%\Explorer.png
ExitApp
return
