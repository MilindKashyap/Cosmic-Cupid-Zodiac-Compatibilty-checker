function toggleAnswer(id) {
    var answer = document.getElementById(id).querySelector('.answer');
    answer.style.display = (answer.style.display === 'none') ? 'block' : 'none';
  }
  