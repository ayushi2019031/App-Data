var gplay = require('google-play-scraper');
var fs = require("fs");

function makeGetRequest(category, collection){
        gplay.list({
            category: gplay.category.BEAUTY,
            collection: gplay.collection.TOP_FREE,
            num: 100000
          })
          .then(function(results) {
            fs.writeFile('./BEAUTY_FREE.json', JSON.stringify(results), function(err) {
                if (err) {
                    console.log(err);
                } else {
                    
                    console.log("JSON saved");
                    return results;
                }
            })
        }).catch(function(err) {
            console.log(err);
        });
}

makeGetRequest("", "");


  
