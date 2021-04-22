// Configure a request to an endpoint of your api that
// returns custom field meta data for the authenticated
// user.  Don't forget to congigure authentication!

const options = {
  url: 'https://regex101.com/api/library/1/',
  method: 'GET',
  headers: {
    'Accept': 'application/json'
  },
  params: {
    'search': bundle.inputData.search_key
  }
}

// first time through
if (!bundle.inputData.search_key) {
  return [{
            "key": "regexes",
            "label": "RegExs",
            "type": "string",
            "helpText": "Regexs to choose from regex101",
            "altersDynamicFields": true
          }
      ]
}

return z.request(options)
  .then((response) => {
    response.throwForStatus();
    const results = response.json;

    // modify your api response to return an array of Field objects
    // see https://zapier.github.io/zapier-platform-schema/build/schema.html#fieldschema
    // for schema definition.

    let choicesArray = [];

    results.data.map(item =>{
    choicesArray.push({sample:item.permalinkFragment, value:item.permalinkFragment, label:item.title})

   // {
     // key:item.id  item.permalinkFragment,
    });


    return [{
            "key": "regexes",
            "label": "RegExs",
            "type": "string",
            "helpText": "Regexs to choose from regex101",
            "choices": choicesArray,
            "altersDynamicFields": true
          },
      ]
  });