let courseData = [];

let handleFiles = (files) => {
    if (window.FileReader) {
        getAsText(files[0]);
    } else {
        alert("The FileReader API is not supported in this browser.");
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
        let tempData = [];
        for (let j = 0; j < currentLine.length; j++) {
            tempData.push(currentLine[j]);
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
                instructor: selectedClass[11].trim() + " " + selectedClass[10],
                availableSeats: parseInt(selectedClass[12])
            };
        }
    }

    return null;
}