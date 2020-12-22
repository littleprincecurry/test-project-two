console.log('hello');

function loadHeadlines() {
    d3.json('/news').then((data) => {
        var listGroup = d3.select('.list-group');
        listGroup.html('');

        data.forEach((item => {
            var li = listGroup.append('li');
            li.text(item['Title']);
            li.attr("class", "list-group-item");
        }))
        console.log(data);

    })

};

loadHeadlines();