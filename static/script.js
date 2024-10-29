

let steps = [];
let barContainer = null;

function sendData() {
    const size = document.getElementById("size").value;
    const algo = document.getElementById("algo").value;
    const data = {
        'size': size,
        'algo': algo
    };

    console.log("Sending data:", data);

    fetch('/getdt', {
        headers: {
            'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify(data)
    })
    .then(function (response) {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Failed to fetch sorting data from server');
        }
    })
    .then(function (responseData) {
        console.log("Response received:", responseData);
        
        steps = responseData.sort_steps;
        const barHeight = responseData.array;
        barContainer = document.getElementById('sort_scr');
        barContainer.innerHTML = '';

        barHeight.forEach(height => {
            const bar = document.createElement("div");
            bar.classList.add("bar");
            bar.style.height = `${height}px`;
            bar.style.width = `${(100 / barHeight.length) - 1}%`;
            bar.style.display = 'inline-block';
            bar.style.background = '#168aad';
            bar.innerHTML = `${height}`;
            barContainer.appendChild(bar);
        });

    })
    .catch(function (error) {
        console.error("Error during fetch:", error);
    });
}

function startAnimation() {
    if (steps.length === 0) {
        console.error("No sorting steps available. Please generate bars first.");
        return;
    }
    animateSorting(steps, barContainer);
}

function animateSorting(steps, barContainer) {
    const bars = Array.from(barContainer.children);
    const delay = 200;

    steps.forEach((step, index) => {
        setTimeout(() => {
            step.forEach((height, i) => {
                bars[i].style.height = `${height}px`;
                bars[i].innerHTML = `${height}`
            });
        }, delay * index);
    });

    bars.forEach((bar,i) => {
        setTimeout(() => {
            bars[i].style.background = '#7ae582'
        } , delay*i)
    });
}

