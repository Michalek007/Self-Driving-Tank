// Function to fetch data from the server
function fetchAcc() {
    // Make an AJAX request to the server
    $.ajax({
        url: 'http://127.0.0.1:5000/acc/',
        method: 'GET',
        dataType: 'json',
        success: function(data) {
            console.log(data);
            // Process the received data and update the graph
            updateAcc(data['acc']);
        },
        error: function(xhr, status, error) {
            console.log('Error:', error);
        }
    });
}
  function fetchPos() {
    // Make an AJAX request to the server
    $.ajax({
        url: 'http://127.0.0.1:5000/position/',
        method: 'GET',
        dataType: 'json',
        success: function(data) {
            console.log(data);
            // Process the received data and update the graph
            updatePos(data['position']);
        },
        error: function(xhr, status, error) {
            console.log('Error:', error);
        }
    });
}

// Function to update the graph with new data
function updateAcc(data) {
    var time = [];
    var x = [];
    var y = [];
    var z = [];
    for (let i=0;i<data.length;i++){
        time.push(data[i]['date']);
        x.push(data[i]['x_axis']);
        y.push(data[i]['y_axis']);
        z.push(data[i]['z_axis']);
    }
    // Create a plotly trace
    var trace_x = {
        x: time,
        y: x,
        mode: 'lines+markers',
        type: 'scatter'
    };
    var trace_y = {
        x: time,
        y: y,
        mode: 'lines+markers',
        type: 'scatter'
    };
    var trace_z = {
        x: time,
        y: z,
        mode: 'lines+markers',
        type: 'scatter'
    };

    // Define layout options
    var layout_x = {
        title: 'X axis acceleration vs time',
        xaxis: {
            title: 'Time'
        },
        yaxis: {
            title: 'Acceleration [m/s^2]'
        }
    };
      var layout_y = {
        title: 'Y axis acceleration vs time',
        xaxis: {
            title: 'Time'
        },
        yaxis: {
            title: 'Acceleration [m/s^2]'
        }
    };
        var layout_z = {
        title: 'Z axis acceleration vs time',
        xaxis: {
            title: 'Time'
        },
        yaxis: {
            title: 'Acceleration [m/s^2]'
        }
    };
    // Create the graph
    Plotly.newPlot('x_acc', [trace_x], layout_x);
    Plotly.newPlot('y_acc', [trace_y], layout_y);
    Plotly.newPlot('z_acc', [trace_z], layout_z);
}
 function updatePos(data) {
    var time = [];
    var x = [];
    var y = [];
    var z = [];
    for (let i=0;i<data.length;i++){
     time.push(data[i]['date']);
     x.push(data[i]['x']);
     y.push(data[i]['y']);
     z.push(data[i]['z']);
    }
    // Create a plotly trace
    var trace_x = {
        x: time,
        y: x,
        mode: 'lines+markers',
        type: 'scatter'
    };
    var trace_y = {
        x: time,
        y: y,
        mode: 'lines+markers',
        type: 'scatter'
    };
    var trace_z = {
        x: x,
        y: y,
        mode: 'lines+markers',
        type: 'scatter'
    };

    // Define layout options
    var layout_x = {
        title: 'x(t)',
        xaxis: {
            title: 'Time'
        },
        yaxis: {
            title: 'x[m]'
        }
    };
      var layout_y = {
        title: 'y(t)',
        xaxis: {
            title: 'Time'
        },
        yaxis: {
            title: 'y[m]'
        }
    };
        var layout_z = {
        title: 'y(x)',
        xaxis: {
            title: 'x[m]'
        },
        yaxis: {
            title: 'y[m]'
        }
    };
    // Create the graph
    Plotly.newPlot('x', [trace_x], layout_x);
    Plotly.newPlot('y', [trace_y], layout_y);
    Plotly.newPlot('z', [trace_z], layout_z);
}