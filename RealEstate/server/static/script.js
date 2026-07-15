// Load locations when page loads
window.onload = function () {
    loadLocations();
};


// Load all locations from Flask
function loadLocations() {

    $.get("/get_location_names", function (data, status) {

        if (status === "success") {

            let locations = data.locations;

            let uiLocations = $("#location");

            uiLocations.empty();

            uiLocations.append(
                "<option disabled selected>Select Location</option>"
            );

            for (let i = 0; i < locations.length; i++) {

                uiLocations.append(
                    "<option>" + locations[i] + "</option>"
                );
            }
        }

    });

}


// Predict button click
$("#predictBtn").click(function () {

    let sqft = $("#sqft").val();
    let bhk = $("#bhk").val();
    let bath = $("#bath").val();
    let location = $("#location").val();

    // Input validation
    if (sqft === "" || bhk === "" || bath === "" || location == null) {

        alert("Please fill all fields.");

        return;
    }

    $("#price").html("Predicting...");

    $.post("/predict_home_price", {

        total_sqft: sqft,
        bhk: bhk,
        bath: bath,
        location: location

    }, function (data, status) {

        if (status === "success") {

            if (data.error) {

                $("#price").html(data.error);

            }
            else {

                $("#price").html(
                    "₹ " +
                    data.estimated_price.toFixed(2) +
                    " Lakhs"
                );

            }

        }

    });

});