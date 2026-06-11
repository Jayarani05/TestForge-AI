export function saveHistory(item){


    const oldHistory =

        JSON.parse(
            localStorage.getItem("history")
        )

        ||

        [];



    const newItem = {

        id:Date.now(),

        time:new Date().toLocaleString(),

        ...item

    };



    oldHistory.unshift(
        newItem
    );



    localStorage.setItem(

        "history",

        JSON.stringify(oldHistory)

    );

}





export function getHistory(){


    return (

        JSON.parse(

            localStorage.getItem("history")

        )

        ||

        []

    );

}





export function clearHistory(){


    localStorage.removeItem(
        "history"
    );


}