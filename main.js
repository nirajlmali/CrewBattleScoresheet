const { app, BrowserWindow } = require('electron')  //Importing 'app' and 'BrowserWindow' modules of electron package
const { ipcMain } = require('electron');

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

ipcMain.handle('add-crew', function(){
  const child = new BrowserWindow({   
    width: 800,
    height: 300,
    webPreferences: {
      nodeIntegration: true
    }
  })

  child.loadFile('newcrew.html')
});

ipcMain.handle('add-player', function(){
  const win = new BrowserWindow({   
    width: 800,
    height: 300,
    webPreferences: {
      nodeIntegration: true
    }
  })

  win.loadFile('newplayer.html')
});

ipcMain.handle('change-alt', function(){
  const win = new BrowserWindow({   
    width: 800,
    height: 300,
    webPreferences: {
      nodeIntegration: true
    }
  })

  win.loadFile('changealt.html')
});