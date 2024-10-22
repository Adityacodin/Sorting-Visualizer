function sendData(){
    var size = document.getElementById("size").value;
    var algo = document.getElementById("algo").value;
    const data = {
        'size' : size,
        'algo' : algo
    }
    console.log(data)
    console.log("Sending data:", data);
    fetch('/getdt', {
        headers: {
            'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify(data)
    })
    .then(function (response) {
        if (response.ok) {
            return response.json().then(function (responseData) {
                console.log("Response received:", responseData);
                bars = []
                array = responseData.array;
            });
        } else {
            throw new Error('Something went wrong');
        }
    })
    .catch(function (error) {
        console.error("Error during fetch:", error);
    });
}