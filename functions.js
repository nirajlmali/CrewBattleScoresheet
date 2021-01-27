function populate(){

    // Code referred to from https://www.skcript.com/svr/how-to-execute-python-scripts-in-electron-and-nodejs/
    const {PythonShell} = require('python-shell');

    let pyshell = new PythonShell('pyscripts/scripts.py');

    pyshell.on('message', function(message) {
        console.log(message);
        //Populate Crew Dropdowns
        let crews = JSON.parse(message)['crew_list'];
        let crews1 = document.getElementById("select_crew1");
        crews1.length = crews.length - 1;
        let crews2 = document.getElementById("select_crew2");
        crews2.length = crews.length - 1;

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
        p1.length = crews.length - 1;
        let p2 = document.getElementById("select_p2");
        p2.length = crews.length - 1;

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
    })

    pyshell.end(function (err) {
    if (err){
        throw err;
    };
    console.log('finished');
    });
}