![By.Ouzrour](/logo.png)
# Mail Header Parser
## Why MHP ?
The main idea of this tool is to parse the mail header and detect the FROM / Subject option to change it + delete unwanted options .
## How it work ?
![ScreenShot](/screenshot.png)
1. **The Main Textbox**: Here you must paste the mail header
2. **the Subject TextBox** : Here you must paste the new subject that you want to be replaced into the Mail Textbox 
3. **The Detect Button** : Detect all options in the header and input them in the Mail listbox **_(9)_**
4. **The Copy Button** : Copy the content of the Main Textbox to the clipboard
5. **The Inject Button** : Inject the Content of the Subject & From to the Main Textbox ( you can copy it after that )
6. **The Delete Button :** Delete the selected element in the listbox from the Main Textbox
7. **The Reset Button :** Delete all the content of the Main Textbox and the Main Listbox
8. **The FROM TextBox :** Here where you must paste the new content of from that you want to be replaced into the Mail Textbox 
9. The Main ListBox : Here where , when you click the DETECT button , all options are listed . 
## Steps to use it ? 
- **_TO CHANGE The FROM/SUBJECT_**
1. install all dependencies : _( do it just 1 time , if already done it , go to Step 2 )_
```cmd
pip install -r requirements.txt
```
2. Paste the Mail Header into the Textbox
3. fill the subject / FROM box 
4. Click "INJECT"
5. Click "COPY" 
6. Enjoy !
- **_TO DELETE some options from the header_**
1. install all dependencies :_( do it just 1 time , if already done it , go to Step 2 )_
```cmd
pip install -r requirements.txt
```
2. Click "DETECT"
3. select the options that you want to be deleted
4. click "DELETE"
5. Click "COPY" 
6. Enjoy !


## For Windows User ( How to Deploy )

1. install pyinstaller
```cmd
pip install pyinstaller
```
2. run cmd in the same folder as the project ( where header_parser_offi exist ) and run :
```cmd
pyinstaller main.spec
```
3. Go to the folder dist and run .exe
4. Enjoy !