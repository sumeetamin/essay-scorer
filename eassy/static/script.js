document.getElementById('essayForm').addEventListener('submit', function(e) {
    e.preventDefault();  // Prevent the default form submission
    const essayText = document.getElementById('essayInput').value;

    fetch('/score', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({essay: essayText}),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('scoreResult').innerText = `Predicted Score: ${data.score}`;
    })
    .catch(error => console.error('Error:', error));
});
