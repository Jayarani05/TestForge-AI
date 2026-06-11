// Repository context

export function saveRepoContext(data){

    localStorage.setItem(
        "repoContext",
        JSON.stringify(data)
    );

}



export function getRepoContext(){

    const data =
        localStorage.getItem("repoContext");


    return data
        ? JSON.parse(data)
        : null;

}






// Test cases


export function saveTestCases(data){

    localStorage.setItem(
        "testCases",
        JSON.stringify(data)
    );

}



export function getTestCases(){

    const data =
        localStorage.getItem("testCases");


    return data
        ? JSON.parse(data)
        : [];

}






// Automation


export function saveAutomationCode(data){

    localStorage.setItem(
        "automationCode",
        JSON.stringify(data)
    );

}



export function getAutomationCode(){

    const data =
        localStorage.getItem("automationCode");


    return data
        ? JSON.parse(data)
        : null;

}