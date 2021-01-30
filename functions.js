function populate(){

    // Code referred to from https://www.skcript.com/svr/how-to-execute-python-scripts-in-electron-and-nodejs/
    const {PythonShell} = require('python-shell');

    let pyshell = new PythonShell('pyscripts/populate.py');

    pyshell.on('message', function(message) {
        console.log(message);
        //Populate Crew Dropdowns
        let crews = JSON.parse(message)['crew_list'];
        let crews1 = document.getElementById("select_crew1");
        let crews2 = document.getElementById("select_crew2");

        let idx = 0;
        crews.forEach(element => {
            let opt = document.createElement('option');
            opt.text = element;
            let opt2 = document.createElement('option');
            opt2.text = element;
            crews1.add(opt);
            crews1.selectedIndex = idx;
            crews2.add(opt2);
            crews2.selectedIndex = idx;
        });

        let players = JSON.parse(message)['player_list'];
        console.log(players)
        let p1 = document.getElementById("select_p1");
        let p2 = document.getElementById("select_p2");

        idx = 0;
        players.forEach(element => {
            let opt = document.createElement('option');
            opt.text = element;
            let opt2 = document.createElement('option');
            opt2.text = element;
            p1.add(opt);
            p1.selectedIndex = idx;
            p2.add(opt2);
            p2.selectedIndex = idx;
        });

        let chars = JSON.parse(message)['character_list'];
        console.log(players)
        let char1 = document.getElementById("select_char1");
        let char2 = document.getElementById("select_char2");

        console.log(chars)

        idx = 0;
        chars.forEach(element => {
            let opt = document.createElement('option');
            opt.text = element;
            let opt2 = document.createElement('option');
            opt2.text = element;
            char1.selectedIndex = idx;
            char1.add(opt);
            char2.selectedIndex = idx;
            char2.add(opt2);
        });
    })

    pyshell.end(function (err) {
    if (err){
        throw err;
    };
    console.log('finished');
    });
}

function addCrew(){
    const { ipcRenderer } = require('electron');
    ipcRenderer.invoke('add-crew');
}

function addPlayer(){
    const { ipcRenderer } = require('electron');
    ipcRenderer.invoke('add-player');
}

function submitPlayer(){
    let newPlayer = document.getElementById("newplayer").value;
    const {PythonShell} = require('python-shell');

    let pyshell = new PythonShell('pyscripts/addplayer.py');
    console.log("Sending " + newPlayer)
    pyshell.send(JSON.stringify(newPlayer));
    populate();

    pyshell.on('message', function(message) {
        console.log(message);
    })

    pyshell.end(function (err) {
        if (err){
            throw err;
        };
        console.log('finished');
    });
}


function submitCrew(){
    let newcrew = document.getElementById("newcrew").value;
    const {PythonShell} = require('python-shell');

    let pyshell = new PythonShell('pyscripts/addcrew.py');
    console.log("Sending " + newcrew)
    pyshell.send(JSON.stringify(newcrew));

    pyshell.on('message', function(message) {
    console.log(message);
    
    })

    pyshell.end(function (err) {
    if (err){
        throw err;
    };
    console.log('finished');
    });
}

function changeAlt(){
    const { ipcRenderer } = require('electron');
    ipcRenderer.invoke('change-alt');
}