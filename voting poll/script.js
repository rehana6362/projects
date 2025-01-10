const submitBtn = document.getElementById('submit-btn');
const resultsContainer = document.querySelector('.result-container');
const jsVotes = document.getElementById('js-votes');
const pythonVotes = document.getElementById('python-votes');
const javaVotes = document.getElementById('java-votes');
const cppVotes = document.getElementById('cpp-votes');

let votes = {
    JavaScript: 0,
    Python: 0,
    Java: 0,
    Cpp: 0
};

submitBtn.addEventListener('click', () => {
    const selectedOption = document.querySelector('input[name="poll"]:checked');
    
    if (selectedOption) {
        const vote = selectedOption.value;
        votes[vote]++;

        jsVotes.textContent = votes.JavaScript;
        pythonVotes.textContent = votes.Python;
        javaVotes.textContent = votes.Java;
        cppVotes.textContent = votes.Cpp;

        resultsContainer.style.display = 'block';
    } else {
        alert("Please select an option before voting.");
    }
});
