async function post_call(url, formData, callBack){
    console.log("post Url Call======>>", url)
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
        body: JSON.stringify(formData),
        credentials: 'same-origin',

    });

    // Storing data in form of JSON
    var data = await response.json();
    if (response) {
        // hideloader();
        callBack(data)

    }
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

    // console.log(data);


}

function nullHandler(value){
    if (value){
        return value
      }else{
        return "--"
      }
}