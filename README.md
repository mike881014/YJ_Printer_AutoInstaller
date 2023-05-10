# YJ_Printer_AutoInstaller
永捷系統科技自動化安裝驅動並設定IP
---
  為解決安裝驅動的過程繁瑣又重複的問題
  作者以AutoInstall.bat為核心
  用Python Tkinter設計UI
  來解決問題
  
## 第一版
  第一版是純粹的利用 os.system 來呼叫 bat 以達到自動安裝的目的
  用 pyinstaller 製作執行檔
  點開時會有 cmd 的執行畫面

## 第二版
  將第一版的 os.system 改成 subprocess
  用 popen 的方式來呼叫
  加上了 unzip() 與 delete()
  將 bat 解壓縮 (有密碼) 處理完成後再刪除
  以達到隱藏程式碼的目的
