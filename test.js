const request = require('request')



// Request URL
var url1 = 'http://127.0.0.1:5000/fullList';
var url2 = 'http://127.0.0.1:5000/ban_ip';
var url3 = 'http://127.0.0.1:5000/validList';
  


request(url1, (error, response, body)=>{
     
    // Printing the error if occurred
    if(error) console.log(error)
    
    // Printing status code
    console.log(response.statusCode);
      
    // Printing body
    console.log(body);
}); 



request.post( url2, { json :{ 'ip': '65.21.66.166'}}, 
    function (error, response, body) {
        if (!error && response.statusCode == 200) {
            console.log(body);
        }
});



request(url3, (error, response, body)=>{
     
    // Printing the error if occurred
    if(error) console.log(error)
    
    // Printing status code
    console.log(response.statusCode);
      
    // Printing body
    console.log(body);
}); 