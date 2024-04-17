let node_index = 0;

let fetch_options = async function () {
    let response = await fetch(`http://127.0.0.1:5000/api/options/${node_index}`);
    let data = await response.json();
    return data;
};

let hydrate = (data) => {
    // let feature = data.feature;
    let question = data.question;
    $("h2#feature").text(question);

    let options = data.options;
    if (options.length === 0) {
        $("h2#result").text(data.label);
        $("#output").addClass("d-none");
        $("#result-wrapper").removeClass("d-none");
        return;
    }

    let options_html = options.map((option, index) => {
        return `<li class="btn btn-md btn-secondary rounded-pill m-2" style="cursor: pointer;" data-value="${index === 0 ? 'left' : 'right'}"> ${option}</li>`;
    }).join("");
    $("ul#options").html(options_html);
    add_event_listeners();
}

let add_event_listeners = () => {
    document.querySelectorAll("ul#options>li").forEach(element => {
        element.addEventListener("click", async () => {
            let selected_option = $(element).data('value');
            node_index = await fetch(`http://127.0.0.1:5000/api/${selected_option}/${node_index}`)
                .then(response => response.json())
                .then(data => {
                    return data.node_index;
                });

            fetch_options().then(data => {
                hydrate(data);
            });
        });
    });
}

$(document).ready(function () {
    // Fetch intial options from '/api/options/<node_index>' and display them
    fetch_options().then(data => {
        hydrate(data);
    });

    // document.querySelector("button.test").addEventListener("click", () => {
    //     console.log(node_index)
    // });
});