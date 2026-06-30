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



    try{


        let response = await fetch(
            "http://127.0.0.1:8000/predict",
            {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },


                body: JSON.stringify({

                    name: name,

                    year: Number(year),

                    km_driven: Number(kms),

                    fuel: fuel,

                    transmission: transmission,

                    owner: owner

                })

            }
        );



        let data = await response.json();


        console.log(data);



        if(data.predicted_price){

    document.getElementById("result")
    .innerHTML =
    "Predicted Price: " + data.predicted_price;

}
else{

document.getElementById("result")
.innerHTML =
"Please enter valid car details";

}


    }


    catch(error){

        console.log(error);

        alert(
        "Error connecting frontend and backend"
        );

    }


});