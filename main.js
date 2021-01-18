const { app, BrowserWindow } = require('electron')  //Importing 'app' and 'BrowserWindow' modules of electron package

function createWindow () {          //Function that creates a browser window
  const win = new BrowserWindow({   
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true
    }
  })

  win.loadFile('index.html')
}

app.whenReady().then(createWindow)  //Function invoked

app.on('window-all-closed', () => {         //Listener that closes app when no windows open
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {                  //Listener that makes new window if app has no visible windows on activation
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow()
  }
})