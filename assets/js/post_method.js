function post_call(url, formData, callBack){
    // console.log("post Url Call======>>", url)
    $.post({
        type : "POST", 
        url: url,
        data: formData,
        
        success: function(data){
            // return data
            callBack(data)
        },

        failure: function(data) {
            callBack(data) 
        }
    });
}

async function get_call(url, formData, callBack){
    // console.log("post Url Call======>>", url)
    
    // Storing response
    const response = await fetch(url);

    // Storing data in form of JSON
    var data = await response.json();

    if (response) {
        // hideloader();
        callBack(data)

    }

    console.log(data);


}

function nullHandler(value){
    if (value){
        return value
      }else{
        return "--"
      }
}