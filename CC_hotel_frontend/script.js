document.getElementById("bookingForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevents the page from reloading on form submission

    // Collect form data
    const guest_id = document.getElementById("guest_id").value;
    const room_id = document.getElementById("room_id").value;
    const datefrom = document.getElementById("date-from").value;
    const dateto = document.getElementById("date-to").value;

    // Create the data object for sending to FastAPI
    const bookingData = {
        guest_id: parseInt(guest_id),  // Ensure integer values
        room_id: parseInt(room_id),
        datefrom: datefrom,
        dateto: dateto
    };

    // Send the POST request to FastAPI
    fetch("http://localhost:8031/bookings", { // Update with your FastAPI server URL
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(bookingData),
    })
    .then(response => response.json())  // Parse JSON from the response
    .then(data => {
        // Show success message with booking ID
        document.getElementById("responseMessage").innerHTML = `Booking created! ID: ${data.id}`;
    })
    .catch(error => {
        console.error("Error creating booking:", error);
        // Show error message
        document.getElementById("responseMessage").innerHTML = "There was an error creating the booking.";
    });
});
