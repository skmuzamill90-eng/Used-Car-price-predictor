document.getElementById("carForm")
.addEventListener("submit", async function(event){

    event.preventDefault();

    let name =
    document.getElementById("name").value;

    let year =
    document.getElementById("year").value;

    let fuel =
    document.getElementById("fuel").value;

    let transmission =
    document.getElementById("transmission").value;

    let owner =
    document.getElementById("owner").value;

    let kms =
    document.getElementById("kms").value;

    let url =
`http://127.0.0.1:8000/predict?name=${encodeURIComponent(name)}&year=${year}&km_driven=${kms}&fuel=${encodeURIComponent(fuel)}&transmission=${encodeURIComponent(transmission)}&owner=${encodeURIComponent(owner)}`;

    try{

        let response =
        await fetch(url);

        let data =
        await response.json();

        console.log(data);

        document.getElementById("result")
        .innerHTML =

        "Predicted Price: ₹ " +
        data.predicted_price;

    }

    catch(error){

        console.log(error);

        alert("Error connecting frontend and backend");

    }

});