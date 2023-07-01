function display_velocity(value){
    document.getElementById("velocity").innerText = "Velocity: " + value;
}

function update_state(state){
    const request = fetch("http://127.0.0.1:5000/update_state/" + state + "/", {method: "UPDATE"})
    .then((response) => response.json())
    .then((json) => {
        console.log(json["message"]);
    });
    console.log(request);
}

function init_controls(){
    // code for controlling the vehicle
    var forwardBtn = document.getElementById("forwardBtn");
    var backwardBtn = document.getElementById("backwardBtn");
    var leftBtn = document.getElementById("leftBtn");
    var rightBtn = document.getElementById("rightBtn");
    var stopBtn = document.getElementById("stopBtn");
    var softTurnForwardLeftBtn = document.getElementById("softTurnForwardLeftBtn");
    var softTurnForwardRightBtn = document.getElementById("softTurnForwardRightBtn");
    var softTurnBackwardLeftBtn = document.getElementById("softTurnBackwardLeftBtn");
    var softTurnBackwardRightBtn = document.getElementById("softTurnBackwardRightBtn");



    forwardBtn.addEventListener("mousedown", function() {
    // Code to move the vehicle forward when button is pressed
    update_state(1);
    console.log("Moving forward");
    this.classList.add("active");
    });

    forwardBtn.addEventListener("mouseup", function() {
    // Code to stop the vehicle when button is released
    update_state(0);
    console.log("Stopping");
    this.classList.remove("active");
    });

    forwardBtn.addEventListener("mouseleave", function() {
    // Code to stop the vehicle when the mouse cursor leaves the button
    update_state(0);
    console.log("Stopping");
    this.classList.remove("active");
    });

    // Repeat the same pattern for the other buttons

    backwardBtn.addEventListener("mousedown", function() {
    update_state(2);
    console.log("Moving backward");
    this.classList.add("active");
    });

    backwardBtn.addEventListener("mouseup", function() {
    update_state(0);
    console.log("Stopping");
    this.classList.remove("active");
    });

    backwardBtn.addEventListener("mouseleave", function() {
    update_state(0);
    console.log("Stopping");
    this.classList.remove("active");
    });

    leftBtn.addEventListener("mousedown", function() {
    update_state(4);
    console.log("Turning left");
    this.classList.add("active");
    });

    leftBtn.addEventListener("mouseup", function() {
    update_state(0);
    console.log("Stopping");
    this.classList.remove("active");
    });

    leftBtn.addEventListener("mouseleave", function() {
    update_state(0);
    console.log("Stopping");
    this.classList.remove("active");
    });

    rightBtn.addEventListener("mousedown", function() {
    update_state(3);
    console.log("Turning right");
    this.classList.add("active");
    });

    rightBtn.addEventListener("mouseup", function() {
    update_state(0);
    console.log("Stopping");
    this.classList.remove("active");
    });

    rightBtn.addEventListener("mouseleave", function() {
    update_state(0);
    console.log("Stopping");
    this.classList.remove("active");
    });

    stopBtn.addEventListener("mousedown", function() {
    update_state(0);
    console.log("Stopping");
    this.classList.add("active");
    });

    stopBtn.addEventListener("mouseup", function() {
    update_state(0);
    console.log("Stopping");
    this.classList.remove("active");
    });

    stopBtn.addEventListener("mouseleave", function() {
    update_state(0);
    console.log("Stopping");
    this.classList.remove("active");
    });

    softTurnForwardLeftBtn.addEventListener("mousedown", function() {
    update_state(5);
    console.log("Soft turn forward left");
    this.classList.add("active");
    });

    softTurnForwardLeftBtn.addEventListener("mouseup", function() {
    update_state(0);
    console.log("Stopping");
    this.classList.remove("active");
    });

    softTurnForwardLeftBtn.addEventListener("mouseleave", function() {
    update_state(0);
    console.log("Stopping");
    this.classList.remove("active");
    });

    softTurnForwardRightBtn.addEventListener("mousedown", function() {
    update_state(6);
    console.log("Soft turn forward right");
    this.classList.add("active");
    });

    softTurnForwardRightBtn.addEventListener("mouseup", function() {
    update_state(0);
    console.log("Stopping");
    this.classList.remove("active");
    });

    softTurnForwardRightBtn.addEventListener("mouseleave", function() {
    update_state(0);
    console.log("Stopping");
    this.classList.remove("active");
    });

    softTurnBackwardLeftBtn.addEventListener("mousedown", function() {
    update_state(7);
    console.log("Soft turn backward left");
    this.classList.add("active");
    });

    softTurnBackwardLeftBtn.addEventListener("mouseup", function() {
    update_state(0);
    console.log("Stopping");
    this.classList.remove("active");
    });

    softTurnBackwardLeftBtn.addEventListener("mouseleave", function() {
    update_state(0);
    console.log("Stopping");
    this.classList.remove("active");
    });

    softTurnBackwardRightBtn.addEventListener("mousedown", function() {
    update_state(8);
    console.log("Soft turn backward right");
    this.classList.add("active");
    });

    softTurnBackwardRightBtn.addEventListener("mouseup", function() {
    update_state(0);
    console.log("Stopping");
    this.classList.remove("active");
    });

    softTurnBackwardRightBtn.addEventListener("mouseleave", function() {
    update_state(0);
    console.log("Stopping");
    this.classList.remove("active");
    });
}

// Function to fetch data from the server
function fetchVelocity(graphId) {
    // Make an AJAX request to the server
    $.ajax({
        url: "http://127.0.0.1:5000/get_velocity/",
        method: "GET",
        dataType: "json",
        success: function(data) {
            console.log(data);
            // Process the received data and update the graph
            updateGraph(graphId, data);
        },
        error: function(xhr, status, error) {
            console.log("Error:", error);
        }
    });
}
function fetchPosition(graphId) {
    // Make an AJAX request to the server
    $.ajax({
        url: "http://127.0.0.1:5000/get_position/",
        method: "GET",
        dataType: "json",
        success: function(data) {
            console.log(data);
            // Process the received data and update the graph
            updateGraph(graphId, data);
        },
        error: function(xhr, status, error) {
            console.log("Error:", error);
        }
    });
}
function fetchAcc(graphId) {
    // Make an AJAX request to the server
    $.ajax({
        url: "http://127.0.0.1:5000/get_acc/",
        method: "GET",
        dataType: "json",
        success: function(data) {
            console.log(data);
            // Process the received data and update the graph
            updateGraph(graphId, data);
        },
        error: function(xhr, status, error) {
            console.log("Error:", error);
        }
    });
}

// Function to update the graph with new data
function updateGraph(graphId, data) {
    if (graphId === "acc"){
        // Extract x and y values from the received data
        var x = [data["time"]];
        var y = [data["value"]];
        // Create a plotly trace
        var trace = {
            x: x,
            y: y,
            mode: 'lines+markers',
            type: 'scatter'
        };

        // Define layout options
        var layout = {
            title: 'Acceleration vs time',
            xaxis: {
                title: 'Time'
            },
            yaxis: {
                title: 'Acceleraion [m/s^2]'
            }
        };
    }
    if (graphId === "pos"){
        // Extract x and y values from the received data
        var x = [data["x"]];
        var y = [data["y"]];
        // Create a plotly trace
        var trace = {
            x: x,
            y: y,
            mode: 'lines+markers',
            type: 'scatter'
        };

        // Define layout options
        var layout = {
            title: 'Position y(x)',
            xaxis: {
                title: 'x[m]'
            },
            yaxis: {
                title: 'y[m]'
            }
        };

    }
    if (graphId === "vel"){
        // Extract x and y values from the received data
        var x = [data["time"]];
        var y = [data["value"]];
        // Create a plotly trace
        var trace = {
            x: x,
            y: y,
            mode: 'lines+markers',
            type: 'scatter'
        };

        // Define layout options
         var layout = {
                title: 'Velocity vs time',
                xaxis: {
                    title: 'Time'
                },
                yaxis: {
                    title: 'Velocity [m/s]'
                }
            };
         display_velocity(y);
    }

    // Create or update the graph
    if (document.getElementById(graphId).data) {
        Plotly.extendTraces(graphId, { x: [x], y: [y] }, [0]);
    } else {
        console.log(y);
        Plotly.newPlot(graphId, [trace], layout);
    }
}
function fetchData() {
    // Make an AJAX request to the server
    $.ajax({
        url: "http://127.0.0.1:5000/get_state/",
        method: "GET",
        dataType: "json",
        success: function(data) {
            console.log(data);
            // Process the received data and update the graph
        },
        error: function(xhr, status, error) {
            console.log("Error:", error);
        }
    });
}