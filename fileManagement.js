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