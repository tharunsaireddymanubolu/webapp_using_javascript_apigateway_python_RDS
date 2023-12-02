document.addEventListener('DOMContentLoaded', function () {
    const surveyForm = document.getElementById('surveyForm');
    const resultDiv = document.getElementById('result');

    surveyForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const name = document.getElementById('name').value;
        const age = document.getElementById('age').value;
        const email = document.getElementById('email').value;
        const feedback = document.getElementById('feedback').value;
        const color = document.getElementById('color').value;

        const surveyData = {
            name: name,
            email: email,
            age: age,
            feedback: feedback,
            rating: color
        };

        document.getElementById('name').value='';
        document.getElementById('age').value='';
        document.getElementById('email').value ='';
        document.getElementById('feedback').value = '';
        document.getElementById('color').value ='';
        
            fetch('Your_API_ENDPOINT', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(surveyData)
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                resultDiv.innerHTML = data['message']; 
            })
            .catch(error => {
                console.error('Error:', error);
                resultDiv.innerHTML = 'Error submitting survey';
            });
    
        
    });
});
