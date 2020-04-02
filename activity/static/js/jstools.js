function parseData(data){
    var stringArray = data.split(",");
    var ArrayData = stringArray.map(function(e){return Number(e); } );
    return ArrayData;
}

function createDataPoint(data){
    var ArrayData = parseData(data);

    dataPoint = [];
    var xVal = 0;
      for (var j = 0; j < ArrayData.length; j++) {
        
        dataPoint.push({
            x: xVal+1,
            y: dataPoint[xVal]
        });
        xVal++;
    }

    return dataPoint;
}


// function fetchData(accident_id){
//   const url = '127.0.0.1/api/accident/?='+accident_id;
//   fetch(url)
//   .then((resp) => resp.json())
//   .then(function(data) {
//     console.log(data)
//   })
//   .catch(function(error) {
//     console.log(error);
//   });   
// }

// function fetchData(accident_id){
//   const url = 'http://127.0.0.1/api/accident/?id='+accident_id;
//   fetch(url)
//   .then( function(data) {
//     console.log(data)
//   })
  
//   .catch(function(error) {
//     console.log(error);
//   });   
// }

function fetchData(accident_id){
  var request = new XMLHttpRequest();
  var value = 0;
    request.open('GET', '/api/accident/?id='+accident_id, true);


    request.onload = function() {
      // Begin accessing JSON data here
      var data = JSON.parse(this.response)

      if (request.status >= 200 && request.status < 400) {
        //console.log(data[0]['fields']);
        // return data[0]['fields'];
        value = data[0]['fields'];
        //return "000";

      } 
      else {
        console.log('error')
      }
    }

    request.send()
    return value;
}