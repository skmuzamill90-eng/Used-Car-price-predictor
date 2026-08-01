// Splash Screen

window.onload = function () {

    document.getElementById("main-content").style.display = "none";

    setTimeout(function () {

        document.getElementById("splash-screen").style.display = "none";

        document.getElementById("main-content").style.display = "block";

    }, 3000);

};


// Prediction

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
            "https://used-car-price-predictor-eanj.onrender.com/predict",
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

        if(response.ok){

            document.getElementById("result").innerHTML = `
                <h3>Estimated Price Range</h3>
                <h2>${data.predicted_price}</h2>
            `;

        }
        else{

            document.getElementById("result").innerHTML =
                "Please enter valid car details.";

        }

    }
    catch(error){

        console.log(error);

        document.getElementById("result").innerHTML =
            "Unable to connect to the server.";

    }

});