document.getElementById('apiForm').addEventListener('submit', async function (event) {
  event.preventDefault();
  

  const length_sepal = document.getElementById('length_sepal').value;
  const length_petal = document.getElementById('length_petal').value;
  const width_sepal = document.getElementById('width_sepal').value;
  const width_petal = document.getElementById('width_petal').value;

    if (isNaN(length_sepal) || isNaN(length_petal)) {
      alert('Por favor, ingresa valores válidos para las medidas.');
      return;
    }

  const response = await fetch('/predict', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({
          length_sepal: parseFloat(length_sepal),
          length_petal: parseFloat(length_petal),
          width_sepal: parseFloat(width_sepal),
          width_petal: parseFloat(width_petal),
      }),
  });

  const result = await response.json();
  
  document.getElementById('result').innerHTML = `Esta es tu flor: ${result.prediction}`;
});
