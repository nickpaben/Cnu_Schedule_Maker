let courseData = [];

let handleFiles = (files) => {
    if (window.FileReader) {
        alertUserAboutOutdatedFile(files[0]);
        getAsText(files[0]);
    } else {
        alert("The FileReader API is not supported in this browser.");
    }
}

let alertUserAboutOutdatedFile = (file) => {
    let date = new Date(file.lastModified);
    let today = new Date();

    let timeDifference = today.getTime() - date.getTime();

    let MILLISECONDS_PER_DAY = 1000 * 60 * 60 * 24;
    let dayDifference = timeDifference / MILLISECONDS_PER_DAY;

    if (dayDifference >= 5) {
        alert("Your CSV schedule of classes is more than 5 days old, and may be outdated. Consider using an updated file.");
    } 
}

let getAsText = (file) => {
    let fileReader = new FileReader();
    fileReader.readAsText(file);
    fileReader.onload = loadHandler;
    fileReader.onerror = errorHandler;
}

let loadHandler = (event) => {
    let csv = event.target.result;
    processCSVData(csv);
}

let processCSVData = (data) => {
    courseData = [];
    let dataLines = data.split(/\r\n|\n/);
    for (let i = 0; i < dataLines.length; i++) {
        dataLines[i] = dataLines[i].replaceAll('\"', '');
        let currentLine = dataLines[i].split(',');
        let lastValidIndex = 0;
        let tempData = [];
        for (let j = 0; j < currentLine.length; j++) {
            if (currentLine[j][0] == " " && currentLine[j][1] != " ") {
                tempData[lastValidIndex] = tempData[lastValidIndex] + "," + currentLine[j];
            } else {
                lastValidIndex = j;
                tempData.push(currentLine[j]);
            }
        }
        courseData.push(tempData);
    }
}

let errorHandler = (event) => {
    if (event.target.error.name == "NotReadableError") {
        alert("File is unreadable.");
    }
}

let crnIsValid = (input) => {
    let inputCRN = parseInt(input);
    if (courseData.length === 0) { alert("The course database is empty!"); }
    for (let i = 0; i < courseData.length; i++) {
        let crn = courseData[i][0];
        if (crn == inputCRN) {
            return true;
        }
    }
    return false;
}

let getClassDataFromCRN = (input) => {
    let inputCRN = parseInt(input);
    for (let i = 0; i < courseData.length; i++) {
        let crn = courseData[i][0];
        if (crn == inputCRN) {
            let selectedClass = courseData[i];
            return {
                crn: parseInt(selectedClass[0]),
                course: selectedClass[1],
                section: selectedClass[2],
                title: selectedClass[3],
                hours: parseInt(selectedClass[4]),
                llc: selectedClass[5],
                days: selectedClass[7],
                time: selectedClass[8],
                location: selectedClass[9],
                instructors: selectedClass[10],
                availableSeats: parseInt(selectedClass[11])
            };
        }
    }

    return null;
}