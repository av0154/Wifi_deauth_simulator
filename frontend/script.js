document.getElementById('deauthForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const target_mac = document.getElementById('target_mac').value;
    const ap_mac = document.getElementById('ap_mac').value;
    const iface = document.getElementById('iface').value;

    fetch('/deauth', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ target_mac, ap_mac, iface }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = data.status;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
